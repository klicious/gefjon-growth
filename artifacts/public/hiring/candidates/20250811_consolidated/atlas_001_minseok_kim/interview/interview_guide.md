# Interview Guide: Minseok Kim

## Pre-Interview Preparation (15 minutes)
- [ ] Review candidate's screening report and take-home assignment
- [ ] Prepare technical questions based on their AWS, OpenStack, Ansible background
- [ ] Set up technical discussion environment

## Interview Structure (90 minutes total)

### 1. Opening & Introductions (10 minutes)
- Welcome and introductions
- Brief overview of Gefjon Growth and the role
- Explain interview structure and timeline

### 2. BEI Core Values Assessment (60 minutes)

#### Value Assessment Priority Matrix
**HIGH PRIORITY** (6 minutes each): Customer-Centric Craftsmanship, Ownership & Proactivity, Integrity & Reliability, Continuous Learning & Mentorship  
**MEDIUM PRIORITY** (4 minutes each): Technical Excellence, Data-Informed Iteration, Collaboration & Knowledge-Sharing, Observability & Guardrails  
**STANDARD PRIORITY** (3 minutes each): Security & Compliance First, Innovative Spirit

#### Value-by-Value BEI Questions

##### 1. Technical Excellence & Scalable Elegance - SUGGESTED EVIDENCE
**Focus**: Verification of architectural thinking and scalability considerations  
**Time Allocation**: 4 minutes  
**Primary Question**: "I see you replaced memory-based ASG policy with RabbitMQ queue metrics. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you measure the improvement in responsiveness?"
- "What trade-offs did you consider when making this architectural decision?"
**What to Listen For**: System thinking, performance considerations, long-term maintainability
**Red Flags**: Quick fixes without architectural consideration, no performance metrics

##### 2. Customer-Centric Craftsmanship - MISSING EVIDENCE
**Focus**: Discovery of user-focused thinking and end-user consideration  
**Time Allocation**: 6 minutes  
**Primary Question**: "Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"  
**Follow-up Probes**:
- "How did you gather feedback from users or stakeholders?"
- "Can you describe a time when user feedback changed your technical approach?"
**What to Listen For**: User empathy, stakeholder consideration, user feedback integration
**Red Flags**: Technology-first thinking, no user validation mentioned

##### 3. Ownership & Proactivity - PROVEN EVIDENCE
**Focus**: Verification of leadership approach and initiative-taking patterns  
**Time Allocation**: 6 minutes  
**Primary Question**: "You mentioned leading the 'Imjangdan' backend and coordinating roles. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you coordinate with team members during this initiative?"
- "What challenges did you face in the delivery process?"
**What to Listen For**: Initiative-taking, accountability, leadership in ambiguous situations
**Red Flags**: Waiting for direction, avoiding responsibility

##### 4. Observability & Guardrails - SUGGESTED EVIDENCE
**Focus**: Verification of monitoring philosophy and operational practices  
**Time Allocation**: 4 minutes  
**Primary Question**: "I see you introduced observability tools like ES, Prometheus, and Grafana. Walk me through a specific situation where you implemented monitoring that caught a problem before it became critical. What was the situation, what metrics did you choose to track, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you decide which metrics are most important to monitor?"
- "Tell me about a time when monitoring data changed your decision-making"
**What to Listen For**: Proactive monitoring, operational excellence, data-driven operations
**Red Flags**: Reactive-only approach, no systematic monitoring strategy

##### 5. Data-Informed Iteration - MISSING EVIDENCE
**Focus**: Discovery of metrics-based decision making and evidence-based choices  
**Time Allocation**: 4 minutes  
**Primary Question**: "Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically validate whether a technical change was successful?"
- "Tell me about a time when data contradicted your initial assumptions"
**What to Listen For**: Evidence-based decision making, measurement focus, iterative improvement
**Red Flags**: Gut-feeling decisions, no measurement approach

##### 6. Integrity & Reliability - MISSING EVIDENCE
**Focus**: Discovery of ethical decision-making and commitment reliability  
**Time Allocation**: 6 minutes  
**Primary Question**: "Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you handle situations where stakeholders ask for shortcuts?"
- "Describe a time when you had to deliver difficult news to a team or manager"
**What to Listen For**: Ethical decision-making, quality focus, honest communication
**Red Flags**: Cutting corners, unreliable commitments, avoiding difficult conversations

##### 7. Security & Compliance First - MISSING EVIDENCE
**Focus**: Discovery of security-conscious practices and risk awareness  
**Time Allocation**: 3 minutes  
**Primary Question**: "Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically consider security when designing systems?"
**What to Listen For**: Security awareness, proactive risk identification
**Red Flags**: Security as afterthought, no security considerations mentioned

##### 8. Collaboration & Knowledge-Sharing - SUGGESTED EVIDENCE
**Focus**: Deep probe into teamwork and knowledge-sharing behaviors  
**Time Allocation**: 4 minutes  
**Primary Question**: "You mentioned presenting a Terraform & Ansible seminar. Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"  
**Follow-up Probes**:
- "How do you typically share knowledge with teammates who are less experienced?"
- "Describe your approach to documentation and knowledge transfer"
**What to Listen For**: Conflict resolution, teaching ability, collaborative approach
**Red Flags**: Poor communication, knowledge hoarding, team conflicts

##### 9. Continuous Learning & Mentorship - SUGGESTED EVIDENCE
**Focus**: Verification of learning motivation and knowledge-sharing behaviors  
**Time Allocation**: 6 minutes  
**Primary Question**: "I see you've built diverse projects across banking, fashion, and defense domains. Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you stay current with new technologies and best practices?"
- "Describe a time when you taught or mentored someone else"
**What to Listen For**: Learning agility, teaching others, staying current with industry
**Red Flags**: Stagnant skills, reluctance to learn, no teaching examples

##### 10. Innovative Spirit - MISSING EVIDENCE
**Focus**: Discovery of creative problem-solving and experimental approaches  
**Time Allocation**: 3 minutes  
**Primary Question**: "Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"  
**Follow-up Probes**:
- "How do you balance innovation with reliability and risk?"
**What to Listen For**: Creative problem-solving, willingness to experiment, novel approaches
**Red Flags**: Always status-quo, fear of new approaches, no creative solutions

### 3. Technical Deep Dive (30 minutes)

#### Core Technical Questions:
Based on candidate's AWS, OpenStack, Ansible background:

**System Design & Architecture**:
- "Walk me through how you would design a scalable task management API that needs to handle 100k+ daily active users"
- "Based on your AWS experience, how would you architect a multi-region disaster recovery solution?"

**Infrastructure & Automation**:
- "Describe your approach to infrastructure as code. What would your ideal CI/CD pipeline look like?"
- "How do you approach monitoring and observability in a microservices architecture?"

### 4. Cultural Fit & Candidate Questions (20 minutes)
- Company culture discussion and team dynamics
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline

## BEI Evaluation Framework

### Core Values Assessment (60% of evaluation)
**PRIMARY FOCUS VALUES** (24 points total - 6 points each):
- **Customer-Centric Craftsmanship**: Discovery of user-focused thinking
- **Ownership & Proactivity**: Verification of leadership and initiative
- **Integrity & Reliability**: Discovery of ethical decision-making
- **Continuous Learning & Mentorship**: Verification of growth mindset

**SECONDARY VALUES** (16 points total - 4 points each):
- **Technical Excellence**: Verification of scalability thinking  
- **Data-Informed Iteration**: Discovery of metrics-based decisions
- **Collaboration & Knowledge-Sharing**: Deep probe of teamwork
- **Observability & Guardrails**: Verification of operational excellence

**STANDARD VALUES** (6 points total - 3 points each):
- **Security & Compliance First**: Discovery of security awareness
- **Innovative Spirit**: Discovery of creative problem-solving

**Total BEI Score**: 46 points maximum

### Technical Competency (25% of evaluation)
- **System Design**: Architecture and scalability considerations (8 points)
- **Infrastructure Knowledge**: AWS, automation, and DevOps practices (8 points)
- **Problem-Solving**: Technical approach and methodology (9 points)

### Communication & Behavioral Consistency (15% of evaluation)
- **STAR Response Quality**: Complete situation-task-action-results responses (10 points)
- **Behavioral Pattern Consistency**: Consistent values demonstration across questions (5 points)

**Total Evaluation Score**: 100 points maximum
**Hiring Threshold**: ≥75 points (Strong Hire: ≥85, Hire: 75-84, Lean Hire: 65-74)

---
*Interview guide prepared for: Strong Hire candidate*
*Screening score: 9.1/10*
