"""Run LongCat-DeepResearch with the local Codex CLI's ChatGPT OAuth session.

The LongCat harness owns orchestration, retrieval, and editing.  This backend
uses Codex only as a structured model turn, keeping the comparison focused on
the LongCat harness rather than Codex's own agent loop.

Required environment variables:
  DR_MODEL=gpt-6.1-sol

Optional environment variables:
  DR_CODEX_EFFORT=medium       # reasoning effort sent to Codex
  DR_CODEX_TIMEOUT_SECONDS=900
  DR_CODEX_CONCURRENCY=1      # keep subscription traffic predictable
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from html import unescape
import ipaddress
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import tempfile
import threading
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote_plus, unquote, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


_ROOT = Path(__file__).resolve().parent
_MODEL = os.environ.get("DR_MODEL", "gpt-6.1-sol")
_EFFORT = os.environ.get("DR_CODEX_EFFORT", "medium")
_TIMEOUT = int(os.environ.get("DR_CODEX_TIMEOUT_SECONDS", "900"))
_MAX_BYTES = 2_000_000
_MODEL_LOCK = threading.BoundedSemaphore(int(os.environ.get("DR_CODEX_CONCURRENCY", "1")))


class _SearchResultParser(HTMLParser):
    """Extract result links and snippets from DuckDuckGo's no-JS result page."""

    def __init__(self) -> None:
        super().__init__()
        self.results: list[dict[str, str]] = []
        self._href: str | None = None
        self._title: list[str] = []
        self._snippet: list[str] = []
        self._in_result = False
        self._in_snippet = False
        self._result_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        classes = attrs_dict.get("class", "") or ""
        if tag == "div" and "result" in classes.split() and not self._in_result:
            self._in_result = True
            self._result_depth = 1
        elif tag == "div" and self._in_result:
            self._result_depth += 1
        if self._in_result and tag == "a" and "result__a" in classes:
            self._href = attrs_dict.get("href")
        if self._in_result and "result__snippet" in classes:
            self._in_snippet = True

    def handle_data(self, data: str) -> None:
        if self._href:
            self._title.append(data)
        elif self._in_snippet:
            self._snippet.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._href:
            href = self._href
            if href.startswith("//"):
                href = "https:" + href
            if "/l/?" in href:
                href = parse_qs(urlparse(href).query).get("uddg", [href])[0]
            if href.startswith("http"):
                self.results.append(
                    {
                        "title": " ".join("".join(self._title).split()),
                        "url": unquote(href),
                        "snippet": "",
                    }
                )
            self._href = None
            self._title = []
        if tag == "div" and self._in_result:
            self._result_depth -= 1
            if self._result_depth == 0:
                if self.results:
                    self.results[-1]["snippet"] = " ".join("".join(self._snippet).split())
                self._in_result = False
                self._in_snippet = False
                self._snippet = []


class _TextParser(HTMLParser):
    """Small dependency-free HTML-to-text converter for fetched public pages."""

    _SKIP = {"script", "style", "noscript", "svg", "template"}

    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self._skip_depth = 0
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self._SKIP:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True
        if tag in {"p", "br", "li", "h1", "h2", "h3", "h4", "tr", "div"}:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self._SKIP and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self._in_title:
            self.title += data
        self._parts.append(data)

    @property
    def text(self) -> str:
        return "\n".join(line.strip() for line in "".join(self._parts).splitlines() if line.strip())


def _public_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("only public http(s) URLs are allowed")
    host = parsed.hostname
    try:
        addresses = {info[4][0] for info in socket.getaddrinfo(host, None)}
    except socket.gaierror as exc:
        raise ValueError(f"cannot resolve host: {host}") from exc
    for address in addresses:
        ip = ipaddress.ip_address(address)
        if not ip.is_global:
            raise ValueError(f"non-public destination refused: {host}")


class _SafeRedirects(HTTPRedirectHandler):
    def redirect_request(self, req: Request, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> Request | None:
        _public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _get(url: str) -> tuple[str, str]:
    _public_url(url)
    request = Request(url, headers={"User-Agent": "LongCatHarnessComparison/1.0 (+local research run)"})
    opener = build_opener(_SafeRedirects())
    with opener.open(request, timeout=30) as response:
        content_type = response.headers.get_content_type()
        charset = response.headers.get_content_charset() or "utf-8"
        payload = response.read(_MAX_BYTES + 1)
        if len(payload) > _MAX_BYTES:
            raise ValueError("response exceeded 2 MB limit")
    if content_type not in {"text/html", "text/plain", "application/xhtml+xml"}:
        raise ValueError(f"unsupported content type: {content_type}")
    return content_type, payload.decode(charset, errors="replace")


def _search_html(query: str) -> str:
    """Retrieve Brave's rendered search page through the system curl client.

    Query text is passed as one argument, never interpolated into a shell
    command. This avoids a required third-party API key for the first local
    experiment; swap this method for a contracted search service before using
    the harness in production.
    """

    url = "https://search.brave.com/search?q=" + quote_plus(query)
    completed = subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            "--max-time",
            "30",
            "--user-agent",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36",
            url,
        ],
        text=True,
        capture_output=True,
        check=False,
        timeout=35,
    )
    if completed.returncode:
        raise RuntimeError("web search failed: " + completed.stderr.strip()[-500:])
    return completed.stdout


_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "content": {"type": ["string", "null"]},
        "tool_calls": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string", "enum": ["web_search", "web_fetch"]},
                    "arguments_json": {
                        "type": "string",
                        "description": "A JSON object encoded as a string.",
                    },
                },
                "required": ["name", "arguments_json"],
            },
        },
    },
    "required": ["content", "tool_calls"],
}


def _model_prompt(request: dict[str, Any]) -> str:
    tools = request.get("tools") or []
    return """You are the language-model turn inside LongCat-DeepResearch. LongCat owns the agent loop.
Do not use Codex tools, inspect files, browse, or do independent agent work. Decide only the next assistant message.
Return JSON conforming to the supplied schema. If an available LongCat function is needed, add it to tool_calls and set content to null. Otherwise put the complete assistant answer in content and return an empty tool_calls list. Encode each function's arguments as a JSON object string in arguments_json; it must satisfy the listed function schema.

Conversation (OpenAI Chat Completions format):
""" + json.dumps(request.get("messages", []), ensure_ascii=False) + "\n\nAvailable functions:\n" + json.dumps(tools, ensure_ascii=False)


class Backend:
    """LongCat backend that delegates one structured model turn to Codex CLI."""

    def llm(self, request: dict[str, Any]) -> dict[str, Any]:
        started = time.monotonic()
        with tempfile.TemporaryDirectory(prefix="longcat-codex-") as temp_dir:
            workdir = Path(temp_dir)
            schema_path = workdir / "response-schema.json"
            output_path = workdir / "response.json"
            schema_path.write_text(json.dumps(_OUTPUT_SCHEMA), encoding="utf-8")
            command = [
                "codex",
                "exec",
                "--ephemeral",
                "--ignore-user-config",
                "--skip-git-repo-check",
                "--sandbox",
                "read-only",
                "--model",
                _MODEL,
                "--config",
                f'model_reasoning_effort="{_EFFORT}"',
                "--output-schema",
                str(schema_path),
                "--output-last-message",
                str(output_path),
                "--cd",
                str(workdir),
                _model_prompt(request),
            ]
            with _MODEL_LOCK:
                try:
                    completed = subprocess.run(
                        command,
                        text=True,
                        capture_output=True,
                        timeout=_TIMEOUT,
                        check=False,
                    )
                except subprocess.TimeoutExpired as exc:
                    partial = (exc.stderr or exc.stdout or "").strip()
                    raise RuntimeError(
                        f"Codex model turn timed out after {_TIMEOUT}s"
                        + (f": {partial[-2000:]}" if partial else "")
                    ) from exc
            if completed.returncode:
                diagnostic = (completed.stderr.strip() or completed.stdout.strip())[-2000:]
                raise RuntimeError(
                    f"Codex model turn failed (exit {completed.returncode})"
                    + (f": {diagnostic}" if diagnostic else " with no diagnostic output")
                )
            try:
                response = json.loads(output_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                raise RuntimeError("Codex did not return the requested structured response") from exc

        calls = []
        for index, call in enumerate(response["tool_calls"], start=1):
            try:
                arguments = json.loads(call["arguments_json"])
            except (TypeError, json.JSONDecodeError) as exc:
                raise RuntimeError("Codex returned invalid JSON in tool arguments") from exc
            if not isinstance(arguments, dict):
                raise RuntimeError("Codex tool arguments must decode to a JSON object")
            calls.append(
                {
                    "id": f"codex_call_{index}",
                    "type": "function",
                    "function": {"name": call["name"], "arguments": json.dumps(arguments)},
                }
            )
        message: dict[str, Any] = {"role": "assistant", "content": response["content"]}
        if calls:
            message["tool_calls"] = calls
        return {
            "choices": [{"message": message, "finish_reason": "tool_calls" if calls else "stop"}],
            "usage": {"total_tokens": 0},
            "comparison": {"model": _MODEL, "effort": _EFFORT, "elapsed_seconds": round(time.monotonic() - started, 3)},
        }

    def web_search(self, request: dict[str, Any]) -> dict[str, Any]:
        query = str(request.get("query", "")).strip()
        top_k = min(10, max(1, int(request.get("top_k", 8))))
        if not query:
            return {"results": []}
        html = _search_html(query)
        results = []
        pattern = re.compile(
            r'<div class="snippet [^"]*" data-pos="[^"]+" data-type="web".*?'
            r'<a href="(?P<href>https?[^\"]+)"[^>]*>.*?'
            r'class="title search-snippet-title[^\"]*" title="(?P<title>[^\"]+)"[^>]*>.*?</div>.*?'
            r'<div class="generic-snippet[^>]*>.*?<div class="content[^>]*>(?P<snippet>.*?)</div>',
            re.DOTALL,
        )
        for match in pattern.finditer(html):
            href = unescape(match.group("href"))
            if href.startswith("//"):
                href = "https:" + href
            if "/l/?" in href:
                href = parse_qs(urlparse(href).query).get("uddg", [href])[0]
            if not href.startswith("http"):
                continue
            title_parser = _TextParser()
            title_parser.feed(match.group("title"))
            snippet_parser = _TextParser()
            snippet_parser.feed(match.group("snippet"))
            results.append(
                {
                    "title": " ".join(title_parser.text.split()),
                    "url": unquote(href),
                    "snippet": " ".join(snippet_parser.text.split()),
                    "published_at": None,
                }
            )
        return {"results": results[:top_k]}

    def web_fetch(self, request: dict[str, Any]) -> dict[str, Any]:
        pages = []
        for url in request.get("urls", []):
            try:
                content_type, body = _get(str(url))
                if content_type == "text/plain":
                    pages.append({"url": str(url), "title": "", "text": body, "error": None})
                else:
                    parser = _TextParser()
                    parser.feed(body)
                    pages.append({"url": str(url), "title": " ".join(parser.title.split()), "text": parser.text, "error": None})
            except (HTTPError, URLError, OSError, ValueError) as exc:
                pages.append({"url": str(url), "title": "", "text": "", "error": str(exc)})
        return {"pages": pages}


def create_backend() -> Backend:
    return Backend()
