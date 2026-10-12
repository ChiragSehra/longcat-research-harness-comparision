# Results register

| Harness | Status | Model / effort | Result location | Notes |
| --- | --- | --- | --- | --- |
| LongCat-DeepResearch | completed (after mid-run failure and research-stage resume) | GPT-6.1 Sol / medium | `longcat-deepresearch/runs/6ad7c38bbe3683f9/` | First attempt failed during concurrent model calls (blank adapter errors); resumed from saved planning state and web cache. Final report 2,555 words, 25 unique direct URLs, two logged editorial failures (URLs removed without explicit deletion instructions), usage telemetry all zeros (adapter never emitted the expected metrics format). The two earlier interrupted attempts are preserved under `runs/c256e14934ac5a74-interrupted-*/`. |
| Codex | completed | GPT-6.1 Sol / medium | `results/codex/` | Native ChatGPT-authenticated Codex CLI. 14m 19s, 1,957-word memo, 33 distinct cited URLs, 34 archived web-research calls, claim-by-claim source trail. Raw event log: `results/codex/run.jsonl`. |
| dsh desktop app | completed | GPT-6.1 Sol / medium | `results/dsh/` | Completed in 10m 50s with two subagents; saved a 2,067-word memo and run note with 31 direct URLs. User-provided dsh model picker shows GPT-6.1 Sol under the ChatGPT-subscription provider. |

LongCat and dsh were run concurrently at the user's request. They remain comparable on prompt and model/effort, but not on latency, rate-limit behavior, or quota use. Future runs should be serialized if those operational measures matter.
