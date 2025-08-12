---
id: data_ingestion_normalization_pipeline
type: architecture_spec
domain: hr_automation
created_date: 2025-08-11
last_updated: 2025-08-11
author: Junie
quality_score: 9.4/10
tags: [architecture, ingestion, normalization, pipeline, pii]
visibility: public
version: 2.0
---

# Data Ingestion & Normalization Pipeline — Enhanced

## Purpose
Define how we ingest candidate-related materials from multiple sources and formats, extract/normalize content, protect PII, and publish structured events and vectors for downstream screening and interview orchestration using Top-Tier Industry Standards.

## Goals
- Accept broad inputs (email, uploads, cloud drives, links) and common formats (PDF/DOCX/PPTX/XLSX, MD/Notion exports, images/scans, ZIP bundles, links)
- Normalize into a consistent schema with provenance and consent, enabling explainable evaluation and auditability
- Enable multilingual content (EN/KR initially) and robust OCR for scanned PDFs/images
- Enforce privacy-by-design (PII tagging/redaction), cost/latency budgets, and idempotent processing
- Support Top-Tier Industry Standards evaluation framework with production-ready data handling

## Cross-References
- `00_overview/README.md` (scope, MVP)
- `03_architecture/architecture_overview.md` (PRD & architecture)
- `02_product/evaluation_framework_and_customization_engine.md` (how normalized data feeds the DSL)
- `04_security_compliance/security_compliance_and_data_governance.md` (PII, audit, retention)
- `06_execution_roadmap/task_breakdown.md` (tasks & AC)
- `ai_docs/aws_bedrock_agents/10_graph_rag_context_infrastructure.md` (context graph)
- `ai_docs/aws_bedrock_agents/07_token_optimization_specification.md` (cost controls)

## Supported Ingestion Channels (v1)
- **Email**: Gmail API / MS Graph (O365); parse messages + attachments; capture sender/subject/date/labels
- **Manual uploads**: Web app/CLI drag-drop; capture uploader identity and consent
- **Cloud drives**: Google Drive/OneDrive file pickers; background sync (optional v2)
- **Links**: GitHub repos/issues, public URLs; fetch/clone and snapshot
- **Bundles**: ZIP packages containing multi-format artifacts

## Supported Formats and Parsers (v1)
- **Text/PDF**: PDF text extraction (pdfminer) with fallback OCR for image-based PDFs (AWS Textract or equivalent)
- **DOCX/PPTX**: python-docx/python-pptx; extract text, tables, speaker notes; track slide/page numbers
- **XLSX/CSV**: openpyxl/csv; parse sheets; coerce to canonical tables
- **Markdown/HTML/Notion export**: frontmatter + content; sanitize and convert to text/sections
- **Images (JPEG/PNG)**: OCR with language detection; preserve bounding boxes for citations (optional)
- **Repos/Code links**: Shallow clone; language stats; readme; last N commit messages; optionally embed code summaries

## Pipeline Flow (Production-Ready)

### 1. Intake
- Receive payload from channel; assign intake_id and idempotency key (hash of content + metadata)
- **Production Considerations**: Rate limiting, malware scanning, size validation

### 2. Type Detection
- MIME sniff + magic bytes + extension; route to parser(s)
- **Resilience**: Fallback parsers for corrupted files

### 3. Parsing/OCR
- Extract text, structure, metadata (page/slide numbers, tables, images), detect language(s)
- **Quality Gates**: Validation of extracted content, confidence scoring

### 4. PII Tagging/Redaction
- Detect emails/phones/addresses and selected demographics; create redacted view for model input; keep original encrypted
- **Compliance**: GDPR-ready redaction with audit trails

### 5. Normalization
- Map to canonical entities (Candidate, Submission, Artifact, ParsedChunk, Event)
- **Data Quality**: Schema validation, consistency checks

### 6. Storage & Provenance
- Store raw (S3 encrypted), normalized (DynamoDB/JSON), and computed vectors; record provenance (source, path, hash, timestamps)
- **Observability**: Full lineage tracking for audit and debugging

### 7. Vectorization
- Chunk text with policy; embed and index in vector store; attach chunk->vector mapping
- **Cost Optimization**: Caching, batch processing, model routing

### 8. Event Publishing
- Emit INGESTED, PARSED, NORMALIZED, VECTORIZED events to EventBridge/SNS/SQS
- **Integration**: Enable downstream processing and monitoring

### 9. Error Handling
- Retries with backoff; DLQ; poison-pill quarantine; operator alerts
- **Reliability**: Circuit breakers, graceful degradation

## Normalization Schema (v1)

### Core Entities
```json
{
  "organization": {
    "id": "string",
    "name": "string",
    "settings": {
      "evaluation_standards": "top_tier_industry",
      "pii_policy": "strict",
      "retention_days": 365
    }
  },
  "candidate": {
    "id": "cand_01HZY3...",
    "external_ids": [{"system": "email", "value": "applicant@example.com"}],
    "name": {"full": "Kwon Min-Seung"},
    "emails": ["applicant@example.com"],
    "languages": ["ko", "en"],
    "links": [{"type": "github", "url": "https://github.com/kwonms"}],
    "evaluation_context": {
      "standards_applied": "top_tier_industry",
      "production_readiness_focus": true
    }
  },
  "submission": {
    "id": "subm_01HZY4...",
    "candidate_id": "cand_01HZY3...",
    "source": {"type": "email", "details": {"provider": "gmail", "thread_id": "17892..."}},
    "received_at": "2025-08-09T07:12:03Z",
    "consent": {"granted": true, "source": "email", "timestamp": "2025-08-09T07:12:05Z"},
    "quality_score": 9.2
  },
  "artifact": {
    "id": "art_01HZY5...",
    "submission_id": "subm_01HZY4...",
    "kind": "document",
    "format": "pdf",
    "filename": "Kwon_Min-Seung_Resume.pdf",
    "sha256": "3b2f...",
    "language": ["ko"],
    "pii_tags": ["email", "phone"],
    "storage": {"bucket": "ingest-raw", "key": "2025/08/09/...pdf"},
    "provenance": {"channel": "email", "origin_path": "attachment:Kwon_Min-Seung_Resume.pdf"},
    "production_indicators": {
      "code_quality_signals": [],
      "architecture_patterns": [],
      "testing_evidence": []
    }
  }
}
```

## Chunking & Embedding Policy (Production-Optimized)
- **Chunk size**: 800–1200 tokens with 100–150 overlap; tighter for OCR text
- **Separate channels**: Resume vs. portfolio/code; tag chunks by artifact kind
- **Caching**: Embed once; reuse via cache keyed by sha256 and model version
- **Quality**: Confidence scoring for chunk relevance and completeness

## PII Tagging & Redaction (GDPR-Ready)
- **Detect**: email, phone, address, date of birth, national ID (disable by region), photo, school names
- **Redact**: For LLM prompts; retain original encrypted with restricted access
- **Audit**: Log PII access as AuditEvent with purpose; include in DSR exports
- **Compliance**: Automated retention policies, consent management

## Error Handling & Idempotency (Production-Grade)
- **Idempotency key**: sha256(content) + normalized metadata; duplicate drops with reference counter
- **Retries**: 3 attempts with exponential backoff; DLQ after 3; quarantine bucket for manual review
- **Partial failures**: Mark artifact status; continue other artifacts; emit ERROR events
- **Monitoring**: Real-time alerts, SLA tracking, performance dashboards

## Security Controls (Enterprise-Ready)
- **Malware scanning**: On intake; size limits and type allowlist
- **Encryption**: At rest (S3 SSE-KMS) and transit (TLS1.2+); per-tenant keys in Growth+
- **Access control**: Least-privilege IAM; VPC endpoints for APIs; no public buckets
- **Audit**: Redacted logs; secrets in AWS Secrets Manager; rotation policy
- **Compliance**: SOC2 Type II ready, GDPR compliant

## AWS Reference Implementation (MVP)
- **Storage**: S3 (ingest-raw, normalized, quarantine)
- **Messaging**: SQS (ingest-queue), EventBridge (domain events)
- **Compute**: Lambda (parsers/OCR orchestrator), Step Functions (workflow)
- **Data**: DynamoDB (entities/config), OpenSearch/SageMaker/Bedrock vector store
- **Monitoring**: CloudWatch (logs/metrics), X-Ray (tracing)
- **Security**: KMS (keys), Secrets Manager, IAM

## Cost & Latency Budgets (Targets)
- **Resume-only**: ≤ 2 minutes p95 end-to-end; VCC ≤ $0.30 for ingestion/embedding portion
- **OCR scans**: Add ≤ 45s p95 and ~$0.10
- **Production SLA**: 99.9% availability, <5s p95 for simple documents

## Integration with Top-Tier Industry Standards
- **Quality Gates**: Automated validation of extracted content quality
- **Production Signals**: Extract evidence of production-ready engineering practices
- **Architecture Patterns**: Identify scalability and design pattern indicators
- **Testing Evidence**: Parse and catalog testing approaches and coverage data
- **Documentation Quality**: Assess completeness and operational readiness

## Open Questions
- Preferred OCR vendor/cost ceilings per page and per language
- Vector DB selection (OpenSearch vs. external) for first MVP and expected dims/throughput
- Allowlist file types per client/security; max bundle size
- Consent capture UX for email/channel imports; retention defaults by tier
- Integration with existing evaluation framework for seamless candidate assessment

## Appendix — LLM Extraction Prompt (Production-Ready)
For resume metadata extraction, use constrained JSON schema; ask model to cite page/line numbers; reject if hallucination detected via pattern checks; apply Top-Tier Industry Standards for technical content evaluation.