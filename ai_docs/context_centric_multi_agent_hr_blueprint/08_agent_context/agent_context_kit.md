---
id: agent_context_kit
type: agent_kit
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 9.3/10
tags: [agent, context, mcp, prompts]
visibility: public
version: 1.0
---

# Agent Context Kit

Purpose: Provide a consistent, structured context package that AI agents can load to perform hiring automation tasks end-to-end with guardrails, using the Context Engineering Protocol.

## Context Engineering Protocol (Mandatory)
1) Load Company and Process Context
- context/company_info/mission_vision_values.yaml
- context/company_info/goals_okrs.yaml
- context/hr_processes/hiring/hiring_stages.yaml
- context/teams/<team>.yaml (when applicable)

2) Load Candidate Inputs and Artifacts
- data/public/hiring/resume/*.json or PDFs under artifacts/public/hiring/input_samples/
- artifacts/public/hiring/takehome_assignment/* (role-based)
- artifacts/public/hiring/interview_materials/* (if reusing)

3) Verify Completeness
- Company values and role profile present
- Hiring stages configured
- Candidate materials available
- If missing, STOP and request: target role, values emphasis, candidate inputs

4) Produce and Store Outputs
- Public outputs → artifacts/public/hiring/*
- Sensitive outputs → artifacts/private/*
- Maintain metadata headers and quality scores ≥ 8.5/10

## MCP Servers (Recommended)
- exa: research competitors, benchmarks, candidate/company background
- sequential-thinking: plan tasks and decompose multi-stage workflows
- playwright: optional for portfolio validation walkthroughs
- fetch: retrieve assets/JSON endpoints (e.g., GitHub README)

## Input Specs (Minimum)
- role_id (string), role_competencies (list), values (list)
- candidate_materials: list of URIs/paths (pdf/docx/md/pptx/xlsx/csv/images/eml/urls)
- config: weights {values_alignment, competencies, experience_relevance}, excerpt_policy

## Output Specs
- ScreeningReport.md with strengths/risks, competency and value alignment
- AssignmentPacket (instructions + evaluation sheet)
- InterviewGuide.md + InterviewScript.md
- EvaluationSummary.md with stage_scores and decision rationale

## Prompts to Use (Pointers)
- ai_docs/prompts/hiring/generate_interview_kit_prompt.md
- ai_docs/prompts/hiring/evaluate_take_home_assignment_prompt.md
- ai_docs/prompts/hiring/generate_interview_process_prompt.md

## Safety & Compliance Checklist (Quick)
- Remove protected-class inferences; ensure job relevance
- Redact PII where required before model calls
- Log prompts/responses, approver IDs, timestamps

## Deterministic Mode (Demo)
- Fix seeds
- Use snapshot context bundles
- Cache outputs; keep offline copies

## Missing Information Protocol
If any required inputs are missing, ask the task provider for:
- Target roles and competencies
- Company values priority/weights
- Candidate input files/links
- Any must-have integrations or compliance constraints
