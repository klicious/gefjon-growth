---
id: observability_and_guardrails
type: architecture_detail
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 9.1/10
tags: [observability, guardrails, quality]
visibility: public
version: 1.0
---

# Observability & Guardrails

Purpose: Ensure safe, compliant, auditable operation with measurable quality.

## Telemetry & Logging
- Structured logs: request_id, candidate_id, stage, agent, prompt_hash, response_hash, duration_ms, model_provider, cost_estimate
- Tracing: per-stage spans; ingest → normalize → bundle → agent actions
- Artifact registry: store prompt+response, inputs, outputs URIs with checksums

## Metrics
- Quality score per artifact (1–10), threshold ≥8.5
- SLA: stage processing time targets; error rate <2%
- Cost metrics: tokens by stage, OCR costs, storage

## Policy & Safety Checks
- EEO-safe language filter; disallow protected-class inferences
- PII detection/redaction; configurable masking policies
- Job relevance classifier for questions and criteria

## Bias Mitigation
- Standardized rubrics; values/competencies weighting documented
- Blind review where possible (remove name/photo)
- Regular audits: outcome parity checks across demographics (if data available)

## Evaluation Harness
- Golden datasets with expected outputs and scoring rubric
- Prompt tests: regression checks on changes; prompt diff + score delta alerts
- Red-team tests: adversarial inputs (garbled PDFs, deceptive resumes)

## Governance
- Approval workflow for prompt changes (PR review + human sign-off)
- Versioning: prompt versions, model versions, config snapshots
- Audit: immutable logs with retention policy

## Incident Response
- Runbooks per failure class (ingestion failure, model outage, compliance alert)
- Fallbacks: offline artifacts; alternate model/provider routing

## Checklists
- Pre-deploy: tests pass; compliance checks green; costs within budget
- Pre-demo: seed locked; outputs verified; fallback artifacts ready
