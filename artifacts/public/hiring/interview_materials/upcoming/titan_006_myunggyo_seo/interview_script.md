# Interview Script: Myunggyo Seo (titan_006)

## Pre-Interview Setup (5 minutes before start)
- [ ] Have candidate projects (RAG search, localization optimization, SSO) easily accessible
- [ ] Prepare note-taking template for STAR responses
- [ ] Set up timer for each interview section
- [ ] Review senior-level expectations for depth and leadership examples

## Opening & BEI Introduction (10 minutes)

### Welcome & Context Setting
"Good [morning/afternoon], Myunggyo. Thank you for taking the time to meet with us today. I'm [Name] and I'll be conducting your interview for the Senior Backend Engineer position at Gefjon Growth. 

Given your 8.5 years of experience, I'm looking forward to diving deep into your technical leadership and system design experience. We'll spend about 90 minutes together, with the majority focused on understanding your past experiences through specific behavioral examples, followed by some advanced technical discussion.

Do you have any questions about the structure before we begin?"

### BEI Methodology Explanation
"Today, I'll be using what we call Behavioral Event Interviewing, or BEI. Given your senior level, I'm particularly interested in understanding your leadership approach, technical decision-making process, and how you've handled complex situations.

When I ask these questions, I'm looking for complete stories using the STAR method:
- **Situation**: What was the context or background?
- **Task**: What was your specific responsibility or challenge?
- **Action**: What specific actions did YOU take?
- **Results**: What was the outcome and what did you learn?

I'll be looking for examples that demonstrate both technical depth and leadership maturity. Does this make sense?"

### Transition to Questions
"Great. Let's begin with some questions about your approach to building systems and leading technical initiatives."

## Core Values BEI Assessment (60 minutes)

### 1. Customer-Centric Craftsmanship (6 minutes)
**DISCOVERY FOCUS** - No evidence found

"I'd like to start by understanding how you think about the end users and business impact of the systems you build."

**Primary Question**: 
"Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"

**Note-taking guide**: [Situation: Context/Users] [Task: Balance challenge] [Actions: User research/feedback] [Results: Business impact]

**Follow-up Probes**:
"How did you gather user feedback for the RAG document search system?"
"Can you describe a time when user requirements changed your technical approach?"

**Red flags to note**: Technology-first thinking, no user validation, purely technical focus

### 2. Integrity & Reliability (6 minutes)
**DISCOVERY FOCUS** - No evidence found, senior responsibility expected

**Transition**: "With your senior experience, you've likely faced difficult decisions. Let me understand your approach."

**Primary Question**:
"Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Challenge/Pressure] [Task: Difficult choice] [Actions: Decision process] [Results: Outcome/learning]

**Follow-up Probes**:
"How do you handle situations where stakeholders ask for shortcuts?"
"Describe a time when you had to deliver difficult news to management"

**Red flags to note**: Cutting corners, unreliable commitments, avoiding difficult conversations

### 3. Innovative Spirit (6 minutes)
**DISCOVERY FOCUS** - No evidence found

**Transition**: "I'd like to explore your approach to creative problem-solving and innovation."

**Primary Question**:
"Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"

**Note-taking guide**: [Situation: Problem context] [Task: Innovation need] [Actions: Creative solution] [Results: Innovation outcome]

**Follow-up Probes**:
"How do you balance innovation with reliability in production systems?"
"Describe a time when you had to convince others to adopt a new approach"

**Red flags to note**: Always status-quo, fear of new approaches, no creative solutions

### 4. Collaboration & Knowledge-Sharing (6 minutes)
**DEEP PROBE FOCUS** - Weak evidence from leadership roles

**Transition**: "You mentioned holding team lead/manager roles. Let me understand your collaborative approach."

**Primary Question**:
"Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"

**Note-taking guide**: [Situation: Conflict/disagreement] [Task: Resolution challenge] [Actions: Leadership steps] [Results: Resolution/relationship]

**Follow-up Probes**:
"How do you typically share knowledge with teammates who are less experienced?"
"Describe your approach to documentation in MSA environments"

**Red flags to note**: Poor communication, knowledge hoarding, authoritarian leadership

### 5. Technical Excellence & Scalable Elegance (4 minutes)
**VERIFICATION FOCUS** - Strong evidence from optimization work

**Transition**: "I want to understand your approach to technical architecture and performance."

**Primary Question**:
"I see you cut localization pipeline time from 1,800 hours to 48 hours via parallelization. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Technical decision] [Task: Architecture choice] [Actions: Analysis/implementation] [Results: Performance impact]

**Follow-up Probes**:
"How did you measure and validate the 97% improvement?"

**Red flags to note**: Quick fixes without consideration, no performance measurement

### 6. Ownership & Proactivity (4 minutes)
**VERIFICATION FOCUS** - Strong evidence from solo delivery

**Transition**: "Let me understand your approach to ownership and solo delivery."

**Primary Question**:
"You delivered multiple solo systems including chat, SSO, and localization. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Unassigned problem] [Task: Initiative needed] [Actions: Ownership steps] [Results: Solo delivery impact]

**Follow-up Probes**:
"How did you coordinate with stakeholders when working solo on complex systems?"

**Red flags to note**: Waiting for direction, poor stakeholder management

### 7. Continuous Learning & Mentorship (4 minutes)
**VERIFICATION FOCUS** - Evidence from self-study and leadership

**Transition**: "Let's discuss your approach to learning and developing others."

**Primary Question**:
"I see you emphasize self-study of OS/CS fundamentals. Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Learning challenge] [Task: Knowledge gap] [Actions: Learning approach] [Results: Application outcome]

**Follow-up Probes**:
"Describe a time when you mentored someone in your team lead roles"

**Red flags to note**: Stagnant skills, no mentoring examples

### 8. Observability & Guardrails (4 minutes)
**VERIFICATION FOCUS** - Evidence from async pipeline design

**Transition**: "Let's explore your operational practices and monitoring approach."

**Primary Question**:
"I see you designed resilient async pipelines using Celery/RabbitMQ. Walk me through a specific situation where you implemented operational practices that caught a problem before it became critical. What was the situation, what practices did you implement, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: System/risk] [Task: Prevention need] [Actions: Implementation] [Results: Problem prevention]

**Follow-up Probes**:
"How do you decide what's important to monitor in MSA environments?"

**Red flags to note**: Reactive-only approach, no systematic strategy

### 9. Data-Informed Iteration (3 minutes)
**DEEP PROBE FOCUS** - Suggested evidence from optimization work

**Transition**: "Let's talk about how you use data to make decisions."

**Primary Question**:
"Your performance optimizations suggest strong use of metrics. Describe a specific situation where you used data or metrics to guide a technical decision. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"

**Note-taking guide**: [Situation: Decision needed] [Task: Data analysis] [Actions: Collection/analysis] [Results: Data-driven outcome]

**Red flags to note**: Gut-feeling decisions, no measurement approach

### 10. Security & Compliance First (3 minutes)
**VERIFICATION FOCUS** - Evidence from auth implementation

**Transition**: "Finally, let's discuss your approach to security."

**Primary Question**:
"I see you implemented HttpOnly cookie tokens and Keycloak/OIDC. Describe a specific time when you identified or addressed a security concern. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"

**Note-taking guide**: [Situation: Security context] [Task: Risk identification] [Actions: Mitigation steps] [Results: Security outcome]

**Red flags to note**: Security as afterthought, no systematic approach

## Technical Deep Dive (30 minutes)

### Transition to Technical Discussion
"Thank you for sharing those experiences. Now I'd like to dive into some advanced technical discussions given your senior background."

### System Design Question (15 minutes)
"Design a scalable financial trading platform that needs to handle multiple asset types with real-time price feeds, order management, and portfolio tracking. Focus on the microservices architecture, data flow, and performance optimization."

**Evaluation criteria**:
- Senior-level system design thinking
- MSA architecture decisions
- Performance and scalability considerations
- Real-time data processing approach

### Performance Deep Dive (15 minutes)
"Walk me through your approach to the content localization optimization in detail. What was your methodology for identifying bottlenecks and implementing the parallelization that achieved 97% improvement?"

**Follow-up**: "How do you approach performance optimization in microservices architectures generally?"

**Evaluation criteria**:
- Performance optimization methodology
- Systematic approach to bottleneck identification
- Parallelization and optimization strategies
- Senior-level technical thinking

## Cultural Fit & Questions (20 minutes)

### Company Culture Discussion (10 minutes)
"Based on what you've learned about Gefjon Growth, how do you see yourself contributing to our technical culture at a senior level?"

"What aspects of our engineering approach resonate most with your experience?"

### Candidate Questions (10 minutes)
"What questions do you have for me about the role, the team, or Gefjon Growth?"

## Closing (5 minutes)

### Next Steps
"Thank you for sharing your experiences today, Myunggyo. Do you have any final questions for me?"

"Here's what happens next: [explain timeline and process]"

## Post-Interview Notes Template

### BEI Values Assessment Summary
**HIGH PRIORITY VALUES**:
- Customer-Centric Craftsmanship: [Score /6] - [Notes]
- Integrity & Reliability: [Score /6] - [Notes]  
- Innovative Spirit: [Score /6] - [Notes]
- Collaboration & Knowledge-Sharing: [Score /6] - [Notes]

**MEDIUM PRIORITY VALUES**:
- Technical Excellence: [Score /4] - [Notes]
- Ownership & Proactivity: [Score /4] - [Notes]
- Continuous Learning: [Score /4] - [Notes]
- Observability & Guardrails: [Score /4] - [Notes]

**STANDARD PRIORITY VALUES**:
- Data-Informed Iteration: [Score /3] - [Notes]
- Security & Compliance: [Score /3] - [Notes]

**BEI Total**: [Score /46]

### Technical Assessment
- System Design: [Score /8] - [Notes]
- Performance Optimization: [Score /8] - [Notes]
- Problem-Solving: [Score /9] - [Notes]

**Technical Total**: [Score /25]

### Overall Recommendation
**Total Score**: [Score /100]
**Recommendation**: [Strong Hire ≥85 | Hire 75-84 | Lean Hire 65-74 | No Hire <65]
**Key Strengths**: 
**Areas of Concern**: 
**Senior-Level Assessment**: [Leadership readiness, technical depth, cultural contribution]

---
*Interview script prepared for BEI methodology - Senior candidate*
*Focus: Discovery of customer focus, integrity, innovation, and leadership collaboration*