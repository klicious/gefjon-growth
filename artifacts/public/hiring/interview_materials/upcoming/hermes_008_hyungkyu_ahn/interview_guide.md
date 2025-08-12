# Interview Guide: Hyungkyu Ahn (hermes_008)

## Pre-Interview Preparation (15 minutes)
- [ ] Review candidate's crypto arbitrage system and stock backtesting projects
- [ ] Prepare technical questions based on their C/ZeroMQ, distributed systems background
- [ ] Set up technical discussion environment
- [ ] Note financial systems context for security/compliance questions

## Interview Structure (90 minutes total)

### 1. Opening & Introductions (10 minutes)
- Welcome and introductions
- Brief overview of Gefjon Growth and the role
- Explain interview structure and timeline

### 2. BEI Core Values Assessment (60 minutes)

#### Value Assessment Priority Matrix
**HIGH PRIORITY** (7 minutes each): Customer-Centric Craftsmanship, Integrity & Reliability, Collaboration & Knowledge-Sharing, Continuous Learning & Mentorship, Security & Compliance First  
**MEDIUM PRIORITY** (5 minutes each): Technical Excellence, Ownership & Proactivity, Observability & Guardrails  
**STANDARD PRIORITY** (2.5 minutes each): Data-Informed Iteration, Innovative Spirit

#### Value-by-Value BEI Questions

##### 1. Technical Excellence & Scalable Elegance - PROVEN EVIDENCE
**Focus**: Verification of architectural thinking and performance-focused decision making  
**Time Allocation**: 5 minutes  
**Primary Question**: "I see you re-architected IPC from System V to ZeroMQ, doubling throughput from 50k/s to 100k/s. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you measure and validate the performance improvement?"
- "What trade-offs did you consider when choosing ZeroMQ over other alternatives?"
**What to Listen For**: System thinking, performance analysis, long-term architectural decisions
**Red Flags**: Quick fixes without analysis, no performance measurement, poor trade-off evaluation

##### 2. Customer-Centric Craftsmanship - MISSING EVIDENCE
**Focus**: Discovery of user-focused thinking and stakeholder consideration  
**Time Allocation**: 7 minutes  
**Primary Question**: "Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"  
**Follow-up Probes**:
- "How did you gather requirements for the arbitrage trading system?"
- "Can you describe a time when user feedback changed your technical approach?"
- "How do you typically think about the end-user experience when making technical decisions?"
**What to Listen For**: User empathy, stakeholder consideration, user feedback integration
**Red Flags**: Technology-first thinking, no user validation, purely internal/technical focus

##### 3. Ownership & Proactivity - SUGGESTED EVIDENCE
**Focus**: Verification of leadership patterns and initiative-taking beyond technical tasks  
**Time Allocation**: 5 minutes  
**Primary Question**: "You implemented an end-to-end arbitrage system with distributed processes and monitoring. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you coordinate with other stakeholders during system development?"
- "What challenges did you face and how did you overcome them?"
**What to Listen For**: Initiative-taking, accountability, leadership in ambiguous situations
**Red Flags**: Waiting for direction, avoiding responsibility, purely technical focus

##### 4. Observability & Guardrails - SUGGESTED EVIDENCE
**Focus**: Verification of systematic approach to operational practices  
**Time Allocation**: 5 minutes  
**Primary Question**: "I see you established blue/green deployment via GitHub Webhook + Jenkins. Walk me through a specific situation where you implemented monitoring or operational practices that caught a problem before it became critical. What was the situation, what practices did you implement, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you decide what's important to monitor in a distributed system?"
- "Tell me about a time when operational practices helped prevent an issue"
**What to Listen For**: Proactive monitoring, operational excellence, systematic practices
**Red Flags**: Reactive-only approach, no systematic operational thinking

##### 5. Data-Informed Iteration - SUGGESTED EVIDENCE
**Focus**: Discovery of systematic approach to measurement and decision-making  
**Time Allocation**: 2.5 minutes  
**Primary Question**: "Your performance measurements in the IPC migration suggest you use metrics. Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically validate whether a technical change was successful?"
**What to Listen For**: Evidence-based decision making, measurement focus, iterative improvement
**Red Flags**: Gut-feeling decisions, no measurement approach

##### 6. Integrity & Reliability - MISSING EVIDENCE
**Focus**: Discovery of ethical decision-making and commitment reliability in financial context  
**Time Allocation**: 7 minutes  
**Primary Question**: "Working with financial systems like arbitrage trading requires high integrity. Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you handle situations where stakeholders ask for shortcuts in financial systems?"
- "Describe a time when you had to deliver difficult news to a team or manager"
- "Tell me about a commitment you made that was difficult to keep - how did you handle it?"
**What to Listen For**: Ethical decision-making, quality focus, honest communication, financial responsibility
**Red Flags**: Cutting corners, unreliable commitments, avoiding difficult conversations

##### 7. Security & Compliance First - MISSING EVIDENCE
**Focus**: Discovery of security practices in financial systems context  
**Time Allocation**: 7 minutes  
**Primary Question**: "Financial systems like your arbitrage platform have strict security requirements. Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically consider security when designing financial systems?"
- "What security practices did you implement in the arbitrage system?"
- "How do you balance performance with security requirements?"
**What to Listen For**: Security awareness, financial compliance understanding, proactive risk identification
**Red Flags**: Security as afterthought, no financial compliance awareness

##### 8. Collaboration & Knowledge-Sharing - MISSING EVIDENCE
**Focus**: Discovery of teamwork and knowledge-sharing behaviors  
**Time Allocation**: 7 minutes  
**Primary Question**: "Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"  
**Follow-up Probes**:
- "How do you typically share knowledge with teammates who are less experienced?"
- "Describe your approach to documentation and knowledge transfer"
- "Give me an example of when you had to collaborate across different teams or functions"
**What to Listen For**: Conflict resolution, teaching ability, collaborative approach
**Red Flags**: Poor communication, knowledge hoarding, team conflicts

##### 9. Continuous Learning & Mentorship - MISSING EVIDENCE
**Focus**: Discovery of learning agility and teaching/mentoring experiences  
**Time Allocation**: 7 minutes  
**Primary Question**: "Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you stay current with new technologies and best practices?"
- "Describe a time when you taught or mentored someone else"
- "What's your approach to learning from failures or mistakes?"
**What to Listen For**: Learning agility, teaching others, staying current with industry
**Red Flags**: Stagnant skills, reluctance to learn, no teaching examples

##### 10. Innovative Spirit - MISSING EVIDENCE
**Focus**: Discovery of creative approaches beyond performance optimization  
**Time Allocation**: 2.5 minutes  
**Primary Question**: "Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"  
**Follow-up Probes**:
- "How do you balance innovation with reliability in financial systems?"
**What to Listen For**: Creative problem-solving, willingness to experiment, novel approaches
**Red Flags**: Always status-quo, fear of new approaches, no creative solutions

### 3. Technical Deep Dive (30 minutes)

#### Core Technical Questions:
Based on candidate's systems programming and distributed systems background:

**System Design & Architecture**:
- "Design a low-latency trading system that needs to process 100k+ transactions per second with sub-millisecond response times. Focus on the architecture, data flow, and performance optimization."
- "How would you architect a distributed arbitrage system with real-time price feeds from multiple exchanges?"

**Systems Programming & Performance**:
- "Walk me through your ZeroMQ implementation. Why ZeroMQ over other messaging solutions?"
- "Describe your approach to performance optimization in systems programming. How do you identify and resolve bottlenecks?"

### 4. Cultural Fit & Candidate Questions (20 minutes)
- Company culture discussion and team dynamics
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline

## BEI Evaluation Framework

### Core Values Assessment (60% of evaluation)
**PRIMARY FOCUS VALUES** (35 points total - 7 points each):
- **Customer-Centric Craftsmanship**: Discovery of user-focused thinking
- **Integrity & Reliability**: Discovery of ethical decision-making in financial context
- **Collaboration & Knowledge-Sharing**: Discovery of teamwork and teaching
- **Continuous Learning & Mentorship**: Discovery of growth mindset
- **Security & Compliance First**: Discovery of financial systems security awareness

**SECONDARY VALUES** (15 points total - 5 points each):
- **Technical Excellence**: Verification of architectural thinking  
- **Ownership & Proactivity**: Verification of initiative-taking
- **Observability & Guardrails**: Verification of operational excellence

**STANDARD VALUES** (5 points total - 2.5 points each):
- **Data-Informed Iteration**: Discovery of metrics-based decisions
- **Innovative Spirit**: Discovery of creative problem-solving

**Total BEI Score**: 55 points maximum

### Technical Competency (25% of evaluation)
- **System Design**: Low-latency architecture and performance considerations (8 points)
- **Systems Programming**: C/ZeroMQ expertise and optimization (8 points)
- **Problem-Solving**: Technical approach and methodology (9 points)

### Communication & Behavioral Consistency (15% of evaluation)
- **STAR Response Quality**: Complete situation-task-action-results responses (10 points)
- **Behavioral Pattern Consistency**: Consistent values demonstration across questions (5 points)

**Total Evaluation Score**: 100 points maximum
**Hiring Threshold**: ≥75 points (Strong Hire: ≥85, Hire: 75-84, Lean Hire: 65-74)

---
*Interview guide prepared for: Lean Hire candidate with systems expertise*
*BEI Focus: Comprehensive discovery of missing behavioral evidence, especially in financial context*