---
name: consolidate-results
description: Consolidates scattered candidate materials into organized directory structure with consistent naming. Use this after generating all interview materials to organize outputs following ai_docs/workflows/hiring/config/workflow_config_ideal.yaml.
---

# Consolidate Results

This skill organizes all generated candidate materials into a clean, consistent directory structure using the configuration defined in `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml`.

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml` for complete directory structure
   - Read `ai_docs/workflows/hiring/tasks/08_post_interview_consolidation.md` for consolidation methodology
   - Understand standardized naming conventions and file organization

2. **Scan Output Directories**
   - Check `artifacts/public/hiring/candidates/` for candidate folders
   - Identify all materials generated for each candidate across all stages
   - List any scattered, misplaced, or duplicated files
   - Verify date format consistency (YYYYMMDD)

3. **Create Standardized Structure**
   For each candidate, ensure directory structure matches `workflow_config_ideal.yaml`:
   ```
   artifacts/public/hiring/candidates/{YYYYMMDD}_consolidated/{candidate_id}_{candidate_name_normalized}/
   ├── candidate_summary.md              # Quick overview (root level)
   ├── screening/
   │   └── screening_report.md           # 4-dimensional assessment
   ├── takehome/
   │   ├── takehome_assignment.md        # Personalized assignment
   │   ├── takehome_evaluation.md        # Evidence-based evaluation
   │   └── agent_evaluation.json         # Machine-readable format (optional)
   ├── interview/
   │   ├── candidate_context.md          # Executive briefing with PROVEN/SUGGESTED/MISSING
   │   ├── interview_guide.md            # Hybrid assessment plan (60% BEI + 40% Technical)
   │   ├── interview_script.md           # BEI STAR questions
   │   └── technical_assessment.md       # AI collaboration + Platform scenarios
   ├── evaluation/
   │   └── evaluation_framework.md       # Weighted scoring rubric
   └── communication/
       └── communication_templates.md    # Email templates
   ```

4. **Validate File Naming Conventions**
   Following `workflow_config_ideal.yaml` file_naming section:
   - `screening/screening_report.md`
   - `takehome/takehome_assignment.md`
   - `takehome/takehome_evaluation.md`
   - `interview/candidate_context.md`
   - `interview/interview_guide.md`
   - `interview/interview_script.md`
   - `interview/technical_assessment.md` (Hybrid framework)
   - `evaluation/evaluation_framework.md`
   - `communication/communication_templates.md`
   - `candidate_summary.md` (root level)

5. **Move and Rename Files**
   - Move any misplaced files to correct subdirectories
   - Rename files to match standard naming convention
   - Merge duplicate files (preserve latest version)
   - Archive old versions if needed (optional)
   - Maintain audit trail of all changes

6. **Generate Candidate Summary**
   Create `candidate_summary.md` at candidate root directory with:
   - **Candidate Overview**: Name, ID, contact, experience level
   - **Current Status**: screening / take-home / interview / evaluation / offer
   - **Screening Score**: Overall score (X.X/10.0) and recommendation
   - **Recommendation**: Strong Hire / Hire / Lean Hire / No Hire
   - **Next Step**: Specific action required
   - **Quick Stats**:
     - PROVEN/SUGGESTED/MISSING values (if interview stage reached)
     - Take-home score (if completed)
   - **Materials Checklist**: Available documents per stage
   - **Focus Areas**: Key assessment priorities

7. **Create Consolidation Log**
   - Document all file moves, renames, and structural changes
   - Record consolidation timestamp and workflow version
   - Log statistics: files moved, directories created, errors
   - Save to: `artifacts/public/hiring/candidates/{date}_consolidated/consolidation_log.json`

8. **Verify Structure Completeness**
   Apply quality assurance from `workflow_config_ideal.yaml`:
   - All required files exist per stage
   - All subdirectories created properly
   - File sizes are non-empty
   - Markdown files properly formatted
   - No scattered or orphaned files

9. **Follow Output Format**
   - Match structure from existing candidates in `20250812_consolidated/`
   - Use consistent date format (YYYYMMDD)
   - Follow naming conventions exactly
   - Preserve metadata and timestamps

## Quality Gates

- ✅ Directory structure matches `workflow_config_ideal.yaml` exactly
- ✅ All file naming conventions followed from `workflow_config_ideal.yaml`
- ✅ All required files exist per workflow stage (screening, takehome, interview, evaluation, communication)
- ✅ Each candidate has `candidate_summary.md` at root level
- ✅ No scattered or misplaced files remaining
- ✅ Consolidation log created with complete audit trail
- ✅ Date format consistent (YYYYMMDD_consolidated)
- ✅ Candidate directory format: `{candidate_id}_{candidate_name_normalized}`
- ✅ All markdown files non-empty and properly formatted

## Examples

```bash
# Success scenario
📋 Consolidating materials for 3 candidates from 20251118_consolidated
✅ atlas_001_dabin_nam: All materials organized (5 stages complete)
✅ phoenix_002_hyungkyu_ahn: All materials organized (5 stages complete)
✅ titan_003_wongyeong_kim: All materials organized (4 stages complete)

📊 Consolidation Statistics:
- Total candidates: 3
- Files moved: 12
- Directories created: 15
- Files renamed: 3
- Errors: 0

✅ Created consolidation_log.json
✅ Consolidation completed successfully
```

```json
// consolidation_log.json
{
  "consolidation_date": "2025-11-18T15:00:00Z",
  "workflow_version": "2.1",
  "total_candidates": 3,
  "operations": [
    {
      "candidate_id": "atlas_001_dabin_nam",
      "actions": [
        "Created candidate_summary.md",
        "Verified screening/screening_report.md exists",
        "Verified takehome/takehome_assignment.md exists",
        "Created interview/ directory structure",
        "Verified evaluation/evaluation_framework.md exists",
        "Created communication/communication_templates.md"
      ],
      "status": "complete"
    }
  ],
  "statistics": {
    "files_moved": 12,
    "directories_created": 15,
    "files_renamed": 3,
    "errors": 0
  },
  "validation": {
    "structure_check": "passed",
    "naming_check": "passed",
    "completeness_check": "passed"
  }
}
```

```markdown
# Candidate Summary: Da Bin Nam (atlas_001)

## Candidate Overview
- **Name**: Da Bin Nam
- **Candidate ID**: atlas_001
- **Email**: dabin@example.com
- **Experience**: 2.5 years
- **Current Role**: Full-Stack Engineer

## Current Status
**Stage**: Interview Ready
**Recommendation**: **HIRE**
**Next Step**: Schedule Hybrid Interview (60% BEI + 40% Technical)

## Screening Results
- **Overall Score**: 8.2/10.0
- **Recommendation**: HIRE (85% confidence)
- **Technical Competency**: 8.5/10.0 (35% weight)
- **Experience Relevance**: 7.8/10.0 (30% weight)
- **Company Culture Fit**: 8.0/10.0 (20% weight)
- **Career Trajectory**: 8.5/10.0 (15% weight)

## Quick Stats
- **PROVEN Values**: 2/10 ✅
- **SUGGESTED Values**: 4/10 🔸
- **MISSING Values**: 4/10 ❌
- **Take-home Score**: 3.9/5.0 (HIRE threshold)

## Materials Available
- ✅ Screening Report (screening/screening_report.md)
- ✅ Take-home Assignment (takehome/takehome_assignment.md)
- ✅ Take-home Evaluation (takehome/takehome_evaluation.md)
- ✅ Interview Kit (interview/candidate_context.md, interview_guide.md, interview_script.md, technical_assessment.md)
- ✅ Evaluation Framework (evaluation/evaluation_framework.md)
- ✅ Communication Templates (communication/communication_templates.md)

## Interview Focus
- **BEI Assessment**: Focus on MISSING values (Observability & Guardrails, Collaboration & Knowledge-Sharing)
- **Technical Assessment**: AI collaboration simulation + Platform engineering scenarios
- **Red Flags**: Validate mathematical aptitude for quantitative systems
- **Strengths**: Leverage ownership mindset and learning agility

---
*Summary generated: 2025-11-18 15:00:00*
*Workflow version: 2.1*
```

## Guidelines

- Always reference `ai_docs/workflows/hiring/config/workflow_config_ideal.yaml` for structure
- Follow directory pattern: `{YYYYMMDD}_consolidated/{candidate_id}_{name_normalized}/`
- Use exact file naming from workflow_config_ideal.yaml
- Create all 5 standard subdirectories: screening, takehome, interview, evaluation, communication
- Generate candidate_summary.md at candidate root level
- Match format from existing candidates in `20250812_consolidated/`
- Maintain audit trail in consolidation_log.json
- Apply quality assurance checks from workflow_config_ideal.yaml
