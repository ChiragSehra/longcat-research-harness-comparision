# Same Model, Three Harnesses: A Research-Experiment Comparison

This repository is the evidence bundle for an experiment that ran the **same
research brief** through **three agent harnesses** with the **same model**
(GPT-6.1 Sol, medium reasoning effort), to show how much the harness — not the
model — determines the result.

- **Benchmark brief:** [`benchmark/political-realignment-2024-india.md`](benchmark/political-realignment-2024-india.md)
- **Results register:** [`benchmark/RESULTS.md`](benchmark/RESULTS.md)

## The task

> Was India's 2024 general-election result a one-off correction or evidence of
> a durable political realignment?

Each harness had to produce a 1,500–2,500 word decision memo with competing
interpretations, a compact evidence table, direct source URLs, and an explicit
"Uncertainties and limits" section. Evidence cutoff: 11 October 2026
(Asia/Kolkata).

## Results at a glance

| Harness | Time | Memo length | Distinct URLs | Notable |
|---|---|---|---|---|
| dsh (desktop) | 10m 50s | 2,067 words | 31 | Two subagents; fastest path to a usable memo |
| Native Codex CLI | 14m 19s | 1,957 words | 33 | Best research receipt: claim-source trail, 34-call web archive, raw event log |
| LongCat-DeepResearch | failed mid-run, resumed from saved state | 2,555 words | 25 | Richest pipeline; recovery test; two logged editorial failures; usage-telemetry gap |

All three converged on a cautious conclusion: politically consequential, not
yet proof of a durable nationwide realignment. Convergence is not proof of
accuracy — see the caveats below.

## Repository layout

~~~text
.
├── benchmark/
│   ├── political-realignment-2024-india.md    # Shared brief and operating rules
│   ├── RESULTS.md                             # Results register
│   └── results/
│       ├── dsh/                               # Memo + run note
│       ├── codex/                             # Memo, run note, claim-source trail,
│       │                                      # sources.json, research-log.json, run.jsonl
│       └── longcat/                           # Adapter run log
└── longcat-deepresearch/                      # Vendored LongCat harness + adapter (see below)
    ├── local_backend.py                       # Codex-CLI-backed backend adapter
    ├── RUN_WITH_CODEX.md                      # How the LongCat arm was run
    └── runs/6ad7c38bbe3683f9/                 # The recorded LongCat run:
                                               # planning, sections, editorial, final report,
                                               # retry summary, telemetry
~~~

## The LongCat arm: vendored harness + adapter

`longcat-deepresearch/` is a vendored snapshot of
[meituan-longcat/LongCat-DeepResearch](https://github.com/meituan-longcat/LongCat-DeepResearch)
at upstream commit `818563e` (MIT license; see
[`longcat-deepresearch/LICENSE`](longcat-deepresearch/LICENSE)). LongCat is used
only as the research harness; every model turn is routed through the local
Codex CLI's ChatGPT OAuth session by [`local_backend.py`](longcat-deepresearch/local_backend.py),
with LongCat's `web_search` and `web_fetch` running locally. See
[`longcat-deepresearch/RUN_WITH_CODEX.md`](longcat-deepresearch/RUN_WITH_CODEX.md)
for the full setup.

Local modifications to the vendored copy:

- Added `local_backend.py` (the adapter) and `RUN_WITH_CODEX.md`.
- Adjusted `.gitignore` so the evidence artifacts (`runs/`, `question.txt`,
  `local_backend.py`) are tracked; upstream ignores them to keep credentials
  and run output out of the source repo.
- Removed upstream's `.github/workflows/ci.yml`: this is an evidence snapshot,
  not an active fork, and upstream's release checks were not designed for a
  tree that includes run artifacts.

To re-clone upstream instead: `git clone https://github.com/meituan-longcat/LongCat-DeepResearch.git`

## Reproducing the LongCat arm

~~~sh
cd longcat-deepresearch
python3 -m venv .venv
.venv/bin/python -m pip install -e .
export DR_BACKEND_MODULE=local_backend
export DR_MODEL=gpt-6.1-sol
export DR_CODEX_EFFORT=medium
export DR_CODEX_CONCURRENCY=1
export PYTHONPATH=.

codex login status   # confirm the intended ChatGPT account
scripts/run_smoke.sh
scripts/run_standard.sh question.txt runs
~~~

The final report lands in `runs/<question-hash>/report_final.md`. Note that a
fresh run will not reproduce the recorded artifacts byte-for-byte; treat
`runs/6ad7c38bbe3683f9/` as the recorded evidence.

## Caveats

- One task, one run per harness — not a statistically meaningful benchmark.
- The LongCat and dsh runs initially shared ChatGPT subscription capacity,
  which likely contributed to LongCat's mid-run failure; they are comparable on
  prompt and model/effort, not on latency or rate-limit behavior.
- Model/effort settings were configured consistently but not independently
  attested by the provider.
- Outputs were assessed for operational behaviour and evidence quality, not
  blind expert fact-checking of every political claim.

## License

The vendored `longcat-deepresearch/` directory is MIT-licensed by the LongCat
team (see its `LICENSE`). Everything else in this repository (benchmark
materials and run artifacts) is provided as-is for documentation of
the experiment.
