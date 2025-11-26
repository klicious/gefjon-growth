---
name: generate-interview-kit
description: Generates comprehensive hybrid interview materials (60% BEI + 40% Technical) including scripts, pair programming tasks, and evaluation framework. Use this to prepare for candidate interviews following ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md.
---

# Generate Interview Kit

This skill creates complete hybrid interview materials using the methodology in `ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md`.

## ⚠️ CRITICAL: File Generation Requirements

**YOU MUST CREATE EXACTLY 5 SEPARATE FILES. DO NOT COMBINE THEM.**

Required files:
1. ✅ `interview/candidate_context.md`
2. ✅ `interview/interview_guide.md`
3. ✅ `interview/interview_script.md` ← SEPARATE FILE (NOT part of guide)
4. ✅ `interview/technical_assessment.md` ← SEPARATE FILE (NOT part of guide)
5. ✅ `evaluation/evaluation_framework.md`

**FORBIDDEN:**
- ❌ DO NOT put interview script inside interview_guide.md
- ❌ DO NOT put technical assessment inside interview_guide.md
- ❌ DO NOT combine files - each must be separate

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read `ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md` for hybrid assessment methodology
   - Read `ai_docs/prompts/hiring/generate_interview_kit_prompt_v2.1_hybrid.md` for detailed instructions
   - Read screening and take-home evaluation reports

2. **Load Complete Candidate Context**
   - Read screening report: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/screening/screening_report.md`
   - Read take-home evaluation: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/takehome/takehome_evaluation.md`
   - Map candidate evidence to 10 core values (PROVEN/SUGGESTED/MISSING framework)
   - Identify technical competency gaps from screening dimensions

3. **Generate Candidate Context Document**
   - **Executive Briefing**: Interview prep summary
   - **Core Value Analysis**: PROVEN/SUGGESTED/MISSING for all 10 values
   - **Key Strengths**: Top achievements with evidence
   - **Red Flags**: Concerns requiring clarification
   - **Interview Strategy**: BEI + Technical focus areas
   - Save to: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/candidate_context.md`

4. **Generate Interview Guide**
   Follow Hybrid Assessment Framework (60% BEI + 40% Technical):
   - **BEI Core Values Assessment (40 minutes, 60% weight)**:
     - Systematic STAR format questions for all 10 core values
     - Focus on MISSING values for deep probing
     - Evidence-based scoring framework
   - **Enhanced Technical Assessment (50 minutes, 40% weight)**:
     - AI-assisted development simulation (25 min)
     - Platform engineering scenarios (25 min)
   - **Total Duration**: 90-95 minutes
   - Save to: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/interview_guide.md`

5. **[FILE 3/5] Generate BEI Interview Script - SEPARATE FILE**

   ⚠️ **THIS MUST BE A SEPARATE FILE - NOT INSIDE interview_guide.md**

   Content requirements:
   - **General Behavioral Questions** (NOT task-specific)
   - STAR method framework for each core value
   - Focus on MISSING values with deep probes
   - 10-15 specific questions covering all values
   - **Probing Follow-ups**: Deep-dive questions
   - **Red Flag Clarification**: Direct questions about concerns

   **REQUIRED ACTION:**
   ```
   Execute Write tool:
   file_path: "artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/interview_script.md"
   content: [BEI STAR questions - 30-50 lines]
   ```

   **Verify:** Confirm interview_script.md exists as separate file

6. **[FILE 4/5] Generate Enhanced Technical Assessment - SEPARATE FILE**

   ⚠️ **THIS MUST BE A SEPARATE FILE - NOT INSIDE interview_guide.md**

   Content requirements:

   **AI Collaboration Simulation (25 min, 12.5 points)**:
   - Specific Claude Code/Cursor scenario
   - Agent prompt engineering task
   - Debug workflow with AI assistance
   - Evaluation criteria

   **Platform Engineering Scenarios (25 min, 12.5 points)**:
   - System design for reliability (specific scenario)
   - Observability strategy (specific scenario)
   - Production incident response (specific scenario)
   - Evaluation criteria

   **REQUIRED ACTION:**
   ```
   Execute Write tool:
   file_path: "artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/technical_assessment.md"
   content: [Technical scenarios - 40-60 lines]
   ```

   **Verify:** Confirm technical_assessment.md exists as separate file

7. **[FILE 5/5] Generate Evaluation Framework**

   Content requirements:
   - **BEI Scoring** (50 points, 60%): PROVEN/SUGGESTED/MISSING validation rubric
   - **Technical Scoring** (25 points, 40%): AI collaboration + Platform engineering rubric
   - **Overall Decision Framework**: Weighted scoring with thresholds
   - **Score-to-Decision Mapping**: Clear thresholds

   **REQUIRED ACTION:**
   ```
   Execute Write tool:
   file_path: "artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/evaluation/evaluation_framework.md"
   content: [Evaluation rubric]
   ```

   **Verify:** Confirm evaluation_framework.md exists

8. **MANDATORY VERIFICATION: Check All 5 Files Created**

   Execute verification:
   ```bash
   ls artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/candidate_context.md
   ls artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/interview_guide.md
   ls artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/interview_script.md
   ls artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/technical_assessment.md
   ls artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/evaluation/evaluation_framework.md
   ```

   Report results:
   ```
   ✅ candidate_context.md: EXISTS
   ✅ interview_guide.md: EXISTS (50-150 lines expected)
   ✅ interview_script.md: EXISTS (30-80 lines expected)
   ✅ technical_assessment.md: EXISTS (40-80 lines expected)
   ✅ evaluation_framework.md: EXISTS
   ```

   **If ANY file missing: SKILL EXECUTION FAILED**

9. **Follow Output Format**
   - Match structure from existing interview kits in `20250812_consolidated/`
   - Use consistent naming conventions
   - Ensure all files properly formatted

## Quality Gates

### File Generation (MANDATORY - Must Pass)
- ✅ **candidate_context.md EXISTS** as separate file
- ✅ **interview_guide.md EXISTS** as separate file (50-150 lines)
- ✅ **interview_script.md EXISTS** as separate file (NOT in guide)
- ✅ **technical_assessment.md EXISTS** as separate file (NOT in guide)
- ✅ **evaluation_framework.md EXISTS** as separate file
- ✅ **Total: 5 files created** (4 in interview/, 1 in evaluation/)
- ✅ **No files combined or merged**

### Content Quality
- ✅ All 10 core values mapped (PROVEN/SUGGESTED/MISSING)
- ✅ BEI questions focus on MISSING values
- ✅ Behavioral questions are general (experience-based, not task-specific)
- ✅ Hybrid assessment framework (60% BEI + 40% Technical)
- ✅ Enhanced technical assessment includes AI collaboration + Platform scenarios
- ✅ Complete evaluation rubric with weighted scoring
- ✅ Format matches existing kits in `20250812_consolidated/`
- ✅ All materials consistent with screening + take-home results

## Examples

```bash
# Success scenario
📋 Generating interview kit for atlas_001_dabin_nam
✅ Core values mapped: 2 PROVEN, 4 SUGGESTED, 4 MISSING
✅ Created candidate_context.md
✅ Created interview_guide.md (Hybrid: 40min BEI + 50min Technical)
✅ Created interview_script.md (10 STAR questions, focus on MISSING values)
✅ Created technical_assessment.md (AI collab + Platform scenarios)
✅ Created evaluation_framework.md (60/40 weighted scoring)
✅ Interview kit completed: artifacts/public/hiring/candidates/20250812_consolidated/atlas_001_dabin_nam/interview/
```

## Guidelines

- Always reference `ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md` for methodology
- Use Hybrid Assessment Framework (60% BEI + 40% Technical)
- Map all 10 core values systematically
- Focus BEI questions on MISSING values
- Include AI collaboration + Platform engineering scenarios
- Follow format from existing kits in `20250812_consolidated/`
- Use weighted scoring framework (50 points BEI + 25 points Technical)
