# Context Loading Guidelines for AI Agents
**Template for Similar Projects**

## Overview
This document provides standardized context loading guidelines for AI agents working on projects similar to sleipnir-flow. These guidelines ensure consistent, reliable context-driven development across all projects.

## Core Principle
**Context-Driven Development**: Always load relevant context before making decisions or taking actions.

## When Context Loading is Mandatory

**ALWAYS** load context before:
- Making AWS CLI calls or infrastructure operations
- Referencing account names, environments, or profiles
- Repository operations or code deployment
- Team member queries or assignments
- Organizational process decisions
- Security or compliance-related actions

## Universal Context Loading Protocol

### Step 1: Identify Project Context Structure
Every project must establish these context directories:
```
{PROJECT_ROOT}/
├── context/
│   ├── org.yaml                          # Organizational context
│   ├── {domain}/
│   │   ├── ontology/
│   │   │   ├── entities/                 # Core entities
│   │   │   │   ├── AWSAccount.yaml      # AWS account mappings
│   │   │   │   ├── Repository.yaml       # Repository definitions
│   │   │   │   ├── Engineer.yaml         # Team member info
│   │   │   │   └── Service.yaml          # Service definitions
│   │   │   ├── relations.yaml            # Entity relationships
│   │   │   └── rules.yaml                # Context validation rules
│   │   └── knowledge/
│   │       ├── team/                     # Team-specific knowledge
│   │       ├── processes/                # Process documentation
│   │       └── okrs/                     # Goals and objectives
└── ai_docs/
    └── context/
        └── context_loading_procedure.md  # Project-specific procedures
```

### Step 2: Pre-Action Context Loading Sequence
Before any significant action, execute this sequence:

1. **Load Organizational Context**
   ```bash
   # Check if org.yaml exists and load organizational mission/values
   find {PROJECT_ROOT}/context -name "org.yaml" | head -1
   ```

2. **Load Account/Infrastructure Context**
   ```bash
   # Load AWS account mappings (critical for infrastructure operations)
   find {PROJECT_ROOT}/context -path "*/entities/AWSAccount.yaml" | head -1
   ```

3. **Load Team Context**
   ```bash
   # Load team composition and responsibilities
   find {PROJECT_ROOT}/context -path "*/team/*.yaml" | head -5
   ```

4. **Load Domain-Specific Context**
   ```bash
   # Load relevant domain entities based on task type
   find {PROJECT_ROOT}/context -name "*.yaml" -path "*/entities/*" | head -10
   ```

### Step 3: Context Validation
Always validate loaded context:
- Verify YAML syntax validity
- Check for required fields (account_id, aws_profile, etc.)
- Confirm mapping consistency (email → profile → account_id)
- Validate timestamp freshness (warn if > 30 days old)

## AWS Account Context Requirements

### Mandatory Fields in AWSAccount.yaml
```yaml
aws_accounts:
  {environment_name}:
    account_id: "{AWS_ACCOUNT_ID}"
    account_email: "{EMAIL_ADDRESS}"
    aws_profile: "{CLI_PROFILE_NAME}"
    environment_type: "{dev|staging|production|devops}"
    purpose: "{DESCRIPTION}"
    
    access_configuration:
      access_method: "{direct|bastion|vpn}"
      accessibility_status: "{full_access|restricted|ip_whitelist_required}"

# CLI Profile Mappings (mandatory)
profile_mappings:
  "{EMAIL}": "{PROFILE_NAME}"

# AI Agent Instructions (mandatory)
ai_agent_instructions:
  context_loading_rule: "Always reference this file when AWS account emails are mentioned"
  profile_enforcement: "Enforce --profile flag usage based on profile_mappings"
```

### AWS CLI Usage Pattern
```bash
# NEVER use default profile
aws sts get-caller-identity --profile {MAPPED_PROFILE}

# Always map email → profile from context
# Example: devops@company.com → devops profile
aws ec2 describe-instances --profile devops
```

## Error Prevention Checklist

### Before AWS Operations
- [ ] Context files loaded and validated
- [ ] Account email mapped to AWS profile
- [ ] Profile explicitly specified in command
- [ ] Access method verified (direct/bastion/VPN)

### Before Repository Operations
- [ ] Repository.yaml loaded for service mappings
- [ ] Engineer.yaml checked for ownership
- [ ] Access permissions validated

### Before Team Operations
- [ ] Team composition loaded from context
- [ ] Role assignments verified
- [ ] Current milestone/sprint context available

## Implementation for New Projects

### Required Files (Minimum Viable Context)
1. `context/org.yaml` - Organizational mission, vision, values
2. `context/{domain}/ontology/entities/AWSAccount.yaml` - AWS account registry
3. `context/{domain}/knowledge/team/{team_name}.yaml` - Team composition
4. `ai_docs/context/context_loading_procedure.md` - Project-specific procedures

### Required Metadata Fields
Every context file must include:
```yaml
metadata:
  version: "1.0"
  last_updated: "{ISO8601_TIMESTAMP}"
  purpose: "{DESCRIPTION}"
```

### Validation Script Template
Create `scripts/validate_context.py`:
```python
#!/usr/bin/env python3
"""Context validation script for {PROJECT_NAME}"""

import yaml
import sys
from pathlib import Path

def validate_aws_accounts():
    """Validate AWS account context"""
    # Implementation based on sleipnir-flow/scripts/validate_context.py
    
def validate_team_context():
    """Validate team context"""
    # Implementation
    
if __name__ == "__main__":
    # Run validation checks
    pass
```

## Best Practices

### Context File Organization
- Use semantic naming (AWSAccount.yaml, not accounts.yaml)
- Group related entities in same directory
- Maintain metadata consistency across files
- Version control all context changes

### Context Loading Patterns
- Load context once per agent session, cache results
- Always validate before usage
- Log context loading for debugging
- Fail fast if critical context missing

### Security Considerations
- Never hardcode credentials in context files
- Use placeholders for sensitive data
- Validate access permissions before operations
- Log all context-based decisions for audit

## Troubleshooting

### Common Issues
1. **Missing profile mappings** → Check AWSAccount.yaml profile_mappings section
2. **Default profile used** → Ensure --profile flag always specified
3. **Context file not found** → Verify directory structure matches template
4. **Stale context data** → Check last_updated timestamps

### Debug Commands
```bash
# Find all context files
find {PROJECT_ROOT}/context -name "*.yaml" -type f

# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('{file}'))"

# Check AWS profile configuration
aws configure list-profiles
```

## Integration with Existing Tools

### With MCP Servers
- Load context before any MCP tool calls
- Pass context data as parameters where relevant
- Cache context to avoid repeated loading

### With CI/CD Pipelines
- Validate context files in pre-commit hooks
- Auto-update timestamps on context changes
- Fail builds on context validation errors

## Customization Guidelines

### Extending Entity Types
Add new entity types in `context/{domain}/ontology/entities/{EntityName}.yaml`

### Adding Validation Rules
Update `context/{domain}/ontology/rules.yaml` with new validation logic

### Domain-Specific Context
Create domain subdirectories under `context/` for specialized knowledge

---

**Note**: This template is based on sleipnir-flow's proven context loading patterns. Adapt the structure to match your project's specific needs while maintaining the core principles of context-driven development.