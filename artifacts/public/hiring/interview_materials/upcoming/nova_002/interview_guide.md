---
id: interview_guide_nova_002_2025-08-10_v1
type: interview_guide
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [guide, BEI, junior, api_design]
visibility: public
version: 1.0
---

# Interview Guide: nova_002 (PII masked)

## General Guidance for Interviewers
Nova is a Moderate Match with strong learning signals and early project initiative. Calibrate to entry level; focus on fundamentals: REST semantics, validation and error models, testing discipline, and basic CI/CD literacy. Use BEI with STAR, validate values where evidence exists (learning, ownership), and probe gaps (observability, testing depth, security). Keep questions concrete and supportive.

## Session Plans

### 1) Behavioral (BEI) — 20–25 min
- Validate evidence:
  - Continuous Learning & Mentorship: “Tell us about the most challenging concept you learned recently. How did you approach it and how did you validate your understanding?”
    - Follow-ups: “What resources worked best?” “How would you teach it to a peer?”
  - Ownership & Proactivity: “Describe a project you started on your own (e.g., recommendation service). What problem were you solving and how did you measure success?”
    - Follow-ups: “What trade-offs did you consider?”
- Probe missing/unclear evidence:
  - Observability & Guardrails: “How do you log and handle errors in your services? What would ‘good’ look like in a small API?”
    - Follow-ups: “What would you add if you had more time?”
  - Security & Compliance First: “How would you handle secrets and PII in a student project? What about rate limiting or abuse prevention?”
    - Follow-ups: “How would you evolve this in production?”

### 2) Pair-Programming — 30–40 min
- Problem: Easy P1 OHLC Candlestick Generator.
- Rationale: Tests data transformation, edge-case handling, and clarity of logic; accessible for juniors and relevant to trading/analytics.
- Success signals: Clear decomposition, correct bucket logic, edge-case coverage, simple tests, readable code.

### 3) System Design — 20–25 min
- Prompt (tailored junior level): “Design a minimal Orders micro-API (v1) for create/amend/fetch. Describe endpoints, request/response schemas, validation rules, error model, and how you would version the API. Discuss basic CI (lint, test) and how you would test it (unit vs request tests).”
- Evaluation: Correct REST verbs and status codes, simple and consistent schema, validation and error handling, test strategy, and minimal CI awareness.

### 4) Technical Deep-Dive — 15–20 min
Primary questions (with follow-ups):
1. REST design fundamentals: “How would you structure POST /orders and GET /orders/{id}? What status codes and error bodies would you return?”
   - Follow-up: “How would you document the API?”
2. Testing approach: “What should be unit-tested vs. request-tested in a FastAPI service?”
   - Follow-up: “How would you mock dependencies?”
3. Data modeling & validation: “Why is Decimal preferred for prices/qty? How would you validate inputs?”
   - Follow-up: “What common pitfalls would you guard against?”
4. Basics of CI/CD: “What steps would you include in a minimal GitHub Actions workflow for a Python API?”
   - Follow-up: “How would you add coverage or lint gates?”
5. Motivation & domain interest: “What about quantitative systems and portfolio analytics interests you?”
   - Follow-up: “What would you learn first in week 1?”

### 5) Scoring Reminders
- Use the standardized rubric; write evidence-based notes referencing specific statements or artifacts.
- Note bias checks and red/green flags explicitly.
