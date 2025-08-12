# Interview Guide: Sumin Kim

## Pre-Interview Preparation (15 minutes)
- [ ] Review candidate's screening report and take-home assignment
- [ ] Prepare BEI questions based on their data migration and integration experience
- [ ] Set up technical discussion environment

## Interview Structure (90 minutes total)

### 1. Opening & Introductions (10 minutes)
- Welcome and introductions
- Brief overview of Gefjon Growth and the role
- Explain interview structure and timeline

### 2. BEI Core Values Assessment (60 minutes)

#### Value Assessment Priority Matrix
**HIGH PRIORITY** (6 minutes each): Customer-Centric Craftsmanship, Integrity & Reliability, Collaboration & Knowledge-Sharing, Technical Excellence  
**MEDIUM PRIORITY** (4 minutes each): Ownership & Proactivity, Data-Informed Iteration, Security & Compliance First, Observability & Guardrails  
**STANDARD PRIORITY** (3 minutes each): Innovative Spirit, Continuous Learning & Mentorship

#### Value-by-Value BEI Questions

##### 1. Technical Excellence & Scalable Elegance - PROVEN EVIDENCE
**Focus**: Verification of data migration architecture and scalability approach  
**Time Allocation**: 6 minutes  
**Primary Question**: "I see you designed an API-based migration that preserved referential integrity across tightly coupled schemas and reduced duration from 2 weeks to 3 days. Tell me about a specific time when you had to choose between a quick solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you decide on the parallelization strategy by queue-id?"
- "What trade-offs did you consider when designing the migration architecture?"
**What to Listen For**: System thinking, scalability patterns, architectural decisions
**Red Flags**: Quick fixes without architectural consideration, no scalability planning

##### 2. Customer-Centric Craftsmanship - MISSING EVIDENCE
**Focus**: Discovery of user-focused thinking in commerce systems  
**Time Allocation**: 6 minutes  
**Primary Question**: "You've worked on commerce systems like POD platforms and Weverse ByFans. Tell me about a specific project where you had to balance technical requirements with end-user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"  
**Follow-up Probes**:
- "How did you gather feedback from users in the commerce domain?"
- "Describe a time when user feedback changed your technical approach"
**What to Listen For**: User empathy, stakeholder consideration, user feedback integration
**Red Flags**: Technology-first thinking, no user validation mentioned

##### 3. Ownership & Proactivity - SUGGESTED EVIDENCE
**Focus**: Verification of initiative-taking in MySQL upgrade and integrations  
**Time Allocation**: 4 minutes  
**Primary Question**: "You led the RDS MySQL 5.7→8.0 upgrade and owned internal production integrations. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you coordinate with stakeholders during the MySQL upgrade?"
- "What challenges did you face when taking ownership of integrations?"
**What to Listen For**: Initiative-taking, accountability, ownership patterns
**Red Flags**: Waiting for direction, avoiding responsibility

##### 4. Observability & Guardrails - PROVEN EVIDENCE
**Focus**: Verification of monitoring philosophy and operational excellence  
**Time Allocation**: 4 minutes  
**Primary Question**: "I see you implemented retry mechanisms (≤5×) with Slack alerts and monitoring. Walk me through a specific situation where you implemented monitoring that caught a problem before it became critical. What was the situation, what metrics did you choose to track, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you decide which alerts and retry patterns are most important?"
- "Tell me about a time when monitoring data changed your operational approach"
**What to Listen For**: Proactive monitoring, operational excellence, alerting strategy
**Red Flags**: Reactive-only approach, no systematic monitoring strategy

##### 5. Data-Informed Iteration - SUGGESTED EVIDENCE
**Focus**: Exploration of metrics-based optimization approach  
**Time Allocation**: 4 minutes  
**Primary Question**: "You achieved measurable improvements like >60% turnaround reduction and 2 weeks→3 days migration time. Describe the specific process you used to measure, analyze, and validate those performance gains. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically establish performance baselines?"
- "Tell me about a time when data contradicted your initial optimization assumptions"
**What to Listen For**: Evidence-based decision making, measurement focus, iterative improvement
**Red Flags**: Gut-feeling decisions, no measurement approach

##### 6. Integrity & Reliability - MISSING EVIDENCE
**Focus**: Discovery of ethical decision-making and commitment reliability  
**Time Allocation**: 6 minutes  
**Primary Question**: "Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you handle situations where stakeholders ask for shortcuts during migrations?"
- "Describe a time when you had to deliver difficult news about data integrity or quality issues"
**What to Listen For**: Ethical decision-making, quality focus, honest communication
**Red Flags**: Cutting corners, unreliable commitments, avoiding difficult conversations

##### 7. Security & Compliance First - PROVEN EVIDENCE
**Focus**: Deep dive into security practices and risk awareness  
**Time Allocation**: 4 minutes  
**Primary Question**: "You applied AES-256 encryption and IP allowlisting for integrations. Tell me about a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically consider security when designing commerce system integrations?"
**What to Listen For**: Security awareness, proactive risk identification, encryption practices
**Red Flags**: Security as afterthought, no security considerations mentioned

##### 8. Collaboration & Knowledge-Sharing - MISSING EVIDENCE
**Focus**: Discovery of teamwork experiences and knowledge-sharing behaviors  
**Time Allocation**: 6 minutes  
**Primary Question**: "Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement about technical direction. What was the situation, what actions did you take, and how did it turn out?"  
**Follow-up Probes**:
- "How do you typically share knowledge with teammates about complex integrations?"
- "Describe your approach to documentation when working on multi-system migrations"
**What to Listen For**: Conflict resolution, teaching ability, collaborative approach
**Red Flags**: Poor communication, knowledge hoarding, team conflicts

##### 9. Continuous Learning & Mentorship - SUGGESTED EVIDENCE
**Focus**: Verification of technology adaptation and learning approach  
**Time Allocation**: 3 minutes  
**Primary Question**: "You mentioned recent focus on tests, MSA, and Kafka. Tell me about a specific time when you had to quickly learn a new technology to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you stay current with new technologies in commerce systems?"
**What to Listen For**: Learning agility, staying current with industry, technology adoption
**Red Flags**: Stagnant skills, reluctance to learn, no teaching examples

##### 10. Innovative Spirit - MISSING EVIDENCE
**Focus**: Discovery of creative problem-solving in commerce systems  
**Time Allocation**: 3 minutes  
**Primary Question**: "Tell me about a time when you came up with a creative or unconventional solution to a technical problem in your commerce systems work. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"  
**Follow-up Probes**:
- "How do you balance innovation with reliability in production commerce systems?"
**What to Listen For**: Creative problem-solving, willingness to experiment, novel approaches
**Red Flags**: Always status-quo, fear of new approaches, no creative solutions

### 3. Technical Deep Dive (30 minutes)

#### Core Technical Questions:
Based on candidate's data migration and commerce systems experience:

**Migration & Integration Architecture**:
- "Walk me through how you would design a data migration system for a high-volume e-commerce platform that needs zero downtime"
- "Based on your experience with commerce integrations, how would you approach building a multi-tenant system that serves different brands?"

**Operational Resilience**:
- "You've implemented retry mechanisms and monitoring. How would you design a resilient payment processing system?"
- "Describe your approach to handling data consistency across multiple commerce systems"

### 4. Cultural Fit & Candidate Questions (20 minutes)
- Company culture discussion and team dynamics
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline

## BEI Evaluation Framework

### Core Values Assessment (60% of evaluation)
**PRIMARY FOCUS VALUES** (24 points total - 6 points each):
- **Customer-Centric Craftsmanship**: Discovery of user-focused thinking in commerce systems
- **Integrity & Reliability**: Discovery of ethical decision-making
- **Collaboration & Knowledge-Sharing**: Discovery of teamwork experiences
- **Technical Excellence**: Verification of migration and integration architecture

**SECONDARY VALUES** (16 points total - 4 points each):
- **Ownership & Proactivity**: Verification of initiative-taking in upgrades/integrations
- **Data-Informed Iteration**: Exploration of metrics-based optimization
- **Security & Compliance First**: Deep dive into security practices
- **Observability & Guardrails**: Verification of monitoring and alerting practices

**STANDARD VALUES** (6 points total - 3 points each):
- **Innovative Spirit**: Discovery of creative problem-solving
- **Continuous Learning & Mentorship**: Verification of technology adaptation

**Total BEI Score**: 46 points maximum

### Technical Competency (25% of evaluation)
- **System Design**: Migration and integration architecture (8 points)
- **Commerce Systems**: E-commerce platforms and multi-system coordination (8 points)
- **Problem-Solving**: Technical approach and methodology (9 points)

### Communication & Behavioral Consistency (15% of evaluation)
- **STAR Response Quality**: Complete situation-task-action-results responses (10 points)
- **Behavioral Pattern Consistency**: Consistent values demonstration across questions (5 points)

**Total Evaluation Score**: 100 points maximum
**Hiring Threshold**: ≥75 points (Strong Hire: ≥85, Hire: 75-84, Lean Hire: 65-74)

---
*Interview guide prepared for: Hire candidate*
*Screening score: 8.0/10*