---
id: bedrock_hiring_workflow_integration
type: integration_plan
domain: hr_automation
created_date: 2025-08-10
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [aws_bedrock, agents, workflow, hiring]
visibility: public
version: 1.0
---

# AWS Bedrock Agents Integration: Hiring End-to-End Workflow

This document aligns the Bedrock multi-agent architecture with the canonical hiring workflow defined in:
- ai_docs\workflows\hiring_end_to_end.yaml (spec)
- ai_docs\workflows\hiring_end_to_end.md (runbook)

## Stage → Agent Mapping
1. Context Load & Verification
   - Agent: Context Manager Agent
   - Services: S3 (context bundle), Bedrock Knowledge Bases
   - Outputs: context verification, checklist adherence
2. Intake & Normalization
   - Agent: Profile Processor Agent
   - Tools: PII Redactor, JSON Normalizer
   - Outputs: data\public\hiring\working\{run_id}\candidates.normalized.json
3. JD Mapping & Competency Alignment
   - Agent: Analysis Agent
   - Tools: Embeddings compare (JD ↔ profile), Values matcher
   - Outputs: jd_mapping.json per candidate
4. Automated Screening & Recommendation
   - Agent: Screening Agent
   - Prompts/Plans: ai_docs\plans\candidate_screening_plan.md
   - Approval: Platform Lead (gate)
   - Outputs: artifacts\public\hiring\evaluation\{Candidate}_screening_report.md
5. Personalized Take-Home Assessment
   - Agent: Assessment Generator
   - Inputs: jd_mapping, screening_report
   - Outputs: assignment.md, evaluation_sheet.md under takehome_assignment\upcoming\{candidate_id}
5b. Take-Home Assignment Evaluation
   - Agent: Assessment Evaluator
   - Checks: Verify GitHub collaborator access to candidate repo (collaborator: ${inputs.evaluator_github_handle})
   - Prompt: ai_docs\prompts\hiring\evaluate_take_home_assignment_prompt.md (standard single-assignment)
   - Outputs: artifacts\public\hiring\evaluation_sheets\upcoming\{candidate_id}\takehome_evaluation.md
   - Decision: Proceed if weighted score \u2265 60% (\u2265 3.0/5), else stop before interview kits
6. Interview Kit Generation
   - Agent: Interview Kit Generator
   - Prompt: ai_docs\prompts\hiring\generate_interview_kit_prompt.md
   - Outputs: candidate_context.md, interview_guide.md, interview_script.md
7. Structured Interview Loop (Human-led)
   - Support: Orchestrator Agent for scheduling and notes templates
   - Bank: artifacts\public\hiring\pair_programming\
8. Post-Interview Consolidation & Scoring
   - Agent: Scoring & Consolidation Agent
   - Functions: Bias check, weighted scoring, rationale generation
   - Outputs: evaluation_sheets\upcoming\{candidate_id}\summary.md
9. Decision, Offer, and Audit
   - Agent: Decision & Audit Agent (human-in-the-loop)
   - Outputs: private decision/offer artifacts + data\public\sleipnir_flow\hiring_runs\{run_id}.json

## Guardrails & Approvals
- Implement approval gates via Orchestrator requiring Platform Lead ID capture at screening, assessment, and interview kits.
- Enforce quality threshold ≥ 8.5/10 on generated materials; re-run or revise on failure.

## Event & Storage Topology
- Inputs: data\public\hiring\resume\candidates.json
- Public Artifacts: artifacts\public\hiring\...
- Private Artifacts: artifacts\private\hiring\...
- Audit: data\public\sleipnir_flow\hiring_runs\{run_id}.json

## Execution Snippet (Pseudo)
- Orchestrator loads ai_docs\workflows\hiring_end_to_end.yaml
- For each candidate: execute stages in order, honoring approval gates and writing artifacts as specified.

Refer to: 03_technical_implementation_specification.md and 20_context_management_system_specification.md for underlying Bedrock configuration.
