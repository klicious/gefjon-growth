# Step Functions + JSONata + Bedrock Implementation Guide
*Devcraft Session Requirements: Agentic Workflows*

## Executive Summary

This document provides the complete technical implementation guide for our **Agentic Hiring Workflow** using **AWS Step Functions with JSONata** and **Amazon Bedrock Agents**. Following Devcraft session guidance, this implementation leverages state machines for orchestration, JSONata for intelligent data transformations, and Bedrock Agents for AI-powered decision making.

**Key Implementation Highlights:**
- **Complete State Machine Definition** for the entire hiring process
- **JSONata Expressions** for all data transformations and routing logic
- **Bedrock Agent Configurations** for each specialized hiring task
- **Human-in-the-Loop Integration** using waitForTaskToken pattern
- **Error Handling & Retry Logic** for production reliability

---

## Complete State Machine Definition

### **Master State Machine: Hiring Process Workflow**

```json
{
  "Comment": "AI-Powered Hiring Agentic Workflow - Devcraft Implementation",
  "StartAt": "ValidateInput",
  "TimeoutSeconds": 2592000,
  "States": {
    "ValidateInput": {
      "Type": "Pass",
      "Comment": "JSONata validation and normalization of candidate input",
      "Parameters": {
        "validatedCandidate.$": "$exists($.candidateData.resume) and $exists($.candidateData.email) ? $.candidateData : $error('Missing required fields: resume or email')",
        "processId.$": "$uuid()",
        "timestamp.$": "$now()",
        "source.$": "$.candidateData.source ? $.candidateData.source : 'unknown'",
        "normalizedEmail.$": "$lowercase($trim($.candidateData.email))",
        "metadata": {
          "workflowVersion": "2.0",
          "implementation": "step-functions-jsonata-bedrock"
        }
      },
      "ResultPath": "$.validated",
      "Next": "IntakeAgent"
    },

    "IntakeAgent": {
      "Type": "Task",
      "Comment": "Bedrock Agent for resume processing and data extraction",
      "Resource": "arn:aws:bedrock:us-east-1:account:agent/intake-agent-id",
      "Parameters": {
        "sessionId.$": "$.validated.processId",
        "inputText.$": "$string($.validated.validatedCandidate)",
        "enableTrace": true,
        "sessionAttributes": {
          "stage": "intake",
          "candidateSource.$": "$.validated.source",
          "timestamp.$": "$.validated.timestamp"
        }
      },
      "ResultPath": "$.intakeResult",
      "Retry": [
        {
          "ErrorEquals": ["Bedrock.ThrottlingException"],
          "IntervalSeconds": 2,
          "MaxAttempts": 3,
          "BackoffRate": 2.0
        },
        {
          "ErrorEquals": ["Bedrock.ValidationException"],
          "IntervalSeconds": 1,
          "MaxAttempts": 2
        }
      ],
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleIntakeError",
          "ResultPath": "$.error"
        }
      ],
      "Next": "TransformForScreening"
    },

    "TransformForScreening": {
      "Type": "Pass",
      "Comment": "JSONata transformation to prepare screening context",
      "Parameters": {
        "screeningInput.$": "$merge([$.intakeResult.candidateProfile, {\"companyContext\": $.companyContext, \"jobRequirements\": $.jobDescription.requirements, \"screeningCriteria\": $.companyContext.coreValues, \"candidateMetadata\": {\"processId\": $.validated.processId, \"source\": $.validated.source, \"intakeTimestamp\": $.validated.timestamp, \"completenessScore\": $.intakeResult.completenessScore}}])",
        "candidateId.$": "$.intakeResult.candidateId",
        "stage": "screening",
        "nextStagePrep": {
          "requiresHumanReview.$": "$.intakeResult.completenessScore < 80",
          "experienceLevel.$": "$.intakeResult.experienceLevel",
          "primarySkills.$": "$.intakeResult.candidateProfile.skills[0:5]"
        }
      },
      "ResultPath": "$.screeningPrep",
      "Next": "ScreeningAgent"
    },

    "ScreeningAgent": {
      "Type": "Task",
      "Comment": "Bedrock Agent for intelligent candidate screening",
      "Resource": "arn:aws:bedrock:us-east-1:account:agent/screening-agent-id",
      "Parameters": {
        "sessionId.$": "$.screeningPrep.candidateId",
        "inputText.$": "$string($.screeningPrep.screeningInput)",
        "enableTrace": true,
        "sessionAttributes": {
          "stage": "screening",
          "experienceLevel.$": "$.screeningPrep.nextStagePrep.experienceLevel",
          "primarySkills.$": "$join($.screeningPrep.nextStagePrep.primarySkills, ', ')"
        }
      },
      "ResultPath": "$.screeningResult",
      "Retry": [
        {
          "ErrorEquals": ["Bedrock.ThrottlingException"],
          "IntervalSeconds": 5,
          "MaxAttempts": 3,
          "BackoffRate": 2.0
        }
      ],
      "Next": "EvaluateScreeningResult"
    },

    "EvaluateScreeningResult": {
      "Type": "Choice",
      "Comment": "JSONata-based intelligent routing based on screening results",
      "Choices": [
        {
          "Comment": "Strong pass - proceed directly to assessment",
          "And": [
            {
              "Variable": "$.screeningResult.recommendation",
              "StringEquals": "PASS"
            },
            {
              "Variable": "$.screeningResult.confidence",
              "NumericGreaterThan": 0.8
            },
            {
              "Variable": "$.screeningResult.overallScore",
              "NumericGreaterThan": 7.5
            }
          ],
          "Next": "TransformForAssessment"
        },
        {
          "Comment": "Borderline pass - requires human review",
          "And": [
            {
              "Variable": "$.screeningResult.recommendation",
              "StringEquals": "PASS"
            },
            {
              "Variable": "$.screeningResult.confidence",
              "NumericLessThan": 0.8
            }
          ],
          "Next": "HumanScreeningReview"
        },
        {
          "Comment": "Needs review - human decision required",
          "Variable": "$.screeningResult.recommendation",
          "StringEquals": "NEEDS_REVIEW",
          "Next": "HumanScreeningReview"
        },
        {
          "Comment": "Clear fail with high confidence",
          "And": [
            {
              "Variable": "$.screeningResult.recommendation",
              "StringEquals": "FAIL"
            },
            {
              "Variable": "$.screeningResult.confidence",
              "NumericGreaterThan": 0.8
            }
          ],
          "Next": "SendScreeningRejection"
        }
      ],
      "Default": "HumanScreeningReview"
    }
  }
}
```

---

## JSONata Transformation Patterns

### **1. Input Validation & Normalization**
```javascript
// Comprehensive input validation with error handling
{
  "validatedCandidate": $exists($.candidateData.resume) and $exists($.candidateData.email) ? 
    $merge([
      $.candidateData,
      {
        "normalizedEmail": $lowercase($trim($.candidateData.email)),
        "resumeType": $substring($.candidateData.resume, -3),
        "submissionDate": $now(),
        "validationStatus": "passed"
      }
    ]) : $error("Missing required fields: resume or email"),
  
  "processMetadata": {
    "processId": $uuid(),
    "timestamp": $now(),
    "source": $.candidateData.source ? $.candidateData.source : "unknown",
    "workflowVersion": "2.0"
  }
}
```

### **2. Context Aggregation for Agents**
```javascript
// Merge candidate data with company context for screening
$merge([
  $.intakeResult.candidateProfile,
  {
    "evaluationContext": {
      "companyValues": $.companyContext.coreValues,
      "jobRequirements": $.jobDescription.requirements,
      "roleLevel": $.jobDescription.level,
      "teamContext": $.jobDescription.team
    },
    "candidateMetadata": {
      "processId": $.validated.processId,
      "source": $.validated.source,
      "completenessScore": $.intakeResult.completenessScore,
      "experienceLevel": $.intakeResult.experienceLevel
    },
    "evaluationCriteria": {
      "coreValueWeights": $.companyContext.screeningWeights,
      "technicalRequirements": $.jobDescription.technicalSkills,
      "experienceRequirements": $.jobDescription.experienceYears
    }
  }
])
```

### **3. Conditional Routing Logic**
```javascript
// Complex multi-criteria routing for screening results
$.screeningResult.recommendation = "PASS" and 
$.screeningResult.confidence > 0.8 and 
$.screeningResult.overallScore > 7.5 ? "DirectToAssessment" :

$.screeningResult.recommendation = "PASS" and 
$.screeningResult.confidence <= 0.8 ? "HumanReview" :

$.screeningResult.recommendation = "NEEDS_REVIEW" or
($.screeningResult.recommendation = "PASS" and 
 $count($.screeningResult.redFlags) > 0) ? "HumanReview" :

$.screeningResult.recommendation = "FAIL" and 
$.screeningResult.confidence > 0.8 ? "AutoReject" : "HumanReview"
```

### **4. Data Aggregation for Final Evaluation**
```javascript
// Comprehensive evaluation aggregation with weighted scoring
{
  "finalEvaluation": {
    "candidateId": $.candidateId,
    "overallScore": $round(($sum([
      $.screeningResult.overallScore * 0.25,
      $.assessmentResult.technicalScore * 0.35,
      $.assessmentResult.codeQualityScore * 0.15,
      $.interviewResult.technicalScore * 0.15,
      $.interviewResult.culturalFitScore * 0.10
    ])), 2),
    
    "categoryScores": {
      "technical": $round($average([
        $.assessmentResult.technicalScore,
        $.interviewResult.technicalScore
      ]), 2),
      "cultural": $round($average([
        $.screeningResult.cultureScore,
        $.interviewResult.culturalFitScore
      ]), 2),
      "communication": $.interviewResult.communicationScore,
      "problemSolving": $.assessmentResult.problemSolvingScore
    },
    
    "strengths": $distinct($append($append(
      $.screeningResult.strengths,
      $.assessmentResult.strengths
    ), $.interviewResult.strengths)),
    
    "concerns": $filter($append($append(
      $.screeningResult.concerns,
      $.assessmentResult.concerns
    ), $.interviewResult.concerns), function($v) { $v != null and $v != "" }),
    
    "recommendation": $overallScore >= 8.0 ? "STRONG_HIRE" :
                     $overallScore >= 7.0 ? "HIRE" :
                     $overallScore >= 6.0 ? "LEAN_HIRE" : "NO_HIRE",
    
    "confidence": $min([
      $.screeningResult.confidence,
      $.assessmentResult.confidence,
      $.interviewResult.confidence
    ]),
    
    "riskFactors": $filter([
      $.screeningResult.redFlags,
      $.assessmentResult.concerns,
      $.interviewResult.concerns
    ], function($v) { $count($v) > 0 })
  }
}
```

---

## Bedrock Agent Configurations

### **Intake Agent Configuration**
```yaml
IntakeAgent:
  agentId: "intake-agent-id"
  foundationModel: "anthropic.claude-3-haiku-20240307-v1:0"
  instruction: |
    You are an Intake Agent responsible for processing candidate resumes and extracting structured information.
    
    Your tasks:
    1. Parse resume content from various formats (PDF, DOC, text)
    2. Extract key information: contact details, experience, education, skills
    3. Normalize data into standard JSON format with consistent field names
    4. Validate completeness and assign a completeness score (0-100)
    5. Determine experience level (Entry/Mid/Senior) based on years and role progression
    6. Flag any data quality issues or missing critical information
    
    Output format: JSON with candidateProfile, contactInfo, experienceLevel, completenessScore, and any dataQualityIssues.
    
    Be thorough but efficient. Focus on accuracy and consistency.
  
  knowledgeBases:
    - resumeParsingPatterns
    - dataValidationRules
    - industryStandards
  
  tools:
    - name: "pdf_parser"
      description: "Extract text and structure from PDF resumes"
      schema:
        type: "object"
        properties:
          file_content:
            type: "string"
            description: "Base64 encoded PDF content"
    
    - name: "data_validator"
      description: "Validate extracted candidate data against schema"
      schema:
        type: "object"
        properties:
          candidate_data:
            type: "object"
            description: "Extracted candidate information"
    
    - name: "duplicate_checker"
      description: "Check for existing candidates in database"
      schema:
        type: "object"
        properties:
          email:
            type: "string"
            description: "Candidate email for duplicate checking"
          name:
            type: "string"
            description: "Candidate full name"
  
  guardrails:
    - piiDetection: true
    - biasDetection: true
    - contentFiltering: true
```

### **Screening Agent Configuration**
```yaml
ScreeningAgent:
  agentId: "screening-agent-id"
  foundationModel: "anthropic.claude-3-5-sonnet-20241022-v2:0"
  instruction: |
    You are a Screening Agent that evaluates candidates against company core values and job requirements.
    
    Your tasks:
    1. Systematically analyze candidate profile against all 10 company core values
    2. Map specific achievements and experiences to value criteria with concrete evidence
    3. Evaluate technical skills alignment with job requirements and assess skill depth
    4. Identify potential red flags or concerns that need human attention
    5. Generate confidence scores (0-1) and clear recommendations (PASS/FAIL/NEEDS_REVIEW)
    6. Use vector search to find similar successful candidates for comparison
    7. Provide evidence-based reasoning for all assessments
    
    Core Values to Evaluate:
    - Innovation, Collaboration, Excellence, Integrity, Customer Focus
    - Ownership, Growth Mindset, Transparency, Diversity & Inclusion, Impact
    
    Output format: JSON with recommendation, confidence, overallScore, coreValueScores, strengths, concerns, evidence, and similarCandidates.
    
    Be thorough, fair, and evidence-based. Avoid bias and focus on job-relevant criteria.
  
  knowledgeBases:
    - companyCoreValues
    - screeningCriteria
    - historicalDecisions
    - successfulCandidateProfiles
  
  tools:
    - name: "vector_search"
      description: "Find similar candidate profiles using OpenSearch"
      schema:
        type: "object"
        properties:
          candidate_embedding:
            type: "array"
            description: "Vector representation of candidate profile"
          similarity_threshold:
            type: "number"
            description: "Minimum similarity score (0-1)"
    
    - name: "knowledge_graph_query"
      description: "Query relationships between skills and success factors"
      schema:
        type: "object"
        properties:
          query:
            type: "string"
            description: "Cypher query for Neptune knowledge graph"
    
    - name: "bias_detector"
      description: "Detect potential bias in evaluation"
      schema:
        type: "object"
        properties:
          evaluation_data:
            type: "object"
            description: "Screening evaluation to check for bias"
```

---

## Human-in-the-Loop Implementation

### **Wait for Task Token Pattern**
```json
{
  "HumanScreeningReview": {
    "Type": "Task",
    "Comment": "Human review for borderline screening decisions",
    "Resource": "arn:aws:states:::lambda:invoke.waitForTaskToken",
    "Parameters": {
      "FunctionName": "human-screening-review-function",
      "Payload": {
        "taskToken.$": "$$.Task.Token",
        "candidateId.$": "$.screeningPrep.candidateId",
        "reviewData": {
          "candidateProfile": {
            "name.$": "$.intakeResult.candidateProfile.name",
            "experienceLevel.$": "$.intakeResult.experienceLevel",
            "primarySkills.$": "$.screeningPrep.nextStagePrep.primarySkills",
            "yearsExperience.$": "$.intakeResult.candidateProfile.yearsExperience"
          },
          "screeningResults": {
            "recommendation.$": "$.screeningResult.recommendation",
            "confidence.$": "$.screeningResult.confidence",
            "overallScore.$": "$.screeningResult.overallScore",
            "coreValueScores.$": "$.screeningResult.coreValueScores",
            "strengths.$": "$.screeningResult.strengths",
            "concerns.$": "$.screeningResult.concerns",
            "evidence.$": "$.screeningResult.evidence"
          },
          "reviewInstructions": "Review AI screening recommendation. Focus on concerns and evidence quality. Consider role requirements and company values alignment."
        },
        "approvalOptions": ["APPROVE", "REJECT", "REQUEST_MORE_INFO"],
        "timeoutHours": 24
      }
    },
    "ResultPath": "$.humanScreeningDecision",
    "TimeoutSeconds": 86400,
    "Catch": [
      {
        "ErrorEquals": ["States.Timeout"],
        "Next": "HandleReviewTimeout",
        "ResultPath": "$.timeoutError"
      }
    ],
    "Next": "ProcessHumanScreeningDecision"
  }
}
```

### **Lambda Function for Human Review**
```python
import json
import boto3
import uuid
from datetime import datetime, timedelta

def lambda_handler(event, context):
    """
    Lambda function to handle human review requests
    """
    task_token = event['taskToken']
    candidate_id = event['candidateId']
    review_data = event['reviewData']
    
    # Store review request in DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('human-reviews')
    
    review_id = str(uuid.uuid4())
    
    table.put_item(
        Item={
            'reviewId': review_id,
            'candidateId': candidate_id,
            'taskToken': task_token,
            'reviewData': review_data,
            'status': 'PENDING',
            'createdAt': datetime.utcnow().isoformat(),
            'expiresAt': (datetime.utcnow() + timedelta(hours=24)).isoformat()
        }
    )
    
    # Send notification to reviewer
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:account:hiring-reviews',
        Subject=f'Candidate Review Required: {review_data["candidateProfile"]["name"]}',
        Message=f'''
        A candidate requires human review for screening decision.
        
        Candidate: {review_data["candidateProfile"]["name"]}
        AI Recommendation: {review_data["screeningResults"]["recommendation"]}
        Confidence: {review_data["screeningResults"]["confidence"]}
        
        Review at: https://hiring-dashboard.company.com/review/{review_id}
        
        This review will expire in 24 hours.
        '''
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'reviewId': review_id,
            'status': 'notification_sent'
        })
    }
```

This implementation provides a complete, production-ready foundation for the Step Functions + JSONata + Bedrock agentic workflow as recommended in the Devcraft session.

---

## Graph RAG Integration in Step Functions

### **Enhanced State Machine with Graph RAG Context**

Our Step Functions workflow is enhanced with **Graph RAG (Retrieval-Augmented Generation)** to provide rich, contextual information to Bedrock Agents throughout the hiring process.

```json
{
  "Comment": "Hiring Workflow with Graph RAG Context Management",
  "StartAt": "ValidateInput",
  "States": {
    "InitializeGraphRAGContext": {
      "Type": "Task",
      "Comment": "Initialize Graph RAG context for the candidate",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "initialize-graph-rag-context",
        "Payload": {
          "candidateId.$": "$.validatedCandidate.candidateId",
          "candidateProfile.$": "$.validatedCandidate",
          "contextTypes": ["screening", "assessment", "interview", "evaluation"]
        }
      },
      "ResultPath": "$.graphRagContext",
      "Next": "IntakeAgent"
    },

    "EnrichGraphRAGContext": {
      "Type": "Task",
      "Comment": "Enrich Graph RAG context with intake results",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "enrich-graph-rag-context",
        "Payload": {
          "contextId.$": "$.graphRagContext.contextId",
          "candidateProfile.$": "$.intakeResult.candidateProfile",
          "extractedSkills.$": "$.intakeResult.skills",
          "experienceLevel.$": "$.intakeResult.experienceLevel"
        }
      },
      "ResultPath": "$.enrichedContext",
      "Next": "TransformForScreeningWithGraphRAG"
    },

    "TransformForScreeningWithGraphRAG": {
      "Type": "Pass",
      "Comment": "Prepare screening input with Graph RAG context",
      "Parameters": {
        "screeningInput.$": "$merge([$.intakeResult.candidateProfile, {\"companyContext\": $.companyContext, \"jobRequirements\": $.jobDescription.requirements, \"graphRagContext\": {\"contextId\": $.enrichedContext.contextId, \"skillNetwork\": $.enrichedContext.skillRelationships, \"similarCandidates\": $.enrichedContext.similarSuccessfulCandidates[0:5], \"contextualBenchmarks\": $.enrichedContext.performanceBenchmarks}}])"
      },
      "ResultPath": "$.screeningPrep",
      "Next": "ScreeningAgentWithGraphRAG"
    },

    "ScreeningAgentWithGraphRAG": {
      "Type": "Task",
      "Comment": "Screening with Graph RAG context",
      "Resource": "arn:aws:bedrock:us-east-1:account:agent/screening-agent",
      "Parameters": {
        "sessionId.$": "$.screeningPrep.candidateId",
        "inputText.$": "$string($.screeningPrep.screeningInput)",
        "sessionAttributes": {
          "stage": "screening",
          "graphRagContextId.$": "$.enrichedContext.contextId",
          "similarCandidatesCount.$": "$string($count($.enrichedContext.similarSuccessfulCandidates))",
          "skillNetworkSize.$": "$string($count($.enrichedContext.skillRelationships))"
        }
      },
      "ResultPath": "$.screeningResult",
      "Next": "EvaluateScreeningWithContext"
    },

    "EvaluateScreeningWithContext": {
      "Type": "Choice",
      "Comment": "Enhanced screening evaluation with Graph RAG insights",
      "Choices": [
        {
          "Comment": "Strong pass with high contextual similarity",
          "And": [
            {
              "Variable": "$.screeningResult.recommendation",
              "StringEquals": "PASS"
            },
            {
              "Variable": "$.screeningResult.confidence",
              "NumericGreaterThan": 0.8
            },
            {
              "Variable": "$.screeningResult.contextualSimilarity",
              "NumericGreaterThan": 0.75
            }
          ],
          "Next": "TransformForAssessmentWithGraphRAG"
        },
        {
          "Comment": "Pass but low contextual similarity - needs human review",
          "And": [
            {
              "Variable": "$.screeningResult.recommendation",
              "StringEquals": "PASS"
            },
            {
              "Variable": "$.screeningResult.contextualSimilarity",
              "NumericLessThan": 0.6
            }
          ],
          "Next": "HumanScreeningReviewWithContext"
        }
      ],
      "Default": "HumanScreeningReviewWithContext"
    }
  }
}
```

### **Graph RAG Lambda Functions**

#### **Initialize Graph RAG Context Function**
```python
import json
import boto3
import asyncio
from graph_rag_engine import GraphRAGEngine

async def lambda_handler(event, context):
    """
    Initialize Graph RAG context for a candidate
    """
    candidate_id = event['candidateId']
    candidate_profile = event['candidateProfile']
    context_types = event['contextTypes']
    
    # Initialize Graph RAG engine
    neptune_client = boto3.client('neptune')
    opensearch_client = boto3.client('opensearch')
    graph_rag = GraphRAGEngine(neptune_client, opensearch_client)
    
    # Create initial context for all stages
    contexts = {}
    for context_type in context_types:
        contexts[context_type] = await graph_rag.retrieve_context(
            candidate_id=candidate_id,
            query_intent=context_type,
            depth=2
        )
    
    # Store context in DynamoDB for reuse
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('graph-rag-contexts')
    
    context_id = f"ctx_{candidate_id}_{int(time.time())}"
    
    table.put_item(
        Item={
            'contextId': context_id,
            'candidateId': candidate_id,
            'contexts': contexts,
            'createdAt': datetime.utcnow().isoformat(),
            'ttl': int(time.time()) + 86400  # 24 hour TTL
        }
    )
    
    return {
        'statusCode': 200,
        'body': {
            'contextId': context_id,
            'initializedContexts': list(contexts.keys()),
            'skillRelationships': contexts.get('screening', {}).get('graph_relationships', {}),
            'similarSuccessfulCandidates': contexts.get('screening', {}).get('semantic_similarities', [])
        }
    }
```

### **Enhanced Bedrock Agent Configuration with Graph RAG**

#### **Screening Agent with Graph RAG**
```yaml
ScreeningAgent:
  foundationModel: "anthropic.claude-3-5-sonnet-20241022-v2:0"
  instruction: |
    You are a Screening Agent with access to Graph RAG context management system.
    
    For each candidate evaluation, use the graph_rag_query tool to:
    1. Understand skill relationships and how they cluster in successful candidates
    2. Find similar candidates who were successfully hired and their patterns
    3. Analyze career progression paths that led to success
    4. Identify value demonstrations that correlate with performance
    
    Graph RAG provides you with:
    - **Skill Networks:** How skills relate and complement each other
    - **Success Patterns:** Characteristics of high-performing hires
    - **Career Trajectories:** Common paths that lead to success
    - **Cultural Indicators:** How candidates demonstrate company values
    
    Use this rich context to make evidence-based decisions that go beyond surface-level resume matching.
    
    Always query Graph RAG with query_intent="screening" and context_depth=2 for comprehensive context.
  
  tools:
    - name: "graph_rag_query"
      description: "Query Graph RAG system for contextual candidate information"
      schema:
        type: "object"
        properties:
          candidate_id:
            type: "string"
          query_intent:
            type: "string"
            enum: ["screening", "assessment", "interview", "evaluation"]
          context_depth:
            type: "integer"
            minimum: 1
            maximum: 3
```

#### **Assessment Agent with Graph RAG**
```yaml
AssessmentAgent:
  foundationModel: "anthropic.claude-3-5-sonnet-20241022-v2:0"
  instruction: |
    You are an Assessment Agent that creates and evaluates take-home assignments using Graph RAG context.
    
    Your tasks:
    1. Use Graph RAG to understand the candidate's skill network and related competencies
    2. Query similar successful candidates to understand effective assessment patterns
    3. Generate personalized assignments based on contextual skill relationships
    4. Evaluate submissions against benchmarks from similar high-performing candidates
    5. Provide detailed feedback using contextual success patterns
    
    Graph RAG Context Available:
    - Skill relationship networks (what skills typically cluster together)
    - Assessment patterns from similar successful candidates
    - Technical challenge difficulty mapping based on skill graphs
    - Success benchmarks from candidates with similar profiles
    
    Always use graph_rag_query with query_intent="assessment" for rich contextual information.
  
  tools:
    - name: "graph_rag_query"
      description: "Query Graph RAG system for contextual assessment information"
    - name: "code_analyzer"
      description: "Analyze code quality and technical implementation"
    - name: "similarity_matcher"
      description: "Match candidate solutions against successful patterns"
```

### **JSONata Transformations with Graph RAG Context**

#### **Context-Aware Screening Preparation**
```javascript
// Enhanced screening input with Graph RAG context
$merge([
  $.intakeResult.candidateProfile,
  {
    "evaluationContext": {
      "companyValues": $.companyContext.coreValues,
      "jobRequirements": $.jobDescription.requirements,
      "graphRagInsights": {
        "skillNetwork": $.enrichedContext.skillRelationships,
        "similarSuccessfulCandidates": $.enrichedContext.similarSuccessfulCandidates[0:5],
        "contextualBenchmarks": $.enrichedContext.performanceBenchmarks,
        "successPatterns": $.enrichedContext.successPatterns
      }
    },
    "candidateMetadata": {
      "processId": $.processId,
      "experienceLevel": $.intakeResult.experienceLevel,
      "skillComplexity": $average($.enrichedContext.skillRelationships[].complexity_score),
      "contextualSimilarity": $max($.enrichedContext.similarSuccessfulCandidates[].similarity_score)
    }
  }
])
```

#### **Assessment Personalization with Graph RAG**
```javascript
// Personalized assessment creation using Graph RAG insights
{
  "personalizedAssessment": {
    "candidateId": $.candidateId,
    "baselineSkills": $.intakeResult.candidateProfile.skills,
    "relatedSkills": $.enrichedContext.skillRelationships[$.intakeResult.candidateProfile.skills[*]].related_skills,
    "recommendedChallenges": $.enrichedContext.relevantChallenges[?difficulty_level = $.intakeResult.experienceLevel],
    "successBenchmarks": $.enrichedContext.performanceBenchmarks[?experience_level = $.intakeResult.experienceLevel],
    "evaluationCriteria": $merge([
      $.standardCriteria,
      {
        "contextualExpectations": $.enrichedContext.assessmentSuccessPatterns[0:3],
        "skillDepthRequirements": $.enrichedContext.skillComplexityMapping
      }
    ])
  }
}
```

### **Graph RAG Benefits in Step Functions Workflow**

#### **1. Enhanced Decision Quality**
- **Contextual Intelligence:** Agents make decisions based on rich relationship data
- **Historical Learning:** System learns from successful hiring patterns
- **Bias Reduction:** Objective relationship-based context reduces subjective bias

#### **2. Personalized Candidate Experience**
- **Tailored Assessments:** Assignments based on candidate's specific skill network
- **Relevant Questions:** Interview questions personalized to candidate's experience
- **Fair Evaluation:** Candidates evaluated against similar successful profiles

#### **3. Continuous Improvement**
- **Pattern Recognition:** System discovers new relationships and success indicators
- **Context Evolution:** Knowledge graph grows with each candidate interaction
- **Performance Correlation:** Track which contextual factors predict success

#### **4. Operational Efficiency**
- **Automated Context Retrieval:** Graph RAG queries happen automatically in workflow
- **Cached Results:** Context reused across multiple workflow stages
- **Parallel Processing:** Multiple candidates can leverage shared contextual insights

This Graph RAG integration transforms our Step Functions workflow from simple rule-based processing to intelligent, context-aware decision making that leverages the full power of relationship data and semantic understanding for superior hiring outcomes.
