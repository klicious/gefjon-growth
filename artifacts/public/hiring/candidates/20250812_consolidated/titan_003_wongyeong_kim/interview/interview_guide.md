# Interview Guide: Titan (Wongyeong Kim)

## General Guidance for Interviewers
Titan is a **strong data engineering candidate** with excellent optimization skills and practical AI/ML experience. He demonstrates exceptional problem-solving with measurable results (35% runtime reduction, 87% accuracy improvement) and has valuable experience with LLM integration. Focus on **validating his technical excellence** while **assessing mathematical aptitude** for quantitative systems and **exploring financial domain learning interest**. His data engineering expertise and AI/ML foundation make him well-suited for our platform's intelligence and data infrastructure needs.

## BEI (Behavioral Event Interview) Section - 50 minutes

### Part 1: Validating Proven Values (30 minutes)

#### Technical Excellence & System Optimization - VALIDATION QUESTION
**Primary Question**: "I'm impressed with your Airflow pipeline optimization that achieved a 35% runtime reduction. Walk me through that project - what was the situation, what specific optimizations did you implement, and how did you measure and validate the improvements?"

**Evidence to Validate**: Performance optimization methodology, systematic improvement approach, measurement and validation

**Follow-up Questions**:
- "How did you identify the specific bottlenecks that were causing the performance issues?"
- "What was your testing approach to ensure the optimizations didn't break existing functionality?"
- "How do you balance performance optimization with system maintainability?"

#### Problem-Solving & Innovation - VALIDATION QUESTION  
**Primary Question**: "Your LLM integration achieved an 87% accuracy improvement over the regex baseline for text processing. Describe the challenge you were solving and your approach to implementing and validating this AI solution."

**Evidence to Validate**: AI/ML integration skills, creative problem-solving, results measurement

**Follow-up Questions**:
- "How did you decide that LLM integration was the right approach for this problem?"
- "What was your methodology for prompt engineering and model selection?"
- "How did you validate the 87% accuracy improvement and ensure it was reliable?"

#### Ownership & Technical Leadership - VALIDATION QUESTION
**Primary Question**: "Tell me about the PDF masking algorithm you developed at Fasoo, where you had to handle varied font encodings without references or prior art. How did you approach this complex, undefined problem?"

**Evidence to Validate**: Independent problem-solving, technical leadership, complex algorithm development

**Follow-up Questions**:
- "How did you research and validate your approach when there were no clear references?"
- "What was your strategy for handling the different font encoding challenges?"
- "How did you ensure the solution would work reliably in production?"

### Part 2: Probing Missing Values (20 minutes)

#### Mathematical/Algorithmic Thinking - DISCOVERY QUESTION
**Primary Question**: "Our platform involves quantitative trading algorithms and mathematical optimization. While your background is in data science, tell me about a time when you had to solve a complex mathematical or algorithmic problem. How did you approach it?"

**Looking For**: Mathematical problem-solving approach, analytical thinking, comfort with quantitative challenges

**Follow-up Questions**:
- "How do you typically break down complex mathematical problems?"
- "What's your experience with statistical analysis or mathematical modeling?"
- "How comfortable are you with financial mathematics or quantitative analysis?"

#### Financial Domain Learning Interest - DISCOVERY QUESTION
**Primary Question**: "Our platform focuses on automated trading and financial systems. While you haven't worked in finance directly, tell me about a time when you had to quickly learn a completely new domain or industry to solve a technical problem."

**Looking For**: Domain learning approach, adaptability, interest in financial systems

**Follow-up Questions**:
- "How do you approach learning new business domains while maintaining technical focus?"
- "What interests you about applying your data engineering skills to financial systems?"
- "How would you approach learning about trading algorithms and market data processing?"

#### Real-Time Systems & Scalability - DISCOVERY QUESTION
**Primary Question**: "Our trading platform requires real-time processing with sub-second latency requirements. Describe your experience with real-time systems or how you would approach designing for low-latency requirements."

**Looking For**: Real-time system thinking, scalability considerations, performance optimization approach

**Follow-up Questions**:
- "How would you modify your data pipeline approach for real-time processing?"
- "What's your strategy for handling high-throughput, low-latency data streams?"
- "How do you balance data consistency with performance in real-time systems?"

## Technical Deep-Dive Section - 25 minutes

### Data Pipeline Architecture Challenge (10 minutes)
**Question**: "Design a real-time data pipeline that ingests market data from 20+ exchanges, processes it for trading signals using ML models, and delivers results to trading algorithms within 100ms. What's your architecture approach?"

**Assessment Focus**:
- Data pipeline design for real-time processing
- ML integration in production systems
- Performance optimization strategies
- Scalability and fault tolerance considerations

**Follow-up Questions**:
- "How would you handle data quality and validation in real-time?"
- "What's your approach to ML model deployment and monitoring?"
- "How would you implement backpressure and flow control?"

### AI/ML Integration Deep-Dive (8 minutes)
**Question**: "Based on your LLM integration experience, how would you design an AI-powered trading signal generation system that processes news, social sentiment, and market data to generate trading recommendations?"

**Assessment Focus**:
- AI/ML system architecture
- Multi-modal data processing
- Model performance optimization
- Production ML system considerations

### Database & Storage Optimization (7 minutes)
**Question**: "For a trading platform that needs to store and query billions of market data points and trading signals with sub-second response times, what's your approach to data storage and retrieval optimization?"

**Assessment Focus**:
- Database design for high-throughput systems
- Time-series data management
- Query optimization strategies
- Storage architecture decisions

## Pair Programming Session - 45 minutes

### Problem Selection: Advanced Level
**Recommended Problem**: "AI-Powered Market Data Processing Pipeline"

**Problem Statement**: Implement a data processing pipeline that ingests market data, applies ML-based signal detection, and outputs trading recommendations with performance optimization.

**Why This Problem**:
- Leverages his data pipeline expertise
- Incorporates his AI/ML integration experience
- Tests performance optimization skills
- Requires system design thinking
- Assesses financial domain adaptability

**Assessment Criteria**:
- Data pipeline design and implementation
- AI/ML integration approach
- Performance optimization techniques
- Error handling and fault tolerance
- Code organization and maintainability

## System Design Interview - 30 minutes

### Design Challenge: Complete Data Infrastructure
**Problem**: "Design the complete data infrastructure for our trading platform, including market data ingestion, signal processing, risk calculation, portfolio tracking, and historical data management with institutional-grade performance and reliability."

**Assessment Focus**:
- End-to-end data architecture
- Component integration and data flow
- Performance and scalability optimization
- Data quality and monitoring strategy
- AI/ML integration points

**Follow-up Questions**:
- "How would you implement real-time risk calculations across the entire portfolio?"
- "What's your approach to data lineage and audit trails?"
- "How would you integrate AI/ML models for signal generation?"
- "What's your strategy for data backup and disaster recovery?"

## Key Assessment Criteria

### Must Validate
- [ ] **Technical Excellence**: Data engineering expertise and system optimization
- [ ] **AI/ML Integration**: Practical experience with LLM and ML systems
- [ ] **Problem-Solving**: Complex algorithm development and optimization
- [ ] **Mathematical Aptitude**: Quantitative problem-solving for trading systems
- [ ] **Financial Domain Interest**: Learning approach and enthusiasm for finance
- [ ] **System Design**: Architecture thinking for real-time, high-performance systems

### Exceptional Strengths to Confirm
- Data pipeline optimization with measurable results
- AI/ML integration with practical applications
- System refactoring and architecture improvement
- Performance measurement and optimization methodology
- Security/privacy system development experience

### Growth Areas to Assess
- Mathematical/algorithmic thinking for quantitative systems
- Financial domain learning interest and approach
- Real-time system design capabilities
- Large-scale distributed system architecture
- Production ML system deployment and monitoring

### Red Flags to Watch For
- Limited mathematical/algorithmic thinking ability
- Lack of interest in financial domain learning
- Difficulty with real-time system requirements
- Poor system design thinking beyond current experience
- Limited scalability considerations

### Success Indicators
- Clear demonstration of data engineering excellence
- Practical AI/ML integration experience
- Systematic approach to performance optimization
- Interest in financial domain learning
- Strong system design and architecture thinking
- Measurable results and optimization mindset

**Interview Duration**: 2.5 hours total
**Recommended Interviewers**: Platform Lead + Senior Engineer + Data Architecture Lead
**Decision Factors**: Mathematical aptitude, financial domain learning interest, real-time system design capability

**Special Considerations**: This candidate has strong data engineering and AI/ML foundations - focus on quantitative aptitude and financial domain fit rather than basic technical validation.