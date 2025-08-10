---
id: interview_script_atlas_001_2025-08-10_v1
type: interview_script
domain: hiring_entry_level_backend
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [script, BEI, deep_dive, system_design]
visibility: public
version: 1.0
---

# Interview Script: atlas_001 (PII masked)

## 0) Introduction (5 mins)
- “Hi Atlas, thanks for joining today. I’m [Interviewer Name], joined by [Panel Names]. We’ll spend about 60–90 minutes together.”
- Company mission: “We engineer cross-region, self-healing fintech platforms that move capital instantly and safely, with <5 min MTTR and strong observability.”
- Values: “We hire for Technical Excellence & Scalable Elegance, Ownership & Proactivity, Observability & Guardrails, Data‑Informed Iteration, and Integrity.”
- Agenda: “We’ll start with a few behavioral questions, then a pair-programming exercise, a short system-design discussion, and a technical deep-dive. We’ll leave time for your questions at the end.”
- “Sound good?”

## 1) Rapport Building (2–3 mins)
- Personalized opener: “Your Toketrip work stood out—especially using WebFlux to tackle latency. I’d love to hear more about the metrics you improved.”

## 2) Behavioral Interview (20–25 mins)
- Validation (Evidence-based):
  - “Tell us about a time you improved service performance under constraints. What were the trade-offs and how did your design scale?”
    - Follow-ups: “How did you measure p95 or throughput?” “What metrics guided your decisions?”
  - “Describe when you implemented CI/CD or tooling proactively. What problem did it solve and what outcomes did you track?”
- Probing missing evidence:
  - “Describe how you handled secrets or sensitive data in projects. What would you change now?”
  - “Share an example of mentorship or knowledge-sharing during your QA→backend transition. What feedback did you incorporate?”
- Reminder: “We use STAR—please cover Situation, Task, Action, Result.”

## 3) Pair-Programming (35–45 mins)
- Problem: Intermediate I-3 Mini Matching Engine.
- Guidance: “Let’s think aloud. Start with data structures, invariants, then simple tests. We can code in Python/Java pseudocode.”
- Checkpoints: Crossed-book logic (bid≥ask), partial fills, FIFO at price level, cancels.

## 4) System Design (30–35 mins)
- Prompt: “Design a minimal portfolio-analytics microservice computing moving-average crossovers and publishing signals via REST.”
- Anchors to cover: schema, ingestion cadence, stateless vs. stateful, correctness checks, logging/metrics, failure handling, simple scale path.

## 5) Technical Deep-Dive (15–20 mins)
- Q1 Toketrip performance root cause and remediation (Why WebFlux? What changed?).
- Q2 Testing philosophy post-QA: unit vs. integration; prevent flaky tests.
- Q3 DS/Algo: heap vs. tree trade-offs for matching.
- Q4 Finance interest and week‑1 learning plan.
- Q5 CI/CD workflow and gates (build, test, lint, security scan, artifacting).

## 6) Candidate Q&A (5–10 mins)
- “What questions do you have for us about the role, team, or roadmap?”

## 7) Closing (2–3 mins)
- “Thanks, Atlas. Next steps: we’ll consolidate feedback within 48 hours and get back to you. If we proceed, we’ll schedule follow-ups quickly. Appreciate your time.”