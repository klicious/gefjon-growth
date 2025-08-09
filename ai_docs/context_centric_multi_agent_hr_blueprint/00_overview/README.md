---
id: overview_index
type: overview_index
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-10
author: Junie
quality_score: 9.3/10
tags: [overview, executive, value-proposition]
visibility: public
version: 1.1
---

# Executive Overview

Purpose: Provide a concise, C-level briefing on the opportunity, vision, and path to a working client-ready model in 5 days.

## Elevator Pitch
Gefjon Growth is a context-centric, multi-agent HR automation platform that converts your mission, values, and role definitions into deterministic, auditable hiring workflows. In 5 days, we deliver an end-to-end, client-ready loop — ingestion → screening → assignments → interviews → evaluations — tailored to your values and role-specific competencies, reducing time-to-hire by 40–60% and interviewer hours by 35–50%.

## Why We Win (Differentiators)
- Context Fabric: Company values, team norms, and role competencies drive every artifact and decision.
- Orchestrated Multi-Agent Flow: Specialized agents collaborate for screening, assignment design, interviews, and scoring.
- Governance by Design: EEO-safe prompts, PII redaction, structured JSON audit logs, and role-based access.
- Deterministic Demo Mode: Seeded runs with fixed context bundles; offline artifacts fallback for reliability.
- Vendor-Agnostic: Pluggable model/tool adapters for privacy, cost, and residency optimization.

## Architecture at a Glance
- Ingestion & Normalization: Drive sandbox inputs (resumes, portfolios, JDs) and multi-format parsing.
- Context Layer: Values, competencies, stage weights, and prompts stored under context/ with overrides per client.
- Orchestration: Stage-by-stage agent workflows with weighted scoring and evidence capture.
- Observability & Guardrails: Structured logs, trace IDs, bias checks, and quality scoring.
- See: ../03_architecture/architecture_overview.md

## Security & Compliance Snapshot
- KR-only data residency for production; demo may use non-KR regions with non-sensitive data.
- Retention (proposed): 12 months for rejected; purge raw artifacts after 6 months for hired; DSAR-ready.
- Approved providers (proposed): OpenAI, Google, Anthropic, local Ollama; no training on customer data; ≤30-day logs; option to disable logging.
- Audit: Immutable, structured JSON with approver IDs and export cadence.
- See: ../04_security_compliance/security_compliance_and_data_governance.md

## Proof in 5 Days (What You Will See)
- End-to-end outputs for two platform roles (Senior & Mid-level Backend):
  - Screening reports with strengths/risks and competency/value alignment
  - Take-home assignment packets and evaluation sheets
  - Interview guides and scripts (BEI + technical)
  - Consolidated evaluation summaries with weighted scoring and rationale
- Deterministic run using a fixed context bundle and seed.
- See: ../06_execution_roadmap/mvp_plan_5day_demo.md

## KPIs & ROI
- Time-to-hire reduction: 40–60%
- Interviewer time savings: 35–50%
- Quality score of generated materials: ≥ 8.5/10
- Adoption: ≥ 80% interviewer usage of standardized kits; rubric completion ≥ 90%

## Risks & Mitigations
- Model variability → Seeded runs, few-shot exemplars, cached outputs.
- Compliance exposure → Pre-reviewed prompts, EEO-safe content, PII redaction, audit trails.
- Demo reliability → Offline artifacts fallback; preflight checklist and rehearsals.

## Readiness Checklist (Client Input)
- Confirm demo roles and competency matrices.
- Provide or approve values weighting and stage weights.
- Share 2 sample candidate profiles per role (or accept synthetic profiles).
- Confirm demo ingestion via Drive sandbox; flag any ATS/SSO priorities for pilot.
- See: ../10_open_questions/missing_information_requests.md and ../10_open_questions/decision_log.md

## Links
- Business Model: ../05_business_model/business_model_and_pricing.md
- Architecture: ../03_architecture/architecture_overview.md
- Security/Compliance: ../04_security_compliance/security_compliance_and_data_governance.md
- 5-Day Plan: ../06_execution_roadmap/mvp_plan_5day_demo.md
