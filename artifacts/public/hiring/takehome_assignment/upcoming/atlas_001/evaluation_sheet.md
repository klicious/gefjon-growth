---
id: eval_takehome_atlas_001_2025-08-10_v1
type: takehome_evaluation_sheet
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [evaluation, rubric, backtesting]
visibility: public
version: 1.0
---

# Take-Home Evaluation — atlas_001 (PII masked)
Candidate: atlas_001  Evaluator: __________  Date: __________

## Quick Rules
1. Time-box assumption: ≤ 8 h; do not penalize polish beyond scope.
2. Gate: Functional, Code Quality, Testing must each be ≥ 2/5.
3. Pass guideline: Weighted ≥ 3.0/5 (60%) ⇒ proceed; 3.0–3.4 = Lean Hire; 3.5–4.4 = Hire; ≥ 4.5 = Strong Hire.
4. Evidence: Any score ≤ 3 or any Red Flag ⇒ cite file:line evidence.
5. Bias guard: Score only on listed criteria.

## 0. Overall Recommendation
- [ ] Strong Hire (≥ 4.5) - [ ] Hire (3.5–4.4) - [ ] Lean Hire (3.0–3.4) - [ ] No Hire (< 3.0)

## 1. Functional Correctness & Completeness (25%)
Raw: __/5  Weighted: ____
- Anchors: 5 = all flows + edge cases; 3 = core works but major feature missing.
- Checklist (Variant C expected):
  - Trades generated correctly on 9/21 SMA crossovers
  - P&L, max drawdown, win % computed
  - trades.csv and summary.json produced
  - Handles missing candles, zero volume, duplicate timestamps
- Red Flags: crashes; incorrect P&L math
- Green Flags: idempotent processing; robust CSV validation

## 2. Code Quality & Best Practices (20%)
Raw: __/5  Weighted: ____
- Anchors: 5 = idiomatic, modular, typed; 2 = spaghetti, duplication
- Checklist: PEP8/ruff, separation (loader/strategy/backtester/cli), mypy --strict
- Red: print-debug; secrets
- Green: pre-commit hooks; ADRs

## 3. Testing Approach & Coverage (15%)
Raw: __/5  Weighted: ____
- Anchors: 5 = unit + 1 integration; ≥ 60% coverage; mocks
- Checklist: pytest green; param tests for SMA; edge tests for duplicates/missing
- Red: tests hit network; fail on clean clone
- Green: fixtures; coverage report

## 4. Documentation (10%)
Raw: __/5  Weighted: ____
- Anchors: 5 = README ≤ 400 words; setup; CLI; diagram
- Checklist: quick-start; file schema; design decisions

## 5. Ownership / Above & Beyond (15%)
Raw: __/5  Weighted: ____
- Anchors: 5 = logging/metrics/ADRs; grid-search

## 6. Scalability & Design Patterns (10%)
Raw: __/5  Weighted: ____
- Anchors: 5 = clear Strategy/Backtester classes; easy extension

## 7. Quantitative & Logical Reasoning (5%)
Raw: __/5  Weighted: ____
- Anchors: 5 = correct math and complexity analysis

## 8. Score Calculation
| Criterion | Weight | Raw | Weighted |
|-----------|-------:|----:|---------:|
| Functional Correctness | 25 | | |
| Code Quality | 20 | | |
| Testing | 15 | | |
| Documentation | 10 | | |
| Ownership | 15 | | |
| Scalability | 10 | | |
| Quant Reasoning | 5 | | |
| Total | 100 | — | __/5 |

## 9. Strengths
- …

## 10. Areas for Improvement
- …

## 11. Alignment with Core Values
- Technical Excellence & Scalable Elegance — …
- Ownership & Proactivity — …
- Observability & Guardrails — …
- Data‑Informed Iteration — …

## 12. Next Steps
- [ ] Proceed to interview — Reason: __________
- [ ] Consider for other role — Reason: __________
- [ ] Do not proceed — Reason: __________
