# Technical Implementation Specification

## Executive Summary

This document provides detailed technical specifications for implementing the multi-agent hiring automation system using Amazon Bedrock, including specific model configurations, API integrations, infrastructure requirements, and deployment architecture.

---

## AWS Bedrock Agent Configurations

### Foundation Model Selection Strategy

Based on task complexity analysis and cost optimization:

| Agent | Primary Model | Fallback Model | Justification |
|-------|---------------|----------------|---------------|
| Orchestrator | Claude 3.5 Sonnet | Claude 3 Haiku | Complex workflow management requires advanced reasoning |
| Intake | Claude 3 Haiku | Claude 3 Haiku | Simple text processing and data extraction |
| Screening | Claude 3.5 Sonnet | Claude 3 Sonnet | Nuanced candidate evaluation requires sophisticated analysis |
| Assessment | Claude 3 Opus | Claude 3.5 Sonnet | Critical technical evaluation demands highest capability |
| Interview | Claude 3.5 Sonnet | Claude 3 Sonnet | Personalization requires advanced contextual understanding |
| Evaluation | Claude 3 Opus | Claude 3.5 Sonnet | Final decisions require maximum accuracy and reasoning |
| Communication | Claude 3 Haiku | Claude 3 Haiku | Straightforward communication tasks |

### Agent-Specific Bedrock Configurations

## 1. Orchestrator Agent Configuration

```json
{
  "agentName": "hiring-orchestrator",
  "description": "Central workflow manager for hiring automation",
  "foundationModel": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "instruction": "You are the Orchestrator Agent managing the complete hiring workflow. Coordinate between specialized agents, track workflow state, and manage human-in-the-loop decision points. Maintain consistency and ensure quality across all stages.",
  "idleSessionTTLInSeconds": 3600,
  "agentResourceRoleArn": "arn:aws:iam::ACCOUNT:role/BedrockAgentRole-Orchestrator",
  "actionGroups": [
    {
      "actionGroupName": "workflow-management",
      "description": "Manage hiring workflow state and transitions",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:REGION:ACCOUNT:function:workflow-manager"
      },
      "apiSchema": {
        "s3": {
          "s3BucketName": "hiring-automation-schemas",
          "s3ObjectKey": "orchestrator-api-schema.json"
        }
      }
    },
    {
      "actionGroupName": "notification-management",
      "description": "Send notifications and manage human decision points",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:REGION:ACCOUNT:function:notification-manager"
      }
    }
  ],
  "knowledgeBases": [
    {
      "knowledgeBaseId": "company-policies-kb",
      "description": "Company policies and procedures"
    },
    {
      "knowledgeBaseId": "context-quality-kb",
      "description": "Context quality validation and management guidelines"
    }
  ]
}
```

## 2. Screening Agent Configuration

```json
{
  "agentName": "candidate-screening",
  "description": "Automated candidate evaluation against company core values",
  "foundationModel": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "instruction": "You are the Screening Agent responsible for evaluating candidates against Dunamis Capital's 10 core values. Analyze candidate profiles systematically, provide evidence-based assessments, and flag potential concerns. Your evaluations must be thorough, unbiased, and consistent.",
  "idleSessionTTLInSeconds": 1800,
  "agentResourceRoleArn": "arn:aws:iam::ACCOUNT:role/BedrockAgentRole-Screening",
  "actionGroups": [
    {
      "actionGroupName": "candidate-evaluation",
      "description": "Core candidate screening and evaluation functions",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:REGION:ACCOUNT:function:candidate-evaluator"
      },
      "apiSchema": {
        "s3": {
          "s3BucketName": "hiring-automation-schemas",
          "s3ObjectKey": "screening-api-schema.json"
        }
      }
    }
  ],
  "knowledgeBases": [
    {
      "knowledgeBaseId": "core-values-kb",
      "description": "Company core values and evaluation criteria"
    },
    {
      "knowledgeBaseId": "screening-examples-kb",
      "description": "Historical screening examples and patterns"
    }
  ]
}
```

## 3. Assessment Agent Configuration

```json
{
  "agentName": "assessment-generator",
  "description": "Create and evaluate take-home assignments",
  "foundationModel": "anthropic.claude-3-opus-20240229",
  "instruction": "You are the Assessment Agent responsible for creating personalized take-home assignments and evaluating submissions. Generate challenging but fair assessments appropriate to candidate level. Evaluate submissions objectively using consistent rubrics.",
  "idleSessionTTLInSeconds": 3600,
  "agentResourceRoleArn": "arn:aws:iam::ACCOUNT:role/BedrockAgentRole-Assessment",
  "actionGroups": [
    {
      "actionGroupName": "assessment-creation",
      "description": "Generate personalized take-home assignments",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:REGION:ACCOUNT:function:assessment-creator"
      }
    },
    {
      "actionGroupName": "assessment-evaluation",
      "description": "Evaluate candidate submissions",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:REGION:ACCOUNT:function:assessment-evaluator"
      }
    }
  ],
  "knowledgeBases": [
    {
      "knowledgeBaseId": "assessment-templates-kb",
      "description": "Take-home assignment templates and examples"
    },
    {
      "knowledgeBaseId": "evaluation-rubrics-kb",
      "description": "Technical evaluation criteria and rubrics"
    }
  ]
}
```

---

## Infrastructure Architecture

### Core AWS Services Integration

```yaml
# CloudFormation Template Structure
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Hiring Automation System Infrastructure'

Parameters:
  Environment:
    Type: String
    Default: 'prod'
    AllowedValues: ['dev', 'staging', 'prod']

Resources:
  # S3 Buckets
  CandidateDataBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub 'hiring-automation-data-${Environment}'
      VersioningConfiguration:
        Status: Enabled
      ServerSideEncryptionConfiguration:
        - ServerSideEncryptionByDefault:
            SSEAlgorithm: AES256
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true

  # DynamoDB Tables
  CandidateTrackingTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub 'candidate-tracking-${Environment}'
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: candidateId
          AttributeType: S
        - AttributeName: stage
          AttributeType: S
      KeySchema:
        - AttributeName: candidateId
          KeyType: HASH
        - AttributeName: stage
          KeyType: RANGE
      GlobalSecondaryIndexes:
        - IndexName: stage-index
          KeySchema:
            - AttributeName: stage
              KeyType: HASH
          Projection:
            ProjectionType: ALL

  WorkflowStateTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub 'workflow-state-${Environment}'
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: workflowId
          AttributeType: S
      KeySchema:
        - AttributeName: workflowId
          KeyType: HASH
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES

  # Step Functions State Machine
  HiringWorkflowStateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineName: !Sub 'hiring-workflow-${Environment}'
      DefinitionString: !Sub |
        {
          "Comment": "Hiring automation workflow",
          "StartAt": "IntakeCandidate",
          "States": {
            "IntakeCandidate": {
              "Type": "Task",
              "Resource": "arn:aws:states:::bedrock:invokeAgent",
              "Parameters": {
                "agentId": "${IntakeAgent}",
                "agentAliasId": "TSTALIASID",
                "inputText.$": "$.candidateData"
              },
              "Next": "ScreenCandidate"
            },
            "ScreenCandidate": {
              "Type": "Task", 
              "Resource": "arn:aws:states:::bedrock:invokeAgent",
              "Parameters": {
                "agentId": "${ScreeningAgent}",
                "agentAliasId": "TSTALIASID",
                "inputText.$": "$.processedCandidate"
              },
              "Next": "HumanApprovalScreening"
            },
            "HumanApprovalScreening": {
              "Type": "Task",
              "Resource": "arn:aws:states:::lambda:invoke.waitForTaskToken",
              "Parameters": {
                "FunctionName": "${HumanApprovalFunction}",
                "Payload": {
                  "taskToken.$": "$$.Task.Token",
                  "decision": "screening",
                  "data.$": "$"
                }
              },
              "Next": "CreateAssessment"
            }
          }
        }
      RoleArn: !GetAtt StepFunctionsRole.Arn

  # SQS Queues for Inter-Agent Communication
  AgentCommunicationQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Sub 'agent-communication-${Environment}'
      VisibilityTimeoutSeconds: 300
      MessageRetentionPeriod: 1209600  # 14 days
      RedrivePolicy:
        deadLetterTargetArn: !GetAtt DeadLetterQueue.Arn
        maxReceiveCount: 3

  DeadLetterQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Sub 'agent-communication-dlq-${Environment}'
      MessageRetentionPeriod: 1209600  # 14 days
```

### Lambda Functions Architecture

```python
# Example: Workflow Manager Lambda Function
import json
import boto3
import logging
from typing import Dict, Any

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
stepfunctions = boto3.client('stepfunctions')
bedrock_agent = boto3.client('bedrock-agent-runtime')

def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    """
    Workflow Manager Lambda Function
    Handles workflow state transitions and agent coordination
    """
    try:
        action = event.get('action')
        workflow_id = event.get('workflowId')
        
        if action == 'start_workflow':
            return start_hiring_workflow(event)
        elif action == 'update_state':
            return update_workflow_state(event)
        elif action == 'get_status':
            return get_workflow_status(workflow_id)
        else:
            raise ValueError(f"Unknown action: {action}")
            
    except Exception as e:
        logger.error(f"Error in workflow manager: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def start_hiring_workflow(event: Dict[str, Any]) -> Dict[str, Any]:
    """Start new hiring workflow for candidate"""
    candidate_data = event.get('candidateData')
    workflow_id = event.get('workflowId')
    
    # Store initial workflow state
    workflow_table = dynamodb.Table('workflow-state-prod')
    workflow_table.put_item(
        Item={
            'workflowId': workflow_id,
            'stage': 'intake',
            'status': 'in_progress',
            'candidateData': candidate_data,
            'timestamp': int(time.time())
        }
    )
    
    # Start Step Functions execution
    response = stepfunctions.start_execution(
        stateMachineArn='arn:aws:states:region:account:stateMachine:hiring-workflow-prod',
        name=workflow_id,
        input=json.dumps(event)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'workflowId': workflow_id,
            'executionArn': response['executionArn']
        })
    }
```

---

## Knowledge Base Configuration

### Vector Database Setup for RAG

```yaml
# Knowledge Base Configuration
KnowledgeBases:
  CoreValuesKB:
    Name: "core-values-kb"
    Description: "Company core values and evaluation criteria"
    DataSource:
      Type: "S3"
      S3Configuration:
        BucketName: "hiring-automation-knowledge"
        InclusionPrefixes: ["core-values/"]
    VectorIndexConfiguration:
      Type: "opensearch-serverless"
      Dimensions: 1536
      Engine: "nmslib"
    ChunkingStrategy:
      Type: "FIXED_SIZE"
      FixedSizeChunkingConfiguration:
        MaxTokens: 512
        OverlapPercentage: 20

  AssessmentTemplatesKB:
    Name: "assessment-templates-kb"
    Description: "Take-home assignment templates and rubrics"
    DataSource:
      Type: "S3"
      S3Configuration:
        BucketName: "hiring-automation-knowledge"
        InclusionPrefixes: ["assessments/"]
    VectorIndexConfiguration:
      Type: "opensearch-serverless"
      Dimensions: 1536
    ChunkingStrategy:
      Type: "SEMANTIC"
      SemanticChunkingConfiguration:
        MaxTokens: 300
        BufferSize: 1
        BreakpointPercentileThreshold: 95

  HistoricalDataKB:
    Name: "historical-screening-kb"
    Description: "Historical screening decisions and patterns"
    DataSource:
      Type: "S3"
      S3Configuration:
        BucketName: "hiring-automation-knowledge"
        InclusionPrefixes: ["historical-data/"]
    VectorIndexConfiguration:
      Type: "opensearch-serverless"
      Dimensions: 1536
```

---

## API Integration Specifications

### External System Integration

```python
# Dooray Task API Integration
class DoorayTaskIntegration:
    def __init__(self, api_token: str, project_id: str):
        self.api_token = api_token
        self.project_id = project_id
        self.base_url = "https://api.dooray.com"
        
    def monitor_new_tasks(self) -> List[Dict]:
        """Monitor for new candidate submissions"""
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        
        # Get tasks created in last 24 hours with resume attachments
        params = {
            'projectId': self.project_id,
            'createdAt': f'since:{datetime.now() - timedelta(days=1)}',
            'hasAttachment': True
        }
        
        response = requests.get(
            f"{self.base_url}/v2/projects/{self.project_id}/tasks",
            headers=headers,
            params=params
        )
        
        return response.json().get('tasks', [])

# Outlook Graph API Integration  
class OutlookIntegration:
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self._get_access_token()
        
    def _get_access_token(self) -> str:
        """Get OAuth2 access token for Graph API"""
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        
        response = requests.post(url, data=data)
        return response.json()['access_token']
        
    def get_hiring_emails(self, mailbox: str = "hiring@dunamiscap.com") -> List[Dict]:
        """Get emails from hiring mailbox with attachments"""
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        # Filter for emails with attachments in last 24 hours
        filter_query = (
            "hasAttachments eq true and "
            f"receivedDateTime ge {(datetime.utcnow() - timedelta(days=1)).isoformat()}Z"
        )
        
        response = requests.get(
            f"https://graph.microsoft.com/v1.0/users/{mailbox}/messages",
            headers=headers,
            params={'$filter': filter_query, '$expand': 'attachments'}
        )
        
        return response.json().get('value', [])
```

---

## Security & Compliance Configuration

### IAM Roles and Policies

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockAgentPermissions",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeAgent",
        "bedrock:InvokeModel",
        "bedrock:RetrieveAndGenerate"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:agent/*",
        "arn:aws:bedrock:*:*:agent-alias/*",
        "arn:aws:bedrock:*:*:knowledge-base/*"
      ]
    },
    {
      "Sid": "DataAccessPermissions",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::hiring-automation-data-*/*",
        "arn:aws:s3:::hiring-automation-knowledge/*"
      ]
    },
    {
      "Sid": "DatabasePermissions",
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:Query",
        "dynamodb:Scan"
      ],
      "Resource": [
        "arn:aws:dynamodb:*:*:table/candidate-tracking-*",
        "arn:aws:dynamodb:*:*:table/workflow-state-*"
      ]
    }
  ]
}
```

### Data Encryption Configuration

```yaml
EncryptionSettings:
  S3Encryption:
    Type: "AES256"
    KMSKeyId: "arn:aws:kms:region:account:key/key-id"
    
  DynamoDBEncryption:
    Type: "AWS_MANAGED"
    SSESpecification:
      SSEEnabled: true
      
  InTransitEncryption:
    TLSVersion: "1.2"
    CipherSuites: 
      - "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
      - "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
```

---

## Monitoring & Observability

### CloudWatch Configuration

```yaml
# Monitoring Setup
LogGroups:
  - LogGroupName: "/aws/lambda/hiring-automation"
    RetentionInDays: 30
    
  - LogGroupName: "/aws/bedrock/agents"
    RetentionInDays: 30

Metrics:
  CustomMetrics:
    - MetricName: "CandidatesProcessed"
      Namespace: "HiringAutomation"
      Dimensions:
        - Name: "Stage"
          Value: "screening"
          
    - MetricName: "ProcessingTime"
      Namespace: "HiringAutomation"
      Unit: "Seconds"
      
    - MetricName: "AgentErrors"
      Namespace: "HiringAutomation"
      Dimensions:
        - Name: "AgentType"

Alarms:
  - AlarmName: "HighErrorRate"
    MetricName: "AgentErrors"
    Threshold: 5
    ComparisonOperator: "GreaterThanThreshold"
    EvaluationPeriods: 2
    AlarmActions:
      - "arn:aws:sns:region:account:hiring-automation-alerts"
      
  - AlarmName: "LongProcessingTime"
    MetricName: "ProcessingTime"
    Threshold: 3600  # 1 hour
    ComparisonOperator: "GreaterThanThreshold"
```

### X-Ray Tracing Configuration

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# Patch all AWS SDK calls
patch_all()

@xray_recorder.capture('hiring_workflow')
def process_candidate(candidate_data):
    """Process candidate through hiring workflow with tracing"""
    
    with xray_recorder.in_subsegment('candidate_intake'):
        intake_result = intake_agent.process(candidate_data)
        
    with xray_recorder.in_subsegment('candidate_screening'):
        screening_result = screening_agent.evaluate(intake_result)
        
    return screening_result
```

---

## Cost Optimization Strategy

### Model Usage Optimization

```yaml
CostOptimization:
  ModelSelection:
    - Task: "Simple text processing"
      Model: "Claude 3 Haiku"
      ExpectedCost: "$0.25 per 1M input tokens"
      
    - Task: "Complex reasoning"
      Model: "Claude 3.5 Sonnet" 
      ExpectedCost: "$3.00 per 1M input tokens"
      
    - Task: "Critical decisions"
      Model: "Claude 3 Opus"
      ExpectedCost: "$15.00 per 1M input tokens"

  EstimatedMonthlyCosts:
    InputTokens: "2M tokens/month"
    OutputTokens: "500K tokens/month"
    TotalEstimate: "$200-400/month"
    
  CostControls:
    - MaxTokensPerRequest: 4000
    - RequestRateLimit: "100/minute"
    - MonthlyBudgetAlert: "$500"
```

This technical specification provides the complete implementation blueprint for building the hiring automation system using AWS Bedrock and related services.