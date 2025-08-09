---
id: decision_log
type: governance_log
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-10
author: Junie
quality_score: 9.2/10
tags: [decisions, assumptions, open-questions, risks]
visibility: public
version: 1.0
---

# Decision Log, Assumptions, and Open Questions

Purpose: Maintain a clear history of key decisions, explicit assumptions, stakeholder questions, and risks with mitigations. This supports auditability and aligned execution across teams and agents.

## A) Decisions Register
| ID | Decision | Date | Owner | Rationale | Status |
|----|----------|------|-------|-----------|--------|
| D-001 | Vendor-agnostic design with pluggable model/tool adapters | 2025-08-09 | Product | Reduce lock-in; support privacy/residency and cost optimization | Decided |
| D-002 | Deterministic demo mode with offline artifacts fallback | 2025-08-09 | Eng | Ensure reliability for client presentation | Decided |
| D-003 | MVP scope: 1–2 roles, 2 candidates each | 2025-08-09 | Product | Scope discipline for 5-day timeline | Decided |
| D-004 | Compliance-by-design: EEO-safe prompts, PII redaction policy | 2025-08-09 | Compliance | Reduce legal risk and build trust | Decided |
| D-005 | Demo roles fixed: Senior Backend (Platform) + Mid-level Backend (Platform) | 2025-08-10 | Product | Align with platform team needs and context | Decided |
| D-006 | Demo ingestion via Google Drive sleipnir-demo-inbox (sandbox) | 2025-08-10 | Eng | Fast, simple ingestion for 5-day demo | Decided |
| D-007 | Stage weights (Values 0.30, Competencies 0.50, Experience 0.20) | 2025-08-10 | Product | Emphasize platform safety and speed per context | Decided |
| D-008 | Scoring scale Dreyfus 1–5 with evidence anchors | 2025-08-10 | Product | Consistent, interpretable scoring aligned with growth | Decided |
| D-009 | Compliance posture proposal: KR-only residency for prod; retention; approved providers & constraints | 2025-08-10 | Compliance | Reduce risk, align with client expectations | Proposed |
| D-010 | Pilot KPIs proposal: TTH ≤ 20–24d, ≥35–50% interviewer hours saved, quality ≥8.5/10, adoption thresholds | 2025-08-10 | Product | Clear success criteria to evaluate pilot | Proposed |

Add future entries as rows; update Status: Proposed / Decided / Superseded.

## B) Assumptions (Current)
- Client will accept a working demo vs. full integration for first presentation.
- Company values and role competencies are available or can be provided quickly.
- Pilot will run with limited roles and candidates to validate value.
- Data may be processed in a compliant manner without cross-border restrictions for demo; final product will support residency controls.

## C) Open Questions / Information Requests (Action Needed)
Please provide or confirm the following to accelerate execution:
1) Target roles for the first demo and pilot (titles, seniority).
2) Role competencies and required experience levels per role.
3) Company values priority/weights for evaluation.
4) Must-have integrations for the pilot (email/calendar/ATS/storage?).
5) Data residency and security constraints (e.g., EU-only processing?).
6) Pilot scope preferences (4–6 weeks?): success criteria and KPIs.
7) Buyer team composition and procurement steps (security review, DPA timing).
8) Budget range and willingness-to-pay expectations by segment (if any).

## D) Risks & Mitigations
- Model output variability → Fix seeds; cache outputs; few-shot exemplars.
- Compliance exposure → Pre-review prompts/artifacts; EEO-safe filters; PII redaction.
- Demo failure risk → Offline artifacts fallback; rehearsals; preflight checklist.
- Cost overrun risk → Token/cost telemetry; provider routing; prompt optimization.

## E) Change History
- 2025-08-09: Initial log created with core decisions, assumptions, and open questions.
