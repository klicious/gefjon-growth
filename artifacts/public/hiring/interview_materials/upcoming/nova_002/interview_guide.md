# Interview Guide: Donghyun Kim (nova_002)

## Pre-Interview Preparation (15 minutes)
- [ ] Review candidate's With-Ins and Cafegory project details
- [ ] Prepare technical questions based on their Java/Spring Boot, AWS, and observability background
- [ ] Set up technical discussion environment

## Interview Structure (90 minutes total)

### 1. Opening & Introductions (10 minutes)
- Welcome and introductions
- Brief overview of Gefjon Growth and the role
- Explain interview structure and timeline

### 2. BEI Core Values Assessment (60 minutes)

#### Value Assessment Priority Matrix
**HIGH PRIORITY** (7.5 minutes each): Customer-Centric Craftsmanship, Integrity & Reliability, Collaboration & Knowledge-Sharing, Continuous Learning & Mentorship  
**MEDIUM PRIORITY** (5 minutes each): Observability & Guardrails, Technical Excellence, Ownership & Proactivity  
**STANDARD PRIORITY** (2.5 minutes each): Data-Informed Iteration, Security & Compliance First, Innovative Spirit

#### Value-by-Value BEI Questions

##### 1. Technical Excellence & Scalable Elegance - PROVEN EVIDENCE
**Focus**: Verification of architectural thinking and scalability considerations  
**Time Allocation**: 5 minutes  
**Primary Question**: "I see you standardized test patterns and converted to multi-module structure in Cafegory. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you measure the improvement from your 250 tests strategy?"
- "What trade-offs did you consider when designing the multi-module architecture?"
**What to Listen For**: System thinking, long-term maintainability, testing as architectural support
**Red Flags**: Quick fixes without architectural consideration, no systematic testing approach

##### 2. Customer-Centric Craftsmanship - MISSING EVIDENCE
**Focus**: Discovery of user-focused thinking and end-user consideration  
**Time Allocation**: 7.5 minutes  
**Primary Question**: "Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"  
**Follow-up Probes**:
- "How did you gather feedback from users when building the Cafegory platform?"
- "Can you describe a time when user feedback changed your technical approach?"
- "How do you typically think about the end-user experience when making technical decisions?"
**What to Listen For**: User empathy, stakeholder consideration, user feedback integration
**Red Flags**: Technology-first thinking, no user validation mentioned, purely internal focus

##### 3. Ownership & Proactivity - PROVEN EVIDENCE
**Focus**: Verification of leadership approach and initiative-taking patterns  
**Time Allocation**: 5 minutes  
**Primary Question**: "You mentioned driving the infrastructure migration from EC2→ECS. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you coordinate with stakeholders during this migration?"
- "What challenges did you face and how did you overcome them?"
**What to Listen For**: Initiative-taking, accountability, leadership in ambiguous situations
**Red Flags**: Waiting for direction, avoiding responsibility, no clear ownership examples

##### 4. Observability & Guardrails - PROVEN EVIDENCE
**Focus**: Verification of monitoring philosophy and operational practices  
**Time Allocation**: 5 minutes  
**Primary Question**: "I see you implemented Prometheus/Loki monitoring that reduced detection time from 30 minutes to 2 minutes. Walk me through a specific situation where you implemented monitoring that caught a problem before it became critical. What was the situation, what metrics did you choose to track, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you decide which metrics are most important to monitor?"
- "Tell me about a time when monitoring data changed your decision-making"
**What to Listen For**: Proactive monitoring, operational excellence, data-driven operations
**Red Flags**: Reactive-only approach, no systematic monitoring strategy

##### 5. Data-Informed Iteration - SUGGESTED EVIDENCE
**Focus**: Discovery of metrics-based decision making and evidence-based choices  
**Time Allocation**: 2.5 minutes  
**Primary Question**: "You fixed test flakiness by adopting Testcontainers. Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically validate whether a technical change was successful?"
**What to Listen For**: Evidence-based decision making, measurement focus, iterative improvement
**Red Flags**: Gut-feeling decisions, no measurement approach

##### 6. Integrity & Reliability - MISSING EVIDENCE
**Focus**: Discovery of ethical decision-making and commitment reliability  
**Time Allocation**: 7.5 minutes  
**Primary Question**: "Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you handle situations where stakeholders ask for shortcuts?"
- "Describe a time when you had to deliver difficult news to a team or manager"
- "Tell me about a commitment you made that was difficult to keep - how did you handle it?"
**What to Listen For**: Ethical decision-making, quality focus, honest communication
**Red Flags**: Cutting corners, unreliable commitments, avoiding difficult conversations

##### 7. Security & Compliance First - SUGGESTED EVIDENCE
**Focus**: Discovery of security-conscious practices and risk awareness  
**Time Allocation**: 2.5 minutes  
**Primary Question**: "Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically consider security when designing systems?"
**What to Listen For**: Security awareness, proactive risk identification
**Red Flags**: Security as afterthought, no security considerations mentioned

##### 8. Collaboration & Knowledge-Sharing - MISSING EVIDENCE
**Focus**: Discovery of teamwork and knowledge-sharing behaviors  
**Time Allocation**: 7.5 minutes  
**Primary Question**: "Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"  
**Follow-up Probes**:
- "How do you typically share knowledge with teammates who are less experienced?"
- "Describe your approach to documentation and knowledge transfer"
- "Give me an example of when you had to collaborate across different teams or functions"
**What to Listen For**: Conflict resolution, teaching ability, collaborative approach
**Red Flags**: Poor communication, knowledge hoarding, team conflicts

##### 9. Continuous Learning & Mentorship - MISSING EVIDENCE
**Focus**: Discovery of learning motivation and knowledge-sharing behaviors  
**Time Allocation**: 7.5 minutes  
**Primary Question**: "Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you stay current with new technologies and best practices?"
- "Describe a time when you taught or mentored someone else"
- "What's your approach to learning from failures or mistakes?"
**What to Listen For**: Learning agility, teaching others, staying current with industry
**Red Flags**: Stagnant skills, reluctance to learn, no teaching examples

##### 10. Innovative Spirit - MISSING EVIDENCE
**Focus**: Discovery of creative problem-solving and experimental approaches  
**Time Allocation**: 2.5 minutes  
**Primary Question**: "Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"  
**Follow-up Probes**:
- "How do you balance innovation with reliability and risk?"
**What to Listen For**: Creative problem-solving, willingness to experiment, novel approaches
**Red Flags**: Always status-quo, fear of new approaches, no creative solutions

### 3. Technical Deep Dive (30 minutes)

#### Core Technical Questions:
Based on candidate's Java/Spring Boot, AWS, and observability background:

**System Design & Architecture**:
- "Walk me through how you would design a scalable trading platform API that needs to handle 100k+ daily active users with sub-100ms response times"
- "Based on your AWS experience, how would you architect the monitoring and alerting for a multi-service platform?"

**Infrastructure & Observability**:
- "Describe your Prometheus/Loki setup in detail. How did you choose what to monitor and alert on?"
- "Walk me through your testing strategy for the Cafegory refactor - how did 250 tests guide your architecture decisions?"

### 4. Cultural Fit & Candidate Questions (20 minutes)
- Company culture discussion and team dynamics
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline

## BEI Evaluation Framework

### Core Values Assessment (60% of evaluation)
**PRIMARY FOCUS VALUES** (30 points total - 7.5 points each):
- **Customer-Centric Craftsmanship**: Discovery of user-focused thinking
- **Integrity & Reliability**: Discovery of ethical decision-making
- **Collaboration & Knowledge-Sharing**: Discovery of teamwork and teaching
- **Continuous Learning & Mentorship**: Discovery of growth mindset

**SECONDARY VALUES** (15 points total - 5 points each):
- **Observability & Guardrails**: Verification of operational excellence
- **Technical Excellence**: Verification of scalability thinking  
- **Ownership & Proactivity**: Verification of initiative-taking

**STANDARD VALUES** (7.5 points total - 2.5 points each):
- **Data-Informed Iteration**: Discovery of metrics-based decisions
- **Security & Compliance First**: Discovery of security awareness
- **Innovative Spirit**: Discovery of creative problem-solving

**Total BEI Score**: 52.5 points maximum

### Technical Competency (25% of evaluation)
- **System Design**: Architecture and scalability considerations (8 points)
- **Observability Knowledge**: Monitoring, alerting, and operational practices (8 points)
- **Problem-Solving**: Technical approach and methodology (9 points)

### Communication & Behavioral Consistency (15% of evaluation)
- **STAR Response Quality**: Complete situation-task-action-results responses (10 points)
- **Behavioral Pattern Consistency**: Consistent values demonstration across questions (5 points)

**Total Evaluation Score**: 100 points maximum
**Hiring Threshold**: ≥75 points (Strong Hire: ≥85, Hire: 75-84, Lean Hire: 65-74)

---
*Interview guide prepared for: Strong Hire candidate*
*BEI Focus: Discovery of collaboration, customer impact, and learning behaviors*