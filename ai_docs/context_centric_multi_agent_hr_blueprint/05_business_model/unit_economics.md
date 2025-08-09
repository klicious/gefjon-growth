---
id: unit_economics
type: financial_model
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 8.9/10
tags: [unit-economics, margins, costs]
visibility: public
version: 1.0
---

# Unit Economics Model (Draft)

Purpose: Provide a simple but actionable framework to estimate gross margin and payback under different tiers and usage profiles.

## Variables
- MRR: monthly subscription revenue ($)
- U_tokens: monthly LLM tokens (1k token units)
- C_token: cost per 1k tokens ($)
- U_ocr: monthly OCR pages
- C_ocr: cost per OCR page ($)
- S_gb: storage GB-month
- C_storage: cost per GB-month ($)
- Infra_overhead: fixed infra allocation ($/mo)
- Support_hours: support hrs/mo; C_support: $/hr
- Services: professional services revenue ($/mo) and cost ($/mo)

## Formulas
- LLM_cost = U_tokens × C_token
- OCR_cost = U_ocr × C_ocr
- Storage_cost = S_gb × C_storage
- Support_cost = Support_hours × C_support
- COGS = LLM_cost + OCR_cost + Storage_cost + Infra_overhead + Support_cost + Services_cost
- Revenue = MRR + Usage_overage + Services_revenue
- Gross_Margin_% = (Revenue - COGS) / Revenue
- CAC_payback_months ≈ CAC / (Revenue - COGS)

## Example Scenarios (Illustrative)
- Essential Tier: MRR=$1,500; U_tokens=6,000; C_token=$0.0015; U_ocr=1,000; C_ocr=$0.01; S_gb=50; C_storage=$0.02; Infra=$150; Support=2hrs@$60/hr
  - Gross Margin ≈ 78–85%
- Pro Tier: MRR=$4,000; U_tokens=16,000; Infra=$250; Support=4hrs@$75/hr → GM ≈ 75–83%
- Enterprise: MRR=$12,000; U_tokens=40,000; Infra=$600; Support=8hrs@$90/hr → GM ≈ 72–82%

## Sensitivity Levers
- Prompt optimization; caching; batch inference; cheaper providers
- OCR engine/provider selection
- Storage lifecycle policies (cold storage, deletion)

## Dashboard (What to Track)
- Tokens per candidate and per stage
- OCR pages per candidate input
- Storage GB per candidate and artifact type
- Support hours per account segment

## Actions
- Maintain a cost sheet with provider rates and discounts
- Implement token/cost telemetry by stage (see Observability)
- Run quarterly pricing reviews with WTP research inputs
