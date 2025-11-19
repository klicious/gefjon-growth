---
name: hiring-pipeline-orchestrator
description: Orchestrates the complete hiring workflow from candidate data validation through final summary generation. Use this to run the entire hiring pipeline end-to-end.
---

# Hiring Pipeline Orchestrator

This skill coordinates the entire hiring workflow by executing individual skills in the correct sequence.

## Overview

The hiring pipeline automates candidate evaluation from resume screening through interview kit generation using AI-powered analysis aligned with company core values and competencies.

## Workflow Stages

```
1. validate-context          → Prerequisite check
2. process-candidates        → Data normalization
3. generate-screening        → AI screening generation
4. generate-takehome        → AI takehome assignment (conditional)
5. evaluate-takehome        → AI takehome evaluation (if submitted)
6. generate-interview-kit   → AI interview materials
7. execute-postprocessing   → Python script execution & formatting
8. consolidate-results      → File organization
9. verify-completeness      → Quality check
10. generate-summary        → Final reporting
```

## Instructions

### Phase 1: Setup and Validation

1. **Invoke: validate-context**
   - Verify all context files exist and are valid
   - Check company values, competencies, hiring stages
   - Confirm prompt templates available
   - **Exit on Failure**: Cannot proceed without valid context

### Phase 2: Data Processing

2. **Invoke: process-candidates**
   - Load candidate JSON files from `data/public/hiring/resume/`
   - Validate data structure and required fields
   - Normalize candidate data
   - Create processing log
   - **Output**: Normalized candidate data ready for screening

### Phase 3: AI Screening

3. **Invoke: generate-screening**
   - For each candidate, generate screening report
   - Analyze against 10 core values
   - Perform PROVEN/SUGGESTED/MISSING gap analysis
   - Determine recommendation (Strong Hire / Hire / Lean Hire / No Hire)
   - Assign next_step (take_home_assignment / senior_level_assessment / additional_assessment / decline)
   - **Output**: Screening reports with recommendations

### Phase 4: Take-home Assignment (Conditional)

4. **Conditional Invoke: generate-takehome**
   - **Condition**: Only for candidates with next_step = take_home_assignment OR senior_level_assessment
   - Generate personalized take-home assignments
   - Target identified value gaps
   - Include evaluation rubric
   - **Output**: Take-home assignments

5. **Conditional Invoke: evaluate-takehome**
   - **Condition**: Only if candidate submitted take-home work
   - **Manual Step**: Developer loads submission into designated folder
   - Evaluate submission against rubric
   - Score using Top-Tier Industry Standards
   - Update value gap assessment
   - **Output**: Take-home evaluation reports

### Phase 5: Interview Kit Generation

6. **Invoke: generate-interview-kit**
   - For candidates proceeding to interview:
   - Generate candidate context document
   - Create interview guide with time allocation
   - Generate BEI script targeting MISSING values
   - Create custom pair programming task
   - Generate skeleton project (for senior candidates)
   - Create evaluation framework
   - **Output**: Complete interview materials

### Phase 6: Post-processing

7. **Invoke: execute-postprocessing**
   - Run Python scripts to format and organize AI outputs
   - Execute `consolidate_hiring_results.py` to organize files
   - Execute `generate_enhanced_materials.py` for additional materials
   - Transform raw outputs into final structured formats
   - **Output**: Properly formatted and organized artifacts

### Phase 7: Consolidation and Verification

8. **Invoke: consolidate-results**
   - Organize all materials into standardized directory structure
   - Move scattered files to correct locations
   - Generate candidate summaries
   - Create consolidation log
   - **Output**: Organized candidate directories

9. **Invoke: verify-completeness**
   - Check all required files exist for each candidate
   - Validate file content and consistency
   - Generate verification report
   - Calculate completeness percentage
   - **Output**: Verification report with quality metrics

### Phase 8: Final Reporting

10. **Invoke: generate-summary**
   - Aggregate all candidate data
   - Calculate statistics and distributions
   - Identify standout candidates
   - Create executive summary
   - Generate actionable recommendations
   - **Output**: Comprehensive hiring summary (markdown + JSON)

## Manual Intervention Points

The following steps require human intervention:

1. **After generate-takehome**: Developer sends assignment to candidates
2. **Before evaluate-takehome**: Developer loads candidate submissions
3. **After generate-interview-kit**: HR schedules interviews
4. **After generate-summary**: Hiring manager reviews and makes decisions

## Quality Gates

The pipeline enforces these quality checkpoints:

- ✅ **After validate-context**: All context files valid
- ✅ **After process-candidates**: All candidate data normalized
- ✅ **After generate-screening**: All candidates have recommendations
- ✅ **After generate-interview-kit**: Interview materials complete
- ✅ **After execute-postprocessing**: All outputs properly formatted
- ✅ **After verify-completeness**: 100% completeness for production candidates
- ✅ **After generate-summary**: Summary report generated

## Error Handling

- **Validation Errors**: Stop pipeline, report missing files
- **Processing Errors**: Skip invalid candidates, continue with valid ones
- **Generation Errors**: Retry once, then mark candidate for manual review
- **Verification Failures**: Report incomplete candidates, do not block summary

## Execution

To run the complete pipeline:

1. Ensure candidate JSON files are in `data/public/hiring/resume/`
2. Invoke this orchestrator skill
3. Monitor progress through console output
4. Review verification report for quality issues
5. Read final summary in `artifacts/public/hiring/candidates/{date}_consolidated/HIRING_SUMMARY_COMPLETE.md`

## Output Structure

Final output directory structure:
```
artifacts/public/hiring/candidates/{date}_consolidated/
├── HIRING_SUMMARY_COMPLETE.md          # Executive summary
├── FINAL_WORKFLOW_SUMMARY.json         # Machine-readable summary
├── consolidation_log.json              # File operations log
├── verification_report.json            # Quality check results
└── {candidate_id}/
    ├── candidate_summary.md
    ├── screening/screening_report.md
    ├── takehome/ (if applicable)
    ├── interview/
    ├── pair_programming/ (if applicable)
    ├── evaluation/
    └── communication/
```

## Success Criteria

The pipeline is successful when:

- All candidates processed (or failures documented)
- Verification completeness ≥ 95%
- Summary reports generated
- Standout candidates identified
- Next steps clearly defined

## Examples

```bash
# Successful execution
🚀 Starting Hiring Pipeline Orchestrator
===========================================

✅ Phase 1: Setup and Validation
   validate-context: All context files valid

✅ Phase 2: Data Processing
   process-candidates: 13 candidates normalized

✅ Phase 3: AI Screening
   generate-screening: 13 screening reports created
   - Strong Hire: 3
   - Hire: 5
   - Lean Hire: 3
   - No Hire: 2

✅ Phase 4: Take-home Assignment
   generate-takehome: 8 assignments created
   evaluate-takehome: 5 evaluations completed

✅ Phase 5: Interview Kit Generation
   generate-interview-kit: 8 interview kits created

✅ Phase 6: Post-processing
   execute-postprocessing: Python scripts executed successfully

✅ Phase 7: Consolidation and Verification
   consolidate-results: All materials organized
   verify-completeness: 97.4% complete (12/13 passed)

✅ Phase 8: Final Reporting
   generate-summary: Summary report created

🎉 HIRING PIPELINE SUCCESSFUL!
📊 Results: artifacts/public/hiring/candidates/20250811_consolidated/
```
