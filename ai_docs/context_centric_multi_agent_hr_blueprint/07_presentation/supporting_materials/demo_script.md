---
id: demo_script_client_pitch
type: demo_script
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 9.2/10
tags: [demo, script, presentation]
visibility: public
version: 1.0
---

# Client Demo Script (Working Model)

Purpose: Provide a polished, time-boxed script to demonstrate the end-to-end hiring automation with customization to client values and role requirements. Target duration: 20–25 minutes + 10 minutes Q&A.

## Roles
- Presenter: Founder/PM
- Driver: Engineer (handles screens)
- Backup: Analyst (answers market/pricing/compliance)

## Setup Checklist (Preflight)
- Deterministic mode enabled (fixed seed/context bundle)
- All inputs and outputs pre-generated in case of network issues
- Fallback offline deck ready (PDF)

## Agenda (Slide Titles)
1. The Problem: Slow, inconsistent, and biased hiring
2. Our Approach: Context-centric, multi-agent automation
3. Live Demo: Resume → Screening → Assignment → Interview → Evaluation
4. Customization: Company values and role competencies
5. ROI & Business Case
6. Security, Compliance, and Guardrails
7. Pilot Proposal & Next Steps

## Live Demo Walkthrough

1) Inputs and Context (2 min)
- Show context/company_info/mission_vision_values.yaml and context/hr_processes/hiring/hiring_stages.yaml
- Explain how values and stages drive downstream generation

2) Ingestion & Screening (5 min)
- Display sample inputs in data/public/hiring/resume/
- Trigger screening (use pre-generated artifacts)
- Open artifacts/public/hiring/evaluation/<candidate>_screening_report.md
- Narrate strengths/risks and competency alignment

3) Take-Home Assignment & Evaluation (4 min)
- Open artifacts/public/hiring/takehome_assignment/<role>/ (instructions)
- Show evaluation sheet template in artifacts/public/hiring/evaluation_sheets/upcoming/
- Explain scoring rubric and fairness

4) Interview Kit Generation (4 min)
- Open artifacts/public/hiring/interview_materials/upcoming/<candidate>/interview_guide.md and interview_script.md
- Show BEI questions aligned to values; technical deep-dive sections

5) Stage-by-Stage Evaluation & Decision (3 min)
- Present consolidated evaluation template (from 06_execution_roadmap outputs)
- Explain weighted scoring and rationale capture

6) Customization Highlights (2 min)
- Show how changing weights/values in config impacts outputs (describe deterministic example)

## ROI & Business Model (3 min)
- Time-to-hire reduction (40–60% target), interviewer hours saved (60–80%)
- Refer to 05_business_model/business_model_and_pricing.md

## Security & Compliance (2 min)
- Summarize 04_security_compliance/security_compliance_and_data_governance.md
- Emphasize audit logs, PII handling, EEO-safe content

## Pilot Proposal (2 min)
- 4–6 week pilot for 1–2 roles; success criteria: quality ≥8.5/10, time saved, adoption
- Pricing options and design partner program

## Q&A (10 min)
- Common questions: integrations, data residency, model providers, bias mitigation

## Appendices
- Architecture: 03_architecture/architecture_overview.md
- Observability & Guardrails: 03_architecture/observability_and_guardrails.md
- Ingestion & Context Fabric: 03_architecture/ingestion_and_context_fabric.md
