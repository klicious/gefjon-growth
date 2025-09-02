---
id: io_samples_sharable_2025-08-21
type: io_samples
domain: aws_bedrock_agents
created_date: 2025-08-21
last_updated: 2025-08-21
author: Junie
quality_score: __TBD__
tags: ["AWS", "Bedrock", "IO", "hiring", "sharable_with_AWS"]
visibility: public
version: 1.0
---
# Sharable Input/Output Samples for AWS Consultation

Note: These examples are intentionally redacted. They show schemas and representative values only. No proprietary prompts, detailed context‑engineering logic, or confidential business rules are included.

---

## Canonical Batch Input (Candidates JSON)
- Entry point to the automated workflow.
- Minimal fields; PII either omitted or represented as placeholders.

```json
{
  "run_id": "demo_2025-08-21",
  "role": "Backend Engineer",
  "candidates": [
    {
      "candidate_id": "cand_001",
      "display_name": "Candidate A",
      "resume_url": "s3://redacted/resumes/cand_001.pdf",
      "years_experience": 5,
      "skills": ["Python", "AWS", "PostgreSQL"]
    },
    {
      "candidate_id": "cand_002",
      "display_name": "Candidate B",
      "resume_url": "s3://redacted/resumes/cand_002.pdf",
      "years_experience": 4,
      "skills": ["Java", "Docker", "OpenSearch"]
    }
  ]
}
```

---

## Stage 2 Output: Screening Report (Redacted Minimal)

```json
{
  "candidate_id": "cand_001",
  "stage": "screening",
  "recommendation": "PASS",
  "confidence": "HIGH",
  "top_strengths": [
    "Backend depth",
    "AWS exposure"
  ],
  "concerns": [],
  "core_values_alignment": {
    "Ownership": 4,
    "Security": 4,
    "Excellence": 4
  },
  "evidence_refs": [
    "repo/path:12-34@abcdef1 — resume keyword evidence",
    "repo/path:40-55@abcdef1 — project match evidence"
  ]
}
```

---

## Stage 3 Follow‑On Input: Take‑Home Assessment Repositories

```json
{
  "candidate_id": "cand_001",
  "assignment_repo_url": "https://github.com/candidate/redacted-repo",
  "branch": "main"
}
```

---

## Stage 3 Output: Take‑Home Assignment Package (Sharable)

```json
{
  "candidate_id": "cand_001",
  "stage": "takehome_assignment",
  "assignment_id": "th_2025_001",
  "brief_uri": "s3://redacted/assignments/th_2025_001/brief.md",
  "repo_template_uri": "s3://redacted/assignments/th_2025_001/template.zip",
  "due_date": "2025-08-28T23:59:00Z",
  "rubric_outline": {
    "functional_correctness": 0.25,
    "code_quality": 0.20,
    "testing": 0.15,
    "documentation": 0.10,
    "ownership_beyond_basics": 0.15,
    "scalability_design": 0.15
  },
  "support_links": [
    "s3://redacted/assignments/th_2025_001/faq.md"
  ]
}
```

---

## Stage 3 Output: Take‑Home Evaluation Summary (Redacted)

```json
{
  "candidate_id": "cand_001",
  "stage": "takehome_evaluation",
  "scores": {
    "functional_correctness": 4.0,
    "code_quality": 3.5,
    "testing": 3.0,
    "documentation": 3.0,
    "observability": 2.5
  },
  "weighted_total": 3.6,
  "summary": "Meets bar on functionality; improve tests and logging.",
  "artifacts": [
    {
      "type": "report",
      "uri": "s3://redacted/artifacts/cand_001/takehome/report.pdf"
    }
  ]
}
```

---

## Stage 4 Follow‑On Input: Live Coding & Interview Notes

```json
{
  "candidate_id": "cand_001",
  "live_coding_repo_url": "https://github.com/candidate/redacted-live",
  "interview_notes_url": "s3://redacted/interviews/cand_001/notes.md"
}
```

---

## Stage 4 Output: Interview Kit Outline (Redacted Content)

```markdown
# Interview Kit (Outline)
- Role: Backend Engineer
- Sections:
  - Behavioral (values alignment) — redacted prompts
  - Technical deep‑dive — redacted prompts
  - System design — redacted prompts
- Evaluation rubric: standardized weights (omitted)
```

---

## Stage 5 Output: Final Evaluation (Consolidated)

```json
{
  "candidate_id": "cand_001",
  "stage": "final_evaluation",
  "overall_recommendation": "Hire",
  "justification_summary": "Strong backend fit; moderate testing gaps acceptable with mentorship.",
  "risk_flags": [],
  "human_decision": {
    "approved": true,
    "approved_by": "Hiring Manager",
    "timestamp": "2025-08-21T10:30:00Z"
  }
}
```

---

## Stage 3 Addendum: Take-Home Assessment Brief (Sample)

This shows the structure of the assessment instructions provided to a candidate.

```markdown
# Backend Engineer Take-Home Assessment

**Objective:** Design and implement a simplified, scalable RESTful API service.

**Scenario:**
You are building a core service for a new product. This service will manage a specific resource (e.g., "widgets"). The service must handle standard CRUD operations and include basic validation.

**Requirements:**
1.  **API Endpoints:**
    *   `POST /widgets`: Create a new widget.
    *   `GET /widgets/{widgetId}`: Retrieve a single widget.
    *   `GET /widgets`: List all widgets with pagination.
    *   `PUT /widgets/{widgetId}`: Update a widget.
    *   `DELETE /widgets/{widgetId}`: Delete a widget.
2.  **Data Model (Widget):**
    *   `widgetId` (string, UUID)
    *   `name` (string, required)
    *   `description` (string)
    *   `createdAt` (timestamp)
    *   `updatedAt` (timestamp)
3.  **Technical Stack:**
    *   Language: Python 3.9+ or Go.
    *   Framework: FastAPI/Flask (for Python) or standard library (for Go).
    *   Data Store: In-memory storage is acceptable. No database is required.
4.  **Deliverables:**
    *   A link to a public Git repository.
    *   A `README.md` with setup and execution instructions.
    *   Unit tests for the API endpoints.

**Evaluation Criteria:**
*   **Functionality:** Does the API meet all requirements?
*   **Code Quality:** Is the code clean, well-structured, and maintainable?
*   **Testing:** Are the tests comprehensive and meaningful?
*   **Documentation:** Is the `README.md` clear and complete?
```

---

## Stage 4 Addendum: Interview Kit Sample (Detailed)

This expands on the outline, showing representative (but redacted) content for the 3-file interview kit.

### 1. `candidate_context.md` (Sample)

```markdown
# Candidate Context: Candidate A

**Role:** Backend Engineer
**Overall Impression:** Strong technical skills with good AWS experience. Appears to align well with our core values of Ownership and Excellence.

**Key Strengths:**
- **Python & Backend:** 5 years of experience, demonstrated in take-home.
- **AWS Services:** Practical experience with S3, RDS, and Lambda.
- **Problem Solving:** Logical and structured approach in assessment.

**Areas to Probe:**
- **Testing:** Take-home tests were functional but could be more robust. Ask about their testing philosophy.
- **Scalability:** The assessment solution was simple. Probe on how they would scale it.
- **Collaboration:** Resume suggests mostly solo project work. Explore team collaboration experiences.

**Suggested Opening:**
"Thanks for coming in. We were really impressed with your take-home project, especially the clean API design..."
```

### 2. `interview_guide.md` (Sample)

```markdown
# Interview Guide: Candidate A (Backend Engineer)

## Part 1: Behavioral & Values (20 mins)
*   **Goal:** Assess alignment with core values. Use BEI questions.
*   **Value: Ownership:**
    *   "Tell me about a time you took responsibility for a project that went beyond your official duties." (Probe for initiative, outcome).
*   **Value: Technical Excellence:**
    *   "Describe a complex technical problem you solved. What was your process?" (Probe for depth, trade-offs).

## Part 2: Technical Deep-Dive (25 mins)
*   **Goal:** Validate technical depth from resume and take-home.
*   **Topic: Take-Home Review:**
    *   "Let's discuss your take-home. Why did you choose [specific library/pattern]?"
    *   "How would you add authentication and authorization to this service?"
*   **Topic: System Design:**
    *   "Let's design a simplified URL shortener service. How would you handle the data model and API?" (Whiteboard exercise).

## Part 3: Candidate Q&A (10 mins)
*   **Goal:** Answer candidate's questions.
```

### 3. `interview_script.md` (Sample)
*Note: This is a condensed script outline.*
```markdown
# Interview Script: Candidate A

**(0:00-0:05) Introduction**
- Interviewer intros, role overview.
- Agenda for the interview.
- Use suggested opening from `candidate_context.md`.

**(0:05-0:25) Behavioral Questions (from `interview_guide.md`)**
- "Let's start with your experience. Tell me about a time..."
- Use STAR method for follow-ups (Situation, Task, Action, Result).

**(0:25-0:50) Technical Deep-Dive (from `interview_guide.md`)**
- Transition: "Great, thanks for sharing. Now let's switch gears to the technical side."
- Discuss take-home project.
- Move to system design question on the whiteboard.

**(0:50-1:00) Wrap-up & Candidate Questions**
- "That's all the questions I have. What questions do you have for me?"
- Explain next steps in the process.
- Thank the candidate for their time.
```

---

## Stage 7 Output: Communication Agent Email Samples

These are representative templates for emails sent to candidates.

### 1. Assessment Invitation Email (Template)

```
Subject: Take-Home Assessment for the Backend Engineer Role at [Company]

Hi [Candidate Name],

Thank you for your interest in the Backend Engineer position and for taking the time to speak with us.

We were impressed with your background and would like to invite you to the next step in our process: a take-home assessment.

The assessment is designed to give you a sense of the work we do here and to allow you to showcase your skills. You can find the full instructions in the attached document.

Please submit your solution within **3-4 days** by providing a link to a public Git repository.

If you have any questions, please don't hesitate to reach out.

Best regards,
The [Company] Team
```

### 2. Post-Screening Rejection Email (Template)

```
Subject: Update on your Backend Engineer application at [Company]

Hi [Candidate Name],

Thank you for your interest in the Backend Engineer role at [Company] and for taking the time to submit your application.

We received a large number of qualified applications, and after careful consideration, we have decided not to move forward with your candidacy at this time.

This was a difficult decision, and we truly appreciate your interest in our team. We wish you the very best in your job search and future endeavors.

Best regards,
The [Company] Team
```

---

## Redaction & Compliance Statement
- All examples are synthetic and non‑identifying.
- Sensitive internals (prompts, context‑engineering methods, state machine specifics) are deliberately omitted.
- Schemas are indicative for AWS architecture consultation only.
