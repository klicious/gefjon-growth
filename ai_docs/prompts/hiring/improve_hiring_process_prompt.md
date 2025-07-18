# Prompt: Comprehensive Hiring Process Overhaul

## 1. Role and Goal

You are an expert HR Technology Consultant and AI Process Designer. Your mission is to overhaul and enhance our engineering hiring process based on a recent internal review. You will address specific feedback points by designing new artifacts, defining clear procedures, and creating robust evaluation frameworks. Your goal is to make our hiring process more effective, fair, and predictive of success, with a strong emphasis on identifying talent aligned with our unique agentic AI-driven culture.

---

## 2. Core Task

Your primary task is to analyze the **"Areas for Improvement & Questions"** section from our internal review document and generate a complete, actionable solution for each point. You must use the extensive context provided below to ensure your solutions are deeply integrated with our company's mission, values, team dynamics, and technical stack.

### Feedback to Address (from `ai_docs/overview/hiring_process_and_feedback.md`):

> 1.  **Technical Assessment:**
>     *   **Feedback:** The on-site loop is strong, but it could benefit from a more hands-on coding assessment to complement the system design and deep-dive sessions.
>     *   **Recommendation:** Introduce a pair-programming session where the candidate works with an engineer to solve a small, well-defined problem. This would provide insights into their coding style, problem-solving process, and ability to collaborate.
>     *   **Question:** *How do you currently assess a candidate's raw coding ability and problem-solving skills in a live setting?*
>
> 2.  **Evaluation Rubric:**
>     *   **Feedback:** The BEI guide provides a good scoring rubric, but it's not clear if a similar rubric exists for the technical interviews.
>     *   **Recommendation:** Develop a clear and consistent evaluation rubric for all technical interviews, outlining the specific criteria and expectations for each level of performance.
>     *   **Question:** *Do you have a standardized evaluation rubric for the system design and technical deep-dive interviews? If so, could you provide more details on the criteria?*
>
> 
>
> 2.  **Technical Assessment:**
>     *   **Feedback:** The on-site loop is strong, but it could benefit from a more hands-on coding assessment to complement the system design and deep-dive sessions.
>     *   **Recommendation:** Introduce a pair-programming session where the candidate works with an engineer to solve a small, well-defined problem. This would provide insights into their coding style, problem-solving process, and ability to collaborate.
>     *   **Question:** *How do you currently assess a candidate's raw coding ability and problem-solving skills in a live setting?*
>
> 3.  **Evaluation Rubric:**
>     *   **Feedback:** The BEI guide provides a good scoring rubric, but it's not clear if a similar rubric exists for the technical interviews.
>     *   **Recommendation:** Develop a clear and consistent evaluation rubric for all technical interviews, outlining the specific criteria and expectations for each level of performance.
>     *   **Question:** *Do you have a standardized evaluation rubric for the system design and technical deep-dive interviews? If so, could you provide more details on the criteria?*
>
> 4.  **Diversity & Inclusion:**
>     *   **Feedback:** While the process is structured to reduce bias, there are no explicit mentions of initiatives to attract a diverse pool of candidates.
>     *   **Recommendation:** Actively source candidates from underrepresented groups and ensure that your interview panels are diverse.
>     *   **Question:** *What measures are you taking to ensure a diverse and inclusive hiring process?*

---

## 3. Comprehensive Context

To succeed in this task, you must deeply understand our organization. The following are the full contents of our internal documents.

### **CONTEXT FILE: `context/company_info/mission_vision_values.yaml`**
```yaml
# context/org.yaml
id: org-core
type: knowledge_base
domain: HR
last_updated: 2025-07-10
tags: [mission, vision, values]
visibility: public
body: |
  ## Mission
  Engineer cross-region, self-healing fintech platforms that move capital instantly for liquidity and strategically for future value—while guaranteeing systemic safety and investor trust.

  ## Vision
  Set the global benchmark for internal fintech engineering, known for real-time observability, < 5 min MTTR, and an innovation cadence that compounds investor advantage.

  ## Core Values — Deep Dive
  | # | Value | “What Good Looks Like” | Anti‑Pattern to Avoid |
  |---|---|---|---|
  | 1 | **Technical Excellence & Scalable Elegance** | • Service meets p95 table.• CodeClimate ≥ A.• Design docs show horizontal scale path. | Premature optimization that ignores readability or horizontal growth. |
  | 2 | **Customer‑Centric Craftsmanship** | • User story captures trader pain (#JIRA‑123).• Usability test with 3 real users pre‑GA. | Feature built “because it’s cool” with zero investor validation. |
  | 3 | **Ownership & Proactivity** | • Engineer pages themselves during incident.• RCA published within 24 h and follow‑ups merged. | “Throw over wall” to SRE; blaming infra without fix. |
  | 4 | **Observability & Guardrails** | • 3 SLOs + burn‑rate alerts.• Kill‑switch toggled in staging weekly. | Shipping code with no metric or alert path. |
  | 5 | **Data‑Informed Iteration** | • A/B leads to > +5 % KPI before 100 % rollout.• Dashboards updated daily. | HIPPO decisions (“highest‑paid person’s opinion”) with zero telemetry. |
  | 6 | **Integrity & Reliability** | • Immutable audit log (AWS QLDB) tied to every trade.• Zero Sev‑0 per quarter. | Silent failure of audit pipeline; post‑incident blame game. |
  | 7 | **Security & Compliance First** | • Secrets in AWS SM, rotated 90 d.• Static‑analysis gate green every PR. | Hard‑coding credentials; manual policy overrides. |
  | 8 | **Collaboration & Knowledge‑Sharing** | • ≥ 2 peer reviews; constructive RFC comments.• Tech talks recorded + wiki’ed. | Lone‑wolf merges to main; tribal knowledge silos. |
  | 9 | **Continuous Learning & Mentorship** | • New hire gains +1 Dreyfus level in 2 skills.• Buddy logs weekly feedback. | “Sink‑or‑swim” onboarding; zero growth plan. |
  | 10 | **Innovative Spirit** | • Quarterly hack‑day POC demo; best ideas enter backlog.• Budget for 1 conf / eng / yr. | Innovation theatre—hack‑day code never revisited. |
```

### **CONTEXT FILE: `context/teams/platform_development_team.yaml`**
```yaml
# context/platform_development_team.yaml
# Platform Development Team - Mission, Responsibilities, Roadmap

mission: "To build and operate a fully-automated, self-healing fintech platform that (a) trades digital assets profitably, (b) exposes portfolio-level risk & P&L in real time, and (c) can eventually run without direct human intervention."

guiding_principles: "Safety -> Quality -> Speed -> Novelty, with a strong preference for Scalable Elegance and Domain-Driven Design (DDD)."

team_composition:
  - role: "Platform Lead"
    count: 1
    focus: "Architecture, algorithm R&D, infra strategy, hiring"
  - role: "Senior / Mid Engineers"
    count: 1
    focus: "Frontend services, CI/CD, infra-as-code, LLM integration"
  - role: "Interns (6-month program)"
    count: 1
    focus: "Growth projects, tooling, live docs automation"

core_responsibilities:
  - "Algorithmic Trading Platform – design, backtest, deploy and maintain market-making, mean-reversion, momentum & hedging strategies across 27 crypto instruments."
  - "Portfolio Management System (PMS) – positions, risk, fee rebates, and treasury flows; Python & Spring micro-services with real-time websockets."
  - "Multi-Agent Automation Framework – Gemini CLI + GitLab DUO + Amazon Q Developer + Claude Code + ChatGPT + MCP servers orchestrating agents for coding, project management, documentation, and infra ops. We are actively developing our own in-house agentic AI capabilities."
  - "Live Documentation – “Runebook” & “Yggdrasil” repositories; auto-sync to GitHub Wiki / Notion; up-to-date for humans and AI agents."
  - "DevOps & SRE – GitLab CI, self-hosted group runners, ECS Blue/Green, automated secrets management, observability & guardrails."
  - "Hiring & Mentorship – evaluation rubric design, intern program, external recruiting presentations (e.g., SIKMA 2024)."

technology_stack:
  languages: "Python 3.12, Java 17 (Spring Boot 3)"
  ai_llm: "OpenAI o3, GPT-4o, Gemini 1.5, Claude 3; local Ollama models (Docker)"
  agent_runtime: "Google ADK 1.5, MCP Docker servers, A2A protocol"
  data_messaging: "PostgreSQL, Redis Streams, WebSockets, REST, gRPC"
  cloud_infra: "AWS EC2, ECS Fargate, S3, CloudWatch, NAT GW, ALB, Route 53"
  ci_cd: "GitLab Cloud + self-hosted runners (Shell executor), uv for Python deps"
  tooling: "Poetry->uv migration, Black + Isort + Flake8 + Mypy, pytest-cov"
```

### **CONTEXT FILE: `artifacts/public/hiring/interview_process.md`**
```markdown
# Gefjon Growth: Mid-Level Backend Engineer Interview Process (v2)

## 1. Philosophy and Principles

Our interview process is a direct reflection of our culture. It is a systematic mechanism designed to help us build an enterprising, customer-centric team, as inspired by our belief in the "power of process." We aim to create a process that is not only effective at identifying top talent but is also a positive and insightful experience for every candidate. Our principles are:

*   **Structured & Evidence-Based:** We use a structured interview process with a consistent set of behavioral and technical questions. We rely on the STAR method and a clear evaluation rubric to make objective, evidence-based decisions, minimizing bias.
*   **Relevant & Practical:** We focus on assessing the skills and competencies that are directly relevant to the challenges and opportunities at Gefjon Growth. Our interviews include practical, real-world problems that mirror the work you would be doing here.
*   **Transparent & Respectful:** We are transparent about our process, our values, and what we are looking for. We value your time and aim to provide timely and constructive feedback.
*   **Focused on the Future:** We are not just hiring for today; we are hiring for the future. We are looking for engineers who have the potential to grow with us and contribute to the development of our agentic AI capabilities.

## 2. Interview Stages

The interview process for the Mid-Level Backend Engineer role has been streamlined to be more focused and respectful of your time:

| Stage | Duration | Purpose | Interviewer(s) |
| :--- | :--- | :--- | :--- |
| **1. Recruiter Connect** | 30 mins | Initial conversation to discuss your background, motivation, and interest in the role. | Recruiter |
| **2. Take-Home Assignment** | 4-6 hours | A practical assignment to assess your ability to design, build, and test a small application. | Candidate (self-paced) |
| **3. On-site/Virtual Loop** | 3.5 hours | A series of interviews to dive deep into your technical and behavioral competencies. | Platform Lead, Senior Engineers |
| **4. Final Leadership Interview** | 30 mins | Final assessment of team fit, career aspirations, and alignment with company vision. | Platform Lead / Hiring Manager |
| **5. Team Coffee Chat** | 30 mins | An informal chat with potential teammates to discuss our culture and ways of working. | 2-3 Team Members |

## 3. Stage Details

### Stage 3: On-site/Virtual Loop
*   **What to Expect:** A 3.5-hour interview loop with multiple interviewers. The loop will consist of the following sessions:
    *   **Behavioral Interview (BEI):** We'll ask you about your past experiences and how you've handled different situations, using the STAR method.
    *   **System Design Interview:** We'll ask you to design a system that is relevant to our domain, focusing on scalability, reliability, and trade-offs.
    *   **Agentic AI & System Design:** This session will focus on your potential to build AI agents. We will discuss your understanding of LLMs, prompt design, and agent orchestration.
    *   **Technical Deep-Dive:** We'll dive deep into a project from your portfolio or your take-home assignment.
```

### **CONTEXT FILE: `artifacts/public/hiring/interview_materials/bei_interview_guide.md`**
```markdown
## **Interview Framework**

### **1. Overview of BEI & STAR**

Behavioral Event Interviewing asks for **specific past incidents**, then probes for **Situation, Task, Action, Result (STAR)** — the most predictive method for future performance when paired with clear scoring anchors.

### **3. Scoring Rubric (per question, 1-5)**

| **Score** | **Behavioral Evidence** |
| --- | --- |
| **1** | Vague or hypothetical; no metrics |
| **3** | Clear STAR story; some metrics; moderate impact |
| **5** | Quantified impact, proactive reflection, aligns with ≥ 2 core-value indicators |

Set a **pass bar of ≥ 3.5 average** per targeted value; candidates with two values < 3 are a no-hire.

## **BEI Question Bank & Expected Signals**
> *Includes detailed questions for 12 value areas, including Technical Excellence, Customer-Centric Craftsmanship, Ownership, Observability, Data-Informed Iteration, Integrity, Security, Collaboration, Continuous Learning, Innovative Spirit, Quantitative Aptitude, and Agentic Mindset.*
```

### **CONTEXT FILE: `data/temp/entry_level_take_home_assignment/entry_level_sw_eng_take_home_task(old).md`**
```markdown
### **Technical Assessment Details**

### **BitMex & Binance REST API Implementation**

### **Objective**

To implement REST API integrations for BitMex and Binance exchanges that support trading cryptocurrency instruments. Your task includes implementing key features that allow us to retrieve, place, amend, and cancel orders efficiently.

---

### **4. Specifications & Requirements**

### **Core Exchanges**
- **BitMex**
- **Binance**

### **API Features**
1. **Get Orders**: By IDs, date range, state.
2. **Get Active Orders**.
3. **Place Orders**: Market and limit.
4. **Amend Orders**: Quantity or price.
5. **Cancel Orders**.

### **Data Handling**
- Must work for production and test servers.
- Use test API keys.

### **Cryptocurrency Instruments**
- BTC, ETH, SOL

### **Markets**
- SPOT, USD-M Futures, USD-C Futures
```

---

## 4. Detailed Instructions & Constraints

### **A. Research Mandate**

Before generating any content, you **must** conduct extensive web research on the following topics. Your final output should reflect modern best practices informed by this research.
*   State-of-the-art technical interviewing techniques for high-growth fintech and AI companies.
*   Designing effective, unbiased, and practical take-home assignments.
*   Best practices for conducting collaborative pair-programming interviews.
*   Creating structured, objective, and legally defensible evaluation rubrics.
*   Actionable and impactful Diversity, Equity, and Inclusion (DEI) strategies for tech hiring.

### **B. Task Breakdown**

You will deliver a single, comprehensive markdown document that contains the solutions to the feedback point.



#### **Part 1: Create Comprehensive Evaluation Rubrics**

*   **Objective:** Create a structured, hands-on coding session to assess raw coding ability, problem-solving, and collaboration skills.
*   **Deliverables:**
    1.  **Session Protocol:** Define the structure and timeline for a 60-minute pair-programming interview.
        *   Example: 5 min intro, 45 min coding, 10 min debrief/Q&A.
    2.  **Interviewer Guide:** Write a short guide for the interviewer on how to conduct the session. It should cover their role (e.g., "act as a collaborator, not just an evaluator"), how to provide hints, and what to look for (e.g., "clarifying questions, testing habits, communication style").
    3.  **Problem Bank:** Create a bank of 3-5 suitable pair-programming problems. The problems should be:
        *   Language-agnostic but well-suited for Python.
        *   Complex enough to require thought but solvable within 45 minutes.
        *   Relevant to our domain (e.g., data processing, simple algorithmic logic, API interaction) without requiring niche knowledge.
        *   For each problem, provide a description, a few test cases, and a hint the interviewer could give if the candidate gets stuck.



*   **Objective:** Develop standardized, objective rubrics for all technical interview stages to ensure consistent and fair evaluations.
*   **Deliverables:**[hiring_process_and_feedback.md](../../overview/hiring_process_and_feedback.md)
    1.  **System Design Interview Rubric:**
        *   Create a detailed rubric with 4-5 key evaluation criteria (e.g., "Problem Decomposition & Clarification," "Scalability & Reliability," "Trade-off Analysis," "Communication & Rationale").
        *   For each criterion, define what constitutes a 1 (Poor), 3 (Average), and 5 (Excellent) performance, using concrete examples relevant to our tech stack.
    2.  **Technical Deep-Dive Rubric:**
        *   Create a rubric for evaluating a candidate's discussion of their past projects or take-home assignment.
        *   Criteria should include "Depth of Knowledge," "Ownership & Impact," "Technical Decision-Making," and "Lessons Learned."
        *   Define performance levels (1, 3, 5) for each criterion.
    3.  **Pair-Programming Rubric:**
        *   Create a rubric for the new pair-programming session.
        *   Criteria should include "Problem Solving & Logic," "Code Quality & Readability," "Testing & Verification," and "Collaboration & Communication."
        *   Define performance levels (1, 3, 5) for each criterion.



*   **Objective:** Formulate an actionable strategy to improve diversity and inclusion in our hiring pipeline.
*   **Deliverables:**
    1.  **Sourcing Strategy:**
        *   List at least 3-5 specific, actionable strategies to source candidates from underrepresented groups (e.g., partnerships with specific organizations, attending certain conferences, using inclusive language in job descriptions).
    2.  **Interview Process Enhancements:**
        *   Propose 3-5 changes to the interview process itself to mitigate bias. Examples could include diverse interview panels, standardized question sets (which we already do with BEI, but can be reinforced), and pre-interview training for interviewers on unconscious bias.
    3.  **Measurement & Accountability:**
        *   Suggest 2-3 key metrics to track the effectiveness of the D&I initiatives (e.g., diversity of applicant pool, pass-through rates for different demographics).
        *   Propose a simple mechanism for accountability (e.g., a quarterly review of hiring metrics with the leadership team).

## 5. Output Format

Your final output must be a single, well-formatted markdown file. Use clear headings, bullet points, and tables to structure your response. The content should be professional, polished, and ready to be implemented by our HR and engineering teams.
