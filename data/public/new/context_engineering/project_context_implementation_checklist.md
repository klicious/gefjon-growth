# Gefjon Growth HR Automation Context Implementation Checklist
**For Setting Up AI-Agent Context Loading in HR Automation Projects**

## Pre-Implementation Assessment

### [ ] HR Automation Project Analysis
- [ ] Identify HR domains: `hiring, performance, onboarding, talent_development`
- [ ] Document company mission, vision, and core values (10 values)
- [ ] Map current HR processes and workflows
- [ ] List team members and their roles (platform development team)
- [ ] Inventory existing interview materials and candidate data
- [ ] Note current HR documentation and process guides

### [ ] HR Automation Tool Prerequisites
- [ ] Python 3.12+ installed (Gefjon Growth requirement)
- [ ] YAML and JSON parsing libraries available
- [ ] Git repository initialized
- [ ] Gemini CLI configured with ReAct workflows
- [ ] Claude Code access for interview kit generation
- [ ] KIRO agent framework (if applicable)

## Phase 1: HR Context Directory Structure Setup

### [ ] Core HR Context Creation
```bash
mkdir -p context/company_info
mkdir -p context/hr_processes/hiring
mkdir -p context/hr_processes/evaluation
mkdir -p context/hr_processes/onboarding
mkdir -p context/hr_processes/sops
mkdir -p context/teams
mkdir -p ai_docs/prompts/hiring
mkdir -p scripts
```

### [ ] HR Artifacts Directory Structure
```bash
mkdir -p artifacts/private/hiring/evaluation
mkdir -p artifacts/private/hiring/interview_feedback
mkdir -p artifacts/private/hiring/screening_reports
mkdir -p artifacts/private/evaluation/bias_check_logs
mkdir -p artifacts/public/hiring/interview_materials/upcoming
mkdir -p artifacts/public/hiring/pair_programming
mkdir -p artifacts/public/hiring/evaluation_sheets/upcoming
mkdir -p data/public/hiring/resume
mkdir -p data/private/hiring
```

## Phase 2: Core HR Context Files

### [ ] Company Foundation
Create `context/company_info/mission_vision_values.yaml` with:
- [ ] Mission statement for fintech platform engineering
- [ ] Vision statement for fintech excellence
- [ ] 10 Core values with examples and anti-patterns
- [ ] Technical excellence standards
- [ ] HR automation principles

**Template Reference**: Based on existing Gefjon Growth mission_vision_values.yaml

### [ ] HR Process Registry
Create `context/hr_processes/hiring/hiring_stages.yaml` with:
- [ ] Interview stages (screening, take-home, technical, cultural)
- [ ] BEI (Behavioral Event Interviewing) framework
- [ ] Technical assessment levels (easy, intermediate, expert)
- [ ] Core values alignment criteria
- [ ] Red flag identification process
- [ ] Interview kit generation requirements

**Critical Fields**:
```yaml
hiring_stages:
  screening:
    purpose: "Initial candidate evaluation"
    duration: "30 minutes"
    focus: ["basic_qualifications", "cultural_fit"]
  technical_interview:
    purpose: "Technical skill validation"
    duration: "60 minutes"
    focus: ["coding_skills", "system_design", "problem_solving"]
    
ai_agent_instructions:
  context_loading_rule: "Always reference this file for interview kit generation"
```

### [ ] Platform Team Composition
Create `context/teams/platform_development_team.yaml` with:
- [ ] Team members and roles (Platform Lead, Senior/Mid Engineers, Interns)
- [ ] Technology stack (Python 3.12, Java 17, AI/LLM tools)
- [ ] Core responsibilities (algorithmic trading, PMS, multi-agent automation)
- [ ] Working hours and collaboration preferences
- [ ] Hiring requirements and skill expectations

### [ ] HR Process Definitions
Create `context/hr_processes/evaluation/performance_review_process.yaml` with:
- [ ] Performance review cycles and schedules
- [ ] Evaluation criteria and rubrics
- [ ] OKR alignment and tracking
- [ ] Feedback collection and analysis
- [ ] Career development planning

### [ ] Onboarding Process
Create `context/hr_processes/onboarding/onboarding_plan.yaml` with:
- [ ] New hire onboarding stages
- [ ] Training requirements and schedules
- [ ] Mentorship program structure
- [ ] Tool access and setup procedures
- [ ] 90-day evaluation milestones

## Phase 3: HR Process Relationships

### [ ] HR Process Relationships
Create `context/hr_processes/sops/sop_implementation_guide.yaml` with:
- [ ] Candidate → Interview Stage relationships (PROGRESSES_THROUGH)
- [ ] Team → Role → Candidate relationships (EVALUATES)
- [ ] Core Values → Assessment Criteria relationships (MAPS_TO)
- [ ] Technical Skills → Problem Level relationships (MATCHES)

### [ ] HR Validation Rules
Create validation rules for:
- [ ] Candidate data completeness and format
- [ ] Interview kit generation requirements
- [ ] Core values alignment scoring
- [ ] Technical assessment level assignment

## Phase 4: HR Process Documentation

### [ ] Core HR Processes
Document in `context/hr_processes/`:
- [ ] `power_of_process.md` - HR process philosophy and principles
- [ ] `sop_implementation_guide.yaml` - Standard operating procedures
- [ ] `interview_best_practices.yaml` - BEI methodology and guidelines
- [ ] `candidate_evaluation_framework.yaml` - Assessment criteria and rubrics

### [ ] HR Quality Standards
- [ ] Interview quality criteria and consistency requirements
- [ ] Candidate evaluation accuracy and fairness standards
- [ ] Core values alignment assessment guidelines
- [ ] Bias prevention and mitigation procedures

## Phase 5: HR Context Loading Implementation

### [ ] HR Context Loading Procedure
Create `ai_docs/context/gefjon_growth_context_loading_procedure.md` with:
- [ ] HR-specific context loading steps
- [ ] Candidate data validation procedures
- [ ] Interview kit generation prerequisites
- [ ] Context completeness verification

### [ ] HR Context Validation Script
Create `scripts/validate_hr_context.py` with:
- [ ] Company values completeness check (10 values)
- [ ] Candidate JSON schema validation
- [ ] Technical problem bank verification
- [ ] Interview materials consistency checks
- [ ] HR process context validation

**Test the HR validator**:
```bash
python scripts/validate_hr_context.py
```

### [ ] Context Update Procedures
Document procedures for:
- [ ] Adding new team members
- [ ] Adding new AWS accounts
- [ ] Adding new repositories/services
- [ ] Updating organizational information

## Phase 6: HR AI Agent Integration

### [ ] Multi-Agent Configuration
For Claude Code, Gemini CLI, and KIRO:
- [ ] Configure HR context loading in each agent's initialization
- [ ] Add context validation to interview kit generation
- [ ] Implement context caching for HR workflows
- [ ] Add context refresh for candidate data updates

### [ ] HR Agent Instructions
Add HR-specific AI agent instructions to each context file:
- [ ] Interview kit generation guidelines
- [ ] Candidate assessment procedures
- [ ] Core values alignment methodology
- [ ] Technical problem selection criteria

### [ ] Testing HR Context Usage
- [ ] Test interview kit generation with complete context
- [ ] Verify candidate assessment accuracy
- [ ] Test core values alignment mapping
- [ ] Validate technical problem level assignment

## Phase 7: HR Documentation and Training

### [ ] HR Implementation Documentation
- [ ] HR context loading guidelines for Gefjon Growth
- [ ] Interview kit generation troubleshooting
- [ ] Candidate data update procedures
- [ ] HR automation performance optimization

### [ ] HR Team Training
- [ ] HR context structure overview for hiring team
- [ ] How to update candidate profiles and processes
- [ ] AI agent requirements for HR automation
- [ ] Debugging interview kit generation issues

## Phase 8: Maintenance and Monitoring

### [ ] Automated Checks
Set up automated validation:
- [ ] Pre-commit hooks for context validation
- [ ] CI/CD pipeline context checks
- [ ] Scheduled context freshness validation
- [ ] Broken reference detection

### [ ] Monitoring Setup
- [ ] Context loading success/failure metrics
- [ ] Context freshness monitoring
- [ ] Usage analytics for optimization
- [ ] Change notification systems

### [ ] Update Procedures
- [ ] Regular context review schedule (monthly/quarterly)
- [ ] Context archival for old data
- [ ] Version control and change tracking
- [ ] Rollback procedures for invalid updates

## HR Verification Checklist

### [ ] HR Context Loading Tests
- [ ] Load company values (all 10) successfully
- [ ] Load hiring process stages correctly
- [ ] Resolve team composition and role requirements
- [ ] Access candidate profile information
- [ ] Validate technical problem bank availability

### [ ] HR AI Agent Tests
- [ ] Agent can load HR context without errors
- [ ] Interview kit generation uses complete context
- [ ] Candidate assessments align with company values
- [ ] Technical problems match candidate skill levels
- [ ] BEI questions reference specific experiences

### [ ] Error Handling Tests
- [ ] Missing context files handled gracefully
- [ ] Invalid YAML syntax detected and reported
- [ ] Broken references identified and logged
- [ ] Stale context warnings generated
- [ ] Validation failures prevent operations

## HR Success Criteria

### [ ] HR Context Completeness
- [ ] All 10 company core values documented and accessible
- [ ] HR processes properly modeled (hiring, performance, onboarding)
- [ ] Candidate validation rules comprehensive
- [ ] Interview materials metadata complete and consistent

### [ ] HR AI Agent Effectiveness
- [ ] Agents consistently load HR context before operations
- [ ] Interview kit generation always uses complete company context
- [ ] Candidate assessments accurately map to core values
- [ ] Technical assessments match role requirements
- [ ] Error rates for HR context-related issues < 1%

### [ ] Maintenance Efficiency
- [ ] Context updates take < 15 minutes
- [ ] Validation runs automatically on changes
- [ ] Team members can update their own context
- [ ] Documentation stays current with context changes

## Common Pitfalls to Avoid

### [ ] Context Design Issues
- [ ] ❌ Avoid: Monolithic context files (split large entities)
- [ ] ❌ Avoid: Hardcoded credentials in context (use placeholders)
- [ ] ❌ Avoid: Missing metadata (always include version, purpose, timestamp)
- [ ] ❌ Avoid: Inconsistent naming (follow conventions strictly)

### [ ] Implementation Issues
- [ ] ❌ Avoid: Skip validation scripts (always implement and run)
- [ ] ❌ Avoid: Missing error handling (implement graceful failures)
- [ ] ❌ Avoid: No context caching (implement for performance)
- [ ] ❌ Avoid: Manual context updates only (automate where possible)

### [ ] Maintenance Issues
- [ ] ❌ Avoid: No update schedule (establish regular reviews)
- [ ] ❌ Avoid: No change tracking (use version control)
- [ ] ❌ Avoid: No freshness monitoring (implement staleness alerts)
- [ ] ❌ Avoid: No team training (ensure team understands system)

## HR Domain-Specific Customizations

### [ ] HR-Specific Entities
Add custom entities relevant to HR automation:
- [ ] Candidate profiles with structured JSON schema
- [ ] Interview stages with BEI methodology
- [ ] Technical problem banks with difficulty levels
- [ ] Core values with concrete examples and anti-patterns

### [ ] HR Industry-Specific Processes
Document HR domain-specific processes:
- [ ] Equal opportunity and bias prevention procedures
- [ ] Candidate privacy and data protection protocols
- [ ] Interview consistency and quality assurance
- [ ] Performance evaluation fairness and transparency

### [ ] Integration Requirements
- [ ] Third-party system integrations
- [ ] Legacy system interfaces
- [ ] External API dependencies
- [ ] Compliance reporting requirements

---

**Completion Timeline**: Following this checklist should result in a fully functional HR automation context loading system within 1-2 weeks for Gefjon Growth.

**Support**: Reference existing Gefjon Growth context files and the customized guidelines in this directory for HR-specific patterns and examples.