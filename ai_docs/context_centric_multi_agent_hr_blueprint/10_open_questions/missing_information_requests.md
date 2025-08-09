---
id: missing_information_requests
type: info_request_list
domain: hr_automation
created_date: 2025-08-09
last_updated: 2025-08-10
author: Junie
quality_score: 9.1/10
tags: [information-requests, demo, pilot, compliance]
visibility: public
version: 1.0
---

# Missing Information Requests (Client + Internal)

Purpose: Enumerate concrete information needed to de-risk the 5‑day demo, pilot scoping, and v1 planning. Please provide answers or pointers to sources. Where not available, we will conduct targeted web research.

## A) Demo (5‑Day) Essentials
1) Target roles for the demo (titles, seniority); pick 1–2 roles.
2) Role competencies and must‑have skills per role (top 6–8), with priority weights.
3) Company values prioritization and weighting for evaluation (e.g., Ownership=0.3, Technical Excellence=0.3, Integrity=0.2, etc.).
4) 2 sample candidate profiles per role (PDF resumes; optionally GitHub links and 1 markdown portfolio each).
5) Any must‑have integrations for the demo (email/calendar/ATS/storage?).
6) Data handling constraints for demo data (redaction expectations, residency requirements, anonymization preference).

## B) Pilot Scope (4–6 Weeks)
1) Expected hiring volumes (candidates/month per role) and roles in scope.
2) Success criteria and KPIs (time‑to‑hire reduction target, interviewer hours saved, quality threshold ≥ 8.5/10, adoption goals).
3) Stakeholder map (Economic Buyer, Champion, Hiring Managers, Security, Legal).
4) Procurement steps and expected timeline (security review, DPA, MSAs, any vendor portal).
5) Required integrations (ATS, SSO, data residency) and environments (sandbox vs prod data).

## C) Compliance & Security
1) Regional data residency requirements (e.g., EU‑only processing?).
2) Retention policies for candidate data (default months, exceptions, deletion triggers).
3) Approved model providers and privacy constraints (no training on customer data, retention windows, logging policies).
4) EEO/legal constraints beyond standard guidance (industry‑specific rules, public sector considerations).
5) Required audit artifacts (log format, export cadence, approver IDs).

## D) Product Configuration
1) Stage weights for evaluation (values_alignment, competencies, experience relevance) and any custom rubrics.
2) Preferred take‑home assessment topics per role and pass/fail gates.
3) Interview formats to include (BEI, system design, pair programming) and timeboxes.
4) Scoring scales (0–5 vs 1–10) and definitions for each level.

## E) Commercials & Pricing Inputs
1) Budget range for pilot and year‑1 subscription.
2) Contract preferences (monthly vs annual, prepay discounts, design partner terms).
3) Willingness‑to‑pay indicators by segment (if any prior data exists).

## F) Evidence/References (to attach if available)
- Current interview guides, rubrics, or values handbooks.
- Security questionnaire templates and DPA redlines.
- Any prior analytics on time‑to‑hire or interviewer hours.

## Notes
- This list complements the open items recorded in 10_open_questions/decision_log.md.
- We will proceed with safe defaults in the absence of inputs, but demo quality and fit improve significantly with the above information.

## Status Update (2025-08-10)

A) Demo (5‑Day) Essentials
1) Target roles: Answered — Senior Backend Engineer (Platform), Mid-level Backend Engineer (Platform).
2) Role competencies: Answered — matrices with weights defined per role (see data/public/new/hr_demo_pilot_blueprint.md §A.2).
3) Company values weighting: Answered — initial weights proposed for platform safety/speed.
4) Sample candidate profiles: Answered — Appendix A includes 2 synthetic profiles per role (Markdown portfolios; PDFs generated during demo).
5) Must‑have integrations (demo): Answered — Google Drive "sleipnir-demo-inbox/" (resumes/, portfolios/, job_descriptions/, evaluations/); future: Outlook/Gmail/ATS/Calendars/Dooray.
6) Data handling constraints: Answered — demo OK with non‑KR regions using non‑sensitive data; synthetic profiles preferred; KR‑only residency for production; guardrails noted.

B) Pilot Scope (4–6 Weeks)
1) Hiring volumes/roles: Partially answered — demo targets 1–2 hires; scalability expectations noted.
2) Success criteria/KPIs: Answered — TTH ≤ 20–24 days; ≥35–50% interviewer hours saved; quality ≥ 8.5/10; adoption ≥ 80%; rubric completion ≥ 90%; process/pipeline metrics.
3) Stakeholder map: Answered — CEO (EB), SW Eng Head/Platform Lead (Champion), Eng Manager/Platform Lead (Hiring), Security (Eng/DevOps), Legal/HR.
4) Procurement steps/timeline: Answered — week-by-week security/DPA/MSA/sandbox/kickoff/evaluation.
5) Integrations/environments: Answered — Sandbox Drive for demo; future ATS + SSO + data residency controls.

C) Compliance & Security
1) Regional residency: Answered — KR-only for production; demo may use non‑KR with non‑sensitive data.
2) Retention policies: Answered (proposal) — 12 months for rejected; purge raw artifacts after 6 months for hired; deletion triggers defined.
3) Model providers & privacy: Answered (proposal) — OpenAI/Google/Anthropic/local Ollama; no training on customer data; log retention ≤ 30 days; option to disable logging; redaction; audit JSON.
4) EEO/legal constraints: Partially answered — fintech context; maintain evidentiary logs; job‑relevant KSAOs.
5) Audit artifacts: Answered — structured JSON; weekly (pilot)/daily (go‑live) exports; approver chain documented.

D) Product Configuration
1) Stage weights: Answered — Values 0.30; Competencies 0.50; Experience 0.20.
2) Take‑home topics/gates: Answered — role‑specific topics and pass gates.
3) Interview formats/timeboxes: Answered — screen/system design/pair/culture/retro.
4) Scoring scales: Answered — Dreyfus 1–5 with anchors and evidence.

E) Commercials & Pricing Inputs
1) Budget range: TBD — client input needed.
2) Contract preferences: TBD — suggestion provided; awaiting client.
3) WTP indicators: TBD — no prior data; client input needed.

Status: Items integrated into blueprint docs as of 2025-08-10; remaining TBDs flagged in decision_log and mvp_plan open items.
