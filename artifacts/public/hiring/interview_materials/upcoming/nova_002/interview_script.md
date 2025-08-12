# Interview Script: Donghyun Kim (nova_002)

## Pre-Interview Setup (5 minutes before start)
- [ ] Have candidate resume and projects (With-Ins, Cafegory) easily accessible
- [ ] Prepare note-taking template for STAR responses
- [ ] Set up timer for each interview section

## Opening & BEI Introduction (10 minutes)

### Welcome & Context Setting
"Good [morning/afternoon], Donghyun. Thank you for taking the time to meet with us today. I'm [Name] and I'll be conducting your interview for the Backend Engineer position at Gefjon Growth. 

Before we begin, I'd like to give you a brief overview of how today's interview will be structured. We'll spend about 90 minutes together, with the majority focused on understanding your past experiences through specific behavioral examples, followed by some technical discussion.

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

### 1. Customer-Centric Craftsmanship (7.5 minutes)
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
"How did you gather feedback from users when building the Cafegory platform?"
"Can you describe a time when user feedback changed your technical approach?"

**Red flags to note**: Technology-first thinking, no user validation, purely internal focus

### 2. Integrity & Reliability (7.5 minutes)
**DISCOVERY FOCUS** - No evidence found

**Transition**: "Now I'd like to understand how you handle challenging situations and commitments."

**Primary Question**:
"Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Challenge/Pressure] [Task: Difficult choice] [Actions: Decision process] [Results: Outcome/learning]

**Follow-up Probes**:
"How do you handle situations where stakeholders ask for shortcuts?"
"Describe a time when you had to deliver difficult news to a team or manager"

**Red flags to note**: Cutting corners, unreliable commitments, avoiding difficult conversations

### 3. Collaboration & Knowledge-Sharing (7.5 minutes)  
**DISCOVERY FOCUS** - No evidence found

**Transition**: "I'd like to explore your experience working with others and sharing knowledge."

**Primary Question**:
"Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"

**Note-taking guide**: [Situation: Conflict/disagreement] [Task: Resolution challenge] [Actions: Specific steps taken] [Results: Resolution/relationship]

**Follow-up Probes**:
"How do you typically share knowledge with teammates who are less experienced?"
"Describe your approach to documentation and knowledge transfer"

**Red flags to note**: Poor communication, knowledge hoarding, team conflicts

### 4. Continuous Learning & Mentorship (7.5 minutes)
**DISCOVERY FOCUS** - No evidence found

**Transition**: "Let's talk about how you approach learning and helping others grow."

**Primary Question**:
"Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Learning challenge] [Task: Knowledge gap] [Actions: Learning approach] [Results: Application/outcome]

**Follow-up Probes**:
"How do you stay current with new technologies and best practices?"
"Describe a time when you taught or mentored someone else"

**Red flags to note**: Stagnant skills, reluctance to learn, no teaching examples

### 5. Observability & Guardrails (5 minutes)
**VERIFICATION FOCUS** - Strong evidence from monitoring implementation

**Transition**: "I noticed your impressive work with monitoring and observability. Let me understand this better."

**Primary Question**:
"I see you implemented Prometheus/Loki monitoring that reduced detection time from 30 minutes to 2 minutes. Walk me through a specific situation where you implemented monitoring that caught a problem before it became critical. What was the situation, what metrics did you choose to track, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: System/risk] [Task: Monitoring need] [Actions: Implementation choices] [Results: Prevention/improvement]

**Follow-up Probes**:
"How do you decide which metrics are most important to monitor?"

**Red flags to note**: Reactive-only approach, no systematic monitoring strategy

### 6. Technical Excellence & Scalable Elegance (5 minutes)
**VERIFICATION FOCUS** - Strong evidence from multi-module architecture

**Transition**: "Let's dive into your approach to technical architecture and quality."

**Primary Question**:
"I see you standardized test patterns and converted to multi-module structure in Cafegory. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Technical decision] [Task: Quick vs elegant choice] [Actions: Analysis/implementation] [Results: Long-term impact]

**Follow-up Probes**:
"How did you measure the improvement from your 250 tests strategy?"

**Red flags to note**: Quick fixes without consideration, no systematic testing approach

### 7. Ownership & Proactivity (5 minutes)
**VERIFICATION FOCUS** - Evidence from ECS migration

**Transition**: "I want to understand your approach to taking ownership and driving initiatives."

**Primary Question**:
"You mentioned driving the infrastructure migration from EC2→ECS. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"

**Note-taking guide**: [Situation: Unassigned problem] [Task: Initiative needed] [Actions: Ownership steps] [Results: Impact/completion]

**Follow-up Probes**:
"How did you coordinate with stakeholders during this migration?"

**Red flags to note**: Waiting for direction, avoiding responsibility

### 8. Data-Informed Iteration (2.5 minutes)
**DEEP PROBE FOCUS** - Weak evidence from testing approach

**Transition**: "Let's talk about how you use data to make decisions."

**Primary Question**:
"You fixed test flakiness by adopting Testcontainers. Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"

**Note-taking guide**: [Situation: Decision needed] [Task: Data analysis] [Actions: Collection/analysis] [Results: Decision/outcome]

**Red flags to note**: Gut-feeling decisions, no measurement approach

### 9. Security & Compliance First (2.5 minutes)
**DISCOVERY FOCUS** - Minimal evidence

**Transition**: "I'd like to understand your approach to security and risk management."

**Primary Question**:
"Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"

**Note-taking guide**: [Situation: Security context] [Task: Risk identification] [Actions: Mitigation steps] [Results: Resolution]

**Red flags to note**: Security as afterthought, no security considerations

### 10. Innovative Spirit (2.5 minutes)
**DISCOVERY FOCUS** - No evidence found

**Transition**: "Finally, let's explore your approach to creative problem-solving."

**Primary Question**:
"Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"

**Note-taking guide**: [Situation: Problem context] [Task: Standard approach limits] [Actions: Creative solution] [Results: Innovation outcome]

**Red flags to note**: Always status-quo, fear of new approaches

## Technical Deep Dive (30 minutes)

### Transition to Technical Discussion
"Thank you for sharing those experiences. Now I'd like to dive deeper into some technical aspects of your work."

### System Design Question (15 minutes)
"Walk me through how you would design a scalable trading platform API that needs to handle 100k+ daily active users with sub-100ms response times. Focus on the architecture, data flow, and how you'd ensure reliability."

**Evaluation criteria**:
- System design thinking
- Scalability considerations  
- Performance optimization
- Reliability patterns

### Observability Deep Dive (15 minutes)
"Describe your Prometheus/Loki setup in detail. How did you choose what to monitor and alert on? Walk me through your decision-making process."

**Follow-up**: "How did your 250 tests in the Cafegory refactor guide your architecture decisions?"

**Evaluation criteria**:
- Monitoring strategy
- Operational thinking
- Testing philosophy
- Decision-making process

## Cultural Fit & Questions (20 minutes)

### Company Culture Discussion (10 minutes)
"Based on what you've learned about Gefjon Growth, how do you see yourself contributing to our technical culture and values?"

"What aspects of our engineering approach resonate most with you?"

### Candidate Questions (10 minutes)
"What questions do you have for me about the role, the team, or Gefjon Growth?"

**Common questions to be prepared for**:
- Team structure and collaboration
- Technology stack and tooling
- Learning and development opportunities
- Project types and challenges

## Closing (5 minutes)

### Next Steps
"Thank you for sharing your experiences today, Donghyun. Do you have any final questions for me?"

"Here's what happens next: [explain timeline and process]"

"We should have a decision for you by [timeframe]. Is there anything else you'd like me to know as we wrap up?"

## Post-Interview Notes Template

### BEI Values Assessment Summary
**HIGH PRIORITY VALUES**:
- Customer-Centric Craftsmanship: [Score /7.5] - [Notes]
- Integrity & Reliability: [Score /7.5] - [Notes]  
- Collaboration & Knowledge-Sharing: [Score /7.5] - [Notes]
- Continuous Learning & Mentorship: [Score /7.5] - [Notes]

**MEDIUM PRIORITY VALUES**:
- Observability & Guardrails: [Score /5] - [Notes]
- Technical Excellence: [Score /5] - [Notes]
- Ownership & Proactivity: [Score /5] - [Notes]

**STANDARD PRIORITY VALUES**:
- Data-Informed Iteration: [Score /2.5] - [Notes]
- Security & Compliance First: [Score /2.5] - [Notes]
- Innovative Spirit: [Score /2.5] - [Notes]

**BEI Total**: [Score /52.5]

### Technical Assessment
- System Design: [Score /8] - [Notes]
- Observability Knowledge: [Score /8] - [Notes]
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
*Focus: Discovery of missing behavioral evidence with verification of technical strengths*