# Context Organization Principles
**For AI-Driven Project Management**

## Core Philosophy
Context organization follows the principle of **"Context-Complete Development"** - every aspect of project operations must be documented, structured, and accessible for both human and AI agents to execute tasks without external knowledge gaps.

## Hierarchical Context Structure

### Level 1: Organizational Foundation
```
context/
├── org.yaml                    # Mission, vision, core values
└── governance/                 # Company-wide policies
    ├── security_policies.yaml
    ├── compliance_standards.yaml  
    └── development_standards.yaml
```

**Purpose**: Provides organizational identity and guiding principles that inform all lower-level decisions.

### Level 2: Domain Separation
```
context/
└── {domain}/                   # e.g., work_mgmt, hr, finance, legal
    ├── ontology/               # Structured entity definitions
    ├── knowledge/              # Domain-specific knowledge
    └── vector/                 # Vector embeddings (optional)
```

**Purpose**: Separates concerns by business domain while maintaining clear boundaries and dependencies.

### Level 3: Ontological Structure
```
context/{domain}/ontology/
├── entities/                   # Core business entities
│   ├── {Entity}.yaml          # Individual entity definitions
├── relations.yaml              # Inter-entity relationships  
├── rules.yaml                  # Validation and business rules
└── validation/                 # Validation schemas and tests
```

**Purpose**: Creates a semantic foundation for understanding business objects and their interactions.

### Level 4: Knowledge Organization
```
context/{domain}/knowledge/
├── team/                      # Team composition and responsibilities
├── processes/                 # Standard operating procedures
├── okrs/                      # Goals and objectives
├── slices/                    # Time-bounded contexts (sprints, quarters)
└── api_guides/                # Technical integration knowledge
```

**Purpose**: Houses operational knowledge that drives day-to-day decision-making.

## Entity Design Patterns

### Canonical Entity Structure
```yaml
# {Entity}.yaml
metadata:
  version: "1.0"
  last_updated: "{ISO8601_TIMESTAMP}"
  purpose: "{CLEAR_PURPOSE_STATEMENT}"
  schema_version: "1.0"

{entity_name}:
  {primary_key}:
    # Core identifying information
    id: "{UNIQUE_IDENTIFIER}"
    name: "{HUMAN_READABLE_NAME}"
    
    # Classification
    type: "{ENTITY_TYPE}"
    category: "{CATEGORY}"
    
    # Operational metadata
    status: "{ACTIVE|INACTIVE|DEPRECATED}"
    created_at: "{ISO8601_TIMESTAMP}"
    
    # Contextual attributes
    purpose: "{BUSINESS_PURPOSE}"
    description: "{DETAILED_DESCRIPTION}"
    
    # Relationships (references to other entities)
    relationships:
      owns: ["{ENTITY_ID}"]
      depends_on: ["{ENTITY_ID}"]
      collaborates_with: ["{ENTITY_ID}"]
    
    # Domain-specific attributes
    domain_specific:
      key: "value"

# Validation rules
validation_rules:
  required_fields: [id, name, type, status]
  field_constraints:
    status: [ACTIVE, INACTIVE, DEPRECATED]
  relationship_constraints:
    max_dependencies: 10

# AI agent instructions
ai_agent_instructions:
  context_usage: "{HOW_AGENTS_SHOULD_USE_THIS_ENTITY}"
  update_triggers: ["{EVENTS_THAT_REQUIRE_UPDATES}"]
```

### Relationship Modeling
```yaml
# relations.yaml
relations:
  - from: Engineer
    to: Repository  
    type: OWNS
    cardinality: "many:many"
    constraints:
      - "ownership_requires_write_access"
      - "max_repositories_per_engineer: 10"
    
  - from: Task
    to: Engineer
    type: ASSIGNED_TO
    cardinality: "many:one"
    metadata:
      assignment_date: "{ISO8601_TIMESTAMP}"
      assignment_method: "{AUTO|MANUAL}"
```

## Context Layering Strategy

### Layer 1: Static Context (Rarely Changes)
- Organizational mission/vision/values
- Core business entities and relationships
- Architectural principles and standards
- Security policies and compliance requirements

### Layer 2: Semi-Static Context (Changes Quarterly)
- Team composition and roles
- Product roadmaps and OKRs
- Technology stack and tooling standards
- Process definitions and SOPs

### Layer 3: Dynamic Context (Changes Weekly/Daily)
- Current sprint/milestone status
- Active tasks and assignments
- Infrastructure state and configurations
- Performance metrics and KPIs

### Layer 4: Real-Time Context (Changes Continuously)
- Live system metrics and alerts
- Current infrastructure state
- Active incidents and responses
- Real-time team availability

## File Naming Conventions

### Entity Files
- **Pattern**: `{EntityName}.yaml` (PascalCase)
- **Examples**: `AWSAccount.yaml`, `Repository.yaml`, `Engineer.yaml`

### Knowledge Files
- **Pattern**: `{domain_concept}.yaml` (snake_case)
- **Examples**: `platform_development_team.yaml`, `agile_handbook.yaml`

### Process Files
- **Pattern**: `{process_name}_guide.yaml`
- **Examples**: `incident_management_guide.yaml`, `pr_review_guide.yaml`

### Time-Bounded Files
- **Pattern**: `{YYYY}-{period}.yaml`
- **Examples**: `2025-Q3.yaml`, `2025-H2.yaml`

## Metadata Standards

### Required Metadata Fields
```yaml
metadata:
  version: "1.0"                    # Semantic versioning
  last_updated: "{ISO8601_TIMESTAMP}"  # Last modification time
  purpose: "{CLEAR_PURPOSE}"        # Why this context exists
  domain: "{BUSINESS_DOMAIN}"       # Which domain owns this
  visibility: "{public|private|restricted}"  # Access control
  dependencies: ["{FILE_REFERENCES}"]  # Other context files this depends on
  schema_version: "1.0"            # Context schema version
```

### Optional Metadata Fields
```yaml
metadata:
  tags: ["{SEARCHABLE_TAGS}"]      # For categorization
  contacts:                        # Who to contact for updates
    - email: "owner@company.com"
      role: "owner"
  change_frequency: "{daily|weekly|monthly|quarterly|yearly}"
  automation_status: "{manual|semi_automated|fully_automated}"
```

## Validation Principles

### Structural Validation
- YAML syntax correctness
- Required field presence
- Data type consistency
- Reference integrity (entity IDs exist)

### Semantic Validation
- Business rule compliance
- Relationship constraint satisfaction
- Domain-specific validation rules
- Temporal consistency (timestamps, dates)

### Consistency Validation
- Cross-file reference validity
- Naming convention adherence
- Metadata completeness
- Version compatibility

## Context Evolution Management

### Versioning Strategy
- **Major versions** (X.0): Breaking changes to structure or relationships
- **Minor versions** (X.Y): New entities or fields added
- **Patch versions** (X.Y.Z): Data updates, corrections, clarifications

### Change Management Process
1. **Propose**: Create change proposal with rationale
2. **Review**: Validate impact on dependent contexts
3. **Test**: Run validation scripts and consistency checks
4. **Deploy**: Update context files atomically
5. **Verify**: Confirm agents can load and use new context

### Migration Patterns
- Maintain backward compatibility for 1 major version
- Provide migration scripts for breaking changes
- Document deprecated fields with sunset timelines
- Use feature flags for gradual rollouts

## Performance Optimization

### Loading Patterns
- **Lazy loading**: Load context on-demand based on task requirements
- **Hierarchical loading**: Load org → domain → specific entities
- **Caching**: Cache frequently accessed context in memory
- **Batch loading**: Load related contexts together

### Size Management
- Keep individual files < 100KB for fast loading
- Split large entities into separate files if needed
- Use references instead of embedding for related data
- Compress context for storage, decompress for usage

## Security and Access Control

### Sensitive Data Handling
- Never store credentials or secrets in context files
- Use placeholders and environment variables for sensitive data
- Separate public/private context with different access controls
- Encrypt sensitive context files at rest

### Access Patterns
- **Public context**: Available to all agents and team members
- **Restricted context**: Available to specific roles or teams
- **Private context**: Available to specific individuals only
- **Audit context**: All access logged for compliance

## Integration Patterns

### With MCP Servers
- Context loading as prerequisite for MCP tool usage
- Context validation before executing MCP commands
- Context updates triggered by MCP tool results
- Error handling when context loading fails

### With CI/CD Pipelines
- Context validation in pre-commit hooks
- Automated context updates from infrastructure changes
- Context consistency checks in build pipelines
- Rollback procedures for invalid context changes

### With Monitoring Systems
- Context freshness monitoring and alerting
- Context usage analytics and optimization
- Context dependency tracking and impact analysis
- Context change notification systems

---

**Implementation Note**: These principles are derived from the sleipnir-flow project's proven context management patterns. They should be adapted to fit specific project requirements while maintaining the core concepts of hierarchical organization, semantic relationships, and AI-agent accessibility.