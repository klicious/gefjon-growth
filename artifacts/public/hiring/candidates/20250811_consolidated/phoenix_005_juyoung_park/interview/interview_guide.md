---
id: interview_guide_2025-08-20
type: interview_guide
domain: hiring
created_date: 2025-08-20
last_updated: 2025-08-20
author: Junie
quality_score: __TBD__
tags: ['interview', 'bei', 'phoenix_005_juyoung_park']
visibility: public
version: 1.0
---


# BEI Interview Guide

Candidate: Juyoung Park (phoenix_005_juyoung_park)

## Structure
- Total: 90 minutes
- BEI & Technical Deep-Dive (Take-Home Focused): 80 minutes
- Candidate Q&A: 10 minutes

## General Guidance for Interviewers
The candidate's take-home project was evaluated as a "Lean Hire," which contrasts with their strong initial screening. This interview is critical to understanding that discrepancy. The focus should be less on generic behavioral questions and more on a deep, Socratic dialogue about the technical choices and omissions in their submitted project. Your goal is to determine if the gaps (testing, security, etc.) stem from a lack of awareness/knowledge or simply from time constraints.

## BEI Value-by-Value Focus (Tied to Take-Home Project)

### Integrity & Reliability
- **What to verify**: Does the candidate understand that comprehensive testing (unit, integration, contract) is non-negotiable for reliable systems? Can they articulate a robust testing strategy?
- **Evidence to probe**: The project only contains a simple unit test for the logger (`tests/test_logger_simple.py`). There are no tests for the core business logic in the BitMEX client.
- **STAR questions**: See `interview_script.md`.

### Technical Excellence & Scalable Elegance
- **What to verify**: Can the candidate explain the trade-offs of their architectural choices? Do they think about resilience beyond basic timeouts?
- **Evidence to probe**: The use of a base class (`src/exchanges/base.py`) is a good start, but the lack of resilience patterns like retries or circuit breakers for the `httpx.Client` is a key gap.
- **STAR questions**: See `interview_script.md`.

### Security & Compliance First
- **What to verify**: Is the candidate aware of standard security practices for handling secrets and dependencies in a production environment?
- **Evidence to probe**: The project has input validation, which is good, but there is no evidence of secret management for API keys.
- **STAR questions**: See `interview_script.md`.

### Observability & Guardrails
- **What to verify**: Does the candidate think about observability beyond just logging? Can they explain the role of metrics, health checks, and automated quality gates?
- **Evidence to probe**: The project uses structured logging but has no metrics, no health endpoints, and no CI/linting configuration.
- **STAR questions**: See `interview_script.md`.

### Ownership & Proactivity
- **What to verify**: Does the candidate demonstrate a sense of ownership by thinking through the full lifecycle of a service, including its operational aspects?
- **Evidence to probe**: The project meets the basic functional requirements but lacks the hallmarks of production-readiness (containerization, robust testing, CI) that indicate a high level of ownership.
- **STAR questions**: See `interview_script.md`.

## Technical Assessment Calibration
- **Topics**:
    1.  **Testing Strategy**: Deep dive on how they would build a full test suite (unit, integration, contract, E2E) for the `dunamis` project.
    2.  **Resilience Patterns**: Discuss implementing retries, circuit breakers, and idempotency for the exchange client.
    3.  **Security**: How to properly manage and inject secrets (API keys) into the application.
    4.  **CI/CD**: Whiteboard a CI/CD pipeline for this project using GitHub Actions. What steps are essential? (Lint, Test, Build, Deploy).
    5.  **API Design**: How would they document the API? What are the pros and cons of their current implicit contract?
- **Depth**: Mid-level. We are not looking for a perfect answer, but for a demonstration of knowledge and a good thought process.
- **Success indicators**: The candidate can articulate the *why* behind these concepts, not just the *what*. They should be able to reason about trade-offs and apply the concepts directly to their submitted code.
