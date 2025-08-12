# Interview Script: Titan (Wongyeong Kim)

## Introduction (5 minutes)

**Interviewer Opening**:
"Good morning, Wongyeong! Thank you for taking the time to interview with us today. I'm [Name], [Title] here at Gefjon Growth, and I'm joined by [Name], [Title]. 

We're really excited to learn more about you today. Your background in data engineering with AI/ML integration is particularly interesting to us. I was impressed with your Airflow pipeline optimization that achieved a 35% runtime reduction, and especially your LLM integration work that improved accuracy by 87% over the baseline - that shows exactly the kind of data-driven optimization and AI integration we need for our platform.

Let me start by telling you about what we do. At Gefjon Growth, our mission is to engineer cross-region, self-healing fintech platforms that move capital instantly for liquidity and strategically for future value, while guaranteeing systemic safety and investor trust. Our Platform Development Team builds and operates a fully-automated trading platform with advanced data processing pipelines, AI-powered signal generation, and real-time risk management.

Today's interview will be about 2.5 hours total. We'll spend the first hour getting to know you better through behavioral questions, then dive into technical discussions about data architecture and AI integration, do a collaborative coding session, and finish with system design. Throughout, please feel free to ask questions - we want this to be a conversation.

Any questions before we get started?"

## Rapport Building & Personalization (3 minutes)

**Personalized Opening**:
"I was really impressed with your progression from the PDF masking algorithm at Fasoo to your data engineering work with LLM integration. The fact that you developed a complex algorithm for handling varied font encodings where there were no clear references shows exactly the kind of independent problem-solving we value. And your 87% accuracy improvement with LLM integration demonstrates the practical AI application skills we need as we expand our platform's intelligence capabilities.

Your '속닥속닥' app success - reaching 200+ DAU and staying in the charts for 12 weeks - also shows you understand how to build systems that real users depend on.

Before we dive into the formal questions, I'm curious - what drew you from the PDF processing work at Fasoo into data engineering and AI/ML integration?"

*[Allow 2-3 minutes for candidate response and natural conversation]*

## Behavioral Interview (BEI) Section (50 minutes)

### Technical Excellence & System Optimization - Validation (12 minutes)

**Transition**: "Let's start by diving into your technical achievements. I want to understand your approach to system optimization."

**Primary Question**: 
"I'm impressed with your Airflow pipeline optimization that achieved a 35% runtime reduction. Walk me through that project - what was the situation, what specific optimizations did you implement, and how did you measure and validate the improvements?"

**Interviewer Notes**: *Look for systematic optimization approach, measurement methodology, and technical decision-making. This demonstrates his performance optimization capabilities.*

**Follow-up Questions**:
1. "How did you identify the specific bottlenecks that were causing the performance issues?"
2. "What was your testing approach to ensure the optimizations didn't break existing functionality?"
3. "How do you balance performance optimization with system maintainability?"

**STAR Method Reminder**: "That's excellent. Can you tell me more about the specific technical actions you took and how you measured the before and after performance?"

### Problem-Solving & AI Integration - Validation (12 minutes)

**Transition**: "That shows great systematic optimization skills. Now let's talk about your AI/ML integration experience."

**Primary Question**:
"Your LLM integration achieved an 87% accuracy improvement over the regex baseline for text processing. Describe the challenge you were solving and your approach to implementing and validating this AI solution."

**Interviewer Notes**: *Assess AI/ML integration skills, prompt engineering, and results validation. This is a key differentiator for our platform needs.*

**Follow-up Questions**:
1. "How did you decide that LLM integration was the right approach for this problem?"
2. "What was your methodology for prompt engineering and model selection?"
3. "How did you validate the 87% accuracy improvement and ensure it was reliable?"

### Ownership & Technical Leadership - Validation (12 minutes)

**Transition**: "Your AI integration skills are impressive. Let's talk about how you handle complex, undefined technical challenges."

**Primary Question**:
"Tell me about the PDF masking algorithm you developed at Fasoo, where you had to handle varied font encodings without references or prior art. How did you approach this complex, undefined problem?"

**Interviewer Notes**: *Look for independent problem-solving, research methodology, and technical leadership in ambiguous situations.*

**Follow-up Questions**:
1. "How did you research and validate your approach when there were no clear references?"
2. "What was your strategy for handling the different font encoding challenges?"
3. "How did you ensure the solution would work reliably in production?"

### Mathematical/Algorithmic Thinking - Discovery (14 minutes)

**Transition**: "That shows excellent independent problem-solving. Our platform involves quantitative trading algorithms, so I want to understand your approach to mathematical problems."

**Primary Question**:
"Our platform involves quantitative trading algorithms and mathematical optimization. While your background is in data science, tell me about a time when you had to solve a complex mathematical or algorithmic problem. How did you approach it?"

**Interviewer Notes**: *Critical assessment area. Look for mathematical thinking, analytical approach, and comfort with quantitative challenges.*

**Follow-up Questions**:
1. "How do you typically break down complex mathematical problems?"
2. "What's your experience with statistical analysis or mathematical modeling?"
3. "How comfortable are you with financial mathematics or quantitative analysis?"

**If Limited Experience**: "That's okay if you haven't had direct experience. Can you walk me through how you would approach a problem like optimizing a portfolio allocation algorithm to maximize returns while minimizing risk across multiple assets?"

## Technical Deep-Dive Section (25 minutes)

### Data Pipeline Architecture Challenge (10 minutes)

**Transition**: "Great mathematical thinking. Let's dive into some technical architecture problems."

**Question**: 
"Design a real-time data pipeline that ingests market data from 20+ exchanges, processes it for trading signals using ML models, and delivers results to trading algorithms within 100ms. What's your architecture approach?"

**Interviewer Guidance**: 
- This plays to his data pipeline expertise
- Look for real-time processing understanding
- Assess ML integration in production systems
- Probe on performance optimization strategies

**Follow-up Prompts**:
- "How would you handle data quality and validation in real-time?"
- "What's your approach to ML model deployment and monitoring?"
- "How would you implement backpressure and flow control?"

### AI/ML Integration Deep-Dive (8 minutes)

**Question**:
"Based on your LLM integration experience, how would you design an AI-powered trading signal generation system that processes news, social sentiment, and market data to generate trading recommendations?"

**Interviewer Notes**: *Assess AI/ML system architecture, multi-modal data processing, and production ML considerations.*

**Follow-up Prompts**:
- "How would you handle different data types and formats?"
- "What's your approach to model performance monitoring and drift detection?"
- "How would you optimize for both accuracy and latency?"

### Financial Domain Learning Interest - Discovery (7 minutes)

**Transition**: "Your AI integration thinking is solid. Our platform focuses on financial systems, so I want to understand your learning approach."

**Question**:
"Our platform focuses on automated trading and financial systems. While you haven't worked in finance directly, tell me about a time when you had to quickly learn a completely new domain or industry to solve a technical problem."

**Follow-up Questions**:
1. "How do you approach learning new business domains while maintaining technical focus?"
2. "What interests you about applying your data engineering skills to financial systems?"
3. "How would you approach learning about trading algorithms and market data processing?"

## Pair Programming Session (45 minutes)

**Transition**: "Now let's do some collaborative coding. I want to see how you approach data processing with AI integration."

**Problem Introduction**:
"We're going to build an AI-powered market data processing pipeline. This should ingest market data, apply ML-based signal detection, and output trading recommendations with performance optimization."

**Initial Requirements**:
- Ingest simulated market data streams
- Apply ML model for signal detection
- Generate trading recommendations with confidence scores
- Optimize for processing latency
- Include error handling and monitoring

**Interviewer Guidance**:
- Let them choose the language (Python preferred)
- Encourage discussion of data pipeline design
- Ask about ML model integration approaches
- Probe on performance optimization strategies
- Look for system design thinking

**Key Assessment Points**:
- [ ] Data pipeline design and implementation
- [ ] AI/ML integration approach
- [ ] Performance optimization techniques
- [ ] Error handling and fault tolerance
- [ ] Code organization and maintainability
- [ ] System monitoring considerations

## System Design Interview (30 minutes)

**Transition**: "Excellent coding session! Now let's think about complete system architecture."

**Design Challenge**:
"Design the complete data infrastructure for our trading platform, including market data ingestion, signal processing, risk calculation, portfolio tracking, and historical data management with institutional-grade performance and reliability."

**Interviewer Guidance**:
- This is comprehensive and plays to his data engineering strengths
- Start with high-level data architecture
- Drill down into AI/ML integration points
- Ask about performance and scalability
- Probe on data quality and monitoring

**Key Questions to Ask**:
1. "How would you implement real-time risk calculations across the entire portfolio?"
2. "What's your approach to data lineage and audit trails?"
3. "How would you integrate AI/ML models for signal generation?"
4. "What's your strategy for data backup and disaster recovery?"
5. "How would you handle data quality monitoring and alerting?"

**Assessment Criteria**:
- [ ] End-to-end data architecture thinking
- [ ] Component integration and data flow design
- [ ] Performance and scalability considerations
- [ ] AI/ML integration strategy
- [ ] Data quality and monitoring approach

## Real-Time Systems Assessment (5 minutes)

**Transition**: "That's excellent data architecture thinking. Our trading platform has strict latency requirements."

**Question**:
"Our trading platform requires real-time processing with sub-second latency requirements. Describe your experience with real-time systems or how you would approach designing for low-latency requirements."

**Follow-up Questions**:
1. "How would you modify your data pipeline approach for real-time processing?"
2. "What's your strategy for handling high-throughput, low-latency data streams?"
3. "How do you balance data consistency with performance in real-time systems?"

## Candidate Q&A (10 minutes)

**Transition**: "That gives me great insight into your system thinking. Now I want to make sure you have all the information you need about us."

**Opening**: "What questions do you have about the role, our data infrastructure, our AI/ML initiatives, or Gefjon Growth in general?"

**Be Prepared to Discuss**:
- Platform Development Team mission and data infrastructure
- AI/ML integration roadmap and current initiatives
- Technology stack and data processing requirements
- Growth opportunities in financial domain learning
- Team culture and collaboration style
- Learning and development support
- Next steps in the process

## Closing (3 minutes)

**Closing Script**:
"Wongyeong, this has been a really excellent conversation. I'm impressed with your data engineering expertise, your practical AI/ML integration experience, and especially your systematic approach to performance optimization. The 35% runtime reduction and 87% accuracy improvement you achieved show exactly the kind of measurable, results-driven engineering we value.

Your experience with complex algorithm development and system optimization, combined with your AI/ML foundation, would be incredibly valuable for our platform's data infrastructure and intelligence capabilities. I'm also impressed with your learning agility and your interest in applying these skills to financial systems.

Here's what happens next: We'll be making our decision within the next few days and will reach out to you by [specific date] with next steps. If you're selected to move forward, the next step would be a final conversation with our Platform Lead to discuss team fit, growth opportunities in financial domain learning, and career development.

Do you have any final questions for us?"

**Thank You**: "Thank you so much for your time today. We really enjoyed seeing how you approach data engineering challenges and AI integration. We'll be in touch soon!"

---

## Interviewer Debrief Notes

### Key Assessment Areas
- [ ] **Technical Excellence**: Data engineering expertise and system optimization
- [ ] **AI/ML Integration**: Practical experience with LLM and ML systems
- [ ] **Problem-Solving**: Complex algorithm development and optimization
- [ ] **Mathematical Aptitude**: Quantitative problem-solving for trading systems
- [ ] **Financial Domain Interest**: Learning approach and enthusiasm for finance
- [ ] **System Design**: Architecture thinking for real-time, high-performance systems
- [ ] **Communication**: Clear technical explanation ability
- [ ] **Cultural Fit**: Alignment with company values and team dynamics

### Exceptional Strengths Confirmed
- [ ] Data pipeline optimization with measurable results
- [ ] AI/ML integration with practical applications
- [ ] System refactoring and architecture improvement
- [ ] Performance measurement and optimization methodology
- [ ] Security/privacy system development experience

### Growth Areas Assessed
- [ ] Mathematical/algorithmic thinking for quantitative systems
- [ ] Financial domain learning interest and systematic approach
- [ ] Real-time system design capabilities
- [ ] Large-scale distributed system architecture
- [ ] Production ML system deployment and monitoring

### Decision Factors
- Mathematical aptitude for quantitative trading systems
- Financial domain learning interest and enthusiasm
- Real-time system design thinking capability
- AI/ML integration depth and production experience
- Cultural fit with data-driven, performance-focused environment

### Recommendation: STRONG HIRE / HIRE / NO HIRE / NEEDS ADDITIONAL ASSESSMENT

**Rationale**: [To be completed by interviewer]

**Unique Value Proposition**: [To be completed by interviewer]

**Next Steps**: [To be completed by interviewer]

**Special Notes**: This candidate has strong data engineering and AI/ML foundations - decision should focus on quantitative aptitude, financial domain fit, and real-time system capabilities.