---
id: web_research_findings
type: research_findings
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 8.8/10
tags: [research, citations, pricing, compliance]
visibility: public
version: 1.0
---

# Web Research Findings (Cited)

Purpose: Capture current, verifiable references to inform pricing benchmarks, compliance guardrails, and provider policies. This file will be expanded iteratively.

## Summary of What We Have Now
- OCR pricing benchmarks from AWS Textract and Google Cloud Vision are available and align around ~$0.0015 per page/image for core OCR at low volumes (see sources below). Use these for initial unit economics and overage pricing assumptions.
- Anthropic pricing page is accessible for current token pricing; use as a live reference for LLM cost modeling. OpenAI pricing page returned 403 with the fetch tool; keep as OPEN item to capture exact current rates in a follow-up.
- EEOC’s Prohibited Employment Policies/Practices page is accessible and establishes anti-discrimination constraints for hiring processes and interview content.

## Citations (with URLs and notes)
1. Amazon Textract Pricing — https://aws.amazon.com/textract/pricing/
   - Notes: Detect Document Text API listed with tiered per-page pricing. Example on page cites $0.0015 per page for first 1M pages in us-west-2 for simple OCR scenarios (subject to region and changes). Includes free tier details and other APIs.

2. Google Cloud Vision Pricing — https://cloud.google.com/vision/pricing
   - Notes: Tiered per-1,000 units pricing. Document Text Detection (OCR for documents) shows pricing blocks; first 1,000 free, then $1.50 per 1,000 images for TEXT and DOCUMENT_TEXT_DETECTION in listed tiers (equivalent to ~$0.0015 per image in that tier). Subject to change.

3. Anthropic Pricing — https://www.anthropic.com/pricing
   - Notes: Official pricing page for Claude models. Use the live table for input/output token rates and prompt caching options. Capture exact numbers during quoting; do not hard-code here.

4. EEOC — Prohibited Employment Policies/Practices — https://www.eeoc.gov/prohibited-employment-policiespractices
   - Notes: Establishes that discrimination based on protected characteristics is illegal; hiring policies must be job-related and necessary. Use this as an anchor for EEO-safe prompts and interview content.

## Pending/To-Confirm Sources (OPEN)
- OpenAI API pricing (403 via fetch) — capture current numbers manually or via browser session before quoting; https://platform.openai.com/docs/pricing
- Azure AI Vision OCR pricing (URL returned 404 in fetch flow) — confirm current region-specific pricing page and add.
- Google Vertex AI data governance/privacy commitments — add enterprise data usage language.
- Cohere enterprise privacy/trust center — add data residency and training policy notes.
- GDPR recruitment data retention and DPIA guidance (EU/UK regulator pages) — add retention norms and lawful basis examples.

## Implications for Our Plan
- Use OCR benchmarks (~$0.0015/page) in unit_economics.md as an initial cost basis with sensitivity analysis.
- Anchor compliance language in security_compliance_and_data_governance.md to EEOC anti-discrimination constraints; append GDPR references once validated.
- Keep LLM provider pricing as configurable inputs in cost models; avoid hard-coding numbers that change frequently.

## Change Log
- 2025-08-09: Initial findings added with OCR and EEOC anchors; more sources to be appended.


5. Google Vertex AI — Generative AI and Zero Data Retention — https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance
   - Notes: Enterprise commitments include no training/fine-tuning on customer data without permission; caching up to 24 hours by default for Gemini models (project-level toggle to disable for zero data retention); certain abuse-monitoring prompt logging applies unless exceptions are granted; grounding with Google Search stores data for 30 days when used.

6. Azure AI Vision Pricing — https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/
   - Notes: Official Azure pricing page for AI Vision (Computer Vision). Includes OCR (Read) and image analysis features with tiered per-1k transaction pricing; region and program can affect rates. Use as a benchmark alongside AWS Textract and Google Cloud Vision.
