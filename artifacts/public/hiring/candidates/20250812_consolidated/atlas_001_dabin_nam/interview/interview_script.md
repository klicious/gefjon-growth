# Interview Script: Atlas (Da Bin Nam)

## Introduction (5 minutes)

**Interviewer Opening**:
"Good morning, Atlas! Thank you for taking the time to interview with us today. I'm [Name], [Title] here at Gefjon Growth, and I'm joined by [Name], [Title]. 

We're really excited to learn more about you today. I was particularly impressed with your container migration work at NAVER System where you solo-led the Java to Node.js transformation - that shows exactly the kind of ownership and technical depth we value on our platform development team.

Let me start by telling you a bit about what we do. At Gefjon Growth, our mission is to engineer cross-region, self-healing fintech platforms that move capital instantly for liquidity and strategically for future value, while guaranteeing systemic safety and investor trust. Our Platform Development Team builds and operates a fully-automated trading platform that trades digital assets profitably and exposes real-time risk and P&L data.

Today's interview will be about 2.5 hours total. We'll spend the first hour getting to know you better through behavioral questions, then dive into some technical discussions, do a collaborative coding session, and finish with system design. Throughout, please feel free to ask questions - we want this to be a conversation, not an interrogation.

Any questions before we get started?"

## Rapport Building & Personalization (3 minutes)

**Personalized Opening**:
"I was really impressed with your progression from the 3D drone simulator project to leading the ndhub container migration. That shows incredible growth in just a couple of years. The fact that you volunteered for the challenging drone simulator project and then learned MQTT and Wireshark on your own to make it work really demonstrates the kind of proactive problem-solving we need on our team.

Before we dive into the formal questions, I'm curious - what drew you to take on that drone simulator challenge when others might have avoided it?"

*[Allow 2-3 minutes for candidate response and natural conversation]*

## Behavioral Interview (BEI) Section (50 minutes)

### Ownership & Proactivity - Validation (12 minutes)

**Transition**: "Let's start by diving deeper into some of the experiences you've had. I want to understand how you approach challenging technical problems."

**Primary Question**: 
"I noticed you volunteered for the challenging 3D drone simulator project and later solo-led the ndhub container migration. Tell me about a time when you took ownership of a complex technical problem that others might have avoided. Walk me through the situation, what you did, and the results."

**Interviewer Notes**: *Listen for STAR format - Situation, Task, Action, Result. Look for evidence of proactive problem-solving, technical leadership, and driving results independently.*

**Follow-up Questions**:
1. "What made you decide to take on this challenge when others didn't?"
2. "How did you handle the uncertainty and technical unknowns?"
3. "What would you do differently if you faced a similar situation again?"

**STAR Method Reminder**: "That's a great start. Can you tell me more about the specific actions you took and what the measurable results were?"

### Problem-Solving & Learning Agility - Validation (12 minutes)

**Transition**: "That's exactly the kind of ownership we value. Now I want to understand your learning approach."

**Primary Question**:
"You mentioned learning MQTT and Wireshark to unblock the drone simulator development, and later self-studying RabbitMQ for the UAM project. Describe a specific situation where you had to quickly learn a completely new technology to solve a critical problem. What was your learning approach and how did you apply it?"

**Interviewer Notes**: *Focus on learning methodology, speed of acquisition, and practical application. This is critical for our AI/ML learning requirements.*

**Follow-up Questions**:
1. "How do you typically approach learning a new technology under pressure?"
2. "What resources do you use and how do you validate your understanding?"
3. "How do you balance learning depth vs. speed when solving urgent problems?"

### Technical Excellence & Craftsmanship - Validation (12 minutes)

**Transition**: "Your learning agility is impressive. Let's talk about how you ensure technical quality."

**Primary Question**:
"Tell me about the ndhub container migration project where you consolidated containers and migrated from Java to Node.js. What was your approach to ensuring the migration maintained system quality and performance?"

**Interviewer Notes**: *Look for systematic approach, quality metrics, testing strategy, and performance considerations.*

**Follow-up Questions**:
1. "How did you decide on the migration strategy and validate it was working?"
2. "What metrics did you use to measure success?"
3. "How did you ensure the new system met or exceeded the original performance?"

### Mathematical/Algorithmic Thinking - Discovery (14 minutes)

**Transition**: "That shows great technical rigor. Now, our platform involves quantitative trading algorithms and mathematical optimization, so I want to understand your approach to analytical problems."

**Primary Question**:
"Our platform involves quantitative trading algorithms and mathematical optimization. Tell me about a time when you had to solve a complex algorithmic or mathematical problem in your work. How did you approach it?"

**Interviewer Notes**: *This is critical assessment area. Look for analytical thinking, mathematical comfort, systematic problem-solving approach.*

**Follow-up Questions**:
1. "How do you typically break down complex mathematical or algorithmic problems?"
2. "What's your experience with performance optimization that required mathematical analysis?"
3. "How comfortable are you with statistical concepts or financial mathematics?"

**If Limited Experience**: "That's okay if you haven't had direct experience. Can you walk me through how you would approach a problem like calculating the optimal portfolio allocation across 10 different assets to minimize risk while maximizing return?"

## Technical Deep-Dive Section (20 minutes)

### System Design Challenge (8 minutes)

**Transition**: "Great, let's shift to some technical problem-solving. I want to see how you think about system architecture."

**Question**: 
"Design a real-time notification system for our trading platform that needs to alert traders when certain market conditions are met. The system should handle 10,000+ concurrent users and deliver notifications within 100ms. How would you architect this?"

**Interviewer Guidance**: 
- Let them think out loud
- Ask clarifying questions about requirements
- Probe on technology choices and trade-offs
- Look for scalability and real-time processing understanding

**Follow-up Prompts**:
- "How would you handle the WebSocket connections at scale?"
- "What's your approach to ensuring 100ms delivery times?"
- "How would you make this fault-tolerant?"

### Database Optimization Scenario (7 minutes)

**Question**:
"You have a PostgreSQL database storing trading positions that's experiencing slow query performance during market hours. Walk me through your debugging and optimization approach."

**Interviewer Notes**: *Assess systematic debugging approach, PostgreSQL knowledge, performance optimization thinking.*

**Follow-up Prompts**:
- "What would be your first steps to identify the bottleneck?"
- "How would you optimize without disrupting live trading?"
- "What monitoring would you put in place?"

### AI/ML Learning Potential - Discovery (5 minutes)

**Transition**: "One more behavioral question. Our platform is increasingly incorporating AI and machine learning capabilities."

**Question**:
"While you haven't worked directly with AI/ML, tell me about a time when you had to quickly adapt to a completely new technical paradigm or way of thinking about problems."

**Follow-up Questions**:
1. "How do you approach learning technologies that require a different way of thinking?"
2. "What's your current understanding of AI/ML and how it might apply to software development?"
3. "How would you approach learning about LLMs and agentic AI systems?"

## Pair Programming Session (45 minutes)

**Transition**: "Now let's do some collaborative coding. This isn't about getting the perfect solution - I want to see how you think through problems and how we work together."

**Problem Introduction**:
"We're going to build a real-time portfolio risk calculator. Imagine you have a service that needs to calculate portfolio risk metrics as trading positions are updated in real-time. Let's start simple and build it up."

**Initial Requirements**:
- REST API to add/update positions
- Calculate total portfolio value
- Calculate unrealized P&L
- WebSocket endpoint for real-time updates

**Interviewer Guidance**:
- Let them choose the language (Java or Node.js)
- Encourage them to think out loud
- Ask about design decisions
- Probe on error handling and edge cases
- Look for code organization and testing approach

**Key Assessment Points**:
- [ ] Code structure and organization
- [ ] API design thinking
- [ ] Real-time processing approach
- [ ] Mathematical calculations accuracy
- [ ] Error handling consideration
- [ ] Testing mindset

## System Design Interview (30 minutes)

**Transition**: "Great coding session! Now let's think about larger system architecture."

**Design Challenge**:
"Design a system that ingests market data from multiple exchanges, processes it for arbitrage opportunities, and distributes signals to trading algorithms. This needs to handle thousands of price updates per second with low latency."

**Interviewer Guidance**:
- Start with high-level architecture
- Drill down into specific components
- Ask about trade-offs and alternatives
- Probe on scalability and fault tolerance

**Key Questions to Ask**:
1. "How would you handle data consistency across exchanges?"
2. "What's your approach to monitoring and alerting?"
3. "How would you optimize for low latency?"
4. "How would you handle exchange connection failures?"
5. "What's your strategy for testing this system?"

**Assessment Criteria**:
- [ ] System architecture thinking
- [ ] Component interaction design
- [ ] Scalability considerations
- [ ] Fault tolerance planning
- [ ] Technology choice rationale

## Candidate Q&A (10 minutes)

**Transition**: "That was excellent system thinking. Now I want to make sure you have all the information you need about us."

**Opening**: "What questions do you have about the role, our team, our technology stack, or Gefjon Growth in general?"

**Be Prepared to Discuss**:
- Platform Development Team mission and current projects
- Technology stack and development practices
- Growth opportunities and learning support
- Team culture and collaboration style
- Next steps in the process

## Closing (3 minutes)

**Closing Script**:
"Atlas, this has been a really great conversation. I'm impressed with your technical depth, your learning agility, and especially your ownership mindset. The way you approached the container migration project and your willingness to dive into new technologies like MQTT and RabbitMQ shows exactly the kind of proactive problem-solving we need.

Here's what happens next: We'll be making our decision within the next few days and will reach out to you by [specific date] with next steps. If you're selected to move forward, the next step would be a final conversation with our Platform Lead to discuss team fit and career goals.

Do you have any final questions for us?"

**Thank You**: "Thank you so much for your time today. We really enjoyed getting to know you and seeing how you approach technical challenges. We'll be in touch soon!"

---

## Interviewer Debrief Notes

### Key Assessment Areas
- [ ] **Ownership & Proactivity**: Clear examples with STAR format
- [ ] **Learning Agility**: Systematic approach to new technologies  
- [ ] **Technical Excellence**: Quality-focused development practices
- [ ] **Mathematical Thinking**: Comfort with quantitative problems
- [ ] **AI/ML Potential**: Learning approach and interest
- [ ] **System Design**: Architecture thinking and scalability
- [ ] **Communication**: Clear technical explanation ability
- [ ] **Cultural Fit**: Alignment with company values

### Decision Factors
- Mathematical aptitude demonstration
- AI/ML learning enthusiasm
- System design depth
- Overall technical competency
- Cultural value alignment

### Recommendation: HIRE / NO HIRE / NEEDS ADDITIONAL ASSESSMENT

**Rationale**: [To be completed by interviewer]

**Next Steps**: [To be completed by interviewer]