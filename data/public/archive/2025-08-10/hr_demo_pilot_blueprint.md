# Sleipnir-Flow Hiring Demo & Pilot Blueprint (Context-Centric)

Source-grounded in this repository’s context. Paths referenced are relative to repo root.
- Core Values: context/org.yaml
- Culture & BEI: context/hr/culture_building.md
- Team & Roles: context/work_mgmt/knowledge/team/platform_development_team.yaml
- OKRs & KPIs: context/work_mgmt/knowledge/okrs/2025_h2.md
- Context Protocol: ai_docs/context/context_loading_procedure.md
- Gefjon Integration Context: ai_docs/context/gefjon_growth_implementation_context.md

Note: Items explicitly marked “TBD” mean intentionally left open pending user input; suggestions are provided where helpful.

---

## A) Demo (5‑Day) Essentials

1) Target roles for the demo
- Role 1: Senior Backend Engineer (Platform)
  - Grounding: team_composition and “open 1 mid-level backend req” in platform_development_team.yaml; stack in sections technology_stack and processes.
- Role 2: Mid-level Backend Engineer (Platform)
  - Grounding: same as above; internship-to-FTE pipeline and Dreyfus leveling in team file.

2) Role competencies and must‑have skills per role (6–8, with weights)
- Senior Backend Engineer (100% total)
  - Distributed systems & API design (DDD, scalability, failure modes) — 18%
  - Cloud & DevOps (AWS ECS Fargate, secrets, rollback, CI/CD) — 18%
  - Observability & Guardrails (SLOs, metrics, tracing, chaos mindset) — 14%
  - Python 3.12/Java 17 proficiency with testing discipline — 14%
  - Security & Compliance (least privilege, scans, audits) — 12%
  - Ownership & Proactivity (RCA within 24h, follow-ups merged) — 12%
  - Collaboration & Knowledge-sharing (PR reviews, docs) — 12%
  - Grounding: org.yaml Core Values; team processes; OKR O‑1/O‑2.

- Mid-level Backend Engineer (100% total)
  - Backend fundamentals (REST/gRPC, data modeling) — 18%
  - Cloud basics (AWS, containers, CI pipelines) — 16%
  - Testing & code quality (coverage habits, static analysis) — 16%
  - Observability foundations (metrics/logs/traces) — 14%
  - Security hygiene (secrets, dependency scanning) — 12%
  - Learning velocity & mentorship receptivity (Dreyfus +1/6mo) — 12%
  - Collaboration & communication — 12%
  - Grounding: org.yaml, culture_building.md, team file, OKR O‑2/O‑4.

3) Company values prioritization and weighting for evaluation (discussion + initial suggestion)
- Initial weights (sum 1.0), tailored for platform safety and speed:
  - Technical Excellence & Scalable Elegance — 0.20
  - Security & Compliance First — 0.18
  - Ownership & Proactivity — 0.16
  - Observability & Guardrails — 0.16
  - Integrity & Reliability — 0.12
  - Data‑Informed Iteration — 0.10
  - Collaboration & Knowledge‑Sharing — 0.08
- Setup discussion (how to operationalize):
  - Tie each value to 1–2 BEI questions (culture_building.md) and evidence checkboxes.
  - Require written examples or artifacts (post‑mortem links, dashboards, design docs).
  - Calibrate with 3 shadow scores across one week before demo day.
  - Keep audit trail in structured JSON (see README Security & Quality section).

4) 2 sample candidate profiles per role
- Included as Appendices (see section “Appendix A: Sample Candidate Profiles”). Each includes: summary, skills, selected projects, GitHub link placeholder, and a one‑page Markdown portfolio. PDFs can be generated from Markdown during the demo (no binaries committed here).

5) Must‑have integrations for the demo
- Demo stage: Storage only
  - Google Drive Shared Drive “sleipnir-demo-inbox/” with structure:
    - resumes/ (PDF/MD)
    - portfolios/ (MD)
    - job_descriptions/
    - evaluations/ (CSV/JSON)
  - Rationale: quick ingestion, simple sharing; sandbox‑only content.
- Later: Outlook Mail, OneDrive, Gmail, ATS, Calendars, Dooray (Tasks, Drive, Calendar, messenger, webhook). Integrations notes should follow ai_docs/context/context_loading_procedure.md discipline and MCP tool registry style.

6) Data handling constraints for demo data
- Location: Seoul (Seolleung). Commute ideally ≤ 1 h, acceptable up to 2 h.
- Anonymization: not required for demo; however, prefer synthetic/sample profiles for public repo hygiene.
- Education preference: logical/engineering thinking; CS not mandatory but strong fundamentals required. Better colleges preferred if evidence lacks.
- AI knowledge: proficiency with AI tools is a plus (aligns with multi‑agent workflows in team file).
- Additional guardrails from context:
  - Secrets never committed; no PII beyond candidate materials; structured audit logs.
  - For future KR data residency, ensure cloud storage selection can be region‑bounded before production.

---

## B) Pilot Scope (4–6 Weeks)

1) Expected hiring volumes and roles in scope
- Demo: 1–2 hires of best talent; high funnel volume, strict bar.
- Scalability note: architecture should scale to tens of thousands of hires annually post‑demo.

2) Success criteria and KPIs
- Targets (context‑aligned; baseline from team/OKRs):
  - Time‑to‑hire: baseline ≈ 32 days (platform_development_team.yaml), pilot target ≤ 20–24 days.
  - Interviewer hours saved: ≥ 35–50% via automation (kit generation, scheduling, summarization).
  - Quality threshold: average final score ≥ 8.5/10 across competencies and values.
  - Adoption: ≥ 80% interviewer usage of standardized kits; ≥ 90% rubric completion rate.
  - Process health: DoR/DoD adherence ≥ 90%; BEI kit usage ≥ 95% of loops (OKR O‑4 alignment).
  - Pipeline signal: reject‑by‑screen ratio improves ≥ 20% due to better filtering.

3) Stakeholder map
- Economic Buyer: CEO
- Champion: SW Engineering Head / Platform Lead
- Hiring Managers: Engineering Manager, Platform Lead
- Security: Engineering + DevOps (secrets, scanning, audit)
- Legal/HR: HR hiring manager (DPA, retention)

4) Procurement steps & expected timeline
- Week 1: Security review (secrets, audit log format, PII policy), DPA draft
- Week 2: MSA redlines, sandbox approval, SSO/SSO-lite decision
- Week 3: Pilot kickoff with Drive-only ingestion, reporting cadence agreed
- Week 4–6: Evaluation, ROI report, decision memo

5) Required integrations & environments
- Demo: Sandbox only, no ATS yet; ingest resumes/portfolios/job descriptions from Google Drive.
- Future: ATS + SSO + data residency controls; align with context_loading_procedure.md and org security posture.

---

## C) Compliance & Security

1) Regional data residency
- Primary: South Korea only for production. Demo may use non‑KR regions but keep data non‑sensitive; avoid real PII if possible.

2) Retention policies for candidate data (proposal)
- Default retention: 12 months for rejected candidates; delete on request.
- Hired candidates: retain core record for employment lifecycle; purge raw artifacts after 6 months.
- Deletion triggers: candidate request, inactivity > 12 months, contract termination.

3) Approved model providers & privacy constraints (proposal)
- Providers: OpenAI, Google, Anthropic, local Ollama (per team file & tools usage).
- Constraints: no training on customer/candidate data; retention ≤ 30 days logs; option to disable vendor logging; redact secrets; maintain audit JSON events (README Security & Quality).

4) EEO/legal constraints beyond standard guidance
- Industry context: fintech; avoid bias on non‑job factors; maintain evidentiary logs for assessments; values and competencies must map to job‑related KSAOs.

5) Required audit artifacts
- Log format: structured JSON with approver IDs, timestamps, doc references, and rubric IDs.
- Export cadence: weekly during pilot; daily upon go‑live.
- Approver chain: Hiring Manager → Engineering Manager → CEO (economic buyer) with HR co‑sign for retention/EEO.

---

## D) Product Configuration

1) Stage weights for evaluation
- Standard starting weights (sum 1.0), aligned to context:
  - Values Alignment — 0.30 (org.yaml + culture_building.md)
  - Competencies — 0.50 (role definitions above)
  - Experience Relevance — 0.20 (domain fit, portfolio evidence)

2) Preferred take‑home assessment topics per role and pass/fail gates
- Senior Backend Engineer
  - Topics: stateless service with one stateful dependency; graceful rollback; secrets via AWS SM; observability (p95, tracing); blue/green deploy plan; property‑based tests.
  - Pass gate: runs locally with instructions; coverage ≥ 70%; clear rollback plan; evidence of SLO thinking; secretless config.
- Mid-level Backend Engineer
  - Topics: small CRUD/gRPC with pagination; containerize; basic metrics; CI YAML; integration tests; dependency scanning awareness.
  - Pass gate: build/run instructions; tests pass; simple metrics exposed; clean code structure; no hardcoded secrets.
- Note: These are context‑aligned best practices. For broader pools, augment with industry references during demo (TBD links).

3) Interview formats & timeboxes (context‑aligned)
- Screen (30–40m): Resume deep‑dive + values BEI (culture_building.md Qs)
- System Design (60m): service boundary, failure modes, observability & rollout plan
- Pair Programming (60m): extend the take‑home or implement a small feature with tests
- Culture & Mentorship (30–45m): collaboration, knowledge sharing, Dreyfus leveling
- Loop retro (15m): candidate Q&A, expectations, feedback logistics

4) Scoring scales and definitions
- 1–5 scale mapped to Dreyfus:
  - 1 Novice — needs handholding, gaps in fundamentals
  - 2 Advanced Beginner — handles small tasks, limited autonomy
  - 3 Competent — delivers end‑to‑end with guidance, sound trade‑offs
  - 4 Proficient — anticipates failure modes, mentors others, raises bar
  - 5 Expert — sets patterns, drives org impact, systemic thinking
- Use per-dimension anchors from org.yaml “What Good Looks Like”; tie evidence fields to artifacts (design docs, dashboards, post‑mortems).

---

## E) Commercials & Pricing Inputs

1) Budget range for pilot and year‑1 subscription — TBD
2) Contract preferences (monthly vs annual, prepay discounts, design partner terms) — TBD (suggest: annual with design‑partner discount; opt‑out at 90 days)
3) Willingness‑to‑pay indicators by segment — TBD (no prior data in repo)

---

## F) Evidence/References (to attach if available)

- Core Values: context/org.yaml (10 values with anti‑patterns)
- Culture & BEI samples, Performance weights: context/hr/culture_building.md
- Team & Roles, Processes, Stack: context/work_mgmt/knowledge/team/platform_development_team.yaml
- OKRs & KPIs: context/work_mgmt/knowledge/okrs/2025_h2.md
- Context Protocol: ai_docs/context/context_loading_procedure.md
- Gefjon Integration Context: ai_docs/context/gefjon_growth_implementation_context.md

---

## Appendix A: Sample Candidate Profiles (Markdown portfolios)

Note: Synthetic demo profiles for evaluation workflow testing; not real PII.

### Role: Senior Backend Engineer — Candidate S1
- Summary: 8+ years backend; built trading risk services; led ECS blue/green adoption; championed observability.
- Skills: Python 3.12, Java 17, AWS ECS Fargate, RDS, Redis, OpenTelemetry, GitLab CI, Docker, DDD.
- GitHub: https://github.com/example-s1 (placeholder)
- Portfolio (1‑page MD):
  - Project A: “Risk Aggregator” — Python + Postgres, p95 < 120ms, chaos test suite; rollback in < 2 min.
  - Project B: “Secretless Config” — moved services to AWS SM; zero hardcoded secrets.
  - Project C: “Observability Pack” — metrics/traces dashboards; drill‑downs to RCA in < 15m.

### Role: Senior Backend Engineer — Candidate S2
- Summary: 10 years; payment orchestration; authored CI/CD templates; security champion.
- Skills: Java 17, Python, gRPC, AWS, Terraform basics, Bandit/Trivy.
- GitHub: https://github.com/example-s2 (placeholder)
- Portfolio:
  - Project A: “Payment Router” — HA design, ALB + ECS; rollback plan; audit trails.
  - Project B: “Test Generator” — property‑based tests; coverage from 55%→82%.

### Role: Mid-level Backend Engineer — Candidate M1
- Summary: 3+ years; built CRUD/gRPC services; eager to learn, mentored interns.
- Skills: Python, Docker, AWS basics, pytest, OpenTelemetry basics.
- GitHub: https://github.com/example-m1 (placeholder)
- Portfolio:
  - Project A: “Portfolio API” — pagination, versioned endpoints; unit+integration tests.
  - Project B: “Metrics First” — added p95 latency and error‑rate alerts.

### Role: Mid-level Backend Engineer — Candidate M2
- Summary: 4 years; logistics microservices; CI pipelines; security hygiene.
- Skills: Python/Go, REST, Docker, GitHub Actions, Secrets Manager basics.
- GitHub: https://github.com/example-m2 (placeholder)
- Portfolio:
  - Project A: “Inventory Service” — clean architecture; feature flags; rollback docs.
  - Project B: “Security Hygiene” — dependency scans; SBOM; secrets detection.

---

## Appendix B: Demo Folder Structure (Google Drive)

sleipnir-demo-inbox/
- resumes/
- portfolios/
- job_descriptions/
- evaluations/

---

## Appendix C: Open Questions for Sponsor

- Budget constraints and preferred commercial structure for pilot and year‑1.
- Confirm KR-only data residency timeline; can demo use non‑KR regions for Drive?
- Confirm acceptance of synthetic sample profiles in demo.
- Preferred ATS for eventual integration; SSO requirements.
- Any legal redlines (DPA/MSA templates) we should pre-fill.
