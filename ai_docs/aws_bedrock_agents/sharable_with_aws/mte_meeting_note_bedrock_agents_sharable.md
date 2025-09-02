---
id: mte_meeting_note_bedrock_agents_sharable_2025-08-21
type: meeting_note
domain: aws_bedrock_agents
created_date: 2025-08-21
last_updated: 2025-08-21
author: Junie
quality_score: __TBD__
tags: ["AWS", "Bedrock", "multi-agent", "hiring", "MTE", "sharable_with_AWS"]
visibility: public
version: 1.0
---
# MTE Meeting Note: AWS Bedrock Agents (Sharable with AWS)

Note: This document is intentionally redacted for AWS consultation. It excludes sensitive internals (detailed context engineering methods, workflow orchestration internals, and prompts). Enough information is provided to enable effective AWS architecture guidance.

---

## Proposal (Plan)
High-level goal: Implement a context‑aware, multi‑agent hiring automation system on AWS to reduce per‑candidate processing from 4–6 hours to under 20 minutes. Leverage Amazon Bedrock (agents/orchestration), Neptune (knowledge graph), OpenSearch (vector search), Step Functions, and managed compute (Lambda/ECS) for scalable, secure operation.

Short feature description (~200 chars): Automate intake → screening → assessment → interview prep → evaluation → communication with human approval gates, using Bedrock agents + Neptune + OpenSearch for context.

---

## MTE with SA Schedule
Owner SA: TBD (AWS Solutions Architect)

- 1st MTE
  - Time: TBD (proposed: 2025-08-26 10:00–11:00, KST)
  - Meeting Link: https://chime.aws/...
  - Objective: Architecture validation (Bedrock + Neptune + OpenSearch + Step Functions)
- 2nd MTE
  - Time: TBD (proposed: 2025-09-02 10:00–11:00, KST)
  - Meeting Link: https://chime.aws/...
  - Objective: Cost model, scaling patterns, security guardrails

---

## Visuals

### 1) Conceptual Architecture (Redacted)
```mermaid
graph TD
    SF[AWS Step Functions
    (Workflow Orchestration)] --> O[Orchestrator Agent
    (Bedrock)]

    O --> IN[Intake Agent]
    O --> SC[Screening Agent]
    O --> AS[Assessment Agent]
    O --> IV[Interview Agent]
    O --> EV[Evaluation Agent]
    O --> CM[Communication Agent]

    IN --> S3[(Amazon S3)]
    IN --> DDB[(DynamoDB)]

    SC --> OS[(Amazon OpenSearch
    Vector Index)]
    SC --> NP[(Amazon Neptune
    Knowledge Graph)]

    EV --> RDS[(Amazon RDS
    (PostgreSQL))]
    CM --> SES[(Amazon SES)]

    O --> CW[(Amazon CloudWatch)]
    O --> SNS[(Amazon SNS)]

    classDef svc fill:#eef7ff,stroke:#4a90e2,color:#0b3f67;
    classDef store fill:#f6fff0,stroke:#7cb342,color:#2e7d32;
    class SF,O,IN,SC,AS,IV,EV,CM,CW,SNS svc;
    class S3,DDB,OS,NP,RDS,SES store;
```

Redaction note: Detailed prompt strategies, internal decision trees, and proprietary context engineering logic are intentionally omitted.

### 2) High-Level Hiring Workflow
```mermaid
flowchart LR
    A[Resume Intake] --> B{Automated Screening}
    B -->|Pass| C[Assessment]
    B -->|Needs Review| HR[Human Review (~5m)]
    B -->|Fail| RJ[Automated Rejection Email]
    C --> D[Interview Preparation]
    D --> E[Final Evaluation]
    E --> F[Decision + HR Communication]

    note over A,F: 90%+ automation; human approvals at key gates
```

---

## Q&A (Prepared Topics for AWS)
- Bedrock Agents: Recommended patterns for tool use, memory, and delegation between specialized agents.
- Knowledge Graph + Vector: Best practices to combine Neptune and OpenSearch for context retrieval (latency, consistency, and updates).
- Orchestration: Step Functions design for long-running processes and human-in-the-loop approvals.
- Cost Optimization: Configuration guidance (rightsizing ECS/Lambda, OpenSearch tiers, Neptune sizing) to keep per-candidate cost <$10.
- Observability: CloudWatch metrics/tracing for agent steps; failure triage patterns; idempotency for retries.
- Security: IAM boundaries, Secrets Manager usage, multi-tenant isolation, PII handling and data retention.
- Scalability: Expected throughput of 60+ candidates/month initially; patterns to scale 10x without re-architecture.

---

## Deliverables

### Workflow Image
Visuals embedded above via mermaid diagrams (Architecture and Workflow).

### Implemented Features Description (~500 chars)
The current prototype automates resume intake, normalizes candidate profiles, and performs automated screening against core criteria with explainable summaries. It generates assessment and interview preparation artifacts and consolidates an evaluation recommendation. Sensitive internals (prompting, context-engineering specifics, orchestration logic) are redacted, while AWS service boundaries (Bedrock, Neptune, OpenSearch, Step Functions, S3, RDS/DynamoDB) are defined for consultation.

### Execution Result (Sample)
Reference: ./sharable_io_samples.md (full multi-stage examples)

- Input (Batch candidates JSON)

```json
{"run_id":"demo_2025-08-21","role":"Backend Engineer","candidates":[{"candidate_id":"cand_001","display_name":"Candidate A","resume_url":"s3://redacted/resumes/cand_001.pdf"},{"candidate_id":"cand_002","display_name":"Candidate B","resume_url":"s3://redacted/resumes/cand_002.pdf"}]}
```

- Outputs (selected stages)

Stage 2 — Screening
```json
{"candidate_id":"cand_001","stage":"screening","recommendation":"PASS","confidence":"HIGH"}
```

Stage 3 — Take-Home Evaluation
```json
{"candidate_id":"cand_001","stage":"takehome_evaluation","weighted_total":3.6,"summary":"Meets bar; improve tests/logging."}
```

Stage 5 — Final Evaluation
```json
{"candidate_id":"cand_001","stage":"final_evaluation","overall_recommendation":"Hire","human_decision":{"approved":true}}
```

---

## References (Sharable Only)
- Executive Summary: ./sharable_executive_summary.md
- Conceptual Architecture: ./sharable_conceptual_architecture.md
- Hiring Workflow: ./sharable_hiring_workflow.md
- Technical Overview: ./sharable_technical_overview.md
- Integrations: ./sharable_integrations.md

---

## Compliance & Redaction Statement
This document is designed for AWS consultation and excludes sensitive intellectual property:
- No proprietary prompts or detailed context engineering methods
- No internal orchestration/state machine specifics beyond high-level design
- No confidential business rules

We welcome AWS guidance on architecture, cost, security, and scalability within the defined service boundaries.
