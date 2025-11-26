# Claude Code Hooks for Gefjon Growth

This directory contains hooks that automatically suggest relevant skills based on user prompts and file context. Hooks are scripts that execute at specific points in Claude's workflow to enhance automation and improve the development experience.

## Overview

The hooks infrastructure enables Claude Code to:
- **Automatically suggest relevant skills** based on your prompts and context
- **Prevent common mistakes** by suggesting guardrail skills before problematic actions
- **Improve workflow efficiency** by proactively recommending the right tools

## Architecture

```
.claude/
├── hooks/
│   ├── skill-activation-prompt.ts     # TypeScript implementation
│   ├── skill-activation-prompt.sh     # Bash wrapper script
│   ├── package.json                    # npm dependencies (tsx, typescript)
│   └── README.md                       # This file
├── skills/
│   ├── skill-rules.json                # Skill trigger definitions
│   └── [skill-name]/
│       └── SKILL.md                    # Individual skill definitions
└── settings.json                        # Hook registration
```

## How It Works

### 1. Hook Execution Flow

```
User submits prompt → UserPromptSubmit event → skill-activation-prompt.sh →
skill-activation-prompt.ts → Reads skill-rules.json → Matches keywords/patterns →
Outputs skill suggestions → Claude receives and considers suggestions
```

### 2. Trigger Matching

The hook matches skills using three mechanisms:

#### a) **Keyword Matching**
Direct string inclusion checks against configured terms (case-insensitive).

**Example:**
```json
"keywords": ["generate screening", "screen candidates", "screening report"]
```
User prompt: "I want to screen candidates for the hiring process"
→ Matches: `generate-screening` skill

#### b) **Intent Pattern Matching**
Regular expression evaluation for complex intent detection.

**Example:**
```json
"intentPatterns": [
  "(generate|create|produce).{0,20}screening",
  "(screen|assess|evaluate).{0,20}candidate"
]
```
User prompt: "Create a comprehensive screening for all applicants"
→ Matches: `generate-screening` skill

#### c) **File Pattern Matching**
Context-aware suggestions based on modified or accessed files.

**Example:**
```json
"filePatterns": [
  "artifacts/public/hiring/candidates/.*/screening/.*"
]
```
When editing: `artifacts/public/hiring/candidates/20250811/atlas_001/screening/screening_report.md`
→ Suggests: `generate-screening` skill

### 3. Priority and Enforcement

Skills are organized by:

- **Priority Levels**: `critical` > `high` > `medium` > `low`
- **Enforcement Types**:
  - `suggest`: Recommends the skill (most common)
  - `warn`: Shows warning but allows proceeding
  - `block`: Prevents action until reviewed (use sparingly)

## Available Skills

### Critical Priority

1. **hiring-pipeline-orchestrator** - Orchestrates complete hiring workflow end-to-end
   - Triggers: "complete hiring pipeline", "full hiring workflow", "end-to-end hiring"

### High Priority

2. **validate-context** - Validates required context files before pipeline operations
   - Triggers: "validate context", "check context", "verify context"

3. **process-candidates** - Normalizes and validates candidate resume data
   - Triggers: "process candidates", "normalize candidate data", "prepare candidates"

4. **generate-screening** - Generates 4-dimensional candidate assessments
   - Triggers: "generate screening", "screen candidates", "screening report"

5. **generate-takehome** - Creates personalized take-home assignments
   - Triggers: "generate take-home", "takehome assignment", "create assignment"

6. **evaluate-takehome** - Evaluates submitted assignments with rubric scoring
   - Triggers: "evaluate take-home", "score assignment", "review submission"

7. **generate-interview-kit** - Creates hybrid interview materials (60% BEI + 40% Technical)
   - Triggers: "generate interview", "interview kit", "BEI questions"

8. **verify-completeness** - Validates all required materials exist
   - Triggers: "verify completeness", "quality check", "validate materials"

9. **generate-summary** - Creates comprehensive hiring summary reports
   - Triggers: "generate summary", "hiring summary", "final report"

### Medium Priority

10. **execute-postprocessing** - Runs Python post-processing scripts
    - Triggers: "post-process", "format outputs", "run python scripts"

11. **consolidate-results** - Organizes materials into standardized structure
    - Triggers: "consolidate results", "organize materials", "organize outputs"

## Configuration

### skill-rules.json Structure

```json
{
  "skills": [
    {
      "id": "skill-identifier",
      "name": "Human-Readable Skill Name",
      "description": "What this skill does and when to use it",
      "type": "domain" | "guardrail",
      "enforcement": "suggest" | "warn" | "block",
      "priority": "critical" | "high" | "medium" | "low",
      "triggers": {
        "keywords": ["keyword1", "keyword2"],
        "intentPatterns": ["regex1", "regex2"],
        "filePatterns": ["path/pattern/*.md"]
      }
    }
  ]
}
```

### settings.json Registration

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/skill-activation-prompt.sh"
          }
        ]
      }
    ]
  }
}
```

## Example Output

When you type: **"I want to generate screening reports for all candidates"**

Claude Code will show:

```
## 🎯 Relevant Skills Detected

The following skills may help with this task:

### ⚡ HIGH Priority

✅ **Generate Screening**
   Generates comprehensive AI-powered screening reports using 4-dimensional assessment
   methodology (Technical/Experience/Culture/Career). Use this to create initial
   candidate assessments.
   **Usage:** `/skill generate-screening`
   *Matched on: keyword: "generate screening", pattern: (generate|create).{0,20}screening*

✅ **Validate Context**
   Validates that all required context files (company info, HR processes, team data)
   exist and are accessible before starting the hiring workflow.
   **Usage:** `/skill validate-context`
   *Matched on: pattern: before.{0,10}(starting|running).{0,20}(hiring|pipeline)*

---
💡 **Tip:** Use the Skill tool to invoke these skills before proceeding with your task.
```

## Adding New Skills

To add a new skill:

1. **Create the skill directory and SKILL.md**:
   ```bash
   mkdir -p .claude/skills/my-new-skill
   # Create SKILL.md with skill instructions
   ```

2. **Add skill entry to skill-rules.json**:
   ```json
   {
     "id": "my-new-skill",
     "name": "My New Skill",
     "description": "What this skill does",
     "type": "domain",
     "enforcement": "suggest",
     "priority": "medium",
     "triggers": {
       "keywords": ["my keyword", "another keyword"],
       "intentPatterns": ["(my|pattern).*regex"]
     }
   }
   ```

3. **Test the trigger**:
   Use a prompt containing your keywords and verify the skill is suggested.

## Modifying Existing Skills

To adjust when a skill triggers:

1. **Edit `.claude/skills/skill-rules.json`**
2. **Modify the triggers section**:
   - Add/remove keywords
   - Update intent patterns
   - Change file patterns
3. **Adjust priority or enforcement** if needed
4. **Test with sample prompts**

## Development

### Requirements

- Node.js ≥18.0.0
- npm (for installing dependencies)
- tsx (TypeScript execution engine)

### Installation

Dependencies are automatically installed via:
```bash
cd .claude/hooks
npm install
```

### Testing the Hook Manually

```bash
# Test with sample input
echo '{"prompt":"generate screening reports"}' | .claude/hooks/skill-activation-prompt.sh
```

### Debugging

Enable debug output by modifying `skill-activation-prompt.ts`:
```typescript
console.error(`[DEBUG] Loaded ${rules.skills.length} skills`);
console.error(`[DEBUG] Matching prompt: ${input.prompt}`);
```

## Best Practices

### 1. Keyword Selection
- Use **natural language phrases** users would actually type
- Include **variations and synonyms** (e.g., "take-home", "takehome", "take home")
- Avoid **overly generic terms** that match too broadly

### 2. Intent Patterns
- Use `.{0,20}` for flexible spacing between key terms
- Test patterns with **multiple sample prompts**
- Keep patterns **specific but not overly restrictive**

### 3. Priority Assignment
- **Critical**: Skills required for complete workflows or major operations
- **High**: Skills for key tasks (screening, interviews, validation)
- **Medium**: Supporting tasks (formatting, organization)
- **Low**: Optional enhancements or utilities

### 4. Enforcement Strategy
- **Suggest** (default): Recommend but don't block
- **Warn**: Show caution for potentially risky operations
- **Block**: Reserve for critical guardrails (use sparingly)

## Troubleshooting

### Hook Not Triggering

1. **Check settings.json registration**:
   ```bash
   cat .claude/settings.json
   ```

2. **Verify script permissions**:
   ```bash
   ls -l .claude/hooks/skill-activation-prompt.sh
   # Should show: -rwxr-xr-x
   ```

3. **Test hook manually**:
   ```bash
   echo '{"prompt":"test"}' | .claude/hooks/skill-activation-prompt.sh
   ```

### No Skill Matches

1. **Review skill-rules.json** for typos
2. **Check keyword case sensitivity** (should be lowercase)
3. **Test intent patterns** with regex tools
4. **Add debug logging** to see matching process

### TypeScript Errors

1. **Reinstall dependencies**:
   ```bash
   cd .claude/hooks
   rm -rf node_modules package-lock.json
   npm install
   ```

2. **Verify Node.js version**:
   ```bash
   node --version  # Should be ≥18.0.0
   ```

## Future Enhancements

Potential improvements to consider:

- **PostToolUse Hook**: Track file modifications to suggest relevant follow-up skills
- **Stop Hook**: Validate completeness after workflow completion
- **Context-Aware Matching**: Use ML for better intent detection
- **Skill Dependencies**: Automatically suggest prerequisite skills
- **Usage Analytics**: Track which skills are most useful

## References

- [Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [GitHub Example: claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase/tree/main/.claude/hooks)
- [Project CLAUDE.md](../../CLAUDE.md) - Project-specific instructions

## Support

For issues or questions:
1. Check this README and troubleshooting section
2. Review skill-rules.json for trigger definitions
3. Test hooks manually with sample inputs
4. Consult Claude Code documentation

---

**Version**: 1.0.0
**Last Updated**: 2025-11-25
**Maintainer**: Gefjon Growth Team
