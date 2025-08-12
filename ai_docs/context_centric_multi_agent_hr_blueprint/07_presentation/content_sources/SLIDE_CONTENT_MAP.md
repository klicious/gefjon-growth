---
id: slide_content_mapping
type: content_map
domain: presentation
created_date: 2025-08-12
author: Claude Code
quality_score: 9.0/10
tags: [content, mapping, sources, presentation]
visibility: public
version: 1.0
---

# Slide Content Mapping Guide

**Purpose**: Map each slide in the presentation skeleton to specific content sources, ensuring comprehensive and accurate information integration.

## Mapping Overview

### Primary Content Sources
1. **PRESENTATION_CONTEXT_COMPLETE.md** - Comprehensive context document
2. **Workflow Documentation** - `ai_docs/workflows/hiring/`
3. **Execution Results** - `artifacts/public/hiring/candidates/20250811_consolidated/`
4. **Blueprint Materials** - `ai_docs/context_centric_multi_agent_hr_blueprint/`
5. **Live Documentation** - Project configuration and architecture files

## Detailed Slide Mappings

### Slide 1: Title & Introduction
**Content Requirements**:
- Company name and branding
- Subtitle positioning statement
- Presenter information
- Professional design elements

**Content Sources**:
- `PRESENTATION_CONTEXT_COMPLETE.md` (Executive Summary)
- Company branding guidelines
- Presenter credentials and role

**Key Data Points**:
- Platform name: "Gefjon Growth HR Automation"
- Tagline: "Transforming Talent Acquisition Through Intelligent Workflow Automation"
- Date: Current presentation date
- Modern, professional design aesthetic

---

### Slide 2: Executive Summary & Ask
**Content Requirements**:
- Clear value proposition
- Primary objectives summary
- Business impact statement
- Specific call to action

**Content Sources**:
- `PRESENTATION_CONTEXT_COMPLETE.md` (Sections 1, 8, 12)
- `ai_docs/context_centric_multi_agent_hr_blueprint/05_business_model/`

**Key Data Points**:
- **Time Efficiency**: 6 hours for 13 candidates vs 40+ hours manual
- **Quality Score**: 9.2/10 average with 92% pass rate
- **Automation Scope**: Hiring → Performance → OKR → Talent Development
- **Current Status**: Production-ready with proven results

---

### Slide 3: Vision & Purpose
**Content Requirements**:
- Long-term vision statement
- Core principles and values
- Current focus areas
- Technology approach overview

**Content Sources**:
- `PRESENTATION_CONTEXT_COMPLETE.md` (Section 1)
- `CLAUDE.md` (Core Values and Mission)
- `ai_docs/context_centric_multi_agent_hr_blueprint/00_overview/README.md`

**Key Data Points**:
- **Vision**: End-to-end HR automation with intelligent decision support
- **Principles**: Context engineering, AI agent orchestration, human oversight
- **Focus**: Hiring pipeline as proof of concept for broader HR automation

---

### Slide 4: Problem & Opportunity
**Content Requirements**:
- Traditional hiring pain points
- Market opportunity sizing
- Current inefficiency statistics
- Scalability challenges

**Content Sources**:
- `ai_docs/context_centric_multi_agent_hr_blueprint/01_market/`
- Industry research and benchmarks
- Time savings analysis from implementation

**Key Data Points**:
- **Manual Process Issues**: Inconsistent evaluation, time consumption, bias potential
- **Market Size**: $50B+ HR technology market
- **Efficiency Problems**: 40+ hours manual vs 6 hours automated
- **Quality Inconsistency**: Variable interviewer performance and evaluation criteria

---

### Slide 5: Solution Overview
**Content Requirements**:
- High-level workflow description
- Context-centric approach explanation
- Technology stack overview
- End-to-end automation scope

**Content Sources**:
- `ai_docs/workflows/hiring/orchestrator.md` (Workflow Overview)
- `CLAUDE.md` (Technology Stack)
- `PRESENTATION_CONTEXT_COMPLETE.md` (Section 2)

**Key Data Points**:
- **7-Stage Pipeline**: Pre-flight → Context → Intake → JD Mapping → Screening → Assignment → Interview Kit
- **Context Engineering**: 90%+ context completeness requirement
- **Tech Stack**: Python 3.12, Gemini CLI, UV, DVC, Git
- **AI Agents**: Claude Code, Gemini CLI, Amazon Q Developer, KIRO

---

### Slide 6: Technical Architecture
**Content Requirements**:
- Core technology components
- MCP server integrations
- Context engineering architecture
- Scalability and reliability features

**Content Sources**:
- `ai_docs/context_centric_multi_agent_hr_blueprint/03_architecture/`
- `PRESENTATION_CONTEXT_COMPLETE.md` (Section 2)
- MCP configuration from `.mcp.json`

**Key Data Points**:
- **MCP Servers**: Exa (research), Sequential Thinking (reasoning), Playwright (automation), Fetch (HTTP)
- **Context Architecture**: Pre-flight validation, automatic discovery, schema validation
- **Storage**: Structured artifacts/ and context/ directories
- **Quality Gates**: 90% context completeness, 80% data quality minimum

---

### Slide 7: Achievements & Metrics
**Content Requirements**:
- Production workflow status
- Real execution statistics
- Performance benchmarks
- Quality measurements

**Content Sources**:
- `artifacts/public/hiring/candidates/20250811_consolidated/HIRING_SUMMARY_COMPLETE.md`
- `artifacts/public/hiring/candidates/20250811_consolidated/FINAL_WORKFLOW_SUMMARY.json`
- Execution logs and performance data

**Key Data Points**:
- **Execution Date**: August 11, 2025
- **Candidates Processed**: 13 backend developers
- **Total Time**: 6 hours complete pipeline
- **Success Rate**: 100% stage completion, 0% error rate
- **Quality Score**: 9.2/10 average
- **Outcomes**: 15.4% strong hire, 53.8% hire, 23.1% lean hire, 7.7% no hire

---

### Slide 8: Workflow Stages (Detail)
**Content Requirements**:
- Detailed stage breakdown
- Quality gates and thresholds
- Processing requirements
- Validation criteria

**Content Sources**:
- `ai_docs/workflows/hiring/orchestrator.md` (Enhanced Execution Workflow)
- `ai_docs/workflows/hiring/tasks/` (Individual stage specifications)

**Key Data Points**:
- **Stage 0**: Pre-flight validation (≥90% context completeness)
- **Stage 1**: Context verification and loading
- **Stage 2**: Data normalization (≥80% quality threshold)
- **Stage 3**: JD mapping (≥75% confidence)
- **Stage 4**: Screening (Strong Hire ≥9.0, Hire ≥8.0, Lean Hire ≥6.5)
- **Stage 5**: Assignment generation (≥8.0/10 candidates)
- **Stage 6**: BEI interview kit generation
- **Stage 7**: Consolidation and organization

---

### Slide 9: Data Flow & Artifacts
**Content Requirements**:
- Input data format and structure
- Output organization and structure
- Candidate directory examples
- File generation statistics

**Content Sources**:
- `data/public/hiring/resume/20250731/candidates_20250731.json` (input format)
- `artifacts/public/hiring/candidates/20250811_consolidated/` (output structure)
- Candidate directory examples (atlas_001_minseok_kim)

**Key Data Points**:
- **Input**: Single JSON with candidate array (13 candidates)
- **Output Structure**: Individual candidate directories with screening/, takehome/, interview/, evaluation/
- **Example**: atlas_001_minseok_kim - 9.1/10 score, strong hire, complete materials
- **File Generation**: 100% completion rate for all required materials

---

### Slide 10: Unique Differentiators
**Content Requirements**:
- Context engineering approach
- AI agent orchestration
- Evidence-based assessment
- End-to-end automation
- BEI integration

**Content Sources**:
- `PRESENTATION_CONTEXT_COMPLETE.md` (Section 9)
- Technical implementation details
- Competitive analysis

**Key Data Points**:
- **Context Engineering**: Complete data verification before decisions
- **Multi-Agent System**: Reduces single-point-of-failure risk
- **Evidence-Based**: All assessments backed by specific examples
- **Complete Pipeline**: Not just screening or tracking
- **BEI Integration**: Behavioral Event Interview for culture fit
- **Customization**: Adaptable workflows and multi-tenant support

---

### Slide 11: Business Model & Value Proposition
**Content Requirements**:
- Demonstrated time savings
- Quality consistency metrics
- Bias reduction approach
- Target market segments
- Revenue model options

**Content Sources**:
- `ai_docs/context_centric_multi_agent_hr_blueprint/05_business_model/`
- ROI calculations from implementation
- `PRESENTATION_CONTEXT_COMPLETE.md` (Section 8)

**Key Data Points**:
- **Time Efficiency**: 6 hours vs 40+ hours (85% reduction)
- **Quality**: 9.2/10 standardized scores
- **Bias Reduction**: Evidence-based, structured evaluation
- **Markets**: Early adopters, growth-stage, enterprise
- **Revenue**: SaaS subscriptions, professional services, enterprise licensing

---

### Slide 12: Future Roadmap
**Content Requirements**:
- Phase-based expansion plan
- Timeline and milestones
- Capability evolution
- Market expansion strategy

**Content Sources**:
- `ai_docs/context_centric_multi_agent_hr_blueprint/06_execution_roadmap/`
- `PRESENTATION_CONTEXT_COMPLETE.md` (Section 7)
- Strategic planning documents

**Key Data Points**:
- **Phase 2 (6 months)**: Performance management, OKR tracking, multi-client pilots
- **Phase 3 (6-12 months)**: Client customization, multi-tenant architecture
- **Phase 4 (12+ months)**: Industry-specific, global expansion, partner ecosystem
- **Vision**: Complete talent development and team evaluation platform

---

### Slide 13: Risk Mitigation & Quality Assurance
**Content Requirements**:
- Technical risk management
- Business risk mitigation
- Quality assurance framework
- Compliance and security measures

**Content Sources**:
- `ai_docs/context_centric_multi_agent_hr_blueprint/04_security_compliance/`
- Quality gates from orchestrator documentation
- Risk assessment analysis

**Key Data Points**:
- **Technical Risks**: Multi-agent redundancy, modular architecture, fallback mechanisms
- **Business Risks**: Proven case studies, flexible implementation, pilot programs
- **Quality Assurance**: ≥8.5/10 threshold, bias detection, continuous monitoring
- **Security**: GDPR compliance, audit trails, access controls

---

### Slide 14: Implementation Strategy & Timeline
**Content Requirements**:
- Phase-based implementation approach
- Milestone definitions
- Resource requirements
- Project management framework

**Content Sources**:
- Implementation timeline from roadmap
- Project phases from execution planning
- Resource allocation analysis

**Key Data Points**:
- **Phase 1 (Completed)**: Core hiring automation, proof of concept
- **Phase 2-4**: Detailed timeline with milestones
- **Project Management**: Defined owners, review cadences, success criteria
- **Scalability**: Cloud-native architecture for growth

---

### Slide 15: Call to Action & Next Steps
**Content Requirements**:
- Specific asks for different audiences
- Next step definitions
- Decision timeline
- Contact information

**Content Sources**:
- Business development strategy
- Client engagement framework
- Partnership opportunities

**Key Data Points**:
- **Clients**: Pilot program, custom demo, ROI assessment
- **Investors**: Market opportunity review, technical due diligence, growth planning
- **Partners**: API integration, reseller programs, technology partnerships
- **Decision Points**: Specific owners, target feedback dates

---

### Slide 16: Conclusion
**Content Requirements**:
- Key message reinforcement
- Value proposition summary
- Future potential highlights
- Final compelling statement

**Content Sources**:
- Executive summary recap
- Vision and mission alignment
- Competitive advantages

**Key Data Points**:
- **Platform Uniqueness**: Context-centric, end-to-end, AI-orchestrated
- **Proven Results**: Reliability, efficiency, quality demonstrated
- **Future Vision**: Beyond hiring to complete talent management
- **Partnership Invitation**: Join the talent acquisition revolution

---

### Slide 17: Appendix Map
**Content Requirements**:
- Navigation guide for deep-dive sections
- Content organization overview
- Quick reference structure

**Content Sources**:
- Appendix content organization
- Technical documentation references
- Q&A preparation materials

## Appendix Content Mapping

### Appendix A: Stage Breakdown - Pre-Flight & Context
**Sources**:
- `ai_docs/workflows/hiring/tasks/00_candidate_splitting.md`
- `ai_docs/workflows/hiring/tasks/01_context_verification.md`
- Context completeness scoring algorithms

### Appendix B: Stage Breakdown - Intake, JD Mapping & Screening
**Sources**:
- `ai_docs/workflows/hiring/tasks/02_intake_normalization.md`
- `ai_docs/workflows/hiring/tasks/03_jd_mapping.md`
- `ai_docs/workflows/hiring/tasks/04_screening.md`
- Scoring models and bias detection

### Appendix C: Stage Breakdown - Assignment & Interview Kit
**Sources**:
- `ai_docs/workflows/hiring/tasks/05_takehome_assignment.md`
- `ai_docs/workflows/hiring/tasks/06_interview_kit.md`
- Sample assignments and BEI questions

### Appendix D: Data Schemas & Integration Details
**Sources**:
- JSON schemas from candidate data
- Directory structures from artifacts
- API integration diagrams

### Appendix E: ROI Model & Sensitivity Analysis
**Sources**:
- Time savings calculations
- Cost-benefit analysis
- Market benchmarking data

### Appendix F: Risk Register & Mitigation Plans
**Sources**:
- Risk assessment documentation
- Mitigation strategies
- Contingency planning

### Appendix G: Implementation Playbook
**Sources**:
- Deployment procedures
- Training materials
- Change management framework

---

## Content Quality Standards

### Data Accuracy Requirements
- All metrics verified against source documents
- Consistent terminology across all slides
- Up-to-date information with clear timestamps
- Proper attribution for all claims and statistics

### Content Completeness Checklist
- [ ] All slides mapped to specific sources
- [ ] Supporting evidence identified for all claims
- [ ] Technical details verified against implementation
- [ ] Business model validated against market research
- [ ] Appendices comprehensive for Q&A support

### Update Triggers
- New workflow execution results
- Performance metric improvements
- Architecture or technology changes
- Market analysis updates
- Competitive landscape shifts

---

**Document Status**: Complete Content Mapping  
**Next Phase**: Begin slide content development  
**Update Schedule**: Weekly during active development  
**Quality Review**: Required before each presentation iteration