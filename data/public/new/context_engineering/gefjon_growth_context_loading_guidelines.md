# Context Loading Guidelines for Gefjon Growth HR Automation
**AI Agent Protocol for Interview Kit Generation & HR Process Automation**

## Overview
This document provides standardized context loading guidelines for AI agents working on Gefjon Growth's HR automation platform. These guidelines ensure consistent, reliable context-driven development across all HR automation workflows including hiring, performance management, OKR tracking, and talent development.

## Core Principle
**HR Context-Driven Development**: Always load complete HR context including company values, team composition, and candidate information before executing any HR automation task.

## When Context Loading is Mandatory

**ALWAYS** load context before:
- Generating interview kits or candidate assessment materials
- Processing candidate profiles or resume analysis
- Creating BEI questions or technical assessment problems
- Making hiring decisions or recommendations
- Performance evaluation or OKR-related operations
- Team composition queries or role assignments
- Company values alignment or culture fit assessments

## Gefjon Growth Context Loading Protocol

### Step 1: HR Context Structure
Gefjon Growth uses this specialized HR context structure:
```
gefjon-growth/
├── context/
│   ├── company_info/
│   │   ├── mission_vision_values.yaml    # Core values for candidate alignment
│   │   ├── goals_okrs.yaml               # Company objectives
│   │   └── hr_trends.yaml                # Industry context
│   ├── hr_processes/
│   │   ├── hiring/
│   │   │   └── hiring_stages.yaml        # Interview process definition
│   │   ├── evaluation/
│   │   │   └── performance_review_process.yaml
│   │   ├── onboarding/
│   │   │   └── onboarding_plan.yaml
│   │   └── sops/
│   │       ├── power_of_process.md
│   │       └── sop_implementation_guide.yaml
│   └── teams/
│       └── platform_development_team.yaml # Team context for role matching
├── data/public/hiring/resume/             # Candidate input data
└── artifacts/
    ├── public/hiring/                     # Generated interview materials
    └── private/                           # Sensitive evaluations
```

### Step 2: HR Context Loading Sequence
Before any HR automation task, execute this sequence:

1. **Load Company Context**
   ```bash
   # Load company mission, vision, and 10 core values
   find context/company_info -name "mission_vision_values.yaml"
   find context/company_info -name "goals_okrs.yaml"
   ```

2. **Load HR Process Context**
   ```bash
   # Load hiring stages and evaluation processes
   find context/hr_processes -name "hiring_stages.yaml"
   find context/hr_processes -name "performance_review_process.yaml"
   ```

3. **Load Team Context**
   ```bash
   # Load team composition for role matching
   find context/teams -name "platform_development_team.yaml"
   ```

4. **Load Candidate Context (for hiring tasks)**
   ```bash
   # Load candidate profiles for interview kit generation
   find data/public/hiring/resume -name "*.json"
   ```

5. **Check Existing Artifacts**
   ```bash
   # Check for existing interview materials and evaluations
   find artifacts/public/hiring -type d -name "upcoming"
   find artifacts/private -type d -name "evaluation"
   ```

### Step 3: Context Validation
Always validate loaded HR context:
- Verify YAML syntax validity for all context files
- Check for required fields (company values, hiring stages, team composition)
- Confirm candidate data completeness and format
- Validate technical problem bank availability (easy/intermediate/expert)

## HR Context Requirements

### Mandatory Fields in mission_vision_values.yaml
```yaml
id: org-core
type: knowledge_base
domain: HR
last_updated: 2025-07-10
tags: [mission, vision, values]
visibility: public

body: |
  ## Mission
  [Company mission statement]
  
  ## Vision
  [Company vision statement]
  
  ## Core Values — Deep Dive
  | # | Value | "What Good Looks Like" | Anti‑Pattern to Avoid |
  |---|---|---|---|
  | 1 | **Technical Excellence & Scalable Elegance** | [Examples] | [Anti-patterns] |
  # ... (10 total values)
```

### Candidate Profile Data Structure
```json
{
  "candidate_id": "unique_identifier",
  "name": "Full Name",
  "contact": {
    "email": "email@example.com",
    "phone": "+1-xxx-xxx-xxxx"
  },
  "experience": {
    "years_total": 5,
    "relevant_years": 3,
    "technologies": ["Python", "Django", "AWS"]
  },
  "education": {...},
  "projects": [...],
  "achievements": [...]
}
```

### Interview Kit Generation Pattern
```bash
# Generate interview kit using Gemini CLI
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/{candidate_file}.json"
```

## Error Prevention Checklist

### Before Interview Kit Generation
- [ ] Company values loaded from mission_vision_values.yaml
- [ ] Hiring process loaded from hiring_stages.yaml
- [ ] Team context loaded for role requirements
- [ ] Candidate profile validated and complete
- [ ] Technical problem bank available for skill level

### Before Candidate Assessment
- [ ] Core values mapping methodology understood
- [ ] BEI (Behavioral Event Interviewing) framework loaded
- [ ] Red flag identification criteria available
- [ ] Assessment rubrics and evaluation criteria loaded

### Before Performance Evaluation Operations
- [ ] Performance review process context loaded
- [ ] OKR framework and current goals available
- [ ] Team composition and reporting structure verified
- [ ] Historical performance data accessible

## Implementation for HR Automation

### Required Files (Minimum Viable HR Context)
1. `context/company_info/mission_vision_values.yaml` - Company core values and culture
2. `context/hr_processes/hiring/hiring_stages.yaml` - Interview process framework
3. `context/teams/platform_development_team.yaml` - Team composition and requirements
4. `ai_docs/prompts/hiring/generate_interview_kit_prompt.md` - Core interview generation logic

### Required Metadata Fields for HR Context
Every HR context file must include:
```yaml
id: unique-identifier
type: knowledge_base|process_definition|team_info
domain: HR|hiring|performance|onboarding
last_updated: 2025-07-10
tags: [relevant, tags, for, searchability]
visibility: public|private|restricted
```

### Validation Script for HR Context
Create `scripts/validate_hr_context.py`:
```python
#!/usr/bin/env python3
"""HR Context validation script for Gefjon Growth"""

import yaml
import json
import sys
from pathlib import Path

def validate_company_context():
    """Validate company mission, vision, and values"""
    context_file = Path("context/company_info/mission_vision_values.yaml")
    if not context_file.exists():
        raise FileNotFoundError(f"Missing {context_file}")
    
    with open(context_file) as f:
        data = yaml.safe_load(f)
    
    required_fields = ['id', 'type', 'domain', 'last_updated', 'body']
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing required fields in {context_file}: {missing}")

def validate_candidate_data():
    """Validate candidate JSON profiles"""
    resume_dir = Path("data/public/hiring/resume")
    if not resume_dir.exists():
        return  # Optional directory
    
    for json_file in resume_dir.glob("*.json"):
        with open(json_file) as f:
            candidate = json.load(f)
        
        required_fields = ['candidate_id', 'name', 'experience']
        missing = [field for field in required_fields if field not in candidate]
        if missing:
            raise ValueError(f"Missing required fields in {json_file}: {missing}")

def validate_technical_problems():
    """Validate technical problem bank"""
    problems_dir = Path("artifacts/public/hiring/pair_programming")
    if not problems_dir.exists():
        raise FileNotFoundError(f"Missing {problems_dir}")
    
    required_levels = ['easy.md', 'intermediate.md', 'expert.md']
    for level in required_levels:
        if not (problems_dir / level).exists():
            raise FileNotFoundError(f"Missing {problems_dir / level}")

if __name__ == "__main__":
    try:
        validate_company_context()
        validate_candidate_data()
        validate_technical_problems()
        print("✅ HR context validation passed")
    except Exception as e:
        print(f"❌ HR context validation failed: {e}")
        sys.exit(1)
```

## HR-Specific Best Practices

### Context File Organization
- Use semantic naming (mission_vision_values.yaml, hiring_stages.yaml)
- Group HR processes by lifecycle stage (hiring, onboarding, performance)
- Separate sensitive candidate data (private vs public artifacts)
- Maintain consistency across candidate profiles

### HR Context Loading Patterns
- Load company context once per agent session, cache results
- Always validate candidate data completeness before interview kit generation
- Log all HR automation decisions for audit trails
- Fail fast if core values or hiring process context missing
- Generate complete candidate context before proceeding with assessments

### Security Considerations for HR Data
- Never store sensitive personal data in public artifacts
- Use candidate IDs instead of full names in file paths
- Encrypt sensitive evaluation data at rest
- Maintain audit logs for all HR automation decisions

## Integration with AI Tools

### With Gemini CLI
- Load HR context before any `gemini run` command
- Pass candidate context as `--context` parameter
- Use structured prompts from `ai_docs/prompts/hiring/`
- Cache context to avoid repeated loading

### With Claude Code
- Reference HR context files in CLAUDE.md
- Use context engineering methodology for all tasks
- Validate HR context completeness before proceeding
- Store all outputs in structured artifacts directories

### With KIRO
- Load HR context according to `.kiro/steering/` guidelines
- Apply HR-specific context validation rules
- Use HR domain knowledge for decision making
- Maintain consistency with other AI agents

## HR Context Troubleshooting

### Common Issues
1. **Missing candidate data** → Check data/public/hiring/resume/ for JSON files
2. **Incomplete core values mapping** → Verify mission_vision_values.yaml has all 10 values
3. **Context file not found** → Verify directory structure matches Gefjon Growth template
4. **Stale interview materials** → Check artifacts/public/hiring/interview_materials/upcoming/
5. **Missing technical problems** → Verify artifacts/public/hiring/pair_programming/ has easy/intermediate/expert files

### HR Debug Commands
```bash
# Find all HR context files
find context -name "*.yaml" -type f

# Validate YAML syntax for HR context
python -c "import yaml; yaml.safe_load(open('context/company_info/mission_vision_values.yaml'))"

# Check candidate data availability
find data/public/hiring/resume -name "*.json" -type f

# Verify interview kit generation
ls -la artifacts/public/hiring/interview_materials/upcoming/

# Test Gemini CLI integration
gemini run --help

# Run HR context validation
python scripts/validate_hr_context.py
```

## Success Criteria for HR Context

### Context Completeness
- [ ] All 10 company core values documented and accessible
- [ ] Hiring process stages clearly defined
- [ ] Team composition and requirements available
- [ ] Technical problem bank complete (easy/intermediate/expert)
- [ ] Candidate profiles follow consistent JSON schema

### AI Agent Effectiveness
- [ ] Agents consistently load HR context before operations
- [ ] Interview kit generation uses complete company context
- [ ] Candidate assessments align with company values
- [ ] Technical problems match candidate skill levels
- [ ] Error rates for context-related issues < 1%

### Interview Quality
- [ ] Generated BEI questions reference specific candidate experiences
- [ ] Core values mapping shows concrete evidence
- [ ] Red flags are identified and addressed in interview plans
- [ ] Technical assessments match role requirements
- [ ] Interview scripts provide complete interviewer guidance

---

**Implementation Note**: These guidelines are specifically customized for Gefjon Growth's HR automation platform, focusing on interview kit generation, candidate assessment, and HR process automation. They build upon proven context engineering principles while addressing the unique requirements of HR automation workflows.