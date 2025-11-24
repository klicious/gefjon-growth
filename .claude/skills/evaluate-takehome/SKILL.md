---
name: evaluate-takehome
description: Evaluates submitted take-home assignments with evidence-based rubric scoring. Use this after candidates submit their work to generate comprehensive assessments following ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md.
---

# Evaluate Take-home Assignment

This skill evaluates candidate take-home submissions using the evidence-required methodology in `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md`.

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md` for complete evaluation methodology
   - Read `ai_docs/prompts/hiring/evaluate_take_home_assignment_prompt.md` for evaluation framework
   - Read original assignment to understand evaluation criteria

2. **Load Assignment Context**
   - Read original assignment from `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/takehome/takehome_assignment.md`
   - Load evaluation rubric and criteria
   - Review target gaps from screening
   - Get candidate GitHub repository URL

3. **Collect Repository Information**
   - Identify default branch and recent commit SHA (short)
   - Gather repository structure (key directories and files)
   - Read README/setup instructions for reproducibility
   - Document GitHub URLs for evidence linking

4. **Analyze Submission with Evidence**
   For each analysis, collect evidence as: `file_path:lineStart-lineEnd @ commitShortSHA`

   - **Architecture**: modules, layering, separation of concerns
   - **Correctness**: tests, CI configs, edge case handling
   - **Security**: secrets, input validation, error handling, licenses
   - **Observability**: logging, metrics, health endpoints, timeouts/retries
   - **Code Quality**: naming, organization, best practices
   - **Documentation**: README, API docs, architecture decisions

5. **Score Against Rubric (1-10 scale, 0.5 granularity)**

   Following `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md`:

   - **Functional Correctness & Completeness (25%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

   - **Code Quality & Best Practices (20%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

   - **Testing Approach & Coverage (15%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

   - **Documentation Quality (10%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

   - **Going Above and Beyond / Ownership (15%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

   - **Scalability & Design Patterns (15%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

   - **Quantitative & Logical Problem Solving (10%)**
     - Score: X/10
     - Evidence: file_path:lines @ SHA
     - Summary: 1-2 sentences explaining score

6. **Calculate Overall Score**
   - Convert 10-point scores to weighted 5-point scale
   - Apply executive decision thresholds:
     - **Strong Hire**: ≥ 4.5
     - **Hire**: ≥ 3.8
     - **Lean Hire**: ≥ 3.0
     - **No Hire**: < 3.0

7. **Complete Quality Checklists**
   - Security & Compliance checklist
   - Observability assessment checklist
   - Reproducibility validation

8. **Generate Evaluation Report**
   - Follow format from existing evaluations in `20250812_consolidated/`
   - Include all evidence with GitHub URLs
   - Provide constructive feedback
   - Make clear recommendation

9. **Create Output Files**
   - Save to: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/takehome/takehome_evaluation.md`
   - Optional: `agent_evaluation.json` for machine-readable format
   - Update candidate status tracking

## Quality Gates

- ✅ Evidence included for every criterion (file_path:lines @ SHA)
- ✅ All rubric dimensions scored (7 criteria)
- ✅ Specific code examples cited with GitHub URLs
- ✅ Security & Compliance checklist completed
- ✅ Observability assessment completed
- ✅ Reproducibility validated
- ✅ Clear recommendation with threshold justification
- ✅ Format matches existing evaluations in `20250812_consolidated/`

## Examples

```bash
# Success scenario
📋 Evaluating take-home for atlas_001_dabin_nam
✅ Repository cloned: https://github.com/namdragonkiller/observability-exercise
✅ Analyzed commit: a1b2c3d (main branch)
📊 Scores:
   - Functional Correctness: 8.5/10 (85%)
   - Code Quality: 7.0/10 (70%)
   - Testing: 6.5/10 (65%)
   - Documentation: 7.5/10 (75%)
   - Ownership: 8.0/10 (80%)
   - Scalability: 7.5/10 (75%)
   - Problem Solving: 8.0/10 (80%)
✅ Overall Score: 3.9/5.0 - HIRE
✅ Created evaluation: artifacts/public/hiring/candidates/20250812_consolidated/atlas_001_dabin_nam/takehome/takehome_evaluation.md
✅ Evaluation completed successfully
```

## Guidelines

- Always reference `ai_docs/workflows/hiring/tasks/05b_takehome_evaluation.md` for methodology
- Provide evidence for EVERY score (file_path:lines @ SHA)
- Include GitHub URLs for all referenced code
- Use neutral, evidence-based language
- Follow format from existing evaluations in `20250812_consolidated/`
- Complete all mandatory checklists
- Apply correct decision thresholds
