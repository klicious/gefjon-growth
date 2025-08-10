---
id: eval_takehome_nova_002_2025-08-10_v1
type: takehome_evaluation_sheet
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [evaluation, rubric, fastapi]
visibility: public
version: 1.0
---

# Take-Home Evaluation — nova_002 (PII masked)
Candidate: nova_002  Evaluator: __________  Date: __________

## Quick Rules
1. Time-box assumption: ≤ 8 h; do not penalize polish beyond scope.
2. Gate: Functional, Code Quality, Testing must each be ≥ 2/5.
3. Pass guideline: Weighted ≥ 3.0/5 (60%) ⇒ proceed; 3.0–3.4 = Lean Hire; 3.5–4.4 = Hire; ≥ 4.5 = Strong Hire.
4. Evidence: Any score ≤ 3 or any Red Flag ⇒ cite file:line evidence.
5. Bias guard: Score only on listed criteria.

## 0. Overall Recommendation
- [ ] Strong Hire (≥ 4.5) - [ ] Hire (3.5–4.4) - [ ] Lean Hire (3.0–3.4) - [ ] No Hire (< 3.0)

## 1. Functional Correctness & Completeness (25%) — Variant D
Raw: __/5  Weighted: ____
- Anchors: 5 = all endpoints + edge cases; graceful errors; 3 = core works, major gap.
- Checklist:
  - POST /orders creates and returns order JSON
  - POST /amend updates qty/price selectively
  - GET /orders/{id} returns 404 when missing
  - Auto OpenAPI at /docs
  - Decimal used for price/qty; 422 for invalid values
- Red Flags: float math for money; incorrect status codes
- Green Flags: idempotency where appropriate; validation messages clear

## 2. Code Quality & Best Practices (20%)
Raw: __/5  Weighted: ____
- Anchors: 5 = idiomatic, modular, typed; 2 = monolith, duplication
- Checklist: models.py/storage.py/api.py separation; ruff/black clean; mypy --strict pass
- Red: print-debug, leaking internals
- Green: pre-commit hooks; ADRs

## 3. Testing Approach & Coverage (15%)
Raw: __/5  Weighted: ____
- Anchors: 5 = unit + request tests; ≥ 60% coverage; fixtures
- Checklist: FastAPI TestClient used; edge cases for negative qty/price; 404 path
- Red: tests hit network; nondeterministic
- Green: parametrised tests; coverage report

## 4. Documentation (10%)
Raw: __/5  Weighted: ____
- Anchors: 5 = README ≤ 400 words; install; run; examples; API table
- Checklist: quick-start; examples for all endpoints; constraints noted

## 5. Ownership / Above & Beyond (15%)
Raw: __/5  Weighted: ____
- Anchors: 5 = metrics or CI workflow added; structured logs

## 6. Scalability & Design Patterns (10%)
Raw: __/5  Weighted: ____
- Anchors: 5 = storage/service layers separable; interfaces noted

## 7. Quantitative & Logical Reasoning (5%)
Raw: __/5  Weighted: ____
- Anchors: 5 = Decimal precision correct; validations logically sound

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
- Continuous Learning & Mentorship — …

## 12. Next Steps
- [ ] Proceed to interview — Reason: __________
- [ ] Consider for other role — Reason: __________
- [ ] Do not proceed — Reason: __________
