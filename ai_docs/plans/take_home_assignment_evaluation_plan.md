# Take-Home Assignment Evaluation Plan: Entry-Level Software Engineer

## 1. Objective
To objectively evaluate candidates' technical skills, problem-solving abilities, code quality, and adherence to requirements through a standardized take-home assignment, ensuring a fair and consistent assessment process.

## 2. Inputs
- **Take-Home Assignment Description:** `data/temp/entry_level_sw_eng_take_home_task.md`
- **Candidate Submission:** GitHub repository URL (private, with `klicious` as collaborator)
- **Job Description:** `data/temp/entry_level_job_description.md` (translated to English)

## 3. Evaluation Process (Human & LLM)

### 3.1. Initial Setup & Access
- **Human:** Verify access to the private GitHub repository. Clone the repository locally.
- **LLM (Assisted):** Can be prompted to provide instructions for cloning and setting up the environment based on the `README.md`.

### 3.2. Deliverables Check
- **Human/LLM:** Verify all required deliverables are present:
    - Functional implementation of specified API features.
    - Unit tests (using `pytest`).
    - `README.md` with setup instructions, navigation guide, usage examples, and API key configuration details.
    - Supportive materials (diagrams/charts) if applicable.

### 3.3. Functional Correctness & Completeness (Technical Implementation)
- **Human (Primary) & LLM (Assisted):**
    - **API Features:** Systematically test each required API feature (Get Orders by IDs/date range/state, Get Active Orders, Place Orders, Amend Orders, Cancel Orders) for both BitMex and Binance.
    - **Market Support:** Verify support for SPOT, USD-M Futures, and USD-C Futures markets.
    - **Instrument Support:** Confirm functionality for BTC, ETH, SOL instruments.
    - **Test/Production Servers:** Ensure the implementation correctly handles both test and production server environments.
    - **Error Handling:** Evaluate how the implementation handles invalid inputs, API errors, and edge cases.
    - **LLM Assistance:** LLM can generate test cases based on the requirements and analyze test output for correctness.

### 3.4. Code Quality & Best Practices
- **Human (Primary) & LLM (Assisted):**
    - **Readability & Maintainability:** Assess code clarity, consistent naming conventions, and appropriate commenting.
    - **Modularity & Design:** Evaluate the modularity of the code, separation of concerns, and overall design choices.
    - **Python Idioms:** Check for idiomatic Python usage and adherence to PEP 8 (or project-specific style guides).
    - **Security:** Review for secure handling of API keys (e.g., environment variables, not hardcoded).
    - **LLM Assistance:** LLM can perform static code analysis, identify potential code smells, and suggest improvements based on best practices.

### 3.5. Testing Approach & Coverage
- **Human (Primary) & LLM (Assisted):**
    - **Unit Test Quality:** Evaluate the quality of unit tests (e.g., clear test names, proper assertions, isolation).
    - **Test Coverage:** Assess the extent to which the code is covered by tests. (LLM can help calculate coverage if a coverage report is generated).
    - **Mocking:** Review the use of mocking for external API calls.
    - **LLM Assistance:** LLM can suggest additional test cases to improve coverage or identify gaps in existing tests.

### 3.6. Documentation Quality
- **Human (Primary) & LLM (Assisted):**
    - **Clarity & Completeness:** Evaluate the `README.md` for clear setup instructions, comprehensive navigation, and useful usage examples.
    - **API Key Configuration:** Verify secure and clear instructions for API key configuration.
    - **Supportive Materials:** Assess the clarity and usefulness of any diagrams or charts.
    - **LLM Assistance:** LLM can check for completeness against a checklist of required documentation elements.

### 3.7. Git Workflow & Commit History
- **Human:** Review the Git commit history for:
    - **Frequency:** Regular commits indicating iterative development.
    - **Commit Messages:** Clear, concise, and descriptive commit messages.
    - **Branching Strategy:** If branching was used, assess its effectiveness.

### 3.8. Going Above and Beyond / Ownership
- **Human (Primary) & LLM (Assisted):**
    - **Initiative:** Did the candidate implement features not explicitly requested but logically extending the task (e.g., advanced logging, metrics, robust configuration, more comprehensive error handling)?
    - **Proactivity:** Did they propose alternative solutions or improvements with clear justifications in their documentation?
    - **Autonomy:** Does the solution demonstrate independent thought and problem-solving beyond basic requirements?
    - **LLM Assistance:** LLM can identify additional features, analyze documentation for proposed improvements, and review commit messages for proactive statements.

### 3.9. Scalability & Design Patterns
- **Human (Primary) & LLM (Assisted):**
    - **Abstraction:** Is there a clear abstraction layer (e.g., interfaces, abstract classes) for integrating with different exchanges, allowing for easy addition of new exchanges?
    - **Unified Data Models:** How are different symbols/instruments managed across exchanges (e.g., a unified symbol mapping or conversion)?
    - **Extensibility:** Does the design allow for easy addition of new order types, market data sources, or trading strategies without significant refactoring?
    - **Design Patterns:** Is there evidence of appropriate design patterns (e.g., Strategy, Factory, Adapter) that promote maintainability, testability, and scalability?
    - **LLM Assistance:** LLM can analyze code structure for design patterns, identify abstraction layers, and evaluate symbol management logic.

### 3.10. Quantitative & Logical Problem Solving
- **Human (Primary) & LLM (Assisted):**
    - **Quantitative Reasoning:** Evaluate how the candidate approaches problems requiring numerical or mathematical solutions within the assignment.
    - **Logical Structuring:** Assess the clarity and efficiency of the logical flow and structure of the code and problem-solving approach.
    - **Problem Decomposition:** How effectively does the candidate break down complex quantitative or logical problems into manageable components?
    - **LLM Assistance:** LLM can analyze the code for mathematical correctness, logical consistency, and efficiency of algorithms.

### 3.11. Overall Evaluation & Scoring
- **Human (Primary):** Assign scores based on the evaluation criteria (Technical Implementation, Code Quality, Testing, Documentation, Going Above and Beyond / Ownership, Scalability & Design Patterns, Quantitative & Logical Problem Solving).
- **LLM (Assisted):** Can provide a preliminary score based on automated checks and flag areas for human attention.

## 4. Output
- **Evaluation Score:** A numerical score or rating for each criterion and an overall score.
- **Detailed Feedback:** Specific, actionable feedback on strengths and areas for improvement, referencing code snippets or documentation sections.
- **Recommendation:** (e.g., "Proceed to Interview," "Consider for another role," "Do not proceed")
- **Comparison to Job Description:** How well the candidate's submission aligns with the technical requirements and values from the job description, including "Ownership & Proactivity" and "Scalable Architecture over Quick Hacks" from our Engineering Values.

## 5. LLM Usage Guidelines
- **Code Review:** LLM can perform automated code reviews, identifying potential bugs, style violations, security vulnerabilities, and adherence to design principles.
- **Test Case Generation:** Generate additional test cases to thoroughly validate the implementation.
- **Documentation Generation/Review:** Assist in generating missing documentation or reviewing existing documentation for clarity and completeness.
- **Plagiarism Detection:** Compare candidate's code against known solutions or other submissions.
- **Performance Benchmarking:** If applicable, LLM can help analyze performance metrics of the implemented solution.
- **Structured Output:** LLM should output evaluation results in a structured format (e.g., JSON, YAML) for easy integration into HR systems.
- **Proactive Feature Identification:** LLM can identify features or design choices that go beyond the explicit requirements and align with the "Going Above and Beyond" criterion.
- **Scalability Pattern Recognition:** LLM can identify and evaluate the use of design patterns and abstraction layers related to scalability and extensibility.
