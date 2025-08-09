---
id: mvp_plan_5day_demo
type: execution_plan
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [mvp, demo, plan, execution, 5-day]
visibility: public
version: 1.0
---

# 5-Day MVP and Client Demo Plan

Purpose: Deliver a compelling, working demo of the context-centric multi-agent HR automation flow with clear business value, while scoping for speed and reliability. This plan targets a client presentation in 5 days.

## Objectives
- Demonstrate end-to-end hiring workflow on a sample role:
  1) Ingestion of multi-format candidate materials
  2) Screening summary and risk flags
  3) Take-home assignment matching and evaluation template
  4) Interview kit generation (BEI + technical)
  5) Stage-by-stage evaluations and decision rationale
- Show customization by company values and role requirements.
- Present business case: ROI, time savings, quality uplift.

## Scope (MVP)
- Sources: Google Drive "sleipnir-demo-inbox/" (resumes/, portfolios/, job_descriptions/, evaluations/); email forward (eml/pdf); manual upload (pdf/docx/md); GitHub link; basic images (jpeg/png) for portfolio.
- Roles: Senior Backend Engineer (Platform), Mid-level Backend Engineer (Platform).
- Outputs: Screening report, assignment packet (from existing templates), interview kit, evaluation sheets.
- Config: Company values and role-specific competencies loaded from context/.
- Non-goals (for demo): Full ATS integration, advanced analytics, production SSO, full multi-tenant RBAC.

## Assumptions
- Context directory has mission/values and hiring stages (already present).
- Existing prompts in ai_docs/prompts can be reused and extended.
- Demo will run with a fixed seed/context bundle for determinism.

## Dependencies
- Prompts and templates availability (reuse existing under ai_docs/prompts and artifacts/public/hiring/*)
- Sample candidate data and artifacts
- Basic ingestion handlers (manual upload + stubbed email parser)

## Critical Path (High-Level)
1) Curate sample inputs and company context
2) Configure prompts and deterministic demo workflow
3) Produce outputs end-to-end for 1 role and 2 candidates
4) Package outputs into a client-facing deck and demo script

---

## Day-by-Day Plan

### Day 1 — Setup, Inputs, and Context
- Gather and normalize sample candidate materials (2 candidates/role):
  - Resume PDFs; optional GitHub links; 1 markdown portfolio/example each
- Confirm company values, role competencies, and hiring stages are present/updated in context/.
- Align demo storyline and success criteria with stakeholder.
- Deliverables:
  - Demo dataset in data/public/hiring/resume/ and artifacts/public/hiring/input_samples/
  - Confirmed values/competencies doc snapshot

### Day 2 — Ingestion & Screening
- Implement lightweight ingestion workflow:
  - Google Drive "sleipnir-demo-inbox/" (resumes/, portfolios/, job_descriptions/, evaluations/)
  - Manual file drop + email stub parser (spec/doc for now if code not required)
- Run screening prompt to generate:
  - Executive summary, strengths/risks, competency match
- Deliverables:
  - Screening reports per candidate in artifacts/public/hiring/evaluation/
  - Ingestion workflow spec and checklist

### Day 3 — Assignments & Interview Kits
- Select or adapt take-home assignments from artifacts/public/hiring/takehome_assignment/
- Generate evaluation sheets using ai_docs/prompts/hiring/evaluate_take_home_assignment_prompt.md
- Generate interview kits (BEI + technical) using existing prompts
- Deliverables:
  - Assignment packet and evaluation sheet per candidate
  - Interview guide + script per candidate

### Day 4 — Evaluation Summaries & Demo Assembly
- Compile stage-by-stage evaluations; create decision rationale template.
- Assemble outputs into a narrative flow for the demo.
- Draft pitch deck and one-pager with ROI metrics and client’s value mapping.
- Deliverables:
  - Consolidated evaluation summaries
  - Pitch deck outline + one-pager draft

### Day 5 — Rehearsal, Quality Gates, and Final Packaging
- Apply quality gates (below). Dry run the demo 2–3 times.
- Finalize deck, demo script, and preflight checklist.
- Deliverables:
  - Final deck, demo script, preflight checklist
  - Demo artifacts bundle with fixed seed/context

---

## Task List in Optimal Execution Order
1. Confirm client role(s) and values focus
2. Lock demo storyline and success metrics
3. Prepare sample candidate inputs
4. Validate context files (mission/values, hiring stages)
5. Configure prompts and deterministic settings
6. Run screening → refine prompts
7. Generate take-home packets and evaluation sheets
8. Generate interview kits (BEI + technical)
9. Compile evaluation summaries and decision rationale
10. Build pitch deck and one-pager
11. Rehearse demo; address gaps
12. Final QA, package demo bundle

## Success Metrics (Demo)
- Time-to-hire savings shown with modeled calculations
- Quality score of generated materials ≥ 8.5/10
- Clear customization mapping to client values/competencies
- Adoption: ≥ 80% interviewer usage of standardized kits; rubric completion rate ≥ 90%
- Stakeholder confidence ≥ 4/5 in pilot adoption

## Quality Gates & Checklists (Demo Edition)
- Context completeness check (values, role profile, stages)
- Legal compliance pass (no discriminatory language; job-relevant criteria)
- Consistency checks across outputs (terminology, scoring scales)
- Bias mitigation steps documented
- Determinism: same inputs → same outputs (seeded)

## Risks & Mitigations
- Variability in LLM output → seed, few-shot examples, fixed context bundle
- Over-scope → limit to 1–2 roles and 2 candidates each
- Compliance flags → pre-review prompts and outputs; sanitize PII
- Demo reliability → offline artifacts fallback if live calls fail

## Demo Storyline (Suggested)
1) Problem framing (inconsistent, slow hiring) → client’s context and values
2) Walkthrough: ingest files → screening → assignment → interview → evaluations
3) Show customization toggles (values weight, competencies, role templates)
4) ROI model: time saved, reduced bias, improved quality
5) Next steps: pilot scope, success criteria, commercial terms

## Open Items to Confirm (Client)
- Budget constraints and preferred commercial structure for pilot and year‑1
- Confirm KR-only data residency timeline; can demo use non‑KR regions for Drive?
- Confirm acceptance of synthetic sample profiles in demo
- Preferred ATS for eventual integration; SSO requirements
- Any legal redlines (DPA/MSA templates) to pre-fill
