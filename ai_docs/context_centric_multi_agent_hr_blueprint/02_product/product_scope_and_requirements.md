---
id: product_scope_and_requirements
type: product_spec
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-10
author: Junie
quality_score: 9.2/10
tags: [product, requirements, customization]
visibility: public
version: 1.0
---

# Product Scope and Requirements

Purpose: Define scope, personas, user stories, functional/non-functional requirements, and customization framework for a context-centric HR automation platform.

## Personas & Primary Jobs-To-Be-Done (JTBD)
- VP People / Head of TA: Reduce time-to-hire, ensure fairness/compliance, reporting.
- Hiring Manager (Eng/Product): High-signal evaluations, consistent interview kits.
- Recruiter / Coordinator: Automate manual tasks, candidate comms, scheduling.

## Scope (v1)
- Multi-format ingestion: pdf, docx, md, pptx, xlsx/csv, images (jpeg/png), eml, URLs (GitHub/Notion).
- Pipeline automation: Screening → Assignment → Interview → Evaluation.
- Customization: Company values, role competencies, stage weights, scoring rubrics.
- Outputs: Screening reports, assignment packets + rubrics, interview guides/scripts, evaluation summaries.
- Governance: RBAC, audit logs, bias checks, PII handling.

## Out-of-Scope (v1)
- Full ATS/HRIS integration; SSO/SAML; advanced analytics dashboards; multi-tenant billing.

## User Stories (Selected)
- As a Hiring Manager, I want to upload diverse candidate materials so the system can produce a holistic screening summary and risk flags.
- As a Recruiter, I want role-specific interview kits aligned to our values so interviews are consistent and fair.
- As a VP People, I want audit logs of every decision so I can ensure compliance and defend decisions.

## Functional Requirements
1. Ingestion & Normalization
   - Accept listed formats; extract text and metadata; OCR for images.
2. Screening
   - Generate executive summary, strengths/risks, competency/value alignment.
3. Assignments
   - Select matching take-home; generate instructions and evaluation sheets.
4. Interview Kits
   - Produce BEI + technical guides and scripts tailored to role and values.
5. Evaluations
   - Aggregate stage results with weighted scoring and rationale.
6. Customization & Config
   - Company values, competencies, stage weights, role templates stored in context/.
7. Governance
   - PII detection/redaction, EEO-compliant prompts, audit logging.

## Non-Functional Requirements
- Reliability: Deterministic demo mode (seeded), offline artifacts fallback.
- Security: RBAC, encryption at rest/in transit for sensitive data, least privilege.
- Compliance: GDPR data subject rights; consent and retention policies.
- Scalability: Process 10–50 candidates/hour per project in v1; horizontally scalable later.
- Observability: Structured logs, quality scoring, trace IDs.

## Customization Framework
- Values & Competencies: YAML under context/company_info and context/teams.
- Role Templates: context/hr_processes/hiring/hiring_stages.yaml + artifacts for role-specific kits.
- Scoring Weights: Config file per client/role.
- Prompt Overrides: ai_docs/prompts overrides via configuration.

## Demo Configuration (5-Day)
- Demo Roles: Senior Backend Engineer (Platform), Mid-level Backend Engineer (Platform)
- Stage Weights (sum 1.0): Values Alignment 0.30; Competencies 0.50; Experience Relevance 0.20
- Scoring Scale: Dreyfus 1–5 (1 Novice → 5 Expert); use per-dimension anchors and evidence fields
- Interview Formats & Timeboxes: Screen 30–40m; System Design 60m; Pair Programming 60m; Culture & Mentorship 30–45m; Loop retro 15m
- Take-home Pass Gates:
  - Senior: coverage ≥ 70%, rollback plan, SLO thinking, secretless config
  - Mid-level: tests pass, basic metrics exposed, clean structure, no hardcoded secrets
- Demo Ingestion: Google Drive "sleipnir-demo-inbox/" (resumes/, portfolios/, job_descriptions/, evaluations/) as primary sandbox source

## Acceptance Criteria (v1)
- Given candidate inputs in supported formats, system produces all outputs with quality ≥ 8.5/10 (human-rated) and no compliance violations.
- Admin can adjust values/competencies/weights and see changes reflected in outputs.

## Open Questions
- Priority integrations for pilot? (Calendar, email, ATS)
- Minimal RBAC roles for v1? (Admin, Recruiter, Interviewer)
