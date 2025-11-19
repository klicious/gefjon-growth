---
name: generate-interview-kit
description: Generates comprehensive hybrid interview materials (60% BEI + 40% Technical) including scripts, pair programming tasks, and evaluation framework. Use this to prepare for candidate interviews following ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md.
---

# Generate Interview Kit

This skill creates complete hybrid interview materials using the methodology in `ai_docs/workflows/hiring/tasks/06_interview_kit_hybrid.md`.

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

5. **Generate BEI Interview Script**
   - **General Behavioral Questions** (NOT task-specific):
     - STAR method framework for each core value
     - Focus on MISSING values with deep probes
     - Reference candidate's career experience broadly
     - 10-15 questions covering all values
   - **Probing Follow-ups**: Deep-dive questions
   - **Red Flag Clarification**: Direct questions about concerns
   - Save to: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/interview_script.md`

6. **Generate Enhanced Technical Assessment**
   **AI Collaboration Simulation (25 min)**:
   - Claude Code/Cursor scenario
   - Agent prompt engineering
   - Debug workflow with AI assistance

   **Platform Engineering Scenarios (25 min)**:
   - System design for reliability
   - Observability strategy
   - Production incident response

   Save to: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/technical_assessment.md`

7. **Generate Evaluation Framework**
   - **BEI Scoring** (50 points, 60%): PROVEN/SUGGESTED/MISSING validation
   - **Technical Scoring** (25 points, 40%): AI collaboration + Platform engineering
   - **Overall Decision Framework**: Weighted scoring with thresholds
   - Save to: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/interview/evaluation_framework.md`

8. **Follow Output Format**
   - Match structure from existing interview kits in `20250812_consolidated/`
   - Include all required files
   - Use consistent naming conventions

## Quality Gates

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
