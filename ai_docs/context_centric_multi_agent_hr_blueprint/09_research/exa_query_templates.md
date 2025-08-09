---
id: exa_query_templates
type: research_templates
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 9.0/10
tags: [exa, research, templates]
visibility: public
version: 1.0
---

# Exa Query Templates (MCP)

Purpose: Provide reusable Exa MCP query patterns to accelerate trustworthy, up-to-date research. Include parameters to constrain by recency and source type.

## Usage Notes
- Always include a time filter (last 12–24 months) when applicable
- Prefer primary sources: vendor docs, official blogs, SEC filings, analyst sites
- Capture citation with title, URL, publisher, and date into the Evidence Log

## 1) Market Sizing & Trends
Query:
- "global recruiting software market size CAGR site:gartner.com OR site:forrester.com OR site:idc.com 2023..2026"
- "HR tech spend per employee benchmark 2023..2026 site:gartner.com OR site:forrester.com"
- "AI in hiring adoption statistics 2023..2026"

## 2) Competitive Pricing & Packaging
Query:
- "Greenhouse pricing tiers 2023..2026 site:greenhouse.io"
- "Lever pricing 2023..2026 site:lever.co"
- "Ashby pricing 2023..2026 site:ashbyhq.com"
- "AI hiring tool pricing 2023..2026 hireEZ Paradox Eightfold"

## 3) Compliance & Legal
Query:
- "EEO interviewing guidelines prohibited questions 2023..2026 site:eeoc.gov"
- "GDPR candidate data retention recruitment 2023..2026"
- "AI bias mitigation in hiring best practices 2023..2026"

## 4) Provider Privacy & Data Usage
Query:
- "OpenAI enterprise privacy policy no training on customer data 2023..2026"
- "Anthropic data retention enterprise 2023..2026"
- "Google Vertex AI data privacy generative 2023..2026"
- "Cohere data residency enterprise 2023..2026"

## 5) Token & OCR Cost Benchmarks
Query:
- "token pricing 1k gpt-4o mini o series 2024..2026"
- "Anthropic token pricing Claude 2024..2026"
- "OCR API pricing Tesseract alternatives Azure Read Google Vision 2024..2026"

## 6) Buyer Journey & Procurement
Query:
- "enterprise procurement security questionnaire recruiting software 2023..2026"
- "DPA template recruiting SaaS 2023..2026"

## 7) Case Studies & ROI
Query:
- "time to hire reduction case study engineering recruiting 2023..2026"
- "interviewer hours saved automation recruiting 2023..2026"

## Template Parameters
- time_range: last_12_months | last_24_months
- site_filters: [domains]
- must_include: [keywords]
- exclude_terms: [keywords]

## Evidence Capture Snippet (for analysts)
- [Title](URL) — Publisher — Date — Key metrics (CAGR, $) — Notes/Implications
