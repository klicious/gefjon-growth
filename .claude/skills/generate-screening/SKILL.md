---
name: generate-screening
description: Generates comprehensive AI-powered screening reports using 4-dimensional assessment methodology (Technical/Experience/Culture/Career). Use this to create initial candidate assessments following ai_docs/workflows/hiring/tasks/04_screening.md.
---

# Generate Screening

This skill generates comprehensive screening reports for candidates using the methodology defined in `ai_docs/workflows/hiring/tasks/04_screening.md`.

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read `ai_docs/workflows/hiring/tasks/04_screening.md` for complete screening methodology
   - Read `ai_docs/plans/candidate_screening_plan.md` for detailed assessment criteria
   - Read `context/company_info/mission_vision_values.yaml` for 10 core values
   - Read `context/company_info/hybrid_competency_framework.yaml` for competency framework
   - Read `context/hr_processes/hiring/hiring_stages.yaml` for hiring stages

2. **Load Candidate Data**
   - Read candidate JSON from `data/public/hiring/resume/{date}/candidates_{date}.json`
   - Extract all candidate information (name, experience, skills, projects, etc.)
   - Identify latest date folder if multiple exist

3. **Apply 4-Dimensional Assessment**
   For each candidate, score across 4 dimensions following `ai_docs/workflows/hiring/tasks/04_screening.md`:

   - **Technical Competency (Weight: 35%)**
     - Skills alignment with job requirements
     - Experience depth and breadth
     - Technology stack familiarity
     - Problem-solving capability indicators
     - **Score**: X.X/10.0

   - **Experience Relevance (Weight: 30%)**
     - Industry experience alignment
     - Role progression analysis
     - Project complexity assessment
     - Leadership and mentorship experience
     - **Score**: X.X/10.0

   - **Company Culture Fit (Weight: 20%)**
     - Value alignment indicators (reference 10 core values)
     - Communication style assessment
     - Collaboration and teamwork evidence
     - Growth mindset indicators
     - **Score**: X.X/10.0

   - **Career Trajectory (Weight: 15%)**
     - Professional growth pattern
     - Goal alignment with role
     - Long-term potential assessment
     - Stability and commitment indicators
     - **Score**: X.X/10.0

4. **Calculate Overall Score**
   - Overall Score = (Technical × 0.35) + (Experience × 0.30) + (Culture × 0.20) + (Career × 0.15)
   - Round to 1 decimal place (e.g., 8.2/10.0)
   - Map score to recommendation:
     - **Strong Hire**: 8.5-10.0 (Confidence: 85-95%)
     - **Hire**: 7.0-8.4 (Confidence: 70-85%)
     - **Lean Hire**: 6.0-6.9 (Confidence: 60-70%)
     - **No Hire**: <6.0 (Confidence: <60%)

5. **Generate Screening Report**
   - Follow EXACT format from `artifacts/public/hiring/candidates/20250812_consolidated/{candidate_id}/screening/screening_report.md`
   - Include all required sections:
     - Executive Summary (Overall Score, Recommendation, Confidence, Key Strengths, Areas of Concern)
     - Detailed Analysis (4 dimensions with Evidence-Based Assessment, Strengths, Gaps)
     - Recommendation Rationale
     - Next Steps (Interview Focus Areas, Technical Assessment, Decision Factors)
   - Use evidence-based analysis with specific examples from resume

6. **Create Output Files**
   - Create directory: `artifacts/public/hiring/candidates/{YYMMDD}_consolidated/{candidate_id}_{name_normalized}/`
   - Create subdirectories: `screening/`, `communication/`, `evaluation/`, `interview/`
   - Save `screening/screening_report.md`
   - Save `candidate_summary.md` in candidate root directory
   - Include metadata footer: timestamp, evaluator "AI Screening System v2.0"

7. **Generate Summary Report**
   - Create `HIRING_SUMMARY_COMPLETE.md` in `{date}_consolidated/` directory
   - Include all candidates with scores, recommendations, and key insights
   - Follow format from `artifacts/public/hiring/candidates/20250812_consolidated/HIRING_SUMMARY_COMPLETE.md`

## Quality Gates

- ✅ All 4 screening dimensions scored (Technical, Experience, Culture, Career)
- ✅ Overall score calculated with correct weights (35%, 30%, 20%, 15%)
- ✅ Recommendation category matches score range
- ✅ Confidence level provided and matches recommendation
- ✅ Next step determined (take_home_assignment / senior_level_assessment / additional_assessment / decline)
- ✅ Evidence-based analysis for all dimensions with specific examples
- ✅ Format matches existing reports in `20250812_consolidated/`
- ✅ Directory structure follows `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml`

## Examples

```bash
# Success scenario
📋 Processing 3 candidates from data/public/hiring/resume/20250812/
✅ atlas_001_dabin_nam: 8.2/10.0 - HIRE (85%)
✅ phoenix_002_hyungkyu_ahn: 9.1/10.0 - STRONG HIRE (92%)
✅ titan_003_wongyeong_kim: 8.7/10.0 - STRONG HIRE (88%)

📊 Created screening reports:
- artifacts/public/hiring/candidates/20250812_consolidated/atlas_001_dabin_nam/screening/screening_report.md
- artifacts/public/hiring/candidates/20250812_consolidated/phoenix_002_hyungkyu_ahn/screening/screening_report.md
- artifacts/public/hiring/candidates/20250812_consolidated/titan_003_wongyeong_kim/screening/screening_report.md

📄 Generated summary:
- artifacts/public/hiring/candidates/20250812_consolidated/HIRING_SUMMARY_COMPLETE.md

✅ Screening completed successfully
```

## Guidelines

- Always reference `ai_docs/workflows/hiring/tasks/04_screening.md` for methodology
- Use exact scoring weights: Technical (35%), Experience (30%), Culture (20%), Career (15%)
- Match output format to existing reports in `20250812_consolidated/`
- Provide evidence-based analysis with specific resume examples
- Use professional, objective language
- Follow directory structure from `workflow_config_ideal.yaml`
