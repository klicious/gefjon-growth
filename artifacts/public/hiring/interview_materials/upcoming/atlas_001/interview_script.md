# Interview Script: atlas_001

## Pre-Interview Preparation

### Interviewer Checklist
- [ ] Review candidate context briefing and interview guide
- [ ] Prepare whiteboard/digital collaboration tools
- [ ] Set up development environment for pair programming
- [ ] Print evaluation rubrics and note-taking templates
- [ ] Confirm interview schedule and room bookings

### Materials Needed
- Candidate resume and portfolio links
- Company information packet
- Whiteboard markers or digital whiteboard access
- Development workstation with IDE
- Evaluation forms and scoring rubrics

## Session 1: Behavioral Event Interview (BEI) - 60 minutes

### Opening Script (5 minutes)

**Interviewer**: "Good morning/afternoon, Minseok. Welcome to Dunamis Capital. I'm [Name], [Title], and I'll be conducting the first part of your interview today. How are you feeling?"

*[Wait for response and engage briefly]*

**Interviewer**: "Great! Let me give you an overview of today's interview process. We have five sessions planned over about 4 hours, with short breaks between each. This first session will focus on behavioral questions to understand your experience and how you approach challenges. After this, you'll have technical discussions, a pair programming session, system design, and finally a culture fit conversation."

**Interviewer**: "The format I'll use is called Behavioral Event Interviewing, where I'll ask you to share specific examples from your experience. I'm looking for detailed stories with context, actions you took, and outcomes. Feel free to ask for clarification on any question."

**Interviewer**: "Do you have any questions about the process before we begin?"

*[Address any questions]*

**Interviewer**: "Perfect. Let's start."

### Ownership & Leadership Section (15 minutes)

**Interviewer**: "I'd like to begin by understanding how you approach ownership and leadership. Tell me about a time when you took ownership of a project or initiative that wasn't explicitly assigned to you."

*[Listen for STAR format: Situation, Task, Action, Result]*

**Follow-up Questions** (use as needed):
- "What specifically motivated you to take ownership in this situation?"
- "How did you approach getting buy-in from others who might have been involved?"
- "What challenges did you face while taking ownership, and how did you overcome them?"
- "What was the ultimate outcome, and what did you learn from this experience?"

**Specific Probe for Candidate**:
"I see from your background that you led the Imjangdan project as team lead. Can you walk me through how you took on that leadership role and coordinated the team?"

**Note-Taking Prompts**:
- Initiative and proactive behavior
- Leadership without formal authority
- Team coordination and communication
- Results and learning outcomes

### Problem-Solving & Technical Excellence Section (15 minutes)

**Interviewer**: "Now I'd like to understand your problem-solving approach. Describe a complex technical problem you solved recently. Walk me through your entire problem-solving process from start to finish."

**Follow-up Questions**:
- "How did you go about identifying the root cause of the problem?"
- "What alternative solutions did you consider before settling on your approach?"
- "How did you evaluate the trade-offs between different approaches?"
- "How did you validate that your solution actually worked and solved the problem?"

**Specific Probe for Candidate**:
"You mentioned replacing memory-based autoscaling with queue metrics in your Code Ground project. Can you walk me through that technical decision-making process?"

**Note-Taking Prompts**:
- Systematic problem-solving approach
- Root cause analysis skills
- Trade-off evaluation and decision-making
- Solution validation and testing

### Communication & Knowledge Sharing Section (15 minutes)

**Interviewer**: "Communication and knowledge sharing are crucial in our collaborative environment. Tell me about a time when you had to explain a complex technical concept to someone with less technical background or expertise."

**Follow-up Questions**:
- "How did you adapt your communication style for your audience?"
- "What specific techniques did you use to ensure they understood the concept?"
- "How did you handle questions or pushback during your explanation?"
- "What feedback did you receive, and how did you know you were successful?"

**Specific Probe for Candidate**:
"I see you presented Terraform and Ansible seminars and created lab materials. Tell me about that experience and how you made complex infrastructure concepts accessible."

**Note-Taking Prompts**:
- Audience awareness and adaptation
- Teaching and mentoring ability
- Patience and clarity in explanation
- Knowledge sharing initiative

### Closing (10 minutes)

**Interviewer**: "Thank you for those detailed examples. Before we wrap up this session, I'd like to give you an opportunity to ask questions about our team, company culture, or growth opportunities."

*[Answer questions thoughtfully and honestly]*

**Interviewer**: "Excellent questions. That concludes our behavioral interview. You'll have a 10-minute break, and then [Next Interviewer Name] will meet with you for the technical deep-dive session. Any final questions for me?"

**Transition**: "Great! I'll walk you to the break area, and [Next Interviewer] will collect you in 10 minutes."

## Session 2: Technical Deep-Dive - 60 minutes

### Opening Script (5 minutes)

**Interviewer**: "Hi Minseok, I'm [Name], [Title]. I hope you had a good break. This session will focus on your technical expertise, particularly around AWS, infrastructure, and system architecture. We'll be using the whiteboard for some discussions, so feel free to draw diagrams or write code as needed."

**Interviewer**: "I've reviewed your background and I'm particularly interested in your AWS experience and the projects you've built. Ready to dive in?"

### AWS Architecture Discussion (25 minutes)

**Interviewer**: "Let's start with your Code Ground project, which sounds fascinating. Walk me through the architecture of this system, focusing on the AWS components and how they interact with each other."

*[Encourage whiteboard usage for architecture diagram]*

**Follow-up Questions**:
- "I see you used ECS for deployment. What led you to choose ECS over alternatives like EKS or Lambda?"
- "Tell me about your ECR image management and deployment pipeline setup."
- "You mentioned queue-metric based autoscaling. Can you explain the technical implementation details?"
- "How did you set up monitoring and observability for this system?"

**Deep Dive on Scaling**:
"You mentioned replacing memory-based autoscaling with queue metrics. This is a sophisticated approach. Can you explain:
- How you integrated RabbitMQ metrics with CloudWatch?
- What specific metrics you used and why?
- How you configured the scaling policies and thresholds?
- What cost implications this had and how you optimized for cost?"

**Note-Taking Prompts**:
- AWS service knowledge depth
- Architecture decision rationale
- Scaling and performance understanding
- Cost optimization awareness

### Infrastructure as Code Discussion (20 minutes)

**Interviewer**: "I'm impressed by your Terraform and Ansible expertise. Let's talk about infrastructure as code. How do you structure Terraform code for a multi-environment setup?"

**Follow-up Questions**:
- "How do you design modules for reusability across environments?"
- "What's your approach to state management and remote backends?"
- "How do you handle environment-specific configurations?"
- "How does your team collaborate on infrastructure code and handle code reviews?"

**Ansible Integration**:
"How do you combine Terraform and Ansible in your infrastructure workflow? What's the handoff mechanism between them?"

**Note-Taking Prompts**:
- Infrastructure as Code best practices
- Team collaboration on infrastructure
- Multi-environment management
- Tool integration patterns

### System Design Challenge (10 minutes)

**Interviewer**: "Let's do a quick system design exercise. Design a monitoring system for a financial trading platform that needs to track order latency, success rates, and system health across multiple exchanges."

*[Give 2-3 minutes for thinking, then discuss approach]*

**Guiding Questions**:
- "What metrics would you collect and how?"
- "How would you store and aggregate this data?"
- "What would your alerting strategy look like?"
- "How would you ensure the monitoring system itself is scalable and reliable?"

**Note-Taking Prompts**:
- System design thinking
- Monitoring and observability expertise
- Scalability considerations
- Financial domain awareness

### Closing

**Interviewer**: "Excellent technical discussion. Your AWS expertise really shows through your project experience. Next up is the pair programming session with [Next Interviewer Name]. Any technical questions about our infrastructure or the challenges you'd be working on?"

## Session 3: Pair Programming - 60 minutes

### Opening Script (5 minutes)

**Interviewer**: "Hi Minseok, I'm [Name], [Title]. This session will be hands-on coding where we'll work together on a problem. I've set up a development environment here with Python and the tools we'll need."

**Interviewer**: "The goal isn't to test your memorization of syntax, but to see how you approach problems, structure code, and collaborate. Feel free to look up documentation, ask questions, and think out loud as you work."

**Interviewer**: "Ready to code together?"

### Programming Challenge Introduction (5 minutes)

**Interviewer**: "Here's the challenge: We need to implement a FastAPI service that aggregates cryptocurrency prices from multiple exchanges. The service should include caching, error handling, and be resilient to exchange outages."

**Requirements Overview**:
"Let's break down the requirements:
1. FastAPI application with async endpoints
2. Integration with 2-3 mock exchange APIs
3. Redis caching with TTL
4. Circuit breaker pattern for external calls
5. Comprehensive error handling
6. Basic logging and metrics

Where would you like to start?"

### Collaborative Coding (45 minutes)

**Guidance During Coding**:
- "What's your thinking behind this approach?"
- "How would you handle errors in this scenario?"
- "What would you do if one of the exchanges was down?"
- "How would you test this functionality?"

**Areas to Observe**:
- FastAPI framework knowledge
- Async/await usage patterns
- Error handling strategies
- Code organization and structure
- Testing considerations
- Collaboration and communication

### Code Review Discussion (5 minutes)

**Interviewer**: "Great work! Let's review what we built together. What do you think works well in this implementation? What would you improve if you had more time?"

**Discussion Points**:
- Production deployment considerations
- Performance optimization opportunities
- Testing strategy and coverage
- Monitoring and observability additions

## Session 4: System Design - 45 minutes

### Opening Script (5 minutes)

**Interviewer**: "Hi Minseok, I'm [Name], [Title]. For this session, we'll work on a system design problem that's relevant to what we do here. We'll use the whiteboard to sketch out architectures and discuss trade-offs."

**Interviewer**: "The goal is to see how you think about large-scale systems, not to get every detail perfect. Feel free to ask clarifying questions and think out loud."

### Problem Statement (5 minutes)

**Interviewer**: "Here's the challenge: Design a high-frequency trading platform that can handle 10,000 orders per second across multiple cryptocurrency exchanges with sub-100ms latency requirements."

**Clarifying Questions to Address**:
- "What types of orders do we need to support?"
- "How many exchanges are we integrating with?"
- "What's our expected data retention period?"
- "Are there specific compliance or audit requirements?"

### Architecture Discussion (30 minutes)

**High-Level Architecture (10 minutes)**:
"Let's start with the big picture. What would the main components of this system look like?"

*[Encourage whiteboard sketching]*

**Scalability and Performance (10 minutes)**:
"Now let's talk about scale. How would you ensure this system can handle 10,000 orders per second with sub-100ms latency?"

**Reliability and Observability (10 minutes)**:
"What about when things go wrong? How would you build in fault tolerance and monitoring?"

### Wrap-up (5 minutes)

**Interviewer**: "Excellent system thinking! What do you see as the biggest challenges in implementing a system like this? What would you want to prototype first?"

## Session 5: Culture Fit & Team Dynamics - 30 minutes

### Informal Opening (5 minutes)

**Interviewer**: "Hi Minseok, I'm [Name], [Title]. This is our final session, and I wanted to make it more conversational. How are you feeling about the interview process so far?"

*[Engage in brief casual conversation]*

**Interviewer**: "I'd like to learn more about how you like to work and what you're looking for in your next role."

### Team Collaboration Discussion (10 minutes)

**Interviewer**: "How do you prefer to work in a team environment? What does your ideal collaborative coding experience look like?"

**Follow-up Areas**:
- "What's your approach to code reviews, both giving and receiving feedback?"
- "How do you like to share knowledge with teammates?"
- "Tell me about a time you had a disagreement with a teammate about a technical approach. How did you handle it?"
- "Do you prefer remote work, in-person collaboration, or a hybrid approach?"

### Learning and Growth Discussion (10 minutes)

**Interviewer**: "What are your learning goals for the next 6-12 months? How do you typically stay current with technology trends?"

**Follow-up Areas**:
- "What interests you about the financial technology domain?"
- "How do you approach learning new technologies or frameworks?"
- "What kind of feedback and mentorship do you find most helpful?"
- "Where do you see your career heading in the next few years?"

### Company and Role Fit (5 minutes)

**Interviewer**: "What excites you most about this role and our company? Do you have any concerns or questions about what we've discussed today?"

**Final Questions**:
"What questions do you have about our team culture, the work environment, or anything else about the company?"

### Closing

**Interviewer**: "Thank you for spending the day with us, Minseok. You've shown impressive technical skills and thoughtful approaches to problem-solving. We'll be in touch within the next few days with feedback and next steps."

**Interviewer**: "Do you have any final questions for me?"

## Post-Interview Debrief

### Immediate Actions
- [ ] Complete evaluation rubrics for each session
- [ ] Document key observations and concerns
- [ ] Compare notes with other interviewers
- [ ] Prepare feedback summary for candidate

### Decision Framework
- Compile scores from all sessions
- Assess against hiring criteria
- Consider team fit and growth potential
- Make final recommendation with rationale

### Follow-up Items
- [ ] Schedule debrief meeting with interview panel
- [ ] Prepare detailed feedback for candidate
- [ ] Update candidate status in tracking system
- [ ] Plan next steps based on decision

---
**Generated**: 2025-08-11T13:00:00Z  
**Quality Score**: 9.2/10.0  
**Reviewer**: Platform Lead  
**Status**: Ready for Interview Execution