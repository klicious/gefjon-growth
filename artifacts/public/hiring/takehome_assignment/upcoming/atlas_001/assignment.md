---
id: takehome_atlas_001_2025-08-10_v1
type: takehome_assignment_brief
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.0/10
tags: [entry-level, quant, backtesting, portfolio_analytics]
visibility: public
version: 1.0
---

# Take-Home Assignment — atlas_001 (PII masked)
- Candidate codename: Atlas (real name masked)
- Email: [redacted]
- Phone: [redacted]
- Role: Entry-Level Backend Engineer (Quant/Analytics focus)

## Summary
Build a simple, testable Moving-Average Crossover Back-Tester over local CSV candles. This aligns with our need for portfolio analytics and quantitative reasoning. Time-box to 4–6 hours (hard stop at 8 hours max), prioritize correctness, tests, and clear documentation over extra features.

## Why this assignment (personalization)
- Strengths observed: testing mindset (QA background), CI/CD exposure, Spring/REST experience, performance optimization, WebFlux.
- Gaps to probe: hands-on quantitative logic and metrics reporting; clarity of design trade-offs.
- Mapping to values: Technical Excellence & Scalable Elegance; Observability & Guardrails; Ownership & Proactivity; Data‑Informed Iteration.

## Scope & Requirements (tailored)
This task follows the “Moving‑Average Crossover Back‑tester” (variant C). Key requirements:
1) Read candles CSV with columns: timestamp,open,high,low,close,volume (1‑minute bars).
2) Compute 9/21 SMA; generate trades: long on fast>slow crossover; flat on fast<slow crossover.
3) P&L: running equity curve; final summary: gross P&L, max drawdown, win %.
4) Outputs: trades.csv (blotter) and summary.json.
5) Edge cases must not crash: missing candles, zero volume, duplicate timestamps.

Non‑functional:
- Modularity (data_loader.py, strategy.py, backtester.py, cli.py); full type hints; mypy --strict clean.
- Logs: INFO for start/finish and key metrics.
- Tests: pytest; parametrize SMA and trade cases; target ≥ 45% coverage.
- Performance: process 1‑month CSV (~40k rows) in < 5 s on a mid‑tier laptop.

Stretch (Ownership): CLI flag --grid to run (fast, slow) grid and report top Sharpe ratios.

## Deliverables
1. Code runnable via: `python cli.py --csv candles.csv`.
2. Tests: `pytest -q` green; coverage report recommended.
3. README (≤ 400 words): setup, CLI examples, file schema, design decisions (brief ADRs encouraged).
4. TIME_SPENT.md with honest hh:mm log.
5. (Stretch) Grid‑search results and short note on findings.

## Evaluation rubric mapping
We evaluate with our Enhanced Entry‑Level SWE rubric:
- Functional 25% — correct trades & P&L; resilient to edge cases.
- Code Quality 20% — modular, typed, lint clean.
- Testing 15% — unit tests incl. edge cases; coverage ≥ 45%.
- Documentation 10% — concise, complete README.
- Ownership 15% — grid-search, logging, ADRs.
- Scalability 10% — strategy/backtester class separation for extensibility.
- Quant 5% — accurate P&L and drawdown math.

Gate ≥ 2/5 on Functional, Code, Tests; total ≥ 3.0/5 advances.

## Submission & Timing
- Time-box: 72h from receipt or stop at 8h of effort (submit as-is; include TODOs).
- Repo: private GitHub; add collaborator: klicious.
- Send: repo URL + GitHub handle + TIME_SPENT.md to hr@[redacted-domain].com.

## Notes on fairness & compliance
- Do not include any 3rd‑party PII. No secrets required.
- You may use public references; cite if copying snippets.
- Adhere to equal opportunity and bias‑safe language in docs.

Good luck—focus on clarity, correctness, and tests.