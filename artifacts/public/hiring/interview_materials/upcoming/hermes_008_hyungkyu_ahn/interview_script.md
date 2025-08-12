# Interview Script: Hyungkyu Ahn (hermes_008)

## Pre-Interview Setup (5 minutes before start)
- [ ] Have candidate projects (arbitrage system, stock backtesting app) easily accessible
- [ ] Prepare note-taking template for STAR responses
- [ ] Set up timer for each interview section
- [ ] Review financial systems context for compliance/security questions

## Opening & BEI Introduction (10 minutes)

### Welcome & Context Setting
"Good [morning/afternoon], Hyungkyu. Thank you for taking the time to meet with us today. I'm [Name] and I'll be conducting your interview for the Backend Engineer position at Gefjon Growth. 

Before we begin, I'd like to give you a brief overview of how today's interview will be structured. We'll spend about 90 minutes together, with the majority focused on understanding your past experiences through specific behavioral examples, followed by some technical discussion focused on your systems programming background.

Do you have any questions about the structure before we begin?"

### BEI Methodology Explanation
"Today, I'll be using what we call Behavioral Event Interviewing, or BEI. The premise is simple: the best predictor of future performance is past behavior in similar situations. So I'll be asking you to share specific examples from your experience.

When I ask these questions, I'm looking for complete stories using what we call the STAR method:
- **Situation**: What was the context or background?
- **Task**: What was your specific responsibility or challenge?
- **Action**: What specific actions did YOU take?
- **Results**: What was the outcome and what did you learn?

I may ask follow-up questions to get more details about specific parts of your examples. The key is to focus on specific situations rather than general approaches. Does this make sense?"

### Transition to Questions
"Great. Let's begin with some questions about how you approach your work and the experiences that have shaped your professional development."

## Core Values BEI Assessment (60 minutes)

### 1. Customer-Centric Craftsmanship (7 minutes)
**DISCOVERY FOCUS** - No evidence found

"I'd like to start by understanding how you think about the end users of the systems you build."

**Primary Question**: 
"Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"

**Note-taking guide**: [Situation: Context/Users] [Task: Balance challenge] [Actions: User research/feedback] [Results: Impact on solution]

**If incomplete STAR, probe**:
- "Can you tell me more about the specific situation you were in?"
- "What exactly was your role and responsibility?"
- "Walk me through the specific actions you personally took"
- "What was the measurable outcome?"

**Follow-up Probes** (if time permits):
"How did you gather requirements for the arbitrage trading system?"
"Can you describe a time when user feedback changed your technical approach?"

**Red flags to note**: Technology-first thinking, no user validation, purely technical focus

### 2. Integrity & Reliability (7 minutes)
**DISCOVERY FOCUS** - No evidence found, financial context important

**Transition**: "Working with financial systems like your arbitrage platform requires high integrity. Let me understand your approach to difficult decisions."

**Primary Question**:
"Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Challenge/Pressure] [Task: Difficult choice] [Actions: Decision process] [Results: Outcome/learning]

**Follow-up Probes**:
"How do you handle situations where stakeholders ask for shortcuts in financial systems?"
"Describe a time when you had to deliver difficult news to a team or manager"

**Red flags to note**: Cutting corners, unreliable commitments, avoiding difficult conversations in financial context

### 3. Collaboration & Knowledge-Sharing (7 minutes)  
**DISCOVERY FOCUS** - No evidence found

**Transition**: "I'd like to explore your experience working with others and sharing knowledge."

**Primary Question**:
"Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"

**Note-taking guide**: [Situation: Conflict/disagreement] [Task: Resolution challenge] [Actions: Specific steps taken] [Results: Resolution/relationship]

**Follow-up Probes**:
"How do you typically share knowledge with teammates who are less experienced?"
"Describe your approach to documentation and knowledge transfer"

**Red flags to note**: Poor communication, knowledge hoarding, team conflicts

### 4. Continuous Learning & Mentorship (7 minutes)
**DISCOVERY FOCUS** - No evidence found

**Transition**: "Let's talk about how you approach learning and helping others grow."

**Primary Question**:
"Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Learning challenge] [Task: Knowledge gap] [Actions: Learning approach] [Results: Application/outcome]

**Follow-up Probes**:
"How do you stay current with new technologies and best practices?"
"Describe a time when you taught or mentored someone else"

**Red flags to note**: Stagnant skills, reluctance to learn, no teaching examples

### 5. Security & Compliance First (7 minutes)
**DISCOVERY FOCUS** - No evidence found, financial systems context

**Transition**: "Financial systems like your arbitrage platform have strict security requirements."

**Primary Question**:
"Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"

**Note-taking guide**: [Situation: Security context] [Task: Risk identification] [Actions: Mitigation steps] [Results: Resolution]

**Follow-up Probes**:
"How do you typically consider security when designing financial systems?"
"What security practices did you implement in the arbitrage system?"

**Red flags to note**: Security as afterthought, no financial compliance awareness

### 6. Technical Excellence & Scalable Elegance (5 minutes)
**VERIFICATION FOCUS** - Strong evidence from IPC optimization

**Transition**: "I want to understand your approach to technical architecture and performance."

**Primary Question**:
"I see you re-architected IPC from System V to ZeroMQ, doubling throughput from 50k/s to 100k/s. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Technical decision] [Task: Quick vs elegant choice] [Actions: Analysis/implementation] [Results: Performance impact]

**Follow-up Probes**:
"How did you measure and validate the performance improvement?"

**Red flags to note**: Quick fixes without analysis, no performance measurement

### 7. Ownership & Proactivity (5 minutes)
**VERIFICATION FOCUS** - Suggested evidence from system implementation

**Transition**: "I want to understand your approach to taking ownership and driving initiatives."

**Primary Question**:
"You implemented an end-to-end arbitrage system with distributed processes and monitoring. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Unassigned problem] [Task: Initiative needed] [Actions: Ownership steps] [Results: Impact/completion]

**Follow-up Probes**:
"How did you coordinate with other stakeholders during system development?"

**Red flags to note**: Waiting for direction, avoiding responsibility, purely technical focus

### 8. Observability & Guardrails (5 minutes)
**VERIFICATION FOCUS** - Evidence from blue/green deployment

**Transition**: "Let's discuss your approach to operational practices and monitoring."

**Primary Question**:
"I see you established blue/green deployment via GitHub Webhook + Jenkins. Walk me through a specific situation where you implemented monitoring or operational practices that caught a problem before it became critical. What was the situation, what practices did you implement, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: System/risk] [Task: Prevention need] [Actions: Implementation] [Results: Problem prevention]

**Follow-up Probes**:
"How do you decide what's important to monitor in a distributed system?"

**Red flags to note**: Reactive-only approach, no systematic operational thinking

### 9. Data-Informed Iteration (2.5 minutes)
**DEEP PROBE FOCUS** - Suggested evidence from performance work

**Transition**: "Let's talk about how you use data to make decisions."

**Primary Question**:
"Your performance measurements in the IPC migration suggest you use metrics. Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"

**Note-taking guide**: [Situation: Decision needed] [Task: Data analysis] [Actions: Collection/analysis] [Results: Decision/outcome]

**Red flags to note**: Gut-feeling decisions, no measurement approach

### 10. Innovative Spirit (2.5 minutes)
**DISCOVERY FOCUS** - No evidence found

**Transition**: "Finally, let's explore your approach to creative problem-solving."

**Primary Question**:
"Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"

**Note-taking guide**: [Situation: Problem context] [Task: Standard approach limits] [Actions: Creative solution] [Results: Innovation outcome]

**Red flags to note**: Always status-quo, fear of new approaches, no creative solutions

## Technical Deep Dive (30 minutes)

### Transition to Technical Discussion
"Thank you for sharing those experiences. Now I'd like to dive deeper into some technical aspects of your systems programming work."

### System Design Question (15 minutes)
"Design a low-latency trading system that needs to process 100k+ transactions per second with sub-millisecond response times. Focus on the architecture, data flow, and performance optimization."

**Evaluation criteria**:
- Low-latency system design thinking
- Performance optimization strategies
- Distributed system considerations
- Financial trading system understanding

### Systems Programming Deep Dive (15 minutes)
"Walk me through your ZeroMQ implementation in detail. Why ZeroMQ over other messaging solutions? How did you measure the performance improvements?"

**Follow-up**: "Describe your approach to performance optimization in systems programming. How do you identify and resolve bottlenecks?"

**Evaluation criteria**:
- Systems programming expertise
- Performance measurement methodology
- Trade-off analysis skills
- Technical decision-making process

## Cultural Fit & Questions (20 minutes)

### Company Culture Discussion (10 minutes)
"Based on what you've learned about Gefjon Growth, how do you see yourself contributing to our technical culture and values, particularly in our financial technology context?"

"What aspects of our engineering approach resonate most with you?"

### Candidate Questions (10 minutes)
"What questions do you have for me about the role, the team, or Gefjon Growth?"

**Common questions to be prepared for**:
- Financial technology stack and requirements
- Team structure and collaboration approach
- Performance expectations and growth opportunities
- Technology choices and architectural decisions

## Closing (5 minutes)

### Next Steps
"Thank you for sharing your experiences today, Hyungkyu. Do you have any final questions for me?"

"Here's what happens next: [explain timeline and process]"

"We should have a decision for you by [timeframe]. Is there anything else you'd like me to know as we wrap up?"

## Post-Interview Notes Template

### BEI Values Assessment Summary
**HIGH PRIORITY VALUES**:
- Customer-Centric Craftsmanship: [Score /7] - [Notes]
- Integrity & Reliability: [Score /7] - [Notes]  
- Collaboration & Knowledge-Sharing: [Score /7] - [Notes]
- Continuous Learning & Mentorship: [Score /7] - [Notes]
- Security & Compliance First: [Score /7] - [Notes]

**MEDIUM PRIORITY VALUES**:
- Technical Excellence: [Score /5] - [Notes]
- Ownership & Proactivity: [Score /5] - [Notes]
- Observability & Guardrails: [Score /5] - [Notes]

**STANDARD PRIORITY VALUES**:
- Data-Informed Iteration: [Score /2.5] - [Notes]
- Innovative Spirit: [Score /2.5] - [Notes]

**BEI Total**: [Score /55]

### Technical Assessment
- System Design: [Score /8] - [Notes]
- Systems Programming: [Score /8] - [Notes]
- Problem-Solving: [Score /9] - [Notes]

**Technical Total**: [Score /25]

### Communication & Consistency
- STAR Response Quality: [Score /10] - [Notes]
- Behavioral Pattern Consistency: [Score /5] - [Notes]

**Communication Total**: [Score /15]

### Overall Recommendation
**Total Score**: [Score /100]
**Recommendation**: [Strong Hire ≥85 | Hire 75-84 | Lean Hire 65-74 | No Hire <65]
**Key Strengths**: 
**Areas of Concern**: 
**Additional Notes**:

---
*Interview script prepared for BEI methodology*
*Focus: Comprehensive discovery of behavioral evidence with financial systems context*