#!/usr/bin/env node
/**
 * Skill Activation Prompt Hook
 *
 * Automatically suggests relevant skills based on user prompts and file context.
 * Triggered on UserPromptSubmit events.
 */

import { readFileSync } from 'fs';
import { join } from 'path';

interface SkillRule {
  id: string;
  name: string;
  description: string;
  type: 'guardrail' | 'domain';
  enforcement: 'block' | 'suggest' | 'warn';
  priority: 'critical' | 'high' | 'medium' | 'low';
  triggers: {
    keywords?: string[];
    intentPatterns?: string[];
    filePatterns?: string[];
    contentPatterns?: string[];
  };
  skipConditions?: {
    commentMarker?: string;
    sessionSkillUsed?: boolean;
  };
}

interface SkillRules {
  skills: SkillRule[];
}

interface HookInput {
  prompt: string;
  context?: {
    modifiedFiles?: string[];
    sessionHistory?: any[];
  };
}

interface MatchedSkill {
  skill: SkillRule;
  matchedOn: string[];
}

const PRIORITY_ORDER = {
  critical: 0,
  high: 1,
  medium: 2,
  low: 3,
};

function loadSkillRules(): SkillRules {
  // Get project directory - if running from hooks/, go up two levels to project root
  let projectDir = process.env.CLAUDE_PROJECT_DIR;

  if (!projectDir) {
    // If no env var, assume we're in .claude/hooks and go up two levels
    projectDir = join(process.cwd(), '..', '..');
  }

  const rulesPath = join(projectDir, '.claude', 'skills', 'skill-rules.json');

  try {
    const content = readFileSync(rulesPath, 'utf-8');
    return JSON.parse(content);
  } catch (error) {
    console.error(`Error loading skill-rules.json: ${error}`);
    console.error(`Tried to load from: ${rulesPath}`);
    process.exit(1);
  }
}

function matchSkills(input: HookInput, rules: SkillRules): MatchedSkill[] {
  const matches: MatchedSkill[] = [];
  const promptLower = input.prompt.toLowerCase();

  for (const skill of rules.skills) {
    const matchedOn: string[] = [];

    // Keyword matching
    if (skill.triggers.keywords) {
      for (const keyword of skill.triggers.keywords) {
        if (promptLower.includes(keyword.toLowerCase())) {
          matchedOn.push(`keyword: "${keyword}"`);
        }
      }
    }

    // Intent pattern matching (regex)
    if (skill.triggers.intentPatterns) {
      for (const pattern of skill.triggers.intentPatterns) {
        const regex = new RegExp(pattern, 'i');
        if (regex.test(input.prompt)) {
          matchedOn.push(`pattern: ${pattern}`);
        }
      }
    }

    // File pattern matching (if file context is available)
    if (skill.triggers.filePatterns && input.context?.modifiedFiles) {
      for (const filePattern of skill.triggers.filePatterns) {
        const regex = new RegExp(filePattern);
        for (const file of input.context.modifiedFiles) {
          if (regex.test(file)) {
            matchedOn.push(`file: ${file}`);
          }
        }
      }
    }

    if (matchedOn.length > 0) {
      matches.push({ skill, matchedOn });
    }
  }

  // Sort by priority
  matches.sort((a, b) => {
    return PRIORITY_ORDER[a.skill.priority] - PRIORITY_ORDER[b.skill.priority];
  });

  return matches;
}

function formatOutput(matches: MatchedSkill[]): string {
  if (matches.length === 0) {
    return '';
  }

  const lines: string[] = [];
  lines.push('## 🎯 Relevant Skills Detected\n');
  lines.push('The following skills may help with this task:\n');

  const groupedByPriority: Record<string, MatchedSkill[]> = {};
  for (const match of matches) {
    const priority = match.skill.priority;
    if (!groupedByPriority[priority]) {
      groupedByPriority[priority] = [];
    }
    groupedByPriority[priority].push(match);
  }

  // Output by priority
  for (const priority of ['critical', 'high', 'medium', 'low'] as const) {
    const group = groupedByPriority[priority];
    if (!group || group.length === 0) continue;

    const icon = priority === 'critical' ? '🚨' : priority === 'high' ? '⚡' : priority === 'medium' ? '📋' : '💡';
    lines.push(`### ${icon} ${priority.toUpperCase()} Priority\n`);

    for (const match of group) {
      const { skill, matchedOn } = match;

      if (skill.enforcement === 'block') {
        lines.push(`❌ **BLOCKED: ${skill.name}**`);
        lines.push(`   ${skill.description}`);
        lines.push(`   **Action Required:** This action is blocked. Please review and ensure compliance.`);
      } else if (skill.enforcement === 'warn') {
        lines.push(`⚠️  **WARNING: ${skill.name}**`);
        lines.push(`   ${skill.description}`);
      } else {
        lines.push(`✅ **${skill.name}**`);
        lines.push(`   ${skill.description}`);
        lines.push(`   **Usage:** \`/skill ${skill.id}\``);
      }

      lines.push(`   *Matched on: ${matchedOn.join(', ')}*\n`);
    }
  }

  lines.push('---');
  lines.push('💡 **Tip:** Use the Skill tool to invoke these skills before proceeding with your task.\n');

  return lines.join('\n');
}

async function main() {
  try {
    // Read input from stdin
    let inputData = '';
    process.stdin.setEncoding('utf-8');

    for await (const chunk of process.stdin) {
      inputData += chunk;
    }

    const input: HookInput = JSON.parse(inputData);
    const rules = loadSkillRules();
    const matches = matchSkills(input, rules);
    const output = formatOutput(matches);

    if (output) {
      console.log(output);
    }
  } catch (error) {
    console.error(`Hook execution error: ${error}`);
    process.exit(1);
  }
}

main();
