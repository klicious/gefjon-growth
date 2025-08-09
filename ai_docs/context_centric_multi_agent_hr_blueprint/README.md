---
id: context_centric_multi_agent_hr_blueprint
type: index
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-09
author: Junie
quality_score: 8.8/10
tags: [blueprint, context-centric, multi-agent, hiring, product]
visibility: public
version: 1.0
---

# Context-Centric Multi-Agent HR Automation Blueprint

Purpose: Provide a vendor-agnostic, end-to-end plan to build and commercialize a scalable HR automation product that covers resume ingestion → screening → assignments → interviews → evaluations, with deep customization per company/team values.

This blueprint is structured for rapid collaboration with AI agents and human stakeholders. Every document includes metadata, actionable checklists, and clear hand-offs.

## How to Use
- Executives: Start with 00_overview and 05_business_model.
- Product/Engineering: Focus on 02_product and 03_architecture; use 08_agent_context to run agent workflows.
- Compliance/Security: Review 04_security_compliance.
- Sales/Marketing: Review 01_market and 05_business_model; leverage 07_presentation.
- Program Management: Drive delivery via 06_execution_roadmap.

## Directory Map
- 00_overview/README.md — Executive summary and value proposition
- 01_market/ — Market research plan, competitive landscape, buyer personas, WTP study
- 02_product/ — Product scope, requirements, customization, evaluation frameworks
- 03_architecture/ — System architecture, multi-agent orchestration, context fabric, data/ingestion
- 04_security_compliance/ — Security, privacy, governance, risk register
- 05_business_model/ — Business model, pricing, unit economics, sales playbook
- 06_execution_roadmap/ — Roadmap, task breakdown, MVP (5-day) demo plan, checklists
- 07_presentation/ — Pitch deck outline, one-pager, demo script, preflight checklist
- 08_agent_context/ — Agent context kit, packaging guide, prompts library
- 09_research/ — Research backlog and Exa query templates
- 10_open_questions/ — Assumptions, gaps, decision log

## Principles
- Context-first: All work products must be saved under artifacts/ or context/ and referenced in prompts.
- Vendor-agnostic: Design for portability across model providers and infra.
- Observability & Guardrails: Auditability, testable prompts, and deterministic checks.
- Customizable: Company/team-level values and process knobs across all stages.

## Quick Links
- Start the 5-day client presentation prep: 06_execution_roadmap/mvp_plan_5day_demo.md
- Demo Script: 07_presentation/demo_script.md
- Agent Kit: 08_agent_context/agent_context_kit.md
