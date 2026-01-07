# Dohyun Mimir Project Evaluation Prompt

## Context & Purpose

This prompt is designed for an AI agent working on the `mimir` project to conduct a comprehensive evaluation of **Dohyun** (노도현), who was part of a 6-month intern program focused on building the **Mimir - Crypto Data Sync Application**. This evaluation will determine whether Dohyun qualifies for conversion from intern to full-time platform engineer at Dunamis Capital's Platform Development Team.

**Critical Context:**
- **Project Era**: This intern project was designed in the pre-AI agent era, requiring significant calibration for current AI-assisted development standards
- **Evaluation Fairness**: Adjustments must be made to fairly evaluate intern-level work in an AI-native development environment
- **Decision Stakes**: This evaluation determines full-time hire eligibility for platform engineering role
- **Dropout Context**: Yongjae Song has already dropped out, making Dohyun's evaluation more critical

## Company Profile & Mission

### Mission
Engineer cross-region, self-healing fintech platforms that move capital instantly for liquidity and strategically for future value—while guaranteeing systemic safety and investor trust.

### Vision
Set the global benchmark for internal fintech engineering, known for real-time observability, < 5 min MTTR, and an innovation cadence that compounds investor advantage.

### Platform Development Team Mission
"To build and operate a fully-automated, self-healing fintech platform that (a) trades digital assets profitably, (b) exposes portfolio-level risk & P&L in real time, and (c) can eventually run without direct human intervention."

## Core Values Assessment Framework (10 Values)

Each value must be assessed with **PROVEN/SUGGESTED/MISSING** methodology:

| # | Value | What Good Looks Like | Anti-Pattern to Avoid |
|---|---|---|---|
| 1 | **Technical Excellence & Scalable Elegance** | Service meets p95 table • CodeClimate ≥ A • Design docs show horizontal scale path | Premature optimization that ignores readability or horizontal growth |
| 2 | **Customer‑Centric Craftsmanship** | User story captures trader pain (#JIRA‑123) • Usability test with 3 real users pre‑GA | Feature built "because it's cool" with zero investor validation |
| 3 | **Ownership & Proactivity** | Engineer pages themselves during incident • RCA published within 24 h and follow‑ups merged | "Throw over wall" to SRE; blaming infra without fix |
| 4 | **Observability & Guardrails** | 3 SLOs + burn‑rate alerts • Kill‑switch toggled in staging weekly | Shipping code with no metric or alert path |
| 5 | **Data‑Informed Iteration** | A/B leads to > +5 % KPI before 100 % rollout • Dashboards updated daily | HIPPO decisions ("highest‑paid person's opinion") with zero telemetry |
| 6 | **Integrity & Reliability** | Immutable audit log (AWS QLDB) tied to every trade • Zero Sev‑0 per quarter | Silent failure of audit pipeline; post‑incident blame game |
| 7 | **Security & Compliance First** | Secrets in AWS SM, rotated 90 d • Static‑analysis gate green every PR | Hard‑coding credentials; manual policy overrides |
| 8 | **Collaboration & Knowledge‑Sharing** | ≥ 2 peer reviews; constructive RFC comments • Tech talks recorded + wiki'ed | Lone‑wolf merges to main; tribal knowledge silos |
| 9 | **Continuous Learning & Mentorship** | New hire gains +1 Dreyfus level in 2 skills • Buddy logs weekly feedback | "Sink‑or‑swim" onboarding; zero growth plan |
| 10 | **Innovative Spirit** | Quarterly hack‑day POC demo; best ideas enter backlog • Budget for 1 conf / eng / yr | Innovation theatre—hack‑day code never revisited |

## Platform Engineering Competency Framework

### Primary Assessment Categories (Current 2025 Standards)

1. **AI Orchestration & Collaboration (35%)**
   - Effective use of AI development tools (Claude, ChatGPT, Copilot, etc.)
   - AI-assisted development workflow optimization
   - Critical validation of AI-generated solutions
   - Learning and iteration through AI collaboration

2. **Systems Thinking & Architecture (30%)**
   - Platform and microservices architecture understanding
   - Cross-system integration and data flow design
   - Production-ready system design considerations
   - Scalability and performance awareness

3. **Critical Thinking & Problem-Solving (20%)**
   - Root cause analysis and debugging approach
   - Structured decision-making processes
   - Trade-off evaluation and documentation (ADRs)
   - Complex system troubleshooting

4. **Continuous Learning & Adaptability (15%)**
   - Learning velocity and knowledge retention
   - Feedback incorporation and improvement
   - Technology adaptation and exploration
   - Growth mindset demonstration

## Mimir Project Specification

### Project Overview
**Mimir** - A real-time crypto data sync application supporting multiple exchanges using Open API endpoints (REST and WebSocket) with CCXT library integration. The application should ingest live crypto data, manage account information, and store data in both live cache and persistent database.

### Technical Requirements Evaluation

#### API Integration & Data Ingestion
- Multi-exchange integration (BitMEX, Binance, Bybit, OKX, Upbit)
- CCXT library utilization with exchange-specific extensions
- Robust error handling ("fail well" principle)
- Data types: Price data (OHLCV, index/mark price), instrument data, account data

#### Data Storage & Persistence
- Caching layer implementation (Redis recommended)
- Data expiration and eviction strategies
- Database schema design for time-series and account data
- Cache-database synchronization

#### Security & API Key Management
- Secure API key management across exchanges
- Data validation and error handling
- Comprehensive error recovery routines

#### Architecture & Infrastructure
- Cloud service selection (AWS/GCP/Azure)
- Containerization (Docker) and orchestration (Kubernetes)
- CI/CD pipeline implementation
- Monitoring and logging systems (ELK stack, Prometheus)

### Project Phases Assessment

#### Q1: Foundation & Project Structure
1. Python project structure research and implementation
2. Design document creation (ADRs)
3. Repository setup and project skeleton
4. Minimal API connector prototype
5. Unit testing implementation
6. Microservices architecture workshop

#### Q2: API Integration & Data Ingestion
1. Domain analysis and functional mapping
2. REST & WebSocket integration strategies
3. Comprehensive API integration module
4. Data normalization and error handling
5. Unit and integration testing
6. Architecture diagram creation

#### Q3: Data Storage, Caching & Security
1. Domain-driven data modeling
2. Data storage and caching strategy research
3. Caching layer implementation
4. Database module design and development
5. Security measures and API key management
6. Comprehensive testing for all modules

#### Q4: System Integration & Finalization
1. Module integration into cohesive system
2. External API endpoint development
3. Performance optimization and load testing
4. CI/CD pipeline and containerization setup
5. Documentation finalization
6. End-to-end testing and final presentation

## Intern Evaluation Criteria (90 Points Total)

### Technical Assessment (54 points)

1. **Basic Programming Skills & Coding Proficiency (8 points)**
2. **Learning Ability & Technology Acquisition Speed (8 points)**
3. **Problem-Solving Ability & Debugging Skills (7 points)**
4. **Development Tools & Environment Utilization (6 points)**
5. **Testing Implementation & Code Quality Awareness (6 points)**
6. **Documentation & Knowledge Organization (6 points)**
7. **Research Skills & Information Gathering (4 points)**
8. **Error Handling & Recovery Skills (3 points)**
9. **Security Awareness & Best Practices (3 points)**
10. **Code Review Participation & Learning (3 points)**

### Professional Skills Assessment (36 points)

1. **Communication & Question-Asking Skills (6 points)**
2. **Project Contribution & Practical Application (6 points)**
3. **Self-Direction & Initiative (5 points)**
4. **Growth Potential & Feedback Reception (5 points)**
5. **Technical Curiosity & Innovation Mindset (4 points)**
6. **Time Management & Task Prioritization (4 points)**
7. **Adaptation to Company Culture & Values (4 points)**
8. **Presentation & Knowledge Sharing Skills (3 points)**

### Minimum Thresholds for Hire Recommendation
- **Overall Score**: ≥ 63/90 (70%)
- **AI Orchestration Competency**: ≥ 75%
- **Technical Excellence Evidence**: Multiple demonstrated examples
- **Core Values Alignment**: ≥ 7/10 values with PROVEN evidence

## AI-Era Calibration Guidelines

### Evaluation Adjustments for AI-Native Development

1. **Traditional vs AI-Assisted Approach Recognition**
   - Acknowledge that project was designed before AI coding agents were available
   - Evaluate foundational programming skills while recognizing AI collaboration potential
   - Consider learning agility as key indicator of AI-era adaptability

2. **Evidence Types for AI-Era Evaluation**
   - **Code Quality**: Focus on architecture, design patterns, and system thinking rather than syntax perfection
   - **Problem-Solving**: Emphasize debugging approach, root cause analysis, and structured thinking
   - **Learning**: Prioritize knowledge acquisition speed and practical application over memorization
   - **Collaboration**: Assess communication, feedback incorporation, and knowledge sharing

3. **AI Collaboration Potential Indicators**
   - Clear articulation of technical problems and solutions
   - Systematic approach to breaking down complex tasks
   - Critical evaluation of technical choices and trade-offs
   - Rapid learning and adaptation to new technologies/concepts

## Evaluation Methodology

### Step 1: Evidence Collection
- Analyze all available project artifacts, documentation, and code repositories
- Review presentation materials, technical decisions, and implementation quality
- Examine learning progression throughout the 6-month program
- Document specific examples supporting each assessment criterion

### Step 2: Core Values Assessment
- Map candidate behavior and decisions to each of the 10 core values
- Classify evidence as PROVEN (clear demonstration), SUGGESTED (partial evidence), or MISSING (no evidence)
- Focus evaluation questions on MISSING values for interview preparation

### Step 3: Technical Competency Evaluation
- Assess platform engineering competency across 4 categories
- Evaluate technical deliverables against current AI-assisted development standards
- Consider project scope and intern-level expectations with appropriate calibration

### Step 4: Comprehensive Scoring
- Score each criterion based on evidence and calibrated expectations
- Calculate weighted scores for technical and professional competencies
- Determine overall recommendation based on minimum thresholds

### Step 5: Recommendation Generation
- Provide clear hire/no-hire recommendation with detailed justification
- Identify strengths and development opportunities
- Suggest onboarding focus areas if hire recommendation is positive
- Document specific evidence supporting all conclusions

## Output Requirements

### Primary Deliverable: Comprehensive Evaluation Report
Create a detailed markdown evaluation report containing:

1. **Executive Summary** (1-2 pages)
   - Overall recommendation (Hire/No Hire)
   - Key strengths and concerns
   - Platform engineering role fit assessment
   - AI collaboration potential evaluation

2. **Core Values Assessment** (2-3 pages)
   - PROVEN/SUGGESTED/MISSING analysis for all 10 values
   - Specific evidence and examples for each value
   - Priority areas for development or interview focus

3. **Technical Competency Analysis** (3-4 pages)
   - Platform engineering competency scoring across 4 categories
   - Project deliverable quality assessment
   - AI-era calibration considerations and adjustments
   - Learning progression and growth demonstration

4. **Intern Evaluation Scoring** (2-3 pages)
   - Detailed scoring across all 18 criteria (90 points total)
   - Evidence-based justification for each score
   - Comparison to minimum thresholds and benchmarks

5. **Platform Engineering Fit Assessment** (1-2 pages)
   - Alignment with team mission and responsibilities
   - Technology stack proficiency evaluation
   - Readiness for full-time platform engineer role

6. **Decision Rationale & Next Steps** (1 page)
   - Detailed justification for hire/no-hire decision
   - Risk factors and mitigation strategies
   - Onboarding recommendations (if hire)
   - Alternative development paths (if no hire)

### Additional Documentation (if needed for readability)

If the main report becomes too lengthy, split into focused documents:

- `dohyun_executive_summary.md` - High-level findings and recommendation
- `dohyun_core_values_analysis.md` - Detailed values assessment
- `dohyun_technical_evaluation.md` - Technical competency deep-dive
- `dohyun_intern_scoring.md` - Detailed criteria scoring
- `dohyun_decision_rationale.md` - Evidence-based decision explanation

### Evidence Documentation Standards
- All claims must be supported by specific evidence
- Reference concrete examples from project work
- Include code references, documentation quality, and technical decisions
- Cite learning progression and adaptation examples
- NO HALLUCINATION OR ASSUMPTIONS - request missing information if needed

## Critical Evaluation Principles

### Fairness & Objectivity
- Maintain objective assessment based on measurable evidence
- Apply consistent evaluation criteria across all competency areas
- Consider intern-level expectations with appropriate benchmarking
- Balance technical skills with growth potential and cultural fit

### AI-Era Contextual Awareness
- Recognize that traditional programming skills may be less relevant in AI-assisted development
- Emphasize systems thinking, architecture understanding, and problem-solving approach
- Evaluate learning agility and adaptation potential for AI-native workflows
- Consider debugging, critical thinking, and validation skills as key differentiators

### Decision Impact Consciousness
- Remember that this evaluation determines full-time employment eligibility
- Consider both current capabilities and growth trajectory
- Weigh technical competency against cultural alignment and team fit
- Provide actionable feedback regardless of final recommendation

### Evidence-Based Rigor
- Demand concrete evidence for all assessments and claims
- Document specific examples and measurable outcomes
- Avoid speculation or assumption-based evaluations
- Request additional information when evidence is insufficient

## Quality Assurance Requirements

- **Comprehensiveness**: Cover all evaluation criteria and competency areas
- **Evidence-Based**: Support all conclusions with specific examples and evidence
- **Contextual**: Apply appropriate AI-era calibration and intern-level expectations
- **Actionable**: Provide clear recommendations and development guidance
- **Professional**: Maintain objective, constructive tone throughout evaluation
- **Complete**: Address all aspects of platform engineering role requirements and cultural fit

This evaluation must be thorough, fair, and decisive in determining Dohyun's readiness for full-time platform engineering role at Dunamis Capital.