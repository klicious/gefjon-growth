---
id: takehome_nova_002_2025-08-10_v1
type: takehome_assignment_brief
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.0/10
tags: [entry-level, api, fastapi, testing]
visibility: public
version: 1.0
---

# Take-Home Assignment — nova_002 (PII masked)
- Candidate codename: Nova (real name masked)
- Email: [redacted]
- Phone: [redacted]
- Role: Entry-Level Backend Engineer (API focus)

## Summary
Implement a minimal Orders API using FastAPI with create/amend/fetch endpoints, validation via Pydantic, and unit tests. This targets REST API design, testing, and foundational CI practices—areas identified as growth opportunities. Time-box 4–6 hours (stop by 8 hours max).

## Why this assignment (personalization)
- Strengths observed: Python, Java/Spring coursework, basic AWS exposure, strong initiative in projects.
- Growth areas: REST API design depth, systematic testing, CI/CD.
- Value mapping: Technical Excellence & Scalable Elegance; Ownership & Proactivity; Observability & Guardrails; Continuous Learning & Mentorship.

## Scope & Requirements (tailored)
This task follows “FastAPI Orders CRUD” (variant D). Implement:
1) POST /orders → create order {id:str, symbol:str, qty:int, price:Decimal} and return JSON.
2) POST /amend → body {id:str, qty:int | None, price:Decimal | None}; return amended order.
3) GET /orders/{id} → return order or 404.
4) Auto OpenAPI docs at /docs.

Constraints:
- In-memory store (thread-safe dict OK for demo).
- Use Decimal for price/qty validation; 422 on invalid values.

Non-functional:
- Modular files (models.py, storage.py, api.py), full type hints, mypy --strict pass.
- Tests: pytest + FastAPI TestClient; ≥ 2 happy-path + 1 edge-case.
- Logging: INFO per request (method, path, latency).
- Coverage target ≥ 45% (junior baseline).

Stretch (Ownership):
- Expose Prometheus metrics at /metrics (Instrumentator), or add a minimal GitHub Actions workflow (.github/workflows/ci.yml) to run ruff/black/pytest on PRs.

## Deliverables
1. Code runnable with: `uvicorn api:app --reload`.
2. Tests: `pytest -q` green; coverage report recommended.
3. README (≤ 400 words): setup, API examples, decisions/trade-offs.
4. TIME_SPENT.md with honest hh:mm log.
5. (Stretch) Metrics endpoint or CI workflow.

## Evaluation rubric mapping
- Functional 25% — endpoints behave as specified; validation and 404s correct.
- Code Quality 20% — modular, typed, lint/format clean.
- Testing 15% — unit tests and edge cases; coverage ≥ 45%.
- Documentation 10% — clear quick-start and examples.
- Ownership 15% — metrics or CI, structured logging.
- Scalability 10% — storage/service separable; clear models.
- Quant 5% — Decimal accuracy and validation logic.

Gate ≥ 2/5 on Functional, Code, Tests; total ≥ 3.0/5 advances.

## Submission & Timing
- Time-box: 72h from receipt or stop at 8h.
- Repo: private GitHub; add collaborator: klicious.
- Send: repo URL + GitHub handle + TIME_SPENT.md to hr@[redacted-domain].com.

## Compliance & fairness
- No PII or secrets; bias-safe language.
- Cite any external snippets. Focus on clarity, correctness, and tests.