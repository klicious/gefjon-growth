# Gefjon Growth Context Loading Procedure
**For Claude Code, Gemini CLI, and KIRO Agents**

## Overview
This document defines the standardized context loading procedure for AI agents (Claude Code, Gemini CLI, KIRO) working on Gefjon Growth's HR automation platform. All agents must follow this procedure before executing any tasks to ensure consistent, context-aware operations.

## Pre-Task Context Loading Checklist

### Phase 1: Company Foundation Context
**REQUIRED for all HR automation tasks**

```bash
# 1. Load company mission, vision, and 10 core values
cat context/company_info/mission_vision_values.yaml

# 2. Load company goals and OKRs
cat context/company_info/goals_okrs.yaml

# 3. Load HR industry trends (optional but recommended)
cat context/company_info/hr_trends.yaml
```

**Validation Step**: Confirm all 10 core values are present and understand the mission statement.

### Phase 2: HR Process Context
**REQUIRED for hiring and performance tasks**

```bash
# 1. Load hiring process stages and BEI framework
cat context/hr_processes/hiring/hiring_stages.yaml

# 2. Load performance review process (for performance tasks)
cat context/hr_processes/evaluation/performance_review_process.yaml

# 3. Load onboarding process (for new hire tasks)
cat context/hr_processes/onboarding/onboarding_plan.yaml

# 4. Load SOPs and process implementation guides
cat context/hr_processes/sops/sop_implementation_guide.yaml
```

**Validation Step**: Understand the interview stages and evaluation criteria.

### Phase 3: Team Context
**REQUIRED for role matching and team-specific tasks**

```bash
# Load platform development team context
cat context/teams/platform_development_team.yaml
```

**Validation Step**: Understand team composition, technology stack, and role requirements.

### Phase 4: Task-Specific Context Loading

#### For Interview Kit Generation Tasks:
```bash
# 1. Load candidate profiles
find data/public/hiring/resume -name "*.json" | head -5

# 2. Check existing interview materials
ls -la artifacts/public/hiring/interview_materials/upcoming/

# 3. Load technical problem bank
ls artifacts/public/hiring/pair_programming/
cat artifacts/public/hiring/pair_programming/easy.md
cat artifacts/public/hiring/pair_programming/intermediate.md
cat artifacts/public/hiring/pair_programming/expert.md

# 4. Load BEI question bank and interview guides
cat artifacts/public/hiring/interview_materials/bei_interview_guide.md
cat artifacts/public/hiring/interview_materials/bei_question_bank.md
```

#### For Performance Evaluation Tasks:
```bash
# 1. Load performance review artifacts
ls -la artifacts/private/evaluation/

# 2. Check existing evaluation logs
find artifacts/private/evaluation -name "*_evaluation_*.md"

# 3. Load bias check logs (if applicable)
ls artifacts/private/evaluation/bias_check_logs/
```

#### For Candidate Screening Tasks:
```bash
# 1. Load screening reports and results
ls artifacts/public/hiring/evaluation/
ls artifacts/private/hiring/screening_reports/

# 2. Load evaluation sheets
cat artifacts/public/hiring/evaluation_sheets/upcoming/take_home_evaluation_sheet.md
```

### Phase 5: Context Completeness Verification

Execute this verification script before proceeding:

```python
#!/usr/bin/env python3
"""Context completeness check for Gefjon Growth HR automation"""

import yaml
import json
from pathlib import Path

def check_context_completeness():
    """Verify all required context is loaded"""
    errors = []
    
    # Check company context
    mission_file = Path("context/company_info/mission_vision_values.yaml")
    if not mission_file.exists():
        errors.append(f"Missing {mission_file}")
    else:
        with open(mission_file) as f:
            data = yaml.safe_load(f)
            # Verify 10 core values are present in the body
            if 'body' not in data or '| 10 |' not in data['body']:
                errors.append("Mission/values file missing all 10 core values")
    
    # Check team context
    team_file = Path("context/teams/platform_development_team.yaml")
    if not team_file.exists():
        errors.append(f"Missing {team_file}")
    
    # Check hiring process context
    hiring_file = Path("context/hr_processes/hiring/hiring_stages.yaml")
    if not hiring_file.exists():
        errors.append(f"Missing {hiring_file}")
    
    # Check technical problem bank
    problems_dir = Path("artifacts/public/hiring/pair_programming")
    if not problems_dir.exists():
        errors.append(f"Missing {problems_dir}")
    else:
        for level in ['easy.md', 'intermediate.md', 'expert.md']:
            if not (problems_dir / level).exists():
                errors.append(f"Missing technical problems: {problems_dir / level}")
    
    return errors

if __name__ == "__main__":
    errors = check_context_completeness()
    if errors:
        print("❌ Context loading incomplete:")
        for error in errors:
            print(f"  - {error}")
        exit(1)
    else:
        print("✅ All required context loaded successfully")
```

## Agent-Specific Loading Procedures

### For Claude Code
1. Follow the standard context loading procedure above
2. Reference CLAUDE.md for additional project-specific guidance
3. Use TodoWrite tool to track context loading steps
4. Validate context completeness before starting main task

### For Gemini CLI
1. Load context using the ReAct methodology (Reason → Act → Observe → Repeat)
2. Use `load_context("*")` command to ingest all context/*.yaml files
3. Follow .gemini/GEMINI.md guidelines for context engineering protocol
4. Execute context completeness verification before proceeding

### For KIRO
1. Follow .kiro/steering/context-engineering.md guidelines
2. Use KIRO-specific context validation rules
3. Maintain consistency with other agents' context loading
4. Apply HR domain-specific validation

## Context Loading Error Handling

### Missing Context Files
If any required context file is missing:
1. **Stop task execution immediately**
2. **Report specific missing files**
3. **Request the files from the task provider**
4. **Wait for complete context before resuming**

### Invalid Context Data
If context data is malformed or incomplete:
1. **Identify specific validation errors**
2. **Report the issues with file paths and line numbers**
3. **Request corrected context data**
4. **Re-validate before proceeding**

### Stale Context Data
If context data is older than 30 days:
1. **Warn about potentially stale data**
2. **Request confirmation to proceed**
3. **Note the staleness in task execution logs**

## Context Caching and Performance

### Caching Strategy
- **Session-level caching**: Cache context data for the duration of an agent session
- **Context invalidation**: Refresh cache when context files are modified
- **Memory management**: Limit cached context to essential data only

### Performance Optimization
- **Lazy loading**: Load specific context only when required for the task
- **Batch loading**: Load related context files together
- **Compression**: Use compressed storage for large context files

## Integration with Existing Workflows

### Interview Kit Generation Workflow
```bash
# 1. Load complete context (Phases 1-4)
python scripts/validate_hr_context.py

# 2. Generate interview kit
gemini run \
  --prompt "ai_docs/prompts/hiring/generate_interview_kit_prompt.md" \
  --context "data/public/hiring/resume/{candidate_file}.json"

# 3. Validate generated outputs
ls artifacts/public/hiring/interview_materials/upcoming/{candidate_id}/
```

### Candidate Screening Workflow
```bash
# 1. Load screening context
cat context/company_info/mission_vision_values.yaml
cat context/teams/platform_development_team.yaml

# 2. Process candidate data
python scripts/screen_candidates.py

# 3. Generate screening reports
# Store in artifacts/private/hiring/screening_reports/
```

### Performance Evaluation Workflow
```bash
# 1. Load performance context
cat context/hr_processes/evaluation/performance_review_process.yaml
cat context/company_info/goals_okrs.yaml

# 2. Load employee data and history
# Process evaluation according to loaded context

# 3. Generate evaluation reports
# Store in artifacts/private/evaluation/
```

## Quality Assurance

### Context Loading Audit Trail
All agents must maintain logs of:
- Which context files were loaded and when
- Any validation errors or warnings
- Context cache hits/misses
- Performance metrics for context loading

### Regular Context Review
- **Weekly**: Review context freshness and completeness
- **Monthly**: Validate context accuracy against current processes
- **Quarterly**: Update context organization and structure
- **As needed**: Update context when processes change

## Troubleshooting Common Issues

### Issue: "Context file not found"
**Solution**: 
```bash
# Verify directory structure
find context -type f -name "*.yaml" | sort

# Check file permissions
ls -la context/company_info/mission_vision_values.yaml
```

### Issue: "Invalid YAML syntax"
**Solution**:
```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('context/company_info/mission_vision_values.yaml'))"

# Check for common issues (tabs vs spaces, quotes, etc.)
```

### Issue: "Incomplete candidate data"
**Solution**:
```bash
# Validate candidate JSON schema
python scripts/validate_candidate_data.py data/public/hiring/resume/

# Check required fields
jq '.candidate_id, .name, .experience' data/public/hiring/resume/candidate.json
```

### Issue: "Missing technical problems"
**Solution**:
```bash
# Verify problem bank completeness
ls artifacts/public/hiring/pair_programming/
cat artifacts/public/hiring/pair_programming/easy.md | head -5
```

## Success Metrics

### Context Loading Effectiveness
- **Context completeness**: 100% of required context loaded before task execution
- **Loading performance**: Context loading completes within 30 seconds
- **Cache hit rate**: >80% for repeated context access
- **Validation success**: 100% of context passes validation checks

### Task Quality Improvements
- **Interview kit quality**: Generated materials reference complete company context
- **Candidate assessment accuracy**: Evaluations align with company values and processes
- **Process consistency**: All agents use identical context and produce consistent outputs
- **Error reduction**: Context-related errors reduced by >90%

---

**Usage Note**: This procedure must be followed by all AI agents (Claude Code, Gemini CLI, KIRO) before executing any HR automation tasks. The procedure ensures consistent, context-aware operations across the entire Gefjon Growth HR automation platform.