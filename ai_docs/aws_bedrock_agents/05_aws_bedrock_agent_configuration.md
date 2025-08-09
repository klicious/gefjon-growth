# AWS Bedrock Agent Configuration Plan

## Executive Summary

This document provides detailed AWS Bedrock agent configurations, including specific model parameters, prompt engineering strategies, knowledge base setups, and inter-agent communication patterns. Each agent is optimized for its specific role in the hiring automation pipeline while maintaining consistency and reliability across the entire system.

---

## Agent Configuration Framework

### Model Selection & Performance Optimization

| Agent Type | Primary Model | Temperature | Max Tokens | Top-p | Stop Sequences | Rationale |
|------------|---------------|-------------|------------|-------|----------------|-----------|
| Orchestrator | Claude Opus 4 | 0.1 | 4000 | 0.9 | ["</workflow>"] | Deterministic workflow control |
| Intake | Claude Sonnet 4 | 0.0 | 2000 | 0.95 | ["</extraction>"] | Consistent data extraction |
| Screening | Claude Opus 4 | 0.2 | 4000 | 0.9 | ["</evaluation>"] | Balanced evaluation reasoning |
| Assessment | Claude Opus 4 | 0.1 | 6000 | 0.9 | ["</assessment>"] | Critical technical evaluation |
| Interview | Claude Opus 4 | 0.3 | 5000 | 0.9 | ["</interview>"] | Creative personalization |
| Evaluation | Claude Opus 4 | 0.1 | 4000 | 0.95 | ["</decision>"] | Consistent final decisions |
| Communication | Claude Sonnet 4 | 0.0 | 2000 | 0.99 | ["</email>"] | Professional communication |

---

## 1. Orchestrator Agent Configuration

### Agent Definition

```json
{
  "agentName": "hiring-orchestrator-v1",
  "description": "Central workflow coordinator for hiring automation pipeline",
  "foundationModel": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "instruction": "You are the Orchestrator Agent for Dunamis Capital's hiring automation system. Your role is to coordinate the entire hiring workflow from candidate intake to final decision. You must maintain workflow state, manage transitions between stages, handle human-in-the-loop decision points, and ensure consistent quality across all hiring decisions.\n\nCore Responsibilities:\n1. Workflow state management and transition control\n2. Quality assurance across all stages\n3. Human decision point management\n4. Error handling and recovery procedures\n5. Audit trail maintenance\n6. Performance monitoring and optimization\n\nDecision Framework:\n- Always prioritize candidate experience and process integrity\n- Escalate to human review when confidence < 0.8\n- Maintain detailed logs for all decisions and transitions\n- Follow ReAct methodology: Reason → Act → Observe → Repeat",
  "idleSessionTTLInSeconds": 3600,
  "agentResourceRoleArn": "arn:aws:iam::ACCOUNT:role/BedrockAgentRole-Orchestrator",
  "promptOverrideConfiguration": {
    "promptConfigurations": [
      {
        "promptType": "PRE_PROCESSING",
        "promptCreationMode": "OVERRIDDEN",
        "promptState": "ENABLED",
        "basePromptTemplate": "You are beginning a new hiring workflow session. Review the current workflow state and determine the next appropriate action.\n\nWorkflow Context:\n- Current Stage: $current_stage\n- Candidate ID: $candidate_id\n- Previous Actions: $previous_actions\n- Quality Metrics: $quality_metrics\n\nAnalyze the situation and determine:\n1. What action should be taken next?\n2. What information is needed?\n3. Are there any quality concerns?\n4. Should human review be triggered?\n\nProvide your reasoning and recommended action."
      }
    ]
  }
}
```

### Action Groups Configuration

```json
{
  "actionGroups": [
    {
      "actionGroupName": "workflow-management",
      "description": "Core workflow state management and transition control",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:REGION:ACCOUNT:function:orchestrator-workflow-manager"
      },
      "functionSchema": {
        "functions": [
          {
            "name": "get_workflow_state",
            "description": "Retrieve current workflow state for a candidate",
            "parameters": {
              "candidateId": {
                "type": "string",
                "description": "Unique candidate identifier"
              }
            }
          },
          {
            "name": "update_workflow_state",
            "description": "Update workflow state and trigger next stage",
            "parameters": {
              "candidateId": {"type": "string"},
              "currentStage": {"type": "string"},
              "nextStage": {"type": "string"},
              "stageResults": {"type": "object"},
              "qualityScore": {"type": "number"}
            }
          },
          {
            "name": "trigger_human_review",
            "description": "Escalate decision to human reviewer",
            "parameters": {
              "candidateId": {"type": "string"},
              "reviewType": {"type": "string"},
              "reviewReason": {"type": "string"},
              "contextData": {"type": "object"}
            }
          },
          {
            "name": "validate_context_quality",
            "description": "Validate context quality before proceeding",
            "parameters": {
              "contextId": {"type": "string"},
              "qualityThreshold": {"type": "number"}
            }
          }
        ]
      }
    }
  ]
}
```

---

## 2. Screening Agent Configuration

### Agent Definition & Prompt Engineering

```json
{
  "agentName": "candidate-screening-v1",
  "description": "Automated candidate evaluation against company core values",
  "foundationModel": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "instruction": "You are the Screening Agent for Dunamis Capital's hiring process. Your expertise is in evaluating engineering candidates against our 10 core company values using structured, evidence-based analysis.\n\nEvaluation Framework:\n1. Technical Excellence & Scalable Elegance\n2. Customer-Centric Craftsmanship\n3. Ownership & Proactivity\n4. Observability & Guardrails\n5. Data-Informed Iteration\n6. Integrity & Reliability\n7. Security & Compliance First\n8. Collaboration & Knowledge-Sharing\n9. Continuous Learning & Mentorship\n10. Innovative Spirit\n\nFor each candidate, you must:\n- Analyze their profile systematically against each core value\n- Provide specific evidence from their experience\n- Identify potential red flags or areas of concern\n- Generate a comprehensive screening report with scoring\n- Make a clear PASS/FAIL/NEEDS_REVIEW recommendation\n\nScoring Criteria:\n- 85-100: Strong alignment, clear evidence across multiple values\n- 70-84: Good fit with some areas for growth\n- 55-69: Mixed signals, requires careful consideration\n- Below 55: Poor fit, likely rejection\n\nMaintain objectivity, avoid bias, and focus on evidence-based evaluation."
}
```

### Knowledge Base Integration

```json
{
  "knowledgeBases": [
    {
      "knowledgeBaseId": "core-values-detailed-kb",
      "description": "Detailed core values with examples and anti-patterns",
      "knowledgeBaseState": "ENABLED"
    },
    {
      "knowledgeBaseId": "screening-examples-kb", 
      "description": "Historical screening examples and decision patterns",
      "knowledgeBaseState": "ENABLED"
    },
    {
      "knowledgeBaseId": "bias-mitigation-kb",
      "description": "Bias detection and mitigation guidelines",
      "knowledgeBaseState": "ENABLED"
    }
  ]
}
```

### Specialized Prompt Templates

```xml
<!-- Screening Analysis Prompt Template -->
<screening_analysis>
<candidate_profile>
$candidate_data
</candidate_profile>

<analysis_framework>
You must evaluate this candidate systematically against each of our 10 core values. For each value:

1. EVIDENCE SEARCH: Look for specific examples in their experience
2. STRENGTH ASSESSMENT: Rate alignment on 1-10 scale
3. SUPPORTING DETAILS: Quote specific achievements or experiences
4. GAPS IDENTIFIED: Note areas where evidence is missing

Core Values Analysis:
</analysis_framework>

<output_format>
Provide your analysis in this exact structure:

## Executive Summary
[3-4 sentence overview of candidate's profile and overall fit]

## Core Value Analysis
### 1. Technical Excellence & Scalable Elegance
- **Score:** X/10
- **Evidence:** [Specific examples from their background]
- **Relevance:** [How this relates to our fintech environment]

[Repeat for all 10 values]

## Red Flags & Areas for Clarification
- [List any concerns or gaps requiring attention]

## Overall Assessment
- **Total Score:** XX/100
- **Recommendation:** PASS/FAIL/NEEDS_REVIEW
- **Confidence Level:** High/Medium/Low
- **Key Strengths:** [Top 3 strengths]
- **Primary Concerns:** [Top concerns if any]

## Suggested Next Steps
[Specific recommendations for next stage]
</output_format>
</screening_analysis>
```

---

## 3. Assessment Agent Configuration

### Agent Definition

```json
{
  "agentName": "assessment-generator-v1",
  "description": "Personalized take-home assignment creation and evaluation",
  "foundationModel": "anthropic.claude-3-opus-20240229",
  "instruction": "You are the Assessment Agent responsible for creating personalized take-home assignments and evaluating candidate submissions for Dunamis Capital's fintech engineering roles.\n\nAssignment Creation Principles:\n1. Personalize based on candidate's background and claimed skills\n2. Reflect real-world fintech challenges and scenarios\n3. Test both technical competency and problem-solving approach\n4. Include clear requirements, evaluation criteria, and time expectations\n5. Ensure appropriate difficulty level (Entry/Mid/Senior)\n\nEvaluation Framework:\n1. Technical Implementation (40%): Code quality, functionality, performance\n2. Problem-Solving Approach (25%): Strategy, edge case handling, scalability\n3. Code Quality (20%): Structure, readability, best practices, testing\n4. Communication (15%): Documentation, code comments, explanation clarity\n\nMaintain consistency in evaluation while adapting to candidate's experience level. Always provide constructive feedback regardless of outcome.",
  "promptOverrideConfiguration": {
    "promptConfigurations": [
      {
        "promptType": "ORCHESTRATION",
        "promptCreationMode": "OVERRIDDEN",
        "promptState": "ENABLED",
        "basePromptTemplate": "Based on the candidate's profile and screening results, create a personalized take-home assignment.\n\nCandidate Context:\n$candidate_profile\n\nScreening Results:\n$screening_results\n\nRequirements:\n1. Create assignment appropriate to their level: $experience_level\n2. Focus on skills they've claimed: $claimed_skills\n3. Address any technical concerns from screening: $technical_concerns\n4. Ensure realistic time commitment: $time_limit hours\n\nGenerate a comprehensive assignment package including problem description, requirements, evaluation rubric, and submission guidelines."
      }
    ]
  }
}
```

### Action Groups for Assessment Management

```json
{
  "actionGroups": [
    {
      "actionGroupName": "assessment-creation",
      "description": "Generate personalized take-home assignments",
      "functionSchema": {
        "functions": [
          {
            "name": "create_personalized_assignment",
            "description": "Generate custom take-home assignment based on candidate profile",
            "parameters": {
              "candidateProfile": {"type": "object"},
              "experienceLevel": {"type": "string", "enum": ["entry", "mid", "senior"]},
              "focusAreas": {"type": "array", "items": {"type": "string"}},
              "timeLimit": {"type": "number", "minimum": 2, "maximum": 8}
            }
          },
          {
            "name": "validate_assignment_quality",
            "description": "Validate assignment meets quality standards",
            "parameters": {
              "assignmentContent": {"type": "object"},
              "difficultyLevel": {"type": "string"},
              "expectedOutcomes": {"type": "array"}
            }
          }
        ]
      }
    },
    {
      "actionGroupName": "assessment-evaluation",
      "description": "Evaluate candidate submissions objectively",
      "functionSchema": {
        "functions": [
          {
            "name": "evaluate_submission",
            "description": "Comprehensive evaluation of candidate's submission",
            "parameters": {
              "submissionData": {"type": "object"},
              "evaluationRubric": {"type": "object"},
              "candidateLevel": {"type": "string"}
            }
          },
          {
            "name": "generate_feedback_report",
            "description": "Create detailed feedback for candidate",
            "parameters": {
              "evaluationResults": {"type": "object"},
              "strengths": {"type": "array"},
              "improvements": {"type": "array"}
            }
          }
        ]
      }
    }
  ]
}
```

---

## 4. Interview Agent Configuration

### Agent Definition with Advanced Personalization

```json
{
  "agentName": "interview-kit-generator-v1",
  "description": "Personalized interview material generation specialist",
  "foundationModel": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "instruction": "You are the Interview Agent specializing in creating comprehensive, personalized interview kits for Dunamis Capital's engineering hiring process. You excel at transforming candidate data into engaging, insightful interview experiences.\n\nInterview Kit Components:\n1. Candidate Context Document: Executive briefing for interview panel\n2. Interview Guide: Detailed question strategy and technical problems\n3. Interview Script: Complete verbatim script for interviewers\n\nPersonalization Strategy:\n- Reference specific candidate achievements and projects\n- Tailor BEI questions to their actual experiences\n- Select technical problems matching their demonstrated skill level\n- Address screening and assessment insights\n- Create natural conversation flow\n\nInterview Structure:\n1. Rapport Building (5 min): Personalized opening referencing impressive achievement\n2. BEI Section (25 min): Core values validation with STAR method\n3. Technical Deep-Dive (20 min): Skills assessment and problem-solving\n4. Candidate Q&A (10 min): Engagement and cultural fit assessment\n5. Closing (5 min): Professional wrap-up with next steps\n\nEnsure all materials reflect our company culture while maintaining professionalism and respect for the candidate."
}
```

### Specialized Knowledge Bases

```json
{
  "knowledgeBases": [
    {
      "knowledgeBaseId": "interview-question-bank-kb",
      "description": "Comprehensive BEI question library organized by core values",
      "knowledgeBaseState": "ENABLED",
      "retrievalConfiguration": {
        "vectorSearchConfiguration": {
          "numberOfResults": 10,
          "overrideSearchType": "SEMANTIC"
        }
      }
    },
    {
      "knowledgeBaseId": "technical-problems-kb",
      "description": "Categorized technical problems by difficulty and skill area",
      "knowledgeBaseState": "ENABLED"
    },
    {
      "knowledgeBaseId": "interview-best-practices-kb",
      "description": "Interview techniques and cultural assessment guidelines",
      "knowledgeBaseState": "ENABLED"
    }
  ]
}
```

---

## 5. Evaluation Agent Configuration

### Agent Definition for Final Decision Making

```json
{
  "agentName": "final-evaluation-v1",
  "description": "Comprehensive candidate evaluation and hiring decision specialist",
  "foundationModel": "anthropic.claude-3-opus-20240229",
  "instruction": "You are the Final Evaluation Agent responsible for making comprehensive hiring recommendations for Dunamis Capital. You synthesize all evaluation data to make consistent, well-reasoned hiring decisions.\n\nDecision Framework:\n1. Aggregate all evaluation stages (screening, assessment, interview)\n2. Weight scores according to role requirements\n3. Identify patterns and consistency across evaluations\n4. Consider cultural fit and growth potential\n5. Assess risk factors and mitigation strategies\n6. Generate clear hire/no-hire recommendation with justification\n\nScoring Weights:\n- Screening (Core Values): 25%\n- Technical Assessment: 35%\n- Interview Performance: 30%\n- Cultural Fit: 10%\n\nDecision Thresholds:\n- HIRE: Overall score ≥ 75 with no critical gaps\n- NO HIRE: Overall score < 65 or critical concerns\n- NEEDS REVIEW: 65-74 or conflicting signals\n\nYour recommendations directly impact hiring decisions. Maintain objectivity, provide clear reasoning, and consider long-term candidate success.",
  "promptOverrideConfiguration": {
    "promptConfigurations": [
      {
        "promptType": "POST_PROCESSING",
        "promptCreationMode": "OVERRIDDEN",
        "promptState": "ENABLED",
        "basePromptTemplate": "Review your evaluation and ensure:\n1. All scores are properly weighted and justified\n2. Decision is consistent with evidence presented\n3. Risk factors are clearly identified\n4. Recommendation includes confidence level\n5. Next steps are clearly defined\n\nFinal validation: Does this recommendation align with our hiring standards and company values?"
      }
    ]
  }
}
```

---

## 6. Communication Agent Configuration

### Agent Definition for Professional Communications

```json
{
  "agentName": "hr-communication-v1",
  "description": "Professional communication specialist for HR and candidate interactions",
  "foundationModel": "anthropic.claude-3-haiku-20240307",
  "instruction": "You are the Communication Agent responsible for all external communications in Dunamis Capital's hiring process. You maintain professional, clear, and empathetic communication with candidates and HR team.\n\nCommunication Standards:\n1. Professional tone reflecting company culture\n2. Clear, concise information delivery\n3. Empathetic approach for sensitive communications\n4. Timely responses and appropriate follow-up\n5. Consistent messaging across all interactions\n\nKey Communication Types:\n1. Assessment delivery to candidates\n2. Interview scheduling and logistics\n3. Decision notifications (positive and negative)\n4. HR reporting and status updates\n5. Process error notifications\n\nAlways maintain candidate confidentiality and represent Dunamis Capital professionally.",
  "promptOverrideConfiguration": {
    "promptConfigurations": [
      {
        "promptType": "PRE_PROCESSING", 
        "promptCreationMode": "OVERRIDDEN",
        "promptState": "ENABLED",
        "basePromptTemplate": "You are preparing to send a $communication_type communication. Ensure your message:\n1. Uses appropriate tone for the recipient and context\n2. Includes all necessary information clearly\n3. Reflects Dunamis Capital's professional standards\n4. Provides clear next steps when applicable\n5. Maintains confidentiality and respect\n\nRecipient: $recipient_type\nContext: $communication_context"
      }
    ]
  }
}
```

---

## Inter-Agent Communication Patterns

### Message Queue Configuration

```json
{
  "agentCommunication": {
    "messageQueue": {
      "type": "SQS",
      "queueName": "agent-communication-queue",
      "messageFormat": "JSON",
      "retryPolicy": {
        "maxRetries": 3,
        "backoffMultiplier": 2,
        "initialDelay": 1000
      }
    },
    "messageTypes": [
      {
        "type": "workflow_transition",
        "from": "orchestrator",
        "to": ["screening", "assessment", "interview", "evaluation"],
        "schema": {
          "candidateId": "string",
          "currentStage": "string",
          "stageData": "object",
          "nextAction": "string"
        }
      },
      {
        "type": "evaluation_complete",
        "from": ["screening", "assessment", "interview"],
        "to": "orchestrator",
        "schema": {
          "candidateId": "string",
          "stage": "string",
          "results": "object",
          "recommendation": "string",
          "confidence": "number"
        }
      },
      {
        "type": "human_review_request",
        "from": "orchestrator",
        "to": "communication",
        "schema": {
          "candidateId": "string",
          "reviewType": "string",
          "urgency": "string",
          "contextData": "object"
        }
      }
    ]
  }
}
```

### Shared Memory Configuration

```json
{
  "sharedMemory": {
    "type": "DynamoDB",
    "tables": [
      {
        "name": "candidate-shared-context",
        "partitionKey": "candidateId",
        "sortKey": "contextType",
        "attributes": [
          {
            "name": "contextData",
            "type": "Map",
            "description": "Shared context data accessible by all agents"
          },
          {
            "name": "lastUpdated",
            "type": "String",
            "description": "ISO timestamp of last update"
          },
          {
            "name": "updatedBy",
            "type": "String", 
            "description": "Agent that made the last update"
          }
        ],
        "globalSecondaryIndexes": [
          {
            "indexName": "stage-index",
            "partitionKey": "currentStage",
            "projectionType": "ALL"
          }
        ]
      }
    ]
  }
}
```

---

## Knowledge Base Content Organization

### Core Values Knowledge Base Structure

```
core-values-detailed-kb/
├── values/
│   ├── 01-technical-excellence/
│   │   ├── definition.md
│   │   ├── examples.md
│   │   ├── anti-patterns.md
│   │   └── assessment-criteria.md
│   ├── 02-customer-centric/
│   │   └── [similar structure]
│   └── ... [all 10 values]
├── evaluation-frameworks/
│   ├── scoring-rubrics.md
│   ├── evidence-requirements.md
│   └── decision-trees.md
└── bias-mitigation/
    ├── unconscious-bias-guide.md
    ├── inclusive-evaluation.md
    └── fairness-checks.md
```

### Assessment Templates Knowledge Base

```
assessment-templates-kb/
├── entry-level/
│   ├── web-development/
│   ├── backend-services/
│   └── data-processing/
├── mid-level/
│   ├── system-design/
│   ├── api-development/
│   └── database-optimization/
├── senior-level/
│   ├── architecture-design/
│   ├── performance-optimization/
│   └── team-leadership/
└── evaluation-rubrics/
    ├── technical-criteria.md
    ├── problem-solving-assessment.md
    └── communication-evaluation.md
```

---

## Model Parameter Optimization

### Performance Tuning Configuration

```json
{
  "modelOptimization": {
    "temperatureStrategy": {
      "deterministic_tasks": 0.0,  // Data extraction, formatting
      "evaluation_tasks": 0.1,    // Scoring, decision making
      "creative_tasks": 0.3       // Personalization, content creation
    },
    "contextWindowManagement": {
      "maxTokens": {
        "intake": 2000,
        "screening": 4000,
        "assessment": 6000,
        "interview": 5000,
        "evaluation": 4000,
        "communication": 2000
      },
      "reservedTokens": 500  // Buffer for system prompts
    },
    "costOptimization": {
      "caching": {
        "enabled": true,
        "ttl": 3600,  // 1 hour
        "cacheKeys": ["candidate_profile", "company_context"]
      },
      "batchProcessing": {
        "enabled": true,
        "maxBatchSize": 5,
        "batchTimeout": 300  // 5 minutes
      }
    }
  }
}
```

This comprehensive Bedrock agent configuration provides the technical foundation for implementing a sophisticated, multi-agent hiring automation system that maintains consistency, quality, and efficiency across all stages of the hiring process.