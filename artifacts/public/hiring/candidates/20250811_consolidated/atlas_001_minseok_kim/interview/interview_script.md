# Interview Script: Minseok Kim

## Pre-Interview Setup
- [ ] Review candidate materials (screening report, take-home assignment)
- [ ] Prepare technical discussion environment
- [ ] Have evaluation form ready

---

## Interview Script

### Opening (10 minutes)

**Interviewer**: "Hi Minseok Kim, thank you for joining us today. I'm [Name], [Title] at Gefjon Growth. How are you doing today?"

*[Wait for response, engage in brief small talk]*

**Interviewer**: "Great! Let me start by telling you a bit about Gefjon Growth and this role, then we'll dive into learning more about you and your background."

*[Brief company overview - 2-3 minutes]*

**Interviewer**: "The structure for today's interview will be about 120 minutes total. We'll start with understanding our approach to behavioral interviewing, then systematically explore your past experiences related to our core values, followed by technical discussions and your questions. This approach helps us understand not just what you can do, but how you work and make decisions. Does that sound good?"

**BEI Methodology Explanation**:
"We use a method called Behavioral Event Interviewing, where we'll ask you to share specific examples from your past experiences. Each question will follow a STAR format - we want to understand the Situation you were in, the Task you needed to accomplish, the specific Actions you took, and the Results that followed. The key is being as specific as possible about what YOU personally did in each situation."

### BEI Core Values Assessment (60 minutes)

#### 1. Technical Excellence & Scalable Elegance (4 minutes)
**Interviewer**: "I see from your background you replaced memory-based ASG policy with RabbitMQ queue metrics. Tell me about a specific time when you had to choose between a quick technical solution and a more elegant, scalable approach. What was the situation, what factors did you consider, what actions did you take, and what were the results?"

*[Wait for complete STAR response. If incomplete, probe:]*
- "How did you measure the improvement in responsiveness?"
- "What trade-offs did you consider when making this architectural decision?"

*[Listen for: System thinking, performance considerations, long-term maintainability]*
*[Red flags: Quick fixes without architectural consideration, no performance metrics]*

#### 2. Customer-Centric Craftsmanship (6 minutes)
**Interviewer**: "Now let's talk about user focus. Tell me about a specific project where you had to balance technical requirements with user needs. What was the situation, who were the end users, what actions did you take to understand their needs, and how did it impact the final solution?"

*[If response is vague, probe:]*
- "How did you gather feedback from users or stakeholders?"
- "Can you describe a time when user feedback changed your technical approach?"

*[Listen for: User empathy, stakeholder consideration, user feedback integration]*
*[Red flags: Technology-first thinking, no user validation mentioned]*

#### 3. Ownership & Proactivity (6 minutes)
**Interviewer**: "You mentioned leading the 'Imjangdan' backend and coordinating roles. Tell me about a specific time when you took ownership of a problem that wasn't explicitly assigned to you. What was the situation, what drove you to take action, what specific actions did you take, and what were the results?"

*[Follow up with:]*
- "How did you coordinate with team members during this initiative?"
- "What challenges did you face in the delivery process?"

*[Listen for: Initiative-taking, accountability, leadership in ambiguous situations]*
*[Red flags: Waiting for direction, avoiding responsibility]*

#### 4. Observability & Guardrails (4 minutes)
**Interviewer**: "I see you introduced observability tools like ES, Prometheus, and Grafana. Walk me through a specific situation where you implemented monitoring that caught a problem before it became critical. What was the situation, what metrics did you choose to track, what actions did you take, and what were the results?"

*[Probe for details:]*
- "How do you decide which metrics are most important to monitor?"
- "Tell me about a time when monitoring data changed your decision-making"

*[Listen for: Proactive monitoring, operational excellence, data-driven operations]*
*[Red flags: Reactive-only approach, no systematic monitoring strategy]*

#### 5. Data-Informed Iteration (4 minutes)
**Interviewer**: "Let's explore how you use data in decision-making. Describe a specific situation where you had to make a technical decision and you used data or metrics to guide your choice. What was the situation, what data did you gather, how did you analyze it, and what was the outcome?"

*[Follow-up probes:]*
- "How do you typically validate whether a technical change was successful?"
- "Tell me about a time when data contradicted your initial assumptions"

*[Listen for: Evidence-based decision making, measurement focus, iterative improvement]*
*[Red flags: Gut-feeling decisions, no measurement approach]*

#### 6. Integrity & Reliability (6 minutes)
**Interviewer**: "Now I'd like to understand how you handle difficult situations. Tell me about a challenging situation where you had to choose between meeting a deadline and maintaining quality or doing what was right. What was the situation, what pressures were you under, what actions did you take, and what were the results?"

*[Additional probes:]*
- "How do you handle situations where stakeholders ask for shortcuts?"
- "Describe a time when you had to deliver difficult news to a team or manager"

*[Listen for: Ethical decision-making, quality focus, honest communication]*
*[Red flags: Cutting corners, unreliable commitments, avoiding difficult conversations]*

#### 7. Security & Compliance First (3 minutes)
**Interviewer**: "Security is crucial in our work. Describe a specific time when you identified or addressed a security concern in a project. What was the situation, how did you identify the issue, what actions did you take, and what was the outcome?"

*[If needed, probe:]*
- "How do you typically consider security when designing systems?"

*[Listen for: Security awareness, proactive risk identification]*
*[Red flags: Security as afterthought, no security considerations mentioned]*

#### 8. Collaboration & Knowledge-Sharing (4 minutes)
**Interviewer**: "You mentioned presenting a Terraform & Ansible seminar. Tell me about a specific time when you had to work with a difficult team member or resolve a significant disagreement. What was the situation, what actions did you take, and how did it turn out?"

*[Follow-up questions:]*
- "How do you typically share knowledge with teammates who are less experienced?"
- "Describe your approach to documentation and knowledge transfer"

*[Listen for: Conflict resolution, teaching ability, collaborative approach]*
*[Red flags: Poor communication, knowledge hoarding, team conflicts]*

#### 9. Continuous Learning & Mentorship (6 minutes)
**Interviewer**: "I see you've built diverse projects across banking, fashion, and defense domains. Tell me about a specific time when you had to quickly learn a new technology or domain to complete a project. What was the situation, how did you approach learning, what actions did you take, and what were the results?"

*[Additional exploration:]*
- "How do you stay current with new technologies and best practices?"
- "Describe a time when you taught or mentored someone else"

*[Listen for: Learning agility, teaching others, staying current with industry]*
*[Red flags: Stagnant skills, reluctance to learn, no teaching examples]*

#### 10. Innovative Spirit (3 minutes)
**Interviewer**: "Finally, let's talk about innovation. Tell me about a time when you came up with a creative or unconventional solution to a technical problem. What was the situation, what made the standard approach insufficient, what innovative solution did you develop, and what were the results?"

*[Probe if needed:]*
- "How do you balance innovation with reliability and risk?"

*[Listen for: Creative problem-solving, willingness to experiment, novel approaches]*
*[Red flags: Always status-quo, fear of new approaches, no creative solutions]*

### Technical Deep Dive (30 minutes)

**Interviewer**: "Now let's shift to some technical discussions. Based on your AWS and infrastructure experience, walk me through how you would design a scalable task management API that needs to handle 100k+ daily active users."

*[Look for: Architecture thinking, scalability patterns, database design, caching strategies]*

**Follow-up**: "Based on your AWS experience, how would you architect a multi-region disaster recovery solution?"

*[Assess: Infrastructure knowledge, reliability planning, operational thinking]*

**Interviewer**: "Describe your approach to infrastructure as code. What would your ideal CI/CD pipeline look like?"

*[Listen for: Automation thinking, best practices, operational excellence]*

### Cultural Fit & Candidate Questions (20 minutes)

**Interviewer**: "Based on what we've discussed, you should have a good sense of our values and how we work. What questions do you have about the role, the team, or working at Gefjon Growth?"

### Closing (5 minutes)

**Interviewer**: "Thank you for those great questions. Before we wrap up, is there anything else you'd like to share about your background or interest in this role?"

**Next Steps**:
"Here's what happens next: We'll be completing our interview process over the next [timeframe], and we'll follow up with you by [date] with an update on next steps."

**Interviewer**: "Thank you so much for your time today, Minseok Kim. It was great learning more about your background and experience. We'll be in touch soon!"

---

## Post-Interview BEI Evaluation

### Immediate Actions (within 30 minutes):
- [ ] Complete BEI value assessment notes for all 10 values
- [ ] Score STAR response completeness for each behavioral question
- [ ] Rate technical competency discussions
- [ ] Note behavioral pattern consistency across responses
- [ ] Record overall impression with BEI focus

### BEI Evaluation Framework Completion (within 24 hours):
**Core Values Assessment (60% - 46 points total):**
- [ ] Customer-Centric Craftsmanship: ___/6 points
- [ ] Ownership & Proactivity: ___/6 points  
- [ ] Integrity & Reliability: ___/6 points
- [ ] Continuous Learning & Mentorship: ___/6 points
- [ ] Technical Excellence: ___/4 points
- [ ] Data-Informed Iteration: ___/4 points
- [ ] Collaboration & Knowledge-Sharing: ___/4 points
- [ ] Observability & Guardrails: ___/4 points
- [ ] Security & Compliance First: ___/3 points
- [ ] Innovative Spirit: ___/3 points

**Technical Competency (25% - 25 points total):**
- [ ] System Design: ___/8 points
- [ ] Infrastructure Knowledge: ___/8 points
- [ ] Problem-Solving: ___/9 points

**Communication & Behavioral Consistency (15% - 15 points total):**
- [ ] STAR Response Quality: ___/10 points
- [ ] Behavioral Pattern Consistency: ___/5 points

**Total Score: ___/100 points**
**Recommendation: Strong Hire (≥85) / Hire (75-84) / Lean Hire (65-74) / No Hire (<65)**

### Follow-up Actions:
- [ ] Submit detailed BEI evaluation with specific behavioral examples
- [ ] Highlight value gaps that need further assessment
- [ ] Recommend focus areas for potential offer discussion

---
*BEI-Enhanced Interview Script for: Strong Hire candidate*
*Total interview time: 120 minutes*
*Focus: Comprehensive behavioral assessment of all 10 core values*
