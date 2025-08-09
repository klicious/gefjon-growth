---
id: quality_gates_and_checklists
type: qa_checklists
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-10
author: Junie
quality_score: 9.2/10
tags: [quality, checklist, compliance, release]
visibility: public
version: 1.0
---

# Quality Gates and Checklists

Purpose: Standardize validation for demos and releases; ensure compliance, consistency, and reliability.

## A. Demo Quality Gate (Pass/Fail)
- Context completeness:
  - Mission/values present, role profile defined, hiring stages configured
- Output quality:
  - Human-rated quality ≥ 8.5/10 for screening, assignment, interview kit, evaluations
- Consistency:
  - Terminology and scoring scales consistent across artifacts
- Determinism:
  - Fixed seed; snapshot context bundle; outputs reproducible
- Compliance:
  - EEO-safe language; PII redacted as per policy; job relevance only
- Adoption:
  - ≥ 80% interviewer usage of standardized kits; rubric completion rate ≥ 90%
- Take-home gates:
  - Role-specific pass gates satisfied (Senior: coverage ≥ 70%, rollback plan, SLO thinking, secretless config; Mid-level: tests pass, basic metrics exposed, clean structure, no hardcoded secrets)
- Audit:
  - Structured JSON logs present; export cadence simulated weekly (pilot), daily upon go-live
- Readiness:
  - Offline artifacts prepared; preflight checklist passed

## B. Release Quality Gate (Minor)
- Prompt regression tests pass (no >0.3 score drop on golden set)
- Observability: logs/traces complete; cost telemetry present
- Security: static checks for secrets; RBAC roles verified
- Docs: change-log updated; README links valid; metadata headers present

## C. Release Quality Gate (Major)
- Security review passed; DPIA updated
- Performance: throughput baseline achieved; error rate <2%
- Data retention: lifecycle policies tested (delete/expire)
- Disaster recovery: fallback/alternate provider proven

## D. Compliance Checklist (Quick)
- GDPR: lawful basis documented; DPA with subprocessors; DSAR flow defined
- EEO: interview guides free of discriminatory content; standardized rubrics
- Audit: immutable logs enabled; retention per policy

## E. Prompt Change Checklist
- Rationale documented; expected effects
- Prompt diff reviewed; regression tests executed
- Approver sign-off; version and date recorded

## F. Pre-Demo Preflight (Summary)
- See ../07_presentation/preflight_checklist.md

## Templates
- Quality Score Rubric (1–10): clarity, completeness, correctness, consistency, compliance
- Sign-off Record:
  - Gate: [Demo/Minor/Major]
  - Owner: [name]
  - Date: [YYYY-MM-DD]
  - Result: [PASS/FAIL]
  - Notes: [text]
