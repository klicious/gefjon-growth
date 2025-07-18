## **Interview Framework**

### **1. Overview of BEI & STAR**

Behavioral Event Interviewing asks for **specific past incidents**, then probes for **Situation, Task, Action, Result (STAR)** — the most predictive method for future performance when paired with clear scoring anchors.

### **2. Panel & Flow**

| **Stage** | **Duration** | **Interviewer(s)** | **Purpose** | **Artifacts** |
| --- | --- | --- | --- | --- |
| **Calibration huddle** | 15 min | All panelists | Align on core values, scoring rubric & “halo/horn” bias reminders | Shared rubric |
| **Warm-up (rapport)** | 5 min | Host | Explain STAR, confidentiality, note-taking | — |
| **Value rounds** | 50 min | Two interviewers (rotate every value pair) | Ask 5–6 questions, dig ≥ 2 follow-ups each, record verbatim quotes | Score sheet |
| **Wrap-up** | 5 min | Host | Candidate Q&A, next-steps | — |
| **Debrief** | 20 min | Panel | Compare evidence, final scores, decide **hire / strong hire / no hire** | Consolidated rubric |

*Tip:* One interviewer drives, the other logs STAR notes to cut context-switching and improve data quality .

### **3. Scoring Rubric (per question, 1-5)**

| **Score** | **Behavioral Evidence** |
| --- | --- |
| **1** | Vague or hypothetical; no metrics |
| **3** | Clear STAR story; some metrics; moderate impact |
| **5** | Quantified impact, proactive reflection, aligns with ≥ 2 core-value indicators |

Set a **pass bar of ≥ 3.5 average** per targeted value; candidates with two values < 3 are a no-hire.

---

## **BEI Question Bank & Expected Signals**

> Structure:
> 
> 
> *Question → What “great” sounds like → Why the question unmasks the value.*
> 

### **1 · Technical Excellence & Scalable Elegance**

| **#** | **Question** | **Look-for Signals** | **Design Rationale** |
| --- | --- | --- | --- |
| 1 | “Describe a time a system you built had to absorb a 10× traffic spike. How did you spot bottlenecks and redesign?” | Mentions load-test data, horizontal scaling (queues/sharding/CDN), rollback plan, post-mortem metrics | Tests depth of scalability thinking; ties to p95/SLO mindset. |
| 2 | “Tell me about the ugliest legacy module you refactored. What trade-offs did you reverse?” | Shows respect for readability, incremental strangler pattern, unit-coverage delta | Surfaces balance of pragmatism vs. gold-plating. |
| 3 | “Walk me through an ADR you authored that changed team standards.” | Clear context, alternatives table, impact on deploy speed | Confirms doc discipline & code-as-communication. |
| 4 | “When have you rejected a ‘clever’ optimization?” | Cites future maintainers, latency budget, premature-opt cost | Detects ability to avoid anti-pattern noted in value table. |
| 5 | “Give an example of debugging a perf regression in production.” | Uses profiling tools, root cause, measurable recovery | Assesses real-world fire-fight under load. |

### **2 · Customer-Centric Craftsmanship**

| **#** | **Question** | **Look-for Signals** | **Rationale** |
| --- | --- | --- | --- |
| 1 | “Share a feature where user pain wasn’t obvious at first. How did you reveal it?” | Shadowed users, heat-map or interview insights, metric uplift post-fix | Validates hidden-pain discovery. |
| 2 | “Describe a time technical debt clashed with delivery for traders. How did you decide?” | Cost-of-delay calc, pilot usability test, phased refactor | Balancing constraints vs. user value. |
| 3 | “Tell me when you simplified UX at cost to backend elegance.” | Prioritized workflow, tracked NPS, iterated later | Checks willingness to trade ego for user joy. |
| 4 | “How have you turned qualitative feedback into backlog items?” | Thematic coding, JIRA IDs, quick wins list | Shows systematic voice-of-customer loop. |
| 5 | “Recall a bug caught by a non-tech stakeholder. How did you respond?” | Blameless stance, root-cause sharing, gratitude culture | Probes empathy and partnership. |

### **3 · Ownership & Proactivity**

| **#** | **Question** | **Signals** | **Rationale** |
| --- | --- | --- | --- |
| 1 | “Tell me about a project you rescued without formal mandate.” | Self-initiated audit, rallied resources, ROI metrics | Classic ownership test. |
| 2 | “Describe an incident where you paged yourself.” | Rapid triage, comms channel, post-incident RCA within 24 h | Aligns with value table’s self-paging cue. |
| 3 | “When did you push a deprecate-and-delete PR others avoided?” | Risk assessment, staged rollout, cleanup impact | Looks for proactive tech-debt removal. |
| 4 | “Give an example of setting guardrails before product asked.” | Forecasted blast radius, added budget alert | Demonstrates anticipatory thinking. |
| 5 | “Tell me about escalating a critical blocker sideways/up.” | Structured brief, solution options, exact ask | Shows bias for unblock vs. victim stance. |

### **4 · Observability & Guardrails First**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “Walk through monitoring you added to a green-field service.” | Chose metrics, logs, traces; SLOs + burn-rate alerts |
| 2 | “Describe catching an error through alerts before users noticed.” | Alert threshold, auto-rollback, MTTR data |
| 3 | “How have you chaos-tested a dependency?” | Fault injection, learnings, policy changes |
| 4 | “Share a time SLO burn forced scope cut.” | Data-informed stop, stakeholder comms |
| 5 | “What’s the first dashboard you open on-call, and why?” | Prioritized signals, reasoning |

### **5 · Data-Informed Iteration**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “Tell me how A/B data overturned your hypothesis.” | Experiment design, p-value, course-correct |
| 2 | “Describe a feature sunset based on metrics.” | Churn/usage graph, savings, redeploy resources |
| 3 | “Walk me through a dashboard you built for PMs.” | KPI definition, refresh cadence, adoption |
| 4 | “How did you handle conflicting data sources?” | Validation, triangulation, decision deferral |
| 5 | “Example of near-real-time feedback loop improving trading PnL.” | Latency, Sharpe delta, iteration cycle |

### **6 · Integrity & Reliability**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “Describe securing data integrity during a migration.” | Checksums, dual writes, back-out plan |
| 2 | “Tell me about resolving a Sev-0.” | RCA depth, fix-forward plan, learning broadcast |
| 3 | “When did you refuse a shortcut due to risk?” | Ethical stance, alternative path |
| 4 | “Explain an immutable audit log you built.” | Tech choice (QLDB), tamper resistance |
| 5 | “How do you verify fix durability?” | Regression tests, canary, observability |

### **7 · Security & Compliance First**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “Walk me through threat-modeling a new API.” | STRIDE/TM, mitigations, remediation SLA |
| 2 | “Describe rotating secrets without downtime.” | Parameter Store/SM, automation, blast test |
| 3 | “Give an example complying with a specific regulation.” | GDPR, SOX, crypto KYC; mapping → controls |
| 4 | “How did you catch a security flaw in PR review?” | Static scan, design comment, fix path |
| 5 | “Explain balancing latency vs. encryption.” | Benchmark, TLS tuning, handshake reuse |

### **8 · Collaboration & Knowledge-Sharing**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “Tell me about pairing with a domain expert.” | Mutual learning, deliverable quality |
| 2 | “Example of conflict resolved through RFC.” | Active listening, compromise, doc outcome |
| 3 | “How did you onboard a new hire fast?” | Buddy plan, cadenced feedback |
| 4 | “When did you turn tribal knowledge into wiki?” | Capture, peer edit, usage stats |
| 5 | “Describe giving a tech talk that shifted team practice.” | Audience fit, follow-up adoption |

### **9 · Continuous Learning & Mentorship**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “What skill did you level-up last quarter and how?” | Specific resource, project apply |
| 2 | “Share mentoring a junior to ship feature.” | Structured sessions, autonomy ramp, success metric |
| 3 | “Describe a time a mentee taught you.” | Humility, reverse mentoring |
| 4 | “How do you track personal learning backlog?” | Journal, OKR, conf notes |
| 5 | “When did you pilot a new tech then evangelize?” | PoC, risk log, internal workshop |

### **10 · Innovative Spirit**

| **Q** | **Signals** | **Rationale** |
| --- | --- | --- |
| 1 | “Tell me about a hack-day project that shipped.” | Problem framing, MVP, backlog merge |
| 2 | “Describe a novel solution that saved cost or latency.” | Creative leap, measurable impact |
| 3 | “When did you adapt tooling from another domain.” | Cross-pollination, proof of value |
| 4 | “Explain proposing risky idea and derisk plan.” | Small bets, guardrails |
| 5 | “Side project demonstrating passion?” | Motivation, tech stack, lessons |

### **11 · Quantitative Aptitude & Logical Reasoning**

| **#** | **Question** | **Look-for Signals** | **Design Rationale** |
| --- | --- | --- | --- |
| 1 | “Describe a complex problem you solved that required strong analytical or mathematical skills. How did you break it down?” | Structured approach, use of quantitative methods, clear logical steps, ability to simplify complexity. | Assesses ability to apply mathematical/logical thinking to real-world problems. |
| 2 | “Tell me about a time you had to explain a highly technical or quantitative concept to a non-technical audience. How did you ensure understanding?” | Clarity of communication, use of analogies, ability to adapt explanation to audience, patience. | Evaluates communication of complex ideas and logical structuring of thoughts. |
| 3 | “Give an example of a time you used data or numerical analysis to make a critical decision. What was the outcome?” | Data-driven decision making, understanding of statistical significance, impact measurement. | Probes practical application of quantitative reasoning. |
| 4 | “How do you approach debugging a system where the issue is subtle and requires deep logical deduction?” | Systematic troubleshooting, hypothesis testing, elimination of variables, attention to detail. | Tests logical problem-solving and analytical rigor. |
| 5 | “Describe a situation where you had to design a system or algorithm that involved complex interdependencies or multi-agent interactions. What challenges did you face and how did you overcome them?” | Understanding of system dynamics, ability to model complex interactions, foresight in design. | Directly assesses skills relevant to multi-agent systems and complex algorithms. |

### **12 · Agentic Mindset & LLM Literacy**

| **#** | **Question** | **Look-for Signals** | **Design Rationale** |
| --- | --- | --- | --- |
| 1 | "Describe a time you used an LLM-based tool (like Copilot or ChatGPT) to solve a complex problem. How did you go beyond simple prompting to get the result you needed?" | Mentions iterative prompt design, providing few-shot examples, or using the LLM as a "thought partner" to refine their approach. | Assesses LLM literacy and the ability to collaborate with AI tools. |
| 2 | "Tell me about a project where you had to integrate with an external API that was unreliable or had poor documentation. How did you build a resilient system around it?" | Discusses implementing retries, circuit breakers, or other resilience patterns. Shows an understanding of building robust systems that can handle failure. | Probes for classic systems thinking, which is crucial for agent orchestration. |
| 3 | "Imagine you are designing an agent to automate a workflow. How would you approach the design of the agent's tools and memory?" | Discusses the importance of clear tool definitions, state management, and providing the agent with the right context to make decisions. | Evaluates their understanding of agentic design patterns. |
| 4 | "Tell me about a time you had to learn a new technology or framework very quickly. What was your process?" | Demonstrates a structured approach to learning, a bias for action, and the ability to apply new knowledge effectively. | Assesses curiosity and lifelong learning, which are critical meta-skills for the agentic era. |

---

## **Putting It All Together**

1. **Prepare**: Assign two values per interviewer; share this guide and scoring rubric 48 h prior.
2. **Run**: Follow the flow; probe deeply until you hear quantifiable *Actions* and *Results*.
3. **Debrief**: Consolidate scores, surface evidence; reject “gut feel” absent data.
4. **Decide**: Hire only when candidate meets or exceeds bar on ≥ 8 / 11 values with no critical lows.

Adhering to this structured BEI playbook yields more reliable, bias-resistant decisions and ensures every new hire actively amplifies the mission, vision, and operating values of your engineering organization.