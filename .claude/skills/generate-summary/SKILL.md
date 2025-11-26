---
name: generate-summary
description: Generates comprehensive hiring summary reports with statistics, recommendations, and next steps. Use this to create final reports for decision makers following existing format in artifacts/public/hiring/candidates/{date}_consolidated/.
---

# Generate Summary

This skill creates comprehensive summary reports for the entire hiring pipeline run based on consolidated screening results and materials.

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read existing `artifacts/public/hiring/candidates/20250812_consolidated/HIRING_SUMMARY_COMPLETE.md` for format reference
   - Read `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml` for summary generation configuration
   - Read `ai_docs/workflows/hiring/tasks/04_screening.md` for scoring methodology
   - Read `ai_docs/workflows/hiring/tasks/08_post_interview_consolidation.md` for consolidation context

2. **Load All Candidate Data**
   - Read all screening reports from `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/screening/`
   - Read take-home evaluations if available
   - Read interview materials if available
   - Extract key metrics from each candidate

3. **Calculate Statistics**
   Following 4-dimensional screening methodology from ai_docs:

   - **Total Candidates**: Count of all candidates processed
   - **Recommendations Breakdown** (based on screening scores):
     - Strong Hire: ≥8.5/10.0 (count and percentage)
     - Hire: ≥7.0/10.0 (count and percentage)
     - Lean Hire: ≥6.0/10.0 (count and percentage)
     - No Hire: <6.0/10.0 (count and percentage)
   - **Next Steps Distribution**:
     - take_home_assignment: count
     - senior_level_assessment: count
     - additional_assessment: count
     - decline: count
   - **Materials Generated**:
     - Screening reports: count
     - Take-home assignments: count
     - Take-home evaluations: count
     - Interview kits: count
     - Evaluation frameworks: count

4. **Generate Executive Overview**
   - **Pipeline Status**: Total candidates and workflow version
   - **Processing Date**: Current date
   - **Overall Quality**: High-level assessment of candidate pool
   - Concise 2-3 sentence summary of key findings

5. **Create Candidate Summary Table**
   Include for each candidate:
   - Name
   - Codename (candidate_id)
   - Screening Score (X.X/10.0)
   - Recommendation (STRONG HIRE / HIRE / LEAN HIRE / NO HIRE)
   - Key Strengths (2-3 bullet points)
   - Primary Concerns (1-2 items)

6. **Generate Detailed Candidate Analysis**
   For each candidate (prioritized by score):

   - **Overall Score**: X.X/10 | **Confidence**: XX%
   - **Exceptional Strengths**: 3-4 bullet points with evidence
   - **Value Proposition**: 1-2 sentence summary of unique value
   - **Assessment Focus**: Key areas to validate in next steps

7. **Create Hiring Recommendations Section**

   **Immediate Actions**:
   - Prioritized candidate list with timelines
   - Interview scheduling recommendations

   **Interview Focus Areas** (per candidate):
   - Specific technical/behavioral areas to probe
   - Red flags to clarify
   - Growth areas to assess

8. **Add Technical Assessment Results** (if applicable)
   - Take-home assignments distributed
   - Assignment complexity levels
   - Evaluation criteria summary

9. **Include Risk Assessment & Mitigation**

   **Candidate Risks**:
   - Individual risk factors per candidate
   - Mitigation strategies

   **Pipeline Risks**:
   - Competition, timeline, compensation concerns

   **Mitigation Strategies**:
   - Fast-track processes, competitive offers, growth opportunities

10. **Generate Next Steps & Timeline**
    - Week-by-week action plan
    - Interview schedules
    - Decision timeline
    - Offer timeline
    - Target start date

11. **Add Success Metrics**
    - Process Efficiency (time per candidate, quality scores)
    - Candidate Quality (technical competency, domain alignment, cultural fit)
    - Hire rate statistics

12. **Create Recommendations for Leadership**
    - Hiring strategy prioritization
    - Team composition impact
    - Onboarding considerations per candidate

13. **MANDATORY: Generate Output Files**

    **[REQUIRED FILE 1/2] Markdown Report:**

    ⚠️ **THIS FILE IS REQUIRED - NOT OPTIONAL**

    Content requirements:
    - Executive overview with pipeline status
    - Candidate summary table
    - Detailed candidate analysis
    - Hiring recommendations
    - Success metrics
    - Metadata footer

    **REQUIRED ACTION:**
    ```markdown
    Execute Write tool:
    file_path: "artifacts/public/hiring/candidates/{YYYYMMDD}_consolidated/HIRING_SUMMARY_COMPLETE.md"
    content: [Full hiring summary following format from 20250812_consolidated example]
    ```

    **Expected sections:**
    1. Title: "Hiring Summary: {Date} Candidate Pipeline"
    2. Executive Overview
    3. Candidate Summary Table
    4. Detailed Candidate Analysis (with 🏆🚀⭐ emojis)
    5. Hiring Recommendations
    6. Success Metrics
    7. Metadata footer with completion timestamp

    **Verify:** Confirm HIRING_SUMMARY_COMPLETE.md exists in {date}_consolidated/ root

    ---

    **[OPTIONAL FILE 2/2] JSON Summary:**

    Content requirements:
    - Machine-readable format with all statistics
    - Same data as markdown report but in JSON structure

    **RECOMMENDED ACTION:**
    ```json
    Execute Write tool:
    file_path: "artifacts/public/hiring/candidates/{YYYYMMDD}_consolidated/FINAL_WORKFLOW_SUMMARY.json"
    content: {
      "summary_date": "2025-XX-XX",
      "total_candidates": X,
      "recommendations": {...},
      "statistics": {...}
    }
    ```

    **Note:** This file is optional but recommended for automation

14. **Follow Output Format**
    - Match structure from `20250812_consolidated/HIRING_SUMMARY_COMPLETE.md` exactly
    - Use emojis for candidate priority (🏆 top candidate, 🚀 strong candidate, ⭐ solid candidate)
    - Include metadata footer with completion timestamp and quality assurance status
    - Use consistent date format (Month DD, YYYY)

## Quality Gates

### File Generation (MANDATORY)
- ✅ **HIRING_SUMMARY_COMPLETE.md EXISTS** in {date}_consolidated/ root
- ✅ **FINAL_WORKFLOW_SUMMARY.json RECOMMENDED** (optional but encouraged)
- ✅ **File is non-empty** (minimum 50 lines for markdown)

### Content Quality
- ✅ All candidates included in summary with complete data
- ✅ Statistics accurate based on 4-dimensional screening scores
- ✅ Recommendations aligned with scoring thresholds (Strong Hire ≥8.5, Hire ≥7.0, etc.)
- ✅ Executive overview concise and actionable
- ✅ Standout candidates identified with evidence-based rationale
- ✅ Format matches existing HIRING_SUMMARY_COMPLETE.md exactly
- ✅ Timeline and next steps specific and actionable
- ✅ Risk assessment and mitigation strategies included
- ✅ Success metrics calculated and reported
- ✅ Metadata footer with completion timestamp included

## Examples

```bash
# Success scenario
📋 Generating hiring summary for 3 candidates from 20251118_consolidated
✅ Loaded screening data for all 3 candidates
✅ Calculated statistics and distributions
✅ Identified standout candidates: Phoenix (9.1/10), Titan (8.7/10), Atlas (8.2/10)
✅ Generated detailed candidate analysis
✅ Created hiring recommendations and timeline
✅ Calculated success metrics

📊 Summary Statistics:
- Total candidates: 3
- Strong Hire: 2 (67%)
- Hire: 1 (33%)
- Overall quality score: 8.7/10.0

✅ Created HIRING_SUMMARY_COMPLETE.md
✅ Summary generation completed successfully
```

```markdown
# Hiring Summary: November 18, 2025 Candidate Pipeline

## Executive Overview
**Pipeline Status**: 3 candidates processed through complete hiring workflow
**Processing Date**: November 18, 2025
**Workflow Version**: 2.1 (4-Dimensional Assessment)
**Overall Quality**: Exceptional candidate pool with 100% hire-eligible candidates

## Candidate Summary

| Candidate | Codename | Screening Score | Recommendation | Key Strengths | Primary Concerns |
|-----------|----------|----------------|----------------|---------------|------------------|
| Hyungkyu Ahn | Phoenix | 9.1/10 | **STRONG HIRE** | Financial systems expertise, performance optimization | AI/ML experience gap, team collaboration depth |
| Wongyeong Kim | Titan | 8.7/10 | **STRONG HIRE** | Data engineering excellence, AI/ML foundation | Financial domain experience, mathematical depth |
| Da Bin Nam | Atlas | 8.2/10 | **HIRE** | Full-stack expertise, learning agility, ownership | AI/ML experience gap, mathematical aptitude |

## Detailed Candidate Analysis

### 🏆 Phoenix (Hyungkyu Ahn) - STRONG HIRE
**Overall Score**: 9.1/10 | **Confidence**: 92%

**Exceptional Strengths**:
- Perfect domain fit with capital markets experience
- 2x throughput improvement through ZeroMQ optimization
- Mathematical foundation with Investment Manager certification
- Systems programming and distributed architecture expertise

**Value Proposition**: Rare combination of deep technical systems programming, direct financial domain experience, and proven performance optimization capabilities.

**Assessment Focus**: AI/ML learning potential, team collaboration depth, mentoring interest

### 🚀 Titan (Wongyeong Kim) - STRONG HIRE
**Overall Score**: 8.7/10 | **Confidence**: 88%

**Exceptional Strengths**:
- 35% runtime reduction in Airflow pipeline optimization
- 87% accuracy improvement through LLM integration
- Systematic optimization approach with quantifiable results
- Security/privacy expertise valuable for compliance

**Value Proposition**: Strong data engineering and AI/ML foundations with practical optimization experience, ideal for platform data infrastructure.

**Assessment Focus**: Mathematical aptitude for quantitative systems, financial domain learning interest

## Hiring Recommendations

### Immediate Actions
1. **Phoenix**: Priority candidate - schedule final interview immediately
2. **Titan**: Strong candidate - schedule final interview within 48 hours
3. **Atlas**: Solid candidate - schedule final interview within week

## Success Metrics

### Process Efficiency
- **Total Processing Time**: 6 hours for 3 candidates (2 hours per candidate)
- **Quality Score Average**: 8.7/10.0 across all candidates
- **Hire Rate**: 100% (3/3 candidates recommended for hire)
- **Strong Hire Rate**: 67% (2/3 candidates strong hire recommendation)

---
**Workflow Completion**: November 18, 2025, 8:00 PM KST
**Quality Assurance**: All materials reviewed and validated
**Approval Status**: Ready for Platform Lead review and final interviews
```

## Guidelines

- Always reference `artifacts/public/hiring/candidates/20250812_consolidated/HIRING_SUMMARY_COMPLETE.md` for format
- Use 4-dimensional screening scores as basis for all statistics and recommendations
- Apply scoring thresholds: Strong Hire ≥8.5, Hire ≥7.0, Lean Hire ≥6.0, No Hire <6.0
- Include all required sections from reference format
- Use emojis for candidate priority visualization (🏆🚀⭐)
- Date format: Month DD, YYYY (e.g., "November 18, 2025")
- Include metadata footer with completion timestamp and approval status
- Provide actionable, specific next steps and timelines
