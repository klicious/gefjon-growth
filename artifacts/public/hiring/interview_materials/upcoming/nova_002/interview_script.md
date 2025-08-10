---
id: interview_script_nova_002_2025-08-10_v1
type: interview_script
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.0/10
tags: [script, junior, BEI, pair_programming, system_design]
visibility: public
version: 1.0
---

# Interview Script: nova_002 (PII masked)

## 0) Introduction (5 mins)
- “Hi Nova, thanks for joining today. I’m [Interviewer Name], joined by [Panel Names]. Our session will run about 60–75 minutes.”
- Company mission: “We engineer cross‑region, self‑healing fintech platforms that move capital instantly and safely, with strong observability and <5 min MTTR.”
- Values: “We focus on Technical Excellence & Scalable Elegance, Ownership & Proactivity, Observability & Guardrails, Data‑Informed Iteration, and Integrity.”
- Agenda: “We’ll start with behavioral questions, then pair‑programming, a junior system design exercise, a short technical deep‑dive, and end with your questions.”
- “Does that sound good?”

## 1) Rapport Building (2–3 mins)
- Personalized opener: “Your camping‑style recommendation project shows initiative. I’d like to hear what you’re most proud of from that build.”

## 2) Behavioral Interview (20–25 mins)
- Validation (Evidence-based):
  - “Tell us about a concept you learned recently that was especially challenging. How did you approach learning it and know you understood it?”
    - Follow-ups: “What resources helped?” “How would you teach it to a peer?”
  - “Describe a project you started on your own. What problem were you solving and how did you measure success?”
- Probing missing evidence:
  - “How do you log and handle errors in your services? What does ‘good’ look like for a small API?”
  - “How would you handle secrets and PII in a student project? What would you change for production?”
- STAR reminder: “Please cover Situation, Task, Action, and Result.”

## 3) Pair-Programming (30–40 mins)
- Problem: Easy P1 OHLC Candlestick Generator.
- Guidance: “Think aloud. Start with the bucket rule, edge cases, then code the happy path and a couple of tests.”
- Checkpoints: Correct bucket assignment, OHLC/V fields, handling gaps/duplicates, time complexity basics.

## 4) System Design (20–25 mins)
- Prompt (junior): “Design a minimal Orders micro‑API (v1) for create/amend/fetch. Describe endpoints, request/response schemas, validation and error model (status codes, error body), versioning approach, and a minimal CI (lint/test). Explain your unit vs. request testing plan.”
- Anchors to cover: REST verbs and status codes, Decimal for money, simple error schema, CI steps (ruff/black/pytest), documentation (OpenAPI).

## 5) Technical Deep-Dive (10–15 mins)
- Q1 REST design fundamentals: POST /orders and GET /orders/{id}; expected responses and errors.
- Q2 Testing approach in FastAPI: what to test, how to mock dependencies, edge cases (negative qty/price, missing fields).
- Q3 Decimal vs float for monetary values and common pitfalls.
- Q4 Motivation and domain interest in quantitative systems; week‑1 learning plan.

## 6) Candidate Q&A (5–10 mins)
- “What questions do you have about the role, team, and roadmap?”

## 7) Closing (2–3 mins)
- “Thank you, Nova. We’ll consolidate feedback within 48 hours and follow up on next steps.”