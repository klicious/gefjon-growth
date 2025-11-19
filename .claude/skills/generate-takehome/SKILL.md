---
name: generate-takehome
description: Generates personalized take-home assignments based on candidate screening results and technical level. Use this after screening to create tailored technical assessments following ai_docs/workflows/hiring/tasks/05_takehome_assignment.md.
---

# Generate Take-home Assignment

This skill creates customized take-home assignments following the methodology in `ai_docs/workflows/hiring/tasks/05_takehome_assignment.md`.

## Instructions

1. **Read Reference Documents**
   - **PRIMARY**: Read `ai_docs/workflows/hiring/tasks/05_takehome_assignment.md` for complete assignment methodology
   - Read `ai_docs/prompts/hiring/takehome_evaluation_prompt.md` for evaluation framework
   - Read screening reports to understand candidate profile and gaps

2. **Load Candidate Context**
   - Read screening report from `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/screening/`
   - Extract Overall Score, Recommendation, and dimension scores
   - Identify candidate's experience level and technical competencies
   - Review areas of concern from screening (gaps to assess)

3. **Select Assignment Template**
   Based on experience level from screening (ai_docs/workflows/hiring/tasks/05_takehome_assignment.md):
   - **Entry Level (0-2 years)**: Basic CRUD application with testing
   - **Mid Level (2-5 years)**: System design with scalability considerations
   - **Senior Level (5+ years)**: Complex architecture with multiple integration points
   - **Staff Level (8+ years)**: Platform design with team leadership scenarios

   Based on specialization:
   - **Backend Focus**: API design, database optimization, system architecture
   - **Full-Stack**: End-to-end application with frontend and backend
   - **DevOps/Infrastructure**: CI/CD, monitoring, infrastructure as code
   - **Performance**: High-throughput systems, optimization, monitoring

   Based on domain:
   - **Fintech**: Trading platform, compliance, audit trails, security
   - **Real-Time Systems**: WebSocket, event-driven architecture, low latency
   - **Data Processing**: ETL pipelines, batch processing, data quality
   - **Microservices**: Service mesh, distributed systems, observability

4. **Customize Assignment**
   - **Problem Statement**: Personalized to candidate's background and experience
   - **Gap Targeting**: Design to specifically assess areas of concern from screening
   - **Technical Requirements**: Include familiar technologies + stretch goals
   - **Deliverables**: Code, tests, documentation, deployment instructions
   - **Time Allocation**: 4-6 hours (72 hours deadline)

5. **Generate Evaluation Framework**
   Create detailed rubrics aligned with company values:
   - Technical implementation quality
   - Code quality and architecture
   - Testing and documentation
   - Production readiness (security, monitoring, error handling)
   - Define success criteria and decision thresholds

6. **Create Output Files**
   - Create directory: `artifacts/public/hiring/candidates/{date}_consolidated/{candidate_id}/takehome/`
   - Save `takehome_assignment.md` with personalized assignment
   - Save `takehome_evaluation.md` with evaluation framework and rubric
   - Follow format from existing assignments in `20250812_consolidated/`

7. **GitHub Collaboration Setup**
   - Generate repository requirements and structure
   - Create collaboration instructions for evaluator access
   - Define submission guidelines and deliverable requirements

## Quality Gates

- ✅ Assignment difficulty matches candidate's experience level
- ✅ Tasks specifically target areas of concern from screening
- ✅ Clear deliverables and success criteria defined
- ✅ Realistic time estimate provided (4-6 hours)
- ✅ Evaluation rubric aligned with company values
- ✅ Format matches existing assignments in `20250812_consolidated/`
- ✅ GitHub collaboration setup included

## Examples

```bash
# Success scenario
📋 Generating take-home for atlas_001_dabin_nam (Experience: 2.75 years, Level: Mid)
✅ Selected template: Mid-Level Backend with Observability Focus
✅ Targeting gaps: Observability & Guardrails, Security practices
✅ Created assignment: artifacts/public/hiring/candidates/20250812_consolidated/atlas_001_dabin_nam/takehome/takehome_assignment.md
✅ Created evaluation: artifacts/public/hiring/candidates/20250812_consolidated/atlas_001_dabin_nam/takehome/takehome_evaluation.md
✅ Take-home assignment generated successfully
```

## Guidelines

- Always reference `ai_docs/workflows/hiring/tasks/05_takehome_assignment.md` for methodology
- Personalize assignment to candidate's specific background
- Target identified gaps from screening report
- Use appropriate complexity based on experience level
- Follow format from existing assignments in `20250812_consolidated/`
- Include comprehensive evaluation criteria
- Ensure production-readiness focus (security, monitoring, testing)
