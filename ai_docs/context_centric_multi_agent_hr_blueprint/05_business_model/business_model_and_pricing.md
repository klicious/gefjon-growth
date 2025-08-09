---
id: business_model_and_pricing
type: business_strategy
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 9.1/10
tags: [business-model, pricing, wtp, margins]
visibility: public
version: 1.0
---

# Business Model and Pricing Strategy

Purpose: Define monetization, packaging, willingness-to-pay (WTP) validation, and margin structure for a context-centric multi-agent HR automation platform.

## Value Hypothesis
- Reduce time-to-hire by 40–60% and interviewer time by 60–80% through automation.
- Improve hiring consistency and fairness; defensible, auditable decisions.
- Enable rapid customization to company values and competencies.

## Revenue Streams
- Core SaaS Subscription (tiered)
- Usage Add-ons (LLM tokens, OCR pages, storage, API calls)
- Professional Services (onboarding, customization, integration)
- Marketplace Add-ons (assessment libraries, premium templates)

## Packaging (Draft)
- Essential (SMB/Teams)
  - Stages: screening, interview kits, basic take-home
  - Limits: up to 2 roles, 200 candidates/mo processed, 2 integrations
  - Support: community + email
- Pro (Mid-market)
  - Adds advanced ingestion (email, URLs), assignment evaluation sheets, basic guardrails
  - Limits: up to 5 roles, 750 candidates/mo, 5 integrations
  - Support: business hours; basic SLA
- Enterprise
  - Full guardrails/observability, RBAC, custom values/competencies, DPA, private networking options
  - Limits: custom roles/candidates; premium integrations; SSO/SAML planned
  - Support: 24/5 with SLA options

## Pricing Corridors (To Validate)
- Essential: indicative $800–$2,000/month
- Pro: indicative $2,000–$6,000/month
- Enterprise: $6,000–$20,000+/month
- Usage overages: per 1k tokens; OCR pages; storage GB-month; discounted in bundles
Note: Corridors are hypotheses; validate via WTP research before quoting.

## Discounting & Terms
- Early design partner discount: 20–30% for 6–12 months with reference rights
- Annual prepay: 10–15% discount; quarterly true-up on usage
- Pilot pricing: fixed fee + success kicker (e.g., per hire) optional

## Unit Economics (Summary)
- Targets: Gross margin 75–85%; Payback < 6 months
- COGS drivers: LLM usage, OCR, storage/egress, inference compute, support
- Simple monthly gross margin model:
  - Revenue = Subscription + Usage + Services
  - COGS = LLM_cost + OCR_cost + Storage_cost + Infra_overhead + Support_cost
  - Gross_Margin_% = (Revenue - COGS) / Revenue
- See ../05_business_model/unit_economics.md for detailed assumptions and scenarios.

## WTP Validation Plan
- Van Westendorp Price Sensitivity Meter (n≥25 per segment)
- Conjoint-lite on feature tiers (values customization, guardrails, integrations)
- Buyer interviews: budget authority, procurement constraints, alternatives
- A/B pilot proposals: subscription-only vs. subscription+usage bundles

## ICPs & Segments (Draft)
- SMB Tech (50–200 employees): need speed; limited integrations; budget constrained
- Mid-market SaaS (200–1,000): multiple roles; compliance needs; ROI-focused
- Enterprise Tech (1,000+): strict compliance; RBAC/SSO; data residency; bespoke integrations
- Agencies/RPO: volume processing; white-label potential

## Pricing Mechanics
- Metering dimensions: candidates processed, roles active, generated artifacts, API calls
- Fair-use policy per tier with transparent overage rates
- Seats optional (admin/interviewer) if used for access control; avoid double-charging

## Monetization Risks & Mitigations
- LLM cost volatility → provider routing, caching, prompt optimization, batch inference
- Price resistance → tier flexibility, per-role pricing, success-based pilots
- Enterprise security requirements → premium support/controls priced appropriately

## Sales Collateral & Offers
- ROI calculator (time saved, avoided interviewer hours, fewer scheduling cycles)
- Compliance one-pager, architecture overview for IT
- Design partner program with clear deliverables and mutual commitments

## Next Actions
- Populate unit_economics.md with cost models and scenarios
- Build sales_playbook.md with pilot→contract motion and objection handling
- Validate corridors via ../09_research/research_backlog.md and ../09_research/exa_query_templates.md


## Sources
- Anthropic Pricing (LLM token rates): https://www.anthropic.com/pricing (accessed: 2025-08-09)
- AWS Textract Pricing (OCR): https://aws.amazon.com/textract/pricing/ (accessed: 2025-08-09)
- Google Cloud Vision Pricing (OCR): https://cloud.google.com/vision/pricing (accessed: 2025-08-09)
- OpenAI API Pricing: https://platform.openai.com/docs/pricing (access currently restricted via fetch; confirm latest before quoting) [OPEN]
- See also research findings: ../09_research/web_research_findings.md
