---
id: blueprint_hiring_workflow_integration
type: integration_plan
domain: hr_automation
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.2/10
tags: [blueprint, execution, workflow, hiring]
visibility: public
version: 1.0
---

# Execution Roadmap Integration: Hiring End-to-End Workflow

This document operationalizes the Context-Centric Multi-Agent HR Blueprint against the canonical hiring workflow:
- ai_docs\workflows\hiring_end_to_end.yaml (spec)
- ai_docs\workflows\hiring_end_to_end.md (runbook)

## Alignment to Architecture
- Context Layer → Consumed at Stage 1 (Context Load & Verification):
  - context\company_info\mission_vision_values.yaml
  - context\hr_processes\hiring\hiring_stages.yaml
  - artifacts\public\hiring\interview_process.md
- Orchestration Layer → Stage-by-stage execution with approval gates and quality thresholds.
- Observability & Guardrails → Audit logs, bias checks, quality scoring ≥ 8.5/10.

## Stage Ownership & Handoffs
1. Context Load & Verification — Context Manager Agent → Orchestrator
2. Intake & Normalization — Profile Processor → Analysis Agent
3. JD Mapping & Competency Alignment — Analysis Agent → Screening Agent
4. Screening & Recommendation — Screening Agent → Platform Lead (Approval)
5. Take-Home Assessment — Assessment Generator → Platform Lead (Approval)
5b. Take-Home Assignment Evaluation — Assessment Evaluator → Platform Lead (Decision Gate)
6. Interview Kit Generation — Interview Kit Generator → Platform Lead (Approval)
7. Interview Loop (BEI, Pair-Programming, System Design, Deep-Dive) — Human Interviewers
8. Consolidation & Scoring — Scoring Agent → Hiring Manager
9. Decision, Offer, Audit — Decision & Audit Agent → HR Ops

## Outputs & Storage Map
- Public: artifacts\public\hiring\...
- Take-home evaluation: artifacts\public\hiring\evaluation_sheets\upcoming\{candidate_id}\takehome_evaluation.md
- Private: artifacts\private\hiring\...
- Audit: data\public\sleipnir_flow\hiring_runs\{run_id}.json

## 5-Day Demo Tie-in
- Day 1–2: Context Load, Intake, JD Mapping
- Day 2–3: Screening, Take-Home Generation & Evaluation (GitHub collaborator access verified)
- Day 3–4: Interview Kits and Loop Scheduling
- Day 4–5: Consolidation, Decision Draft, Audit Log

## KPIs & Quality Gates
- Artifact quality ≥ 8.5/10; approval gates at screening, assessment, kits.
- Take-home proceed threshold: weighted score ≥ 60% (≥ 3.0/5) prior to interview kits.
- Rubric completion ≥ 90%; time-to-hire reduction 40–60%.

## How to Run
- Follow the runbook and invoke prompts per stage; for interview kits use:
  gemini run \
    --prompt "ai_docs\prompts\hiring\generate_interview_kit_prompt.md" \
    --context "data\public\hiring\resume\candidates.json"

Refer to 06_execution_roadmap\mvp_plan_5day_demo.md for timeboxed execution.
