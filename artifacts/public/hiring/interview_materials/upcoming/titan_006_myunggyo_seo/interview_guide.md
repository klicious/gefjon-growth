# Interview Guide: Myunggyo Seo (titan_006)

## Pre-Interview Preparation (15 minutes)
- [ ] Review candidate's RAG document search, content localization, and SSO integration projects
- [ ] Prepare technical questions based on their Python/Django/FastAPI, AWS, and MSA background
- [ ] Set up technical discussion environment
- [ ] Note senior-level expectations for depth and leadership

## Interview Structure (90 minutes total)

### 1. Opening & Introductions (10 minutes)
- Welcome and introductions
- Brief overview of Gefjon Growth and the role
- Explain interview structure and timeline

### 2. BEI Core Values Assessment (60 minutes)

#### Value Assessment Priority Matrix
**HIGH PRIORITY** (6 minutes each): Customer-Centric Craftsmanship, Integrity & Reliability, Innovative Spirit, Collaboration & Knowledge-Sharing  
**MEDIUM PRIORITY** (4 minutes each): Technical Excellence, Ownership & Proactivity, Continuous Learning & Mentorship, Observability & Guardrails  
**STANDARD PRIORITY** (3 minutes each): Data-Informed Iteration, Security & Compliance First

#### Value-by-Value BEI Questions

##### 1. Technical Excellence & Scalable Elegance - PROVEN EVIDENCE
**Focus**: Verification of architectural decisions and system thinking  
**Time Allocation**: 4 minutes  
**Primary Question**: "I see you applied hexagonal/MSA architecture and cut localization pipeline time from 1,800 hours to 48 hours. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you measure and validate the 97% improvement in processing time?"
- "What trade-offs did you consider when choosing the SDK-driven parallelism approach?"
**What to Listen For**: System thinking, scalability considerations, performance measurement, architectural decision-making
**Red Flags**: Quick fixes without long-term consideration, no performance measurement

##### 2. Customer-Centric Craftsmanship - MISSING EVIDENCE
**Focus**: Discovery of user-focused thinking and stakeholder consideration  
**Time Allocation**: 6 minutes  
**Primary Question**: "Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"  
**Follow-up Probes**:
- "How did you gather user feedback for the RAG document search system?"
- "Can you describe a time when user requirements changed your technical approach?"
- "How do you typically think about the end-user experience when designing backend systems?"
**What to Listen For**: User empathy, stakeholder consideration, user feedback integration, business impact focus
**Red Flags**: Technology-first thinking, no user validation, purely technical focus

##### 3. Ownership & Proactivity - PROVEN EVIDENCE
**Focus**: Verification of solo delivery approach and leadership patterns  
**Time Allocation**: 4 minutes  
**Primary Question**: "You delivered multiple solo systems including Channels chat, SSO, and content localization. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How did you coordinate with stakeholders when working solo on complex systems?"
- "What challenges did you face in solo delivery and how did you overcome them?"
**What to Listen For**: Initiative-taking, accountability, leadership in ambiguous situations, solo delivery capability
**Red Flags**: Waiting for direction, avoiding responsibility, poor stakeholder management

##### 4. Observability & Guardrails - SUGGESTED EVIDENCE
**Focus**: Verification of systematic approach to operational excellence  
**Time Allocation**: 4 minutes  
**Primary Question**: "I see you designed resilient async pipelines using Celery/RabbitMQ and AWS managed services. Walk me through a specific situation where you implemented monitoring or operational practices that caught a problem before it became critical. What was the situation, what practices did you implement, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you decide what's important to monitor in MSA environments?"
- "Tell me about a time when operational practices prevented a major issue"
**What to Listen For**: Proactive monitoring, operational excellence, systematic practices, MSA operational thinking
**Red Flags**: Reactive-only approach, no systematic operational strategy

##### 5. Data-Informed Iteration - SUGGESTED EVIDENCE
**Focus**: Discovery of systematic approach to measurement and decision-making  
**Time Allocation**: 3 minutes  
**Primary Question**: "Your performance optimizations suggest strong use of metrics. Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically validate whether a performance optimization was successful?"
**What to Listen For**: Evidence-based decision making, measurement focus, iterative improvement approach
**Red Flags**: Gut-feeling decisions, no measurement approach

##### 6. Integrity & Reliability - MISSING EVIDENCE
**Focus**: Discovery of ethical decision-making and commitment reliability  
**Time Allocation**: 6 minutes  
**Primary Question**: "With your senior experience, you've likely faced difficult decisions. Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you handle situations where stakeholders ask for shortcuts?"
- "Describe a time when you had to deliver difficult news to management or clients"
- "Tell me about a commitment you made that was difficult to keep - how did you handle it?"
**What to Listen For**: Ethical decision-making, quality focus, honest communication, senior-level responsibility
**Red Flags**: Cutting corners, unreliable commitments, avoiding difficult conversations

##### 7. Security & Compliance First - SUGGESTED EVIDENCE
**Focus**: Verification of security practices and compliance awareness  
**Time Allocation**: 3 minutes  
**Primary Question**: "I see you implemented HttpOnly cookie tokens and centralized auth via Keycloak/OIDC. Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"  
**Follow-up Probes**:
- "How do you typically approach security in MSA environments?"
**What to Listen For**: Security awareness, proactive risk identification, security architecture understanding
**Red Flags**: Security as afterthought, no systematic security approach

##### 8. Collaboration & Knowledge-Sharing - SUGGESTED EVIDENCE
**Focus**: Discovery of specific teamwork examples and knowledge sharing practices  
**Time Allocation**: 6 minutes  
**Primary Question**: "You mentioned holding team lead/manager roles. Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"  
**Follow-up Probes**:
- "How do you typically share knowledge with teammates who are less experienced?"
- "Describe your approach to documentation and knowledge transfer in MSA environments"
- "Give me an example of when you had to collaborate across different teams or functions"
**What to Listen For**: Conflict resolution, teaching ability, collaborative approach, leadership communication
**Red Flags**: Poor communication, knowledge hoarding, team conflicts, authoritarian leadership

##### 9. Continuous Learning & Mentorship - SUGGESTED EVIDENCE
**Focus**: Verification of self-study approach and mentoring experiences  
**Time Allocation**: 4 minutes  
**Primary Question**: "I see you emphasize self-study of OS/CS fundamentals applied to system design. Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"  
**Follow-up Probes**:
- "How do you stay current with new technologies in the rapidly evolving backend space?"
- "Describe a time when you mentored or developed someone else in your team lead roles"
**What to Listen For**: Learning agility, teaching others, staying current with industry, systematic learning approach
**Red Flags**: Stagnant skills, reluctance to learn, no mentoring examples

##### 10. Innovative Spirit - MISSING EVIDENCE
**Focus**: Discovery of creative problem-solving beyond performance optimization  
**Time Allocation**: 6 minutes  
**Primary Question**: "Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"  
**Follow-up Probes**:
- "How do you balance innovation with reliability in production systems?"
- "Describe a time when you had to convince others to adopt a new or unconventional approach"
**What to Listen For**: Creative problem-solving, willingness to experiment, novel approaches, innovation leadership
**Red Flags**: Always status-quo, fear of new approaches, no creative solutions

### 3. Technical Deep Dive (30 minutes)

#### Core Technical Questions:
Based on candidate's senior Python/Django/FastAPI and MSA background:

**System Design & Architecture**:
- "Design a scalable financial trading platform that needs to handle multiple asset types with real-time price feeds, order management, and portfolio tracking. Focus on the microservices architecture, data flow, and performance optimization."
- "How would you architect a system like your RAG document search but for real-time financial data analysis and alerts?"

**Performance & Optimization**:
- "Walk me through your approach to the content localization optimization. What was your methodology for identifying bottlenecks and implementing parallelization?"
- "How do you approach performance optimization in microservices architectures? What metrics do you track?"

### 4. Cultural Fit & Candidate Questions (20 minutes)
- Company culture discussion and team dynamics
- Encourage candidate questions about role, team, company
- Discuss next steps and timeline

## BEI Evaluation Framework

### Core Values Assessment (60% of evaluation)
**PRIMARY FOCUS VALUES** (24 points total - 6 points each):
- **Customer-Centric Craftsmanship**: Discovery of user-focused thinking
- **Integrity & Reliability**: Discovery of ethical decision-making and senior responsibility
- **Innovative Spirit**: Discovery of creative problem-solving beyond optimization
- **Collaboration & Knowledge-Sharing**: Discovery of leadership and teamwork

**SECONDARY VALUES** (16 points total - 4 points each):
- **Technical Excellence**: Verification of architectural thinking  
- **Ownership & Proactivity**: Verification of solo delivery and leadership
- **Continuous Learning & Mentorship**: Verification of learning and teaching
- **Observability & Guardrails**: Verification of operational excellence

**STANDARD VALUES** (6 points total - 3 points each):
- **Data-Informed Iteration**: Discovery of metrics-based decisions
- **Security & Compliance First**: Verification of security practices

**Total BEI Score**: 46 points maximum

### Technical Competency (25% of evaluation)
- **System Design**: MSA architecture and scalability considerations (8 points)
- **Performance Optimization**: Methodology and results achievement (8 points)
- **Problem-Solving**: Senior-level technical approach and leadership (9 points)

### Communication & Behavioral Consistency (15% of evaluation)
- **STAR Response Quality**: Complete situation-task-action-results responses (10 points)
- **Behavioral Pattern Consistency**: Consistent values demonstration across questions (5 points)

**Total Evaluation Score**: 100 points maximum
**Hiring Threshold**: ≥75 points (Strong Hire: ≥85, Hire: 75-84, Lean Hire: 65-74)

---
*Interview guide prepared for: Strong Hire senior candidate*
*BEI Focus: Discovery of customer-centric thinking, integrity, innovation, and collaboration at senior level*