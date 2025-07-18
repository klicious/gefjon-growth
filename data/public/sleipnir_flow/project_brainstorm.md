# Initial Brainstorming

- Name:  **`sleipnir-flow`**
    - Odin’s eight-legged horse crosses realms as fast as thought—mirrors shuttling tasks between Dooray & GitHub.
    - Speed, cross-system integration
- mother project
    
    ```markdown
    # Yimir: The Universal AI Knowledge Base Template
    
    This repository is the definitive template for building universal, scalable, and dynamic AI knowledge bases. It is meticulously designed to leverage the Gemini CLI, incorporating best practices for multi-subject context management, automated data ingestion, and live documentation. Any project forked from Yimir is immediately AI-ready and highly maintainable.
    
    ## Key Features
    
    *   **Multi-Subject Context Architecture**: A generalized `context/` structure designed to support multiple, distinct knowledge domains (e.g., HR, Finance, Engineering) in parallel.
    *   **Live Documentation**: The project is self-documenting. Core system prompts automatically update this README and other key documents to reflect the current state of the knowledge base.
    *   **Automated Knowledge Ingestion**: Includes standard prompts and scripts for intelligently processing and integrating new data sources into the KB.
    *   **Secure Data Lifecycle**: Implements a clear, secure pattern for handling input data, including a timestamped, immutable archive for processed files.
    *   **AI-Native Document Management**: A dedicated `ai_docs/` directory to manage the prompts, examples, and templates that drive AI-generated content.
    *   **Staging & Review Workflow**: A built-in `artifacts/staging/` area for AI-generated outputs that require human review before being finalized.
    
    ## Directory & File Layout
    
        ```
        └── yimir-root/
            ├── README.md                # Live document, auto-updated by the AI
            ├── context/                 # Manages context for distinct knowledge domains
            │   └── {subject_domain}/    # e.g., "hr", "finance", "work_mgmt"
            │       ├── ontology/        # Defines the "shape" of the knowledge
            │       │   ├── entities/    # Schema for each type of entity (e.g., User.yaml)
            │       │   ├── relations.yaml # Defines how entities connect
            │       │   └── rules.yaml   # Validation and operational rules
            │       ├── knowledge/       # Contains the actual facts and data
            │       │   ├── slices/      # Time-based or partitioned data (e.g., 2025-07.yaml)
            │       │   ├── projects/    # Data organized by project
            │       │   └── README.md    # Instructions on how to add knowledge
            │       └── vector/          # (Optional) FAISS index or pgvector dump for prose
            ├── data/                    # Input data for ingestion
            │   ├── public/
            │   └── private/
            │       └── archive/
            ├── artifacts/               # AI-generated outputs
            │   ├── public/
            │   ├── private/
            │   └── staging/
            ├── ai_docs/                 # Prompts, examples, and templates for the AI
            │   ├── prompts/
            │   │   ├── system/
            │   │   └── user/
            │   ├── examples/
            │   └── templates/
            ├── scripts/
            │   ├── validate_context.py  # CI script to validate all context files
            │   └── ...
            ├── .gemini/
            ├── .gitignore
            ├── dvc.yaml
            └── pyproject.toml
        ```
    
    ## Data Hygiene and Versioning
    
    This template enforces a robust data lifecycle:
    
    1.  **Ingestion**: New data is placed in `data/private` or `data/public`.
    2.  **Processing**: The AI processes the data using prompts from `ai_docs/prompts/`.
    3.  **Archiving**: After successful processing, the original source file from `data/private/` is moved to `data/private/archive/` with a `{timestamp}_{original_filename}` format, creating an immutable audit trail.
    4.  **Output Staging**: Generated artifacts are placed in `artifacts/staging/` for review.
    5.  **Finalization**: After review, artifacts are moved to `artifacts/public` or `artifacts/private`.
    
    ## Gemini CLI Execution Plan
    
    1.  **Populate a Subject Domain** (Lego YAML style):
        ```bash
        # Create the structure for a new "work_mgmt" domain
        mkdir -p context/work_mgmt/ontology/entities context/work_mgmt/knowledge/slices
        # Define a new entity
        touch context/work_mgmt/ontology/entities/DoorayTask.yaml
        # Add the first knowledge slice
        touch context/work_mgmt/knowledge/slices/2025-Q3.yaml
        ```
    2.  **Ingest New Data**:
        ```bash
        # Add a new data file
        cp ~/Downloads/new_project_brief.md data/private/
        # Run the ingestion prompt, which now understands the sliced format
        gemini run --prompt "Integrate new_project_brief.md into the 'work_mgmt' knowledge base" --context "ai_docs/prompts/system/integrate_new_data_prompt.md"
        ```
    3.  **Maintain the Project**:
        ```bash
        # After significant changes, trigger the live documentation update
        gemini run --prompt "Update the README to reflect the new context structure." --context "ai_docs/prompts/system/update_readme_prompt.md"
        ```
    
    ## Context Management Principles
    
    To prevent monolithic YAML files and ensure the knowledge base remains scalable and maintainable, this template employs a set of graduated patterns.
    
    ### Pattern 1: Directory-per-Facet ("Lego YAML")
    Instead of one large `ontology.yaml`, we break it into atomic parts.
    
    -   **`ontology/entities/*.yaml`**: Each file defines a single entity (e.g., `User.yaml`, `Ticket.yaml`).
    -   **`ontology/relations.yaml`**: Defines how entities relate to each other.
    -   **`knowledge/`**: Is similarly broken down by entity type or time.
    
    This keeps pull requests small and focused. Editing a milestone never creates a diff in an entity definition.
    
    ### Pattern 2: Time-Sliced Knowledge
    For facts that change frequently (like tasks or events), we store deltas instead of the full state.
    
    -   **`knowledge/slices/2025-Q3.yaml`**: A new file is created for each time period (e.g., quarter or sprint).
    -   An ingestion run appends new records to the latest slice. When a slice reaches a size limit, it's sealed, and a new one is created.
    
    ### Pattern 3: Hybrid DB + YAML (for Scale)
    When knowledge grows into thousands of records, YAML becomes inefficient.
    -   **Ontology**: Stays in YAML files for easy versioning.
    -   **Knowledge**: Is loaded into a lightweight database (SQLite, DuckDB). The AI queries this DB via a tool, receiving structured data back.
    
    ### Pattern 4: Vector Store for Prose
    For unstructured text like policies or long descriptions:
    -   The text is stored in a vector database (e.g., FAISS, pgvector).
    -   The `knowledge.yaml` files store only the vector ID, not the full text, keeping them lean.
    
    ### Recommended Adoption Path
    | Maturity                  | Suggested Mix                                               |
    | ------------------------- | ----------------------------------------------------------- |
    | **PoC / < 500 lines**     | Start with single `ontology.yaml` & `knowledge.yaml`.       |
    | **Team / Weekly Updates** | Use **Pattern 1 (Lego YAML)** + **Pattern 2 (Slices)**.     |
    | **Org-wide / >10k tasks** | Use **Pattern 1 + 3 (DB)** + **Pattern 4 (Vector Store)**.  |
    
    Start with Lego YAML and slices. You can always migrate slices to a database later with a one-off script.
    
    ## Context Validation
    The `scripts/validate_context.py` script should be integrated into your CI/CD pipeline. On every commit, it can:
    1.  Merge ontology snippets and validate them against a master schema.
    2.  Check knowledge slices for schema conformance.
    3.  Warn if any file exceeds a recommended size limit (e.g., 200KB).
    
    ```
    
- Purpose
    - To generate all tasks for the platform development team based on the complete set of contexts.
- Work the platform development team does
    - DevOps
        - AWS
    - Application Development
        - Python
        - JavaScript - React.js
    - Services
        - crypto currency algorithm trading
            - BE - Python, FastAPI
            - FE - React.js
            - repositories
                - crypto-maester
                - bifrost
                - mimir
                - ishtar
        - Portfolio Management System
            - BE - Java 18+, Spring Boot
            - FE - React.js
            - repositories
                - jophiel
                - silver-city
                - silver-city-config
                - schemhampharae
                - seraphiel
                - cherubim
                - metatron
                - config-server
                - grunt
        - AI agents development (for the platform development team’s complete automation)
            - This a brand new project at incubating stage
            - BE - Python
            - FE - N/A yet
            - repositories
                - gefjon-growth
                - yimir-root
                - runebook
                - basalt
                - ion-forge
                - yggdrasil
    - Service management
        - AWS
        - monitor
        - debug
        - update
- Contexts
    - Tools we use
        - Messenger: Dooray Messenger (instead of Slack)
        - Task Management: Dooray Task Management (instead of Jira)
        - GitHub
        - AWS
            - ECS
            - EC2
            - RDS
                - Aurora DB - PosgreSQL
            - AWS Secret Manager
        - PyCharm
        - Outlook (e-mail)
        - Google
            - Google Sheets
            - Google Docs
            - Google Slides
            - Google Drive
            - Google Forms
        - AI Tools
            - ChatGPT
            - Gemini
            - Gemini CLI
            - Claude Code
            - Amazon Q Developer
        - Docker
            - MCP Tools
            - Models - Local LLMs
    - Dooray Tasks
        - access points: [https://dunamis.dooray.com](https://dunamis.dooray.com/task)
            - management API: https://helpdesk.dooray.com/share/pages/9wWo-xwiR66BO5LGshgVTg/2939987729788437786
            - Service API: https://helpdesk.dooray.com/share/pages/9wWo-xwiR66BO5LGshgVTg/2939987647631384419
        - projects
            - (make entirely new projects from onwards. Toss out the old projects)
        - tasks
    - GitHub source codes
        - account
            - `klicious` : https://github.com/klicious
                - repositories
                    - grunt
                    - gefjon-growth
                    - yimir-root
                    - runebook
                    - basalt
                    - ion-forge
                    - yggdrasil
        - orgs
            - `dunamis-capital`: https://github.com/dunamis-capital
                - repositories
                    - jophiel
                    - silver-city
                    - news-scrapper
                    - ishtar
                    - crypto-maester
                    - mimir
                    - seraphiel
                    - metatron
                    - silver-city-config
                    - ratatoskr
                    - schemhampharae
                    - config-server
                    - cherubim
                    - bifrost
                    - peon
            
    - AWS (infrastructure)
        - 3 accounts
            - 
            
            ```markdown
            DevOps 환경
            - account ID: 319470692494
            - root 계정 ID: devops@dunamiscap.com
              - Access Key ID: AKIAUUYPP5CHCTV5NHMW
              - Secret Access Key: {ask}
            - region: ap-northeast-2
            ```
            
            ```
            Dev 환경
            - account ID: 418867772055
            - root 계정 ID: dev@dunamiscap.com
              - Access Key ID: AKIAWDBTW7KLSNNGGRS2
              - Secret Access Key: {ask}
            - region: ap-northeast-2
            
            ```
            
            ```
            Prod 환경
            - account ID: 723373476465
            - root 계정 ID:
            - 현재 사용 중인 IAM 사용자: dnjsgur0629
              - Access Key ID: AKIA2Q3DLJJY7ITXOSR7
              - Secret Access Key: {ask}
            - region: ap-northeast-2
            ```
            
            - DevOps
                - servers/roles
                    - bastion
                    - build
                    - GitLab Runner
            - Development
            - Production
    - about the team
        - team members
            - T: BE engineer
                - 9-year experience
                - language
                    - Python - MAIN
                    - Java - MAIN
                    - JavaScript
                    - 
            - W: FE Engineer
                - 4-year experience
                - language
                    - Javascript (React.js) - MAIN
                    - python
            - D: BE engineer
                - intern
                - language
                    - python
        - OKRs
        - mission, vision, and core-values
        - 
- What the agent should be able to do
    - Do everything based on the accessible contexts
        - within the project
            - `context` directory
            - `artifacts` directory
            - `data` directory
        - outside the project
            - GitHub
            - Dooray Task Manager
    - manage projects
        - create, modify, or delete projects based on the well designed structures. Tasks will be managed by the projects
        - Tagging strategy. tag exists in `{group}:{name}` fashion
        - manage milestones
        - manage priorities between the tasks
    - Manage tasks
        - manage task templates
        - create/modify tasks
            - use the current state of the projects and team information to create a complete and comprehensive tasks
            - the tasks should be so well defined that there won’t be much of the room for misled actions.
            - the tasks should be written in a format that is comprehensive and clear for both human and LLM
        - assign tasks to an appropriate team member
    - Follow the Agile process described in the `power of process`
    - The task agent should know about and have access to the source codes
        - access Github repositories
            - perhaps it’ll be more efficient to keep a clone under this project and keep them updated with the upstream?
        - check issues
    - use the current state of the projects and team information to create a complete and comprehensive tasks
    - Keep/update the live document that shows exactly what’s up with the platform development team.
        - what they did
        - what they are working on now.
        - the progress so far
        - what they are trying to do
        - what they will do this year
        - what they will to in a far future.
        - what they are trying to achieve.
    - AWS access (read-only)
        - Access AWS to find out about the current architecture.
        - access to the logs and metrics to find out any current/potential issues if there’s any
    -