# LongCat + Codex subscription experiment

This directory runs the **LongCat-DeepResearch harness** while using the local
Codex CLI's ChatGPT OAuth session for model inference. It deliberately does
not use Codex as an agent: LongCat performs the planning, independent section
research, retrieval, report assembly, and local editing.

## Fixed comparison settings

| Setting | Value |
| --- | --- |
| Model | `gpt-6.1-sol` |
| Reasoning effort | `medium` |
| Model authentication | Existing local Codex ChatGPT login |
| LongCat configuration | `standard` |
| Model-call concurrency | 1 (to make subscription-rate behavior repeatable) |

The backend is `local_backend.py`. It invokes `codex exec` for exactly one
structured model turn at a time, with native Codex tools disabled by prompt and
with a read-only temporary working directory. LongCat's `web_search` and
`web_fetch` tools run locally; the model returns only their requested calls in
the Chat-Completions shape LongCat expects.

## Setup

```sh
cd longcat-deepresearch
python3 -m venv .venv
.venv/bin/python -m pip install -e .
export DR_BACKEND_MODULE=local_backend
export DR_MODEL=gpt-6.1-sol
export DR_CODEX_EFFORT=medium
export DR_CODEX_CONCURRENCY=1
export PYTHONPATH=.
```

Confirm the local Codex client is signed in with the intended ChatGPT account:

```sh
codex login status
```

## Smoke test

The upstream smoke test makes one short model call, one search request, and one
page fetch. It does not run a full research report.

```sh
scripts/run_smoke.sh
```

## Full run

The benchmark question used for the recorded comparison is the India 2024
political-realignment brief from `../benchmark/political-realignment-2024-india.md`.

```sh
printf '%s\n' \
  "Was India's 2024 general-election result a one-off correction or evidence of a durable political realignment?" \
  > question.txt
scripts/run_standard.sh question.txt runs
```

The completed report and all intermediate artifacts are written under
`runs/<question-hash>/`. The recorded benchmark run is
`runs/6ad7c38bbe3683f9/`. Preserve the entire directory: it is the LongCat
arm's evidence bundle for the Codex and dsh comparisons.

## Scope and caveats

This is an adapter, not an official LongCat or OpenAI integration. It sends
each LongCat model turn through the installed Codex CLI and inherits the
account's normal ChatGPT usage limits. The adapter is intentionally serialised
to avoid multiplying concurrent subscription requests; that changes elapsed
time, so assess quality and model-turn count separately from wall-clock time.
