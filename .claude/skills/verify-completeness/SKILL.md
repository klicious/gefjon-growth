---
name: verify-completeness
description: Verifies that all required materials exist for each candidate based on their status and next steps. Use this to ensure quality and completeness before making hiring decisions following ai_docs/workflows/hiring/config/workflow_config_ideal.yaml.
---

# Verify Completeness

This skill performs comprehensive quality checks on all generated hiring materials using the quality assurance framework defined in `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml`.

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml` for required files and quality assurance rules
   - Read `ai_docs/workflows/hiring/tasks/04_screening.md` for screening validation criteria
   - Read `ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md` for interview materials requirements
   - Read `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md` for take-home evaluation criteria

2. **Load Candidate Status Data**
   - Read all screening reports from `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/screening/`
   - Extract next_step from each screening report
   - Identify candidate progression stage (screening / take-home / interview / evaluation)
   - Determine required files based on workflow stage and next_step

3. **Define Required Materials by Stage**

   Following `workflow_config_ideal.yaml` stages configuration:

   **Stage 1 - Screening (All Candidates):**
   - `screening/screening_report.md`
   - Content must include: Overall Score, Recommendation, Confidence, Next Step
   - 4-dimensional assessment: Technical (35%), Experience (30%), Culture (20%), Career (15%)

   **Stage 2 - Take-home (next_step = take_home_assignment):**
   - `screening/screening_report.md`
   - `takehome/takehome_assignment.md`
   - Optional: `takehome/takehome_evaluation.md` (if completed)
   - Optional: `takehome/agent_evaluation.json` (machine-readable format)

   **Stage 3 - Interview (next_step = take_home_assignment, senior_level_assessment, additional_assessment):**
   - All Stage 2 files
   - `interview/candidate_context.md` (PROVEN/SUGGESTED/MISSING analysis)
   - `interview/interview_guide.md` (Hybrid: 60% BEI + 40% Technical)
   - `interview/interview_script.md` (BEI STAR questions)
   - `interview/technical_assessment.md` (AI collaboration + Platform scenarios)

   **Stage 4 - Evaluation (All interview candidates):**
   - All Stage 3 files
   - `evaluation/evaluation_framework.md` (Weighted scoring rubric)

   **Stage 5 - Communication (All Candidates):**
   - All relevant stage files
   - `communication/communication_templates.md` (Email templates)

   **Root Level (All Candidates):**
   - `candidate_summary.md` (Quick overview at root)

4. **Verify File Existence**
   - Check each required file exists at expected path
   - Verify files are non-empty (> 100 bytes minimum)
   - Ensure all markdown files are valid UTF-8
   - Check directory structure matches `workflow_config_ideal.yaml`

5. **Validate File Content Quality**

   **Screening Reports** (`screening/screening_report.md`):
   - Must contain Overall Score (X.X/10.0)
   - Must have clear Recommendation (Strong Hire / Hire / Lean Hire / No Hire)
   - Must include Confidence Level (XX%)
   - Must specify Next Step (take_home_assignment / senior_level_assessment / additional_assessment / decline)
   - Must have 4-dimensional scores matching weights

   **Interview Materials** (`interview/` directory):
   - `candidate_context.md`: Must include PROVEN/SUGGESTED/MISSING analysis for all 10 core values
   - `interview_guide.md`: Must specify Hybrid assessment (60% BEI + 40% Technical)
   - `interview_script.md`: Must use STAR method, focus on MISSING values
   - `technical_assessment.md`: Must include AI collaboration + Platform engineering scenarios

   **Take-home Evaluation** (`takehome/takehome_evaluation.md`):
   - Must include evidence format: `file_path:lines @ SHA`
   - Must have 7-criterion rubric scores (1-10 scale)
   - Must include Overall Score (X.X/5.0) and decision threshold

   **Evaluation Framework** (`evaluation/evaluation_framework.md`):
   - Must include weighted scoring breakdown
   - Must have clear decision thresholds

6. **Check Consistency**
   - Verify screening recommendation aligns with next_step:
     - Strong Hire (≥8.5) → take_home_assignment or senior_level_assessment
     - Hire (≥7.0) → take_home_assignment
     - Lean Hire (≥6.0) → additional_assessment
     - No Hire (<6.0) → decline
   - Ensure interview materials reference screening gaps
   - Validate BEI questions target MISSING values from candidate_context.md
   - Check file naming matches `workflow_config_ideal.yaml` conventions

7. **Generate Verification Report**
   - List all candidates checked with status
   - Report missing or invalid files per candidate
   - Identify content validation errors
   - Document consistency check failures
   - Calculate completeness percentage per candidate
   - Provide actionable error messages with file paths

8. **Save Verification Results**
   - Create: `artifacts/public/hiring/candidates/{YYYYMMDD}_consolidated/verification_report.json`
   - Include detailed findings for each candidate
   - Mark overall status: PASS / FAIL
   - Include summary statistics
   - Timestamp all checks

9. **Follow Quality Assurance Rules**
   From `workflow_config_ideal.yaml` quality_assurance section:
   - `verify_all_files_generated`: true
   - `verify_directory_structure`: true
   - `verify_file_content_completeness`: true
   - `generate_completion_report`: true

## Quality Gates

- ✅ All required files exist per workflow stage from `workflow_config_ideal.yaml`
- ✅ Directory structure matches `workflow_config_ideal.yaml` exactly
- ✅ All files are non-empty and valid UTF-8 markdown
- ✅ Content validation passes for all critical fields (scores, recommendations, next_step)
- ✅ Screening recommendations align with next_step thresholds
- ✅ Interview materials reference screening gaps appropriately
- ✅ BEI questions target MISSING values from candidate_context.md
- ✅ File naming follows `workflow_config_ideal.yaml` conventions
- ✅ 100% completeness for all candidates at their current stage
- ✅ Verification report generated with detailed findings

## Examples

```bash
# Success scenario
🔍 Verifying completeness for 3 candidates from 20251118_consolidated...

✅ phoenix_001_hyungkyu_ahn - 100% complete (Stage 1: Screening)
   - screening/screening_report.md ✓
   - candidate_summary.md ✓
   - Next step: take_home_assignment ✓

✅ phoenix_002_wongyeong_kim - 100% complete (Stage 3: Interview)
   - screening/screening_report.md ✓
   - takehome/takehome_assignment.md ✓
   - takehome/takehome_evaluation.md ✓
   - interview/candidate_context.md ✓
   - interview/interview_guide.md ✓
   - interview/interview_script.md ✓
   - interview/technical_assessment.md ✓
   - evaluation/evaluation_framework.md ✓
   - communication/communication_templates.md ✓
   - candidate_summary.md ✓

✅ phoenix_003_dabin_nam - 100% complete (Stage 2: Take-home)
   - screening/screening_report.md ✓
   - takehome/takehome_assignment.md ✓
   - candidate_summary.md ✓

📊 Verification Summary:
   ✅ Passed: 3/3 candidates (100%)
   ❌ Failed: 0/3 candidates
   📈 Overall Completeness: 100%

✅ VERIFICATION PASSED - All materials complete and valid
✅ Created verification_report.json
```

```json
// verification_report.json
{
  "verification_date": "2025-11-18T16:00:00Z",
  "workflow_version": "2.1",
  "total_candidates": 3,
  "verification_results": [
    {
      "candidate_id": "phoenix_001_hyungkyu_ahn",
      "candidate_name": "Hyungkyu Ahn",
      "status": "PASS",
      "current_stage": "screening",
      "completeness": "100%",
      "required_files": 2,
      "found_files": 2,
      "missing_files": [],
      "validation_checks": {
        "screening_score_format": "PASS (9.1/10.0)",
        "recommendation_present": "PASS (STRONG HIRE)",
        "confidence_present": "PASS (92%)",
        "next_step_present": "PASS (take_home_assignment)",
        "4d_scores_present": "PASS"
      },
      "consistency_checks": {
        "recommendation_matches_next_step": true,
        "score_matches_recommendation": true
      }
    },
    {
      "candidate_id": "phoenix_002_wongyeong_kim",
      "candidate_name": "Wongyeong Kim",
      "status": "PASS",
      "current_stage": "interview",
      "completeness": "100%",
      "required_files": 10,
      "found_files": 10,
      "missing_files": [],
      "validation_checks": {
        "screening_score_format": "PASS (8.7/10.0)",
        "interview_hybrid_structure": "PASS (60% BEI + 40% Technical)",
        "proven_suggested_missing": "PASS",
        "bei_star_method": "PASS",
        "technical_assessment_scenarios": "PASS"
      },
      "consistency_checks": {
        "recommendation_matches_next_step": true,
        "bei_targets_missing_values": true,
        "interview_references_gaps": true
      }
    }
  ],
  "summary": {
    "passed": 3,
    "failed": 0,
    "overall_completeness": "100%",
    "total_missing_files": 0,
    "total_validation_errors": 0
  },
  "overall_status": "PASS"
}
```

## Guidelines

- Always reference `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml` for required files
- Validate files based on candidate's current workflow stage
- Check content quality, not just file existence
- Verify consistency between related documents (screening → interview materials)
- Use exact file naming from workflow_config_ideal.yaml
- Apply scoring thresholds from screening methodology (Strong Hire ≥8.5, Hire ≥7.0, etc.)
- Generate actionable error messages with file paths
- Include detailed validation results in verification_report.json
- Mark overall status as PASS only if ALL candidates pass their stage requirements
