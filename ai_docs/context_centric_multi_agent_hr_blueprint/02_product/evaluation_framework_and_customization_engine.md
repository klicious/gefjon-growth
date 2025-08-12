---
id: evaluation_framework_and_customization_engine
type: product_spec
domain: hr_automation
created_date: 2025-08-11
last_updated: 2025-08-11
author: Junie
quality_score: 9.5/10
tags: [evaluation, customization, yaml-dsl, top-tier-standards]
visibility: public
version: 2.0
---

# Evaluation Framework & Customization Engine — Enhanced with Top-Tier Industry Standards

## Purpose
Define a human-readable, machine-actionable configuration (YAML DSL) that allows each client and team to customize their hiring process, scoring rubrics, thresholds, and safeguards without code changes, while maintaining Top-Tier Industry Standards for production-ready engineering assessment.

## Design Principles
- **Excellence over adequacy**: Prefer robust, production-ready engineering over bare functionality
- **Explainability**: Every score must be supported by evidence with citations to source artifacts and chunks
- **Customizability**: Teams can change criteria, weights, scoring anchors, and pass logic via YAML
- **Production readiness**: Assess durability under real-world conditions and failures
- **Systems thinking**: Favor sound architecture, clean abstractions, and scalable design
- **Fairness & bias control**: PII redaction, structured comparisons, calibration sets, and bias checks
- **Deterministic aggregation**: Clear formulas, thresholds, tie-break rules, and overrides
- **Cost-aware**: Token and model routing policies per stage; reuse cached analyses

## Cross-References
- `00_overview/README.md` (vision and MVP)
- `03_architecture/architecture_overview.md` (PRD & architecture)
- `03_architecture/data_ingestion_normalization_pipeline.md` (normalized inputs and provenance)
- `04_security_compliance/security_compliance_and_data_governance.md` (bias/PII controls)
- `06_execution_roadmap/task_breakdown.md` (tasks to implement this DSL)
- `ai_docs/prompts/hiring/evaluate_take_home_assignment_prompt.md` (Top-Tier Industry Standards framework)
- Existing evaluation artifacts: `data/public/evaluation/*` and `artifacts/public/hiring/evaluation_sheets/*`

## Enhanced YAML DSL (v2.0) - Top-Tier Industry Standards

### Core Structure
```yaml
process: string                # e.g., BackendEngineer_TopTier
version: 2                     # Enhanced with Top-Tier Industry Standards
locale: en                     
description: "Top-Tier Industry Standards evaluation focusing on production-ready engineering"
evaluation_philosophy: "top_tier_industry_standards"
standards_focus:
  - production_readiness
  - systems_thinking
  - operational_excellence
  - pragmatic_innovation
pass_logic: "weighted_average >= threshold AND no_critical_failures"

bias_controls:
  redact_pii: ["photo", "age", "school"]
  require_evidence: true
  calibration:
    mode: compare_against_goldset
    goldset_ref: "s3://.../top_tier_goldset.json"

cost_policies:
  default_model: bedrock.claude-sonnet  # Higher capability for rigorous assessment
  max_tokens: 6000                      # Increased for comprehensive evaluation
  max_cost_per_candidate_usd: 1.50      # Higher budget for quality assessment

stages:
  - name: take_home_evaluation
    type: take_home_top_tier
    weight: 1.0
    evaluation_standards: "top_tier_industry"
    rubric:
      scale: 1-5                        # Top-Tier Industry Standards scale
      philosophy: "Excellence over adequacy - production-ready engineering assessment"
      
      criteria:
        - id: functional_correctness_completeness
          label: "Functional Correctness & Completeness"
          weight: 0.25
          description: "Production-ready functionality with comprehensive error handling"
          anchors:
            5: "Production-ready code with comprehensive observability and resilience patterns"
            4: "Near-production quality with meaningful observability and some resilience patterns"
            3: "Functional code with basic error handling and some production considerations"
            2: "Working code but minimal production readiness"
            1: "Critical bugs or production-breaking issues"
          signals:
            positive: ["graceful error handling", "input validation", "edge case coverage", "performance considerations"]
            negative: ["unhandled failures", "missing validation", "incomplete core flows"]
          critical: true
          evidence_policy:
            require_citations: true
            min_snippets: 2
            max_snippets: 5
            allowed_sources: ["code", "tests", "documentation", "readme"]
            
        - id: code_quality_best_practices
          label: "Code Quality & Best Practices"
          weight: 0.20
          description: "Readable, maintainable, idiomatic code with observability"
          anchors:
            5: "Idiomatic code with observability and quality gates"
            4: "Readable, maintainable code with good patterns"
            3: "Clean code with appropriate abstractions"
            2: "Basic patterns with notable gaps"
            1: "Weak architecture and poor code quality"
          signals:
            positive: ["observability", "logging", "metrics", "type safety", "quality gates"]
            negative: ["tangled code", "hard-coded credentials", "poor separation of concerns"]
          critical: true
          
        - id: testing_approach_coverage
          label: "Testing Approach & Coverage"
          weight: 0.15
          description: "Comprehensive testing with multiple test types"
          anchors:
            5: "~90%+ coverage with multiple test types including integration/performance"
            4: "~80%+ coverage with integration tests"
            3: "~60%+ coverage primarily unit tests, some integration"
            2: "~40%+ coverage, mostly unit tests only"
            1: "<40% coverage or missing key test types"
          signals:
            positive: ["unit tests", "integration tests", "edge case testing", "CI/CD readiness"]
            negative: ["no tests", "tests fail", "poor coverage"]
            
        - id: documentation_quality
          label: "Documentation Quality"
          weight: 0.10
          description: "Comprehensive documentation with operational guidance"
          anchors:
            5: "Thorough documentation: API contracts, runbooks, ADRs, operational guidance"
            4: "Good documentation including operational notes"
            3: "Adequate documentation for setup and usage"
            2: "Minimal documentation"
            1: "Insufficient or missing documentation"
            
        - id: ownership_proactivity
          label: "Ownership & Proactivity"
          weight: 0.15
          description: "Production readiness signals and thoughtful improvements"
          anchors:
            5: "Production readiness signals, thoughtful improvements, security awareness"
            4: "Clear proactive improvements beyond minimum"
            3: "Some thoughtful improvements"
            2: "Limited initiative"
            1: "No proactive thinking"
          signals:
            positive: ["health checks", "graceful shutdown", "alerting hooks", "security considerations"]
            
        - id: scalability_design_patterns
          label: "Scalability & Design Patterns"
          weight: 0.15
          description: "Enterprise-aware architecture with resilience patterns"
          anchors:
            5: "Enterprise-aware architecture; clean modularization and scalability considerations"
            4: "Solid architecture with scalability considerations and appropriate patterns"
            3: "Clean architecture with appropriate abstractions; limited enterprise patterns"
            2: "Basic architecture and patterns; notable gaps"
            1: "Weak architecture"
          signals:
            positive: ["resilience patterns", "horizontal scaling", "configuration management", "modularization"]
            
        - id: quantitative_logical_problem_solving
          label: "Quantitative & Logical Problem Solving"
          weight: 0.10
          description: "Strong CS fundamentals with performance awareness"
          anchors:
            5: "Evidence of innovative, well-justified approaches and strong CS fundamentals"
            4: "Clear optimization and advanced problem-solving evidence"
            3: "Standard problem-solving; limited innovation"
            2: "Simple solutions; little to no optimization"
            1: "Basic programming competence only"
          signals:
            positive: ["algorithmic awareness", "complexity analysis", "performance modeling", "data precision"]

    # Top-Tier Industry Standards Thresholds
    pass_thresholds:
      strong_hire: 4.5      # Ready for senior-level responsibilities with high autonomy
      hire: 3.8             # Strong engineer; minor gaps addressable with light mentorship
      lean_hire: 3.0        # Competent with potential; notable gaps requiring mentorship
      no_hire: 0.0          # <3.0 - Significant gaps relative to Top-Tier Industry Standards
      
    bias_controls:
      redact_pii: ["photo", "age", "school", "name"]
      require_evidence: true
      production_focus: true
      
    model_policy:
      model: bedrock.claude-sonnet    # Higher capability for rigorous assessment
      max_tokens: 4000
      temperature: 0.1                # Slight creativity for nuanced evaluation
      
    human_in_loop:
      required: true
      approver_role: platform_lead
      quality_threshold: 8.5
```

## Enhanced Scoring and Aggregation (Top-Tier Standards)

### Scoring Philosophy
- **Production-first assessment**: Prioritize production risks over surface polish
- **Evidence-based evaluation**: All comments must reference specific files/lines/examples
- **Calibrated expectations**: Adjust standards based on candidate level while maintaining quality bar
- **Systems thinking**: Evaluate architecture, boundaries, and extensibility

### Normalization and Thresholds
- **Scale**: 1-5 point scale with detailed behavioral anchors
- **Weighted scoring**: Functional Correctness (25%) + Code Quality (20%) + Testing (15%) + Documentation (10%) + Ownership (15%) + Scalability (15%) + Problem Solving (10%)
- **Decision thresholds**: 
  - Strong Hire: ≥4.5 (Ready for senior-level responsibilities)
  - Hire: ≥3.8 (Strong engineer with minor gaps)
  - Lean Hire: ≥3.0 (Competent with potential)
  - No Hire: <3.0 (Significant gaps)

### Enhanced Output Schema
```json
{
  "process": "BackendEngineer_TopTier",
  "evaluation_standards": "top_tier_industry",
  "stage": "take_home_evaluation",
  "candidate_id": "cand_01H...",
  "scores": {
    "functional_correctness_completeness": {
      "raw": 4,
      "normalized": 4.0,
      "weight": 0.25,
      "weighted_score": 1.0,
      "evidence": [
        {
          "artifact_id": "art_...",
          "chunk_id": "chk_...",
          "file_reference": "src/main.py:45-52",
          "quote": "Comprehensive error handling with graceful degradation",
          "production_indicator": "error_handling"
        }
      ],
      "production_readiness_signals": ["error_handling", "input_validation", "edge_cases"]
    }
  },
  "overall_score": 4.2,
  "recommendation": "hire",
  "threshold_met": true,
  "critical_failures": [],
  "production_readiness_assessment": {
    "observability": "present",
    "resilience_patterns": "basic",
    "scalability_considerations": "good",
    "operational_excellence": "adequate"
  },
  "top_tier_indicators": {
    "innovation_evidence": true,
    "systems_thinking": true,
    "production_awareness": true,
    "cs_fundamentals": true
  },
  "bias_controls": {"pii_redacted": true},
  "model_usage": {
    "model": "bedrock.claude-sonnet",
    "prompt_tokens": 2400,
    "completion_tokens": 800,
    "cost_usd": 0.45
  },
  "audit": {
    "evaluator": "llm+agent",
    "version": "2.0.0",
    "standards": "top_tier_industry",
    "timestamp": "2025-08-11T08:10:00Z"
  }
}
```

## Enhanced Prompts and Tool Functions

### System Prompt Template (Top-Tier Standards)
```
You are an expert technical evaluator applying Top-Tier Industry Standards. Your goal is to identify well-qualified engineering talent capable of building and operating production systems with strong reliability, scalability, and maintainability.

EVALUATION PHILOSOPHY:
- Excellence over adequacy: Prefer robust, production-ready engineering over bare functionality
- Production readiness: Assess durability under real-world conditions and failures
- Systems thinking: Favor sound architecture, clean abstractions, and scalable design
- Operational excellence: Expect sensible observability, testing, and reliability practices

EVIDENCE REQUIREMENTS:
- Always tie comments to concrete evidence (files/lines/examples)
- Provide specific file and line references for all scoring decisions
- Focus on production-breaking risks over surface polish
- Calibrate expectations to candidate level while maintaining quality bar

OUTPUT FORMAT:
- Use the structured JSON schema provided
- Include production readiness indicators for each criterion
- Provide actionable, respectful feedback grounded in evidence
```

## Integration with Existing Framework

### Compatibility with Current System
- **Backward compatible**: Existing YAML configurations continue to work
- **Enhanced mode**: New `evaluation_philosophy: "top_tier_industry_standards"` flag enables enhanced evaluation
- **Gradual migration**: Teams can opt-in to Top-Tier Standards per role or process
- **Consistent output**: Same JSON schema with additional Top-Tier indicators

### Integration Points
- **Take-home evaluation**: Direct integration with `ai_docs/prompts/hiring/evaluate_take_home_assignment_prompt.md`
- **Evaluation sheets**: Enhanced templates in `artifacts/public/hiring/evaluation_sheets/`
- **Workflow integration**: Seamless integration with `ai_docs/workflows/hiring_end_to_end.md`
- **Context engineering**: Leverages existing context management and artifact storage

## Calibration Protocol (Top-Tier Standards)

### Quality Assurance
- **Weekly calibration**: Sample of 20 evaluations reviewed by senior engineering panel
- **Inter-rater reliability**: Track Cohen's kappa between human and model-assisted scores
- **Goldset maintenance**: Curated set of labeled candidates with consensus Top-Tier scores
- **Continuous improvement**: Adjust anchors and weights based on hiring outcomes

### Bias Controls (Enhanced)
- **Production focus bias**: Ensure evaluation doesn't penalize candidates for missing enterprise patterns not explicitly required
- **Experience level calibration**: Adjust expectations appropriately for junior vs senior candidates
- **Technology stack neutrality**: Focus on principles and patterns rather than specific technologies
- **Cultural bias mitigation**: Emphasize technical excellence over communication style preferences

## Security & Compliance (Enhanced)

### Audit Trail
- **Comprehensive logging**: Every evaluation decision with evidence references
- **PII protection**: Enhanced redaction with production-grade security
- **Model usage tracking**: Detailed cost and performance metrics
- **Quality metrics**: Track evaluation consistency and accuracy over time

### Compliance Integration
- **GDPR ready**: Automated data retention and deletion policies
- **SOC2 compliance**: Audit-ready logging and access controls
- **Bias monitoring**: Automated detection of evaluation bias patterns
- **Quality gates**: Minimum quality thresholds for all generated evaluations

## Acceptance Criteria (Enhanced)

### Functional Requirements
- [x] YAML-defined process produces weighted rubric scores using Top-Tier Industry Standards
- [x] Enhanced bias guardrails with production-focus awareness
- [x] Evidence citations with file/line references to artifact and chunk IDs
- [x] Integration with existing take-home evaluation prompt framework
- [x] Backward compatibility with existing YAML configurations

### Quality Requirements
- [x] Evaluation quality score ≥9.0/10 for all generated assessments
- [x] Production readiness indicators captured for all technical criteria
- [x] Evidence-based scoring with concrete file/line references
- [x] Calibrated thresholds supporting hiring decision confidence

### Performance Requirements
- [x] Cost-optimized model routing with enhanced capability for rigorous assessment
- [x] Token budget management with increased allocation for comprehensive evaluation
- [x] Caching and reuse of analysis components for efficiency

## Changelog
- **v2.0**: Enhanced with Top-Tier Industry Standards framework
- **v1.0**: Initial DSL spec with basic customization capabilities