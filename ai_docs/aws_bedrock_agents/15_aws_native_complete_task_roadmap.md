# AWS-Native Complete Implementation Task Roadmap

## Executive Summary

This document provides the complete task-by-task implementation roadmap for building the Graph RAG-based context-centric multi-agent system using AWS native services. Each task from the original .kiro specifications has been mapped to specific AWS services with detailed implementation guidance, cost optimization strategies, and success criteria validation.

**Key AWS Services Integration:**
- **Amazon Bedrock**: Multi-agent orchestration and LLM management
- **Amazon Neptune**: Knowledge graph database for Graph RAG
- **Amazon OpenSearch**: Vector search and semantic similarity
- **AWS Lambda**: Serverless context processing and API endpoints
- **Amazon ECS Fargate**: Containerized microservice deployment
- **AWS Secrets Manager**: Credential management and security
- **Amazon CloudWatch**: Monitoring, metrics, and alerting
- **AWS Step Functions**: Workflow orchestration for hiring pipeline

**Target Metrics (AWS Optimized):**
- **Cost**: <$10 per candidate (target $2-5) using AWS Reserved Instances and Spot pricing
- **Performance**: <200ms context retrieval (p95) via Neptune + OpenSearch caching
- **Scalability**: 40+ candidates/month, 15/week peak using ECS auto-scaling
- **Availability**: >99.5% uptime with multi-AZ deployment

---

## Phase 1: Graph RAG Infrastructure on AWS (Weeks 1-3)

### Task 1: AWS-Native Graph RAG Context Service Architecture

**AWS Implementation:**
```python
# AWS CDK Infrastructure Setup
from aws_cdk import (
    aws_ecs as ecs,
    aws_neptune as neptune,
    aws_opensearch as opensearch,
    aws_lambda as lambda_,
    core
)

class ContextGraphServiceStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        # Neptune Cluster for Knowledge Graph
        self.neptune_cluster = neptune.DatabaseCluster(
            self, "ContextGraphCluster",
            engine=neptune.DatabaseEngine.GREMLIN,
            instance_type=neptune.InstanceType.R5_LARGE,
            deletion_protection=True,
            backup_retention=core.Duration.days(7),
            vpc=self.vpc
        )
        
        # OpenSearch for Vector Search
        self.opensearch_domain = opensearch.Domain(
            self, "ContextVectorSearch",
            version=opensearch.EngineVersion.OPENSEARCH_2_5,
            capacity={
                "data_nodes": 3,
                "data_node_instance_type": "t3.small.search"
            },
            ebs={
                "volume_size": 20,
                "volume_type": ec2.EbsDeviceVolumeType.GP3
            }
        )
        
        # ECS Fargate Service
        self.context_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "ContextGraphService",
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("context-graph-service:latest"),
                container_port=8000,
                environment={
                    "NEPTUNE_ENDPOINT": self.neptune_cluster.cluster_endpoint.socket_address,
                    "OPENSEARCH_ENDPOINT": self.opensearch_domain.domain_endpoint
                }
            ),
            memory_limit_mib=2048,
            cpu=1024,
            desired_count=2
        )
```

**Success Criteria:**
- [ ] Neptune cluster deployed with Multi-AZ availability
- [ ] OpenSearch domain configured with 3-node cluster
- [ ] ECS Fargate service running with auto-scaling (2-10 instances)
- [ ] Application Load Balancer with health checks configured
- [ ] All services within existing AWS account (319470692494) VPC

### Task 1.1: Neptune Knowledge Graph Schema Implementation

**AWS Neptune Schema:**
```python
# Neptune Gremlin Schema Creation
import boto3
from gremlin_python.driver import client
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

class NeptuneGraphSchema:
    def __init__(self, neptune_endpoint):
        self.connection = DriverRemoteConnection(
            f'wss://{neptune_endpoint}:8182/gremlin', 'g'
        )
        self.g = client.Client(self.connection, 'g')
    
    def create_schema(self):
        # Candidate vertices
        self.g.submit("""
            g.addV('candidate')
             .property('id', 'candidate_001')
             .property('name', 'John Doe')
             .property('email', 'john@example.com')
             .property('skills_vector', [0.1, 0.2, 0.3])  # Embedding
             .property('created_at', datetime())
        """)
        
        # Core Value vertices
        for i, value in enumerate(CORE_VALUES):
            self.g.submit(f"""
                g.addV('core_value')
                 .property('id', 'value_{i:03d}')
                 .property('name', '{value['name']}')
                 .property('description', '{value['description']}')
                 .property('examples', '{json.dumps(value['examples'])}')
            """)
        
        # Skills and Projects vertices
        self.g.submit("""
            g.addV('skill')
             .property('id', 'skill_python')
             .property('name', 'Python')
             .property('category', 'programming')
             .property('level_embeddings', [0.8, 0.9, 0.7])
        """)
        
        # Rich Relationships with Properties
        self.g.submit("""
            g.V().has('candidate', 'id', 'candidate_001')
             .addE('HAS_SKILL')
             .to(g.V().has('skill', 'id', 'skill_python'))
             .property('proficiency_level', 'expert')
             .property('years_experience', 5)
             .property('evidence_strength', 0.85)
             .property('last_validated', datetime())
        """)

CORE_VALUES = [
    {
        "name": "Technical Excellence & Scalable Elegance",
        "description": "Readable, domain-driven code that scales horizontally",
        "examples": ["Clean architecture", "Performance optimization", "Code maintainability"]
    },
    # ... other 9 core values
]
```

**AWS Integration Features:**
- Neptune Multi-AZ deployment for high availability
- Automated backups with 7-day retention
- VPC security groups for network isolation
- CloudWatch metrics for query performance monitoring

**Success Criteria:**
- [ ] Neptune schema supports all entity types (candidates, skills, values, projects, companies)
- [ ] Rich relationships implemented with strength scoring properties
- [ ] Graph queries achieving <50ms response time for single-hop traversal
- [ ] Multi-hop relationship discovery working within 200ms SLA

### Task 1.2: OpenSearch Vector Database Integration

**AWS OpenSearch Implementation:**
```python
from opensearchpy import OpenSearch, RequestsHttpConnection
from aws_requests_auth.aws_auth import AWSRequestsAuth
import numpy as np

class OpenSearchVectorStore:
    def __init__(self, opensearch_endpoint, region='us-east-1'):
        awsauth = AWSRequestsAuth(
            aws_access_key=boto3.Session().get_credentials().access_key,
            aws_secret_access_key=boto3.Session().get_credentials().secret_key,
            aws_token=boto3.Session().get_credentials().token,
            aws_host=opensearch_endpoint,
            aws_region=region,
            aws_service='es'
        )
        
        self.client = OpenSearch(
            hosts=[{'host': opensearch_endpoint, 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )
    
    def create_indices(self):
        # Candidate profile embeddings index
        candidate_mapping = {
            "mappings": {
                "properties": {
                    "candidate_id": {"type": "keyword"},
                    "profile_embedding": {
                        "type": "knn_vector",
                        "dimension": 768,  # Sentence transformer dimension
                        "method": {
                            "name": "hnsw",
                            "space_type": "cosinesimil",
                            "engine": "faiss"
                        }
                    },
                    "skills_embedding": {"type": "knn_vector", "dimension": 768},
                    "values_evidence_embedding": {"type": "knn_vector", "dimension": 768},
                    "metadata": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "text"},
                            "role": {"type": "keyword"},
                            "experience_years": {"type": "integer"}
                        }
                    }
                }
            },
            "settings": {
                "index": {
                    "knn": True,
                    "knn.algo_param.ef_search": 100
                }
            }
        }
        
        self.client.indices.create(
            index="candidate-profiles",
            body=candidate_mapping
        )
    
    def semantic_similarity_search(self, query_vector, k=10):
        search_query = {
            "size": k,
            "query": {
                "knn": {
                    "profile_embedding": {
                        "vector": query_vector,
                        "k": k
                    }
                }
            },
            "_source": ["candidate_id", "metadata"]
        }
        
        response = self.client.search(
            index="candidate-profiles",
            body=search_query
        )
        
        return [{
            "candidate_id": hit["_source"]["candidate_id"],
            "similarity_score": hit["_score"],
            "metadata": hit["_source"]["metadata"]
        } for hit in response["hits"]["hits"]]
```

**Cost Optimization Features:**
- T3.small.search instances for development (scale to R6g.medium for production)
- GP3 EBS volumes with optimized IOPS/throughput ratio
- Index lifecycle management for old candidate data
- Reserved Instance pricing for predictable workloads

**Success Criteria:**
- [ ] OpenSearch domain deployed with 3-node cluster configuration
- [ ] KNN vector search achieving <100ms query latency
- [ ] Support for 768-dimension embeddings (sentence-transformers compatible)
- [ ] Index capacity for 10,000+ candidate profiles with auto-scaling

### Task 1.3: Multi-Database Integration Layer

**AWS RDS + DynamoDB + ElastiCache Integration:**
```python
import boto3
import asyncpg
import aioboto3

class MultiDatabaseManager:
    def __init__(self, config):
        self.rds_config = config['rds']
        self.dynamodb = boto3.resource('dynamodb')
        self.elasticache_config = config['elasticache']
        
    async def setup_connections(self):
        # PostgreSQL RDS for structured data
        self.pg_pool = await asyncpg.create_pool(
            host=self.rds_config['host'],
            database=self.rds_config['database'],
            user=self.rds_config['user'],
            password=await self.get_secret('rds-credentials'),
            min_size=2,
            max_size=10
        )
        
        # DynamoDB for session and cache data
        self.session_table = self.dynamodb.Table('candidate-sessions')
        self.context_cache_table = self.dynamodb.Table('context-cache')
        
        # ElastiCache Redis for high-performance caching
        self.redis_client = aioredis.from_url(
            f"redis://{self.elasticache_config['endpoint']}:6379"
        )
    
    async def sync_candidate_data(self, candidate_id: str, graph_data: dict, 
                                vector_data: dict, structured_data: dict):
        """Synchronize candidate data across all databases"""
        async with self.pg_pool.acquire() as conn:
            # Store structured candidate data in RDS
            await conn.execute(
                "INSERT INTO candidates (id, name, email, role, experience) VALUES ($1, $2, $3, $4, $5)",
                candidate_id, structured_data['name'], structured_data['email'],
                structured_data['role'], structured_data['experience']
            )
        
        # Cache frequently accessed data in ElastiCache
        await self.redis_client.setex(
            f"candidate:{candidate_id}:profile",
            3600,  # 1 hour TTL
            json.dumps(structured_data)
        )
        
        # Store session data in DynamoDB
        self.session_table.put_item(
            Item={
                'candidate_id': candidate_id,
                'session_data': vector_data,
                'created_at': int(time.time()),
                'ttl': int(time.time()) + 86400  # 24 hour TTL
            }
        )
```

**AWS Cost Optimization:**
- RDS PostgreSQL t3.micro instance (upgradable to t3.small)
- DynamoDB On-Demand pricing for variable workloads
- ElastiCache Redis t3.micro node with Multi-AZ disabled for development
- Connection pooling to minimize database connections

**Success Criteria:**
- [ ] Multi-database synchronization achieving <500ms for complete candidate profile
- [ ] Transaction consistency across all three database types
- [ ] Connection pooling reducing database overhead by 60%
- [ ] Automated failover and recovery procedures tested

---

## Phase 2: Graph RAG-Powered Token Optimization (Weeks 4-5)

### Task 2: Intelligent Context Selection with AWS Bedrock

**AWS Bedrock Integration:**
```python
import boto3
from langchain_aws import ChatBedrock
from langchain.prompts import PromptTemplate

class BedrockGraphRAGOptimizer:
    def __init__(self):
        self.bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.chat_model = ChatBedrock(
            model_id="anthropic.claude-3-sonnet-20240229-v1:0",
            client=self.bedrock,
            model_kwargs={"temperature": 0.1, "max_tokens": 4000}
        )
    
    def optimize_context_for_token_limit(self, graph_context: dict, 
                                       vector_context: dict, 
                                       task_type: str, 
                                       token_limit: int = 8000):
        """
        Use AWS Bedrock to intelligently compress context while preserving
        relationship quality and semantic meaning
        """
        optimization_prompt = PromptTemplate(
            template="""
            You are a Graph RAG context optimizer. Your task is to compress the following
            context while preserving the most important relationships and semantic meaning.
            
            Task Type: {task_type}
            Token Budget: {token_limit}
            
            Graph Relationships:
            {graph_context}
            
            Vector Similarity Results:
            {vector_context}
            
            Requirements:
            1. Preserve all candidate-to-core-value relationships with evidence
            2. Maintain skill-to-project connections with proficiency levels
            3. Keep similar candidate patterns for comparison
            4. Compress less relevant details while maintaining semantic coherence
            5. Output in JSON format optimized for the specified task type
            
            Optimized Context:
            """,
            input_variables=["task_type", "token_limit", "graph_context", "vector_context"]
        )
        
        chain = optimization_prompt | self.chat_model
        
        optimized_result = chain.invoke({
            "task_type": task_type,
            "token_limit": token_limit,
            "graph_context": json.dumps(graph_context, indent=2),
            "vector_context": json.dumps(vector_context, indent=2)
        })
        
        return json.loads(optimized_result.content)
    
    def calculate_relationship_priority_scores(self, candidate_id: str, 
                                             task_requirements: dict):
        """Use graph algorithms to score relationship importance"""
        # Multi-hop graph traversal scoring
        relationship_scores = {}
        
        # Core value alignment paths get highest priority
        core_value_paths = self.neptune_client.execute_query(f"""
            g.V().has('candidate', 'id', '{candidate_id}')
             .outE('DEMONSTRATES')
             .inV().has('label', 'core_value')
             .path()
        """)
        
        for path in core_value_paths:
            evidence_strength = path['edges'][0]['properties']['evidence_strength']
            value_importance = CORE_VALUE_WEIGHTS.get(path['vertices'][1]['name'], 1.0)
            relationship_scores[path['path_id']] = evidence_strength * value_importance
        
        return relationship_scores
```

**Token Optimization Strategy:**
- **Primary Model**: Claude Sonnet 3.5 for context optimization (cost-efficient)
- **Fallback**: Claude Haiku for simple compression tasks (ultra-low-cost)
- **Caching**: ElastiCache Redis for frequently optimized contexts
- **Target**: 50-70% token reduction while maintaining 95%+ relationship quality

**Success Criteria:**
- [ ] Context compression achieving 50-70% token reduction
- [ ] Relationship quality preservation >95% (measured by downstream task success)
- [ ] Optimization processing time <30 seconds per candidate
- [ ] Cost per optimization <$0.10 using Bedrock pricing

### Task 2.1: Relationship-Aware Context Prioritization

**AWS Step Functions Workflow:**
```python
import json
import boto3

def lambda_relationship_prioritization(event, context):
    """AWS Lambda function for relationship scoring"""
    candidate_id = event['candidate_id']
    task_type = event['task_type']
    
    neptune_client = boto3.client('neptune-graph')
    
    # Multi-hop relationship discovery
    relationship_query = f"""
    MATCH (c:Candidate {{id: '{candidate_id}'}})
    MATCH (c)-[r1:HAS_SKILL]->(s:Skill)
    MATCH (s)-[r2:REQUIRED_FOR]->(role:Role)
    MATCH (c)-[r3:DEMONSTRATES]->(v:CoreValue)
    RETURN c, r1, s, r2, role, r3, v, 
           r1.proficiency_level as skill_level,
           r3.evidence_strength as value_evidence
    ORDER BY r3.evidence_strength DESC, r1.proficiency_level DESC
    """
    
    results = neptune_client.execute_open_cypher_query(
        graphIdentifier=os.environ['NEPTUNE_GRAPH_ID'],
        queryString=relationship_query
    )
    
    # Calculate priority scores
    prioritized_relationships = []
    for record in results['results']:
        score = calculate_relationship_score(record, task_type)
        prioritized_relationships.append({
            'relationship': record,
            'priority_score': score,
            'relationship_type': classify_relationship_type(record)
        })
    
    # Sort by priority and return top relationships within token budget
    prioritized_relationships.sort(key=lambda x: x['priority_score'], reverse=True)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'candidate_id': candidate_id,
            'prioritized_relationships': prioritized_relationships[:50],  # Top 50
            'optimization_metadata': {
                'total_relationships_found': len(prioritized_relationships),
                'processing_time_ms': context.get_remaining_time_in_millis()
            }
        })
    }

def calculate_relationship_score(record, task_type):
    """Calculate relationship importance score based on task requirements"""
    base_score = 1.0
    
    # Core value evidence gets highest priority
    if 'value_evidence' in record and record['value_evidence']:
        base_score *= (1.0 + record['value_evidence'])
    
    # Skill proficiency impacts technical roles
    if task_type in ['technical_interview', 'coding_assessment']:
        if 'skill_level' in record:
            skill_multiplier = {'expert': 1.5, 'advanced': 1.2, 'intermediate': 1.0, 'beginner': 0.8}
            base_score *= skill_multiplier.get(record['skill_level'], 1.0)
    
    return base_score
```

**Step Functions State Machine:**
```json
{
  "Comment": "Relationship-aware context prioritization workflow",
  "StartAt": "ExtractRelationships",
  "States": {
    "ExtractRelationships": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:relationship-prioritization",
      "Next": "OptimizeContext"
    },
    "OptimizeContext": {
      "Type": "Task",
      "Resource": "arn:aws:bedrock:us-east-1:319470692494:model/anthropic.claude-3-sonnet-20240229-v1:0",
      "Parameters": {
        "modelId": "anthropic.claude-3-sonnet-20240229-v1:0",
        "contentType": "application/json",
        "body.$": "$.prioritized_relationships"
      },
      "Next": "CacheResults"
    },
    "CacheResults": {
      "Type": "Task", 
      "Resource": "arn:aws:states:::aws-sdk:elasticache:set",
      "End": true
    }
  }
}
```

**Success Criteria:**
- [ ] Multi-hop relationship discovery completing within 100ms
- [ ] Relationship scoring algorithm achieving 90%+ relevance accuracy
- [ ] Step Functions workflow handling 15 concurrent candidates
- [ ] Lambda functions operating within 1GB memory limit

---

## Phase 3: Independent Context Service API (Weeks 6-8)

### Task 3: Universal JSON API with AWS API Gateway

**API Gateway + Lambda Architecture:**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import boto3

app = FastAPI(title="Context Graph Service", version="2.0")

class ContextRequest(BaseModel):
    agent_type: str  # gemini_cli, claude_code, amazon_q, kiro_mcp, openai_o3
    task_type: str   # screening, interview_kit, assessment, evaluation
    entity_id: str   # candidate_id, role_id, etc.
    token_limit: Optional[int] = 8000
    format_preferences: Optional[Dict[str, Any]] = {}

class ContextResponse(BaseModel):
    context_id: str
    agent_type: str
    task_type: str
    optimized_context: Dict[str, Any]
    metadata: Dict[str, Any]
    performance_metrics: Dict[str, float]

@app.post("/api/v2/context/generate", response_model=ContextResponse)
async def generate_context(request: ContextRequest):
    """Universal context generation endpoint for any AI agent"""
    
    try:
        # Route to appropriate context generator based on agent type
        context_generator = get_agent_context_generator(request.agent_type)
        
        # Execute Graph RAG context discovery
        raw_context = await context_generator.discover_context(
            entity_id=request.entity_id,
            task_type=request.task_type
        )
        
        # Apply token optimization
        optimized_context = await context_generator.optimize_for_agent(
            raw_context=raw_context,
            token_limit=request.token_limit,
            format_preferences=request.format_preferences
        )
        
        # Cache results for similar requests
        cache_key = f"{request.agent_type}:{request.task_type}:{request.entity_id}"
        await cache_optimized_context(cache_key, optimized_context)
        
        return ContextResponse(
            context_id=f"ctx_{uuid4().hex[:8]}",
            agent_type=request.agent_type,
            task_type=request.task_type,
            optimized_context=optimized_context,
            metadata={
                "processing_time_ms": context_generator.last_processing_time,
                "cache_hit": False,
                "relationships_discovered": len(raw_context.get('relationships', [])),
                "token_compression_ratio": calculate_compression_ratio(raw_context, optimized_context)
            },
            performance_metrics={
                "graph_query_time_ms": context_generator.graph_query_time,
                "vector_search_time_ms": context_generator.vector_search_time,
                "optimization_time_ms": context_generator.optimization_time
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Context generation failed: {str(e)}")

class GeminiCLIContextGenerator:
    """Context generator optimized for Gemini CLI with ReAct methodology"""
    
    async def discover_context(self, entity_id: str, task_type: str):
        # Graph RAG discovery optimized for ReAct workflows
        graph_context = await self.neptune_client.execute_graph_query(
            f"MATCH (e {{id: '{entity_id}'}}) RETURN e, relationships(e) LIMIT 100"
        )
        
        vector_context = await self.opensearch_client.semantic_search(
            entity_id=entity_id,
            task_context=task_type,
            k=20
        )
        
        return {
            "graph_relationships": graph_context,
            "similar_entities": vector_context,
            "task_metadata": await self.get_task_metadata(task_type)
        }
    
    async def optimize_for_agent(self, raw_context: dict, token_limit: int, format_preferences: dict):
        # Gemini CLI prefers YAML-structured context with clear action steps
        optimization_prompt = f"""
        Convert the following Graph RAG context into ReAct methodology format for Gemini CLI:
        
        Requirements:
        - YAML structure with clear reasoning steps
        - Action items with specific graph relationships
        - Observable evidence from candidate profile
        - Token limit: {token_limit}
        
        Context: {json.dumps(raw_context, indent=2)}
        """
        
        bedrock_response = await self.bedrock_client.invoke_model(
            modelId="anthropic.claude-3-haiku-20240307-v1:0",  # Cost-efficient for formatting
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": token_limit,
                "messages": [{"role": "user", "content": optimization_prompt}]
            })
        )
        
        return yaml.safe_load(bedrock_response['content'][0]['text'])

# Agent-specific context generators
AGENT_GENERATORS = {
    'gemini_cli': GeminiCLIContextGenerator(),
    'claude_code': ClaudeCodeContextGenerator(),
    'amazon_q': AmazonQContextGenerator(),
    'kiro_mcp': KiroMCPContextGenerator(),
    'openai_o3': OpenAIO3ContextGenerator()
}
```

**AWS API Gateway Configuration:**
```yaml
# AWS SAM Template for API Gateway deployment
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  ContextGraphAPI:
    Type: AWS::Serverless::Api
    Properties:
      Name: context-graph-api
      StageName: v2
      Cors:
        AllowMethods: "'POST, GET, OPTIONS'"
        AllowHeaders: "'Content-Type,X-Api-Key'"
        AllowOrigin: "'*'"
      Auth:
        ApiKeyRequired: true
        UsagePlan:
          CreateUsagePlan: PER_API
          Description: "Usage plan for context graph service"
          Quota:
            Limit: 10000
            Period: MONTH
          Throttle:
            BurstLimit: 100
            RateLimit: 50

  ContextGeneratorFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: context-generator
      CodeUri: src/
      Handler: main.lambda_handler
      Runtime: python3.12
      MemorySize: 1024
      Timeout: 30
      Environment:
        Variables:
          NEPTUNE_ENDPOINT: !GetAtt NeptuneCluster.Endpoint
          OPENSEARCH_ENDPOINT: !GetAtt OpenSearchDomain.DomainEndpoint
          BEDROCK_REGION: !Ref AWS::Region
      Events:
        GenerateContext:
          Type: Api
          Properties:
            RestApiId: !Ref ContextGraphAPI
            Path: /context/generate
            Method: post
```

**Success Criteria:**
- [ ] API Gateway deployed with 50 RPS throttling and usage plans
- [ ] Lambda functions handling all 5 agent types with <1 second response time
- [ ] Universal JSON API supporting extensible agent integration
- [ ] API key authentication and usage monitoring configured

### Task 3.1: Agent-Specific Context Formatting

**Claude Code CLI Integration:**
```python
class ClaudeCodeContextGenerator:
    """Optimized for Claude Sonnet 4 with 200k context window and technical accuracy"""
    
    async def optimize_for_agent(self, raw_context: dict, token_limit: int, format_preferences: dict):
        # Claude Code prefers structured markdown with technical details
        technical_context = await self.extract_technical_details(raw_context)
        
        markdown_context = f"""
# Candidate Technical Profile

## Core Technical Skills
{self.format_technical_skills(technical_context['skills'])}

## Project Experience & Architecture Decisions  
{self.format_project_experience(technical_context['projects'])}

## Core Values Evidence (Technical Excellence Focus)
{self.format_technical_values_evidence(technical_context['values_evidence'])}

## Similar Candidate Patterns
{self.format_similar_candidates(technical_context['similar_candidates'])}

## Recommended Interview Focus Areas
{self.generate_technical_interview_focus(technical_context)}
"""
        
        # Use Claude Sonnet's enhanced reasoning for technical accuracy
        if token_limit > 50000:  # Take advantage of large context window
            return {
                "format": "enhanced_markdown",
                "content": markdown_context,
                "technical_metadata": technical_context['metadata'],
                "context_utilization": "full_200k_window"
            }
        else:
            # Compress for smaller token budgets
            compressed_context = await self.bedrock_technical_compression(markdown_context, token_limit)
            return {
                "format": "compressed_markdown", 
                "content": compressed_context,
                "compression_ratio": len(markdown_context) / len(compressed_context)
            }
    
    def format_technical_skills(self, skills_data):
        """Format skills with proficiency evidence and project context"""
        formatted_skills = []
        
        for skill in skills_data:
            skill_section = f"""
### {skill['name']} ({skill['proficiency_level']})
- **Experience**: {skill['years_experience']} years
- **Evidence Strength**: {skill['evidence_strength']}/1.0  
- **Recent Projects**: {', '.join(skill['recent_projects'])}
- **Technical Depth**: {skill['technical_examples']}
"""
            formatted_skills.append(skill_section)
        
        return '\n'.join(formatted_skills)
```

**Amazon Q Developer Integration:**
```python
class AmazonQContextGenerator:
    """Optimized for AWS service integration and automated test generation"""
    
    async def optimize_for_agent(self, raw_context: dict, token_limit: int, format_preferences: dict):
        # Amazon Q prefers structured JSON with AWS service context
        aws_optimized_context = {
            "candidate_profile": {
                "aws_experience": await self.extract_aws_skills(raw_context),
                "infrastructure_projects": await self.extract_infra_projects(raw_context),
                "automation_experience": await self.extract_automation_skills(raw_context)
            },
            "test_generation_focus": {
                "backend_testing": self.identify_backend_test_needs(raw_context),
                "infrastructure_testing": self.identify_infra_test_needs(raw_context),
                "integration_testing": self.identify_integration_test_needs(raw_context)
            },
            "aws_service_recommendations": await self.recommend_aws_services(raw_context),
            "development_workflow": {
                "ci_cd_experience": await self.extract_cicd_experience(raw_context),
                "monitoring_experience": await self.extract_monitoring_skills(raw_context)
            }
        }
        
        return aws_optimized_context
    
    async def extract_aws_skills(self, context):
        """Extract AWS-specific skills and certifications"""
        aws_services = []
        
        for skill in context.get('graph_relationships', {}).get('skills', []):
            if any(aws_term in skill['name'].lower() for aws_term in 
                   ['aws', 'lambda', 'ec2', 'rds', 'dynamodb', 's3', 'cloudformation']):
                aws_services.append({
                    "service": skill['name'],
                    "proficiency": skill.get('proficiency_level', 'unknown'),
                    "evidence": skill.get('project_usage', [])
                })
        
        return aws_services
```

**Success Criteria:**
- [ ] All 5 agent types receiving optimized context formats
- [ ] Claude Code CLI utilizing full 200k context window when beneficial
- [ ] Amazon Q Developer receiving AWS-focused technical context
- [ ] Gemini CLI getting ReAct-methodology structured YAML
- [ ] KIRO MCP integration working with JSON-structured strategic context

---

## Phase 4: Hiring Process Automation with AWS Step Functions (Weeks 9-12)

### Task 4: Complete Hiring Workflow Orchestration

**AWS Step Functions State Machine:**
```json
{
  "Comment": "Complete hiring workflow with Graph RAG-powered automation",
  "StartAt": "CandidateIntake",
  "States": {
    "CandidateIntake": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:candidate-intake",
      "Parameters": {
        "candidate_profile.$": "$.candidate_data",
        "role_requirements.$": "$.role_requirements"
      },
      "Next": "BuildKnowledgeGraph",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleIntakeError",
          "ResultPath": "$.error"
        }
      ]
    },
    "BuildKnowledgeGraph": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "ExtractSkillsAndProjects",
          "States": {
            "ExtractSkillsAndProjects": {
              "Type": "Task",
              "Resource": "arn:aws:bedrock:us-east-1:319470692494:model/anthropic.claude-3-sonnet-20240229-v1:0",
              "End": true
            }
          }
        },
        {
          "StartAt": "AnalyzeCoreValuesEvidence", 
          "States": {
            "AnalyzeCoreValuesEvidence": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:us-east-1:319470692494:function:core-values-analysis",
              "End": true
            }
          }
        },
        {
          "StartAt": "GenerateVectorEmbeddings",
          "States": {
            "GenerateVectorEmbeddings": {
              "Type": "Task", 
              "Resource": "arn:aws:bedrock:us-east-1:319470692494:model/amazon.titan-embed-text-v1",
              "End": true
            }
          }
        }
      ],
      "Next": "CoreValuesScreening"
    },
    "CoreValuesScreening": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:core-values-screening",
      "Next": "ScreeningDecision"
    },
    "ScreeningDecision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.screening_result.recommendation",
          "StringEquals": "PROCEED",
          "Next": "TechnicalAssessmentGeneration"
        },
        {
          "Variable": "$.screening_result.recommendation", 
          "StringEquals": "NEEDS_REVIEW",
          "Next": "ManualReviewRequired"
        }
      ],
      "Default": "RejectCandidate"
    },
    "TechnicalAssessmentGeneration": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:assessment-generator",
      "Parameters": {
        "candidate_id.$": "$.candidate_id",
        "role_type.$": "$.role_requirements.type",
        "technical_focus.$": "$.graph_analysis.primary_skills"
      },
      "Next": "InterviewKitGeneration"
    },
    "InterviewKitGeneration": {
      "Type": "Task",
      "Resource": "arn:aws:bedrock:us-east-1:319470692494:model/anthropic.claude-3-sonnet-20240229-v1:0",
      "Parameters": {
        "modelId": "anthropic.claude-3-sonnet-20240229-v1:0",
        "contentType": "application/json",
        "body": {
          "anthropic_version": "bedrock-2023-05-31",
          "max_tokens": 8000,
          "messages": [
            {
              "role": "user", 
              "content": "Generate comprehensive interview kit using Graph RAG context: $.graph_context"
            }
          ]
        }
      },
      "Next": "CreateDoorayTasks"
    },
    "CreateDoorayTasks": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:dooray-integration",
      "Parameters": {
        "candidate_id.$": "$.candidate_id",
        "interview_kit.$": "$.interview_kit",
        "interviewer_assignments.$": "$.interviewer_assignments"
      },
      "Next": "NotifyStakeholders"
    },
    "NotifyStakeholders": {
      "Type": "Task",
      "Resource": "arn:aws:sns:us-east-1:319470692494:hiring-notifications",
      "End": true
    },
    "ManualReviewRequired": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:manual-review-trigger",
      "End": true
    },
    "RejectCandidate": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:319470692494:function:rejection-handler", 
      "End": true
    },
    "HandleIntakeError": {
      "Type": "Task",
      "Resource": "arn:aws:sns:us-east-1:319470692494:error-notifications",
      "End": true
    }
  }
}
```

**Core Values Screening Lambda:**
```python
import json
import boto3
from typing import Dict, List, Any

def lambda_handler(event, context):
    """
    Graph RAG-powered core values screening using Neptune relationship discovery
    """
    candidate_id = event['candidate_id']
    graph_context = event['graph_context']
    
    # Initialize AWS services
    neptune_client = boto3.client('neptune-graph')
    bedrock_runtime = boto3.client('bedrock-runtime')
    
    try:
        # Discover evidence for each of the 10 core values
        core_values_evidence = []
        
        for value in CORE_VALUES:
            evidence_query = f"""
            MATCH (c:Candidate {{id: '{candidate_id}'}})
            MATCH (c)-[r:DEMONSTRATES]->(v:CoreValue {{name: '{value['name']}'}})
            MATCH (c)-[proj:WORKED_ON]->(p:Project)
            WHERE p.description CONTAINS ANY {value['keywords']}
            RETURN v, r.evidence_strength, p, r.evidence_examples
            ORDER BY r.evidence_strength DESC
            LIMIT 5
            """
            
            evidence_results = neptune_client.execute_open_cypher_query(
                graphIdentifier=os.environ['NEPTUNE_GRAPH_ID'],
                queryString=evidence_query
            )
            
            # Use Bedrock to analyze evidence quality
            evidence_analysis = analyze_evidence_with_bedrock(
                bedrock_runtime, value, evidence_results['results']
            )
            
            core_values_evidence.append({
                'core_value': value['name'],
                'evidence_strength': evidence_analysis['strength_score'],
                'evidence_examples': evidence_analysis['examples'],
                'recommendation': evidence_analysis['recommendation']
            })
        
        # Calculate overall core values alignment score
        total_score = sum(ev['evidence_strength'] for ev in core_values_evidence)
        average_score = total_score / len(CORE_VALUES)
        
        # Determine screening recommendation
        if average_score >= 7.5:
            recommendation = "PROCEED"
        elif average_score >= 6.0:
            recommendation = "NEEDS_REVIEW"
        else:
            recommendation = "REJECT"
        
        screening_result = {
            'candidate_id': candidate_id,
            'core_values_analysis': core_values_evidence,
            'overall_score': average_score,
            'recommendation': recommendation,
            'processing_metadata': {
                'graph_queries_executed': len(CORE_VALUES),
                'processing_time_ms': context.get_remaining_time_in_millis(),
                'bedrock_analyses': len(core_values_evidence)
            }
        }
        
        # Store results in DynamoDB for audit trail
        dynamodb = boto3.resource('dynamodb')
        screening_table = dynamodb.Table('candidate-screening-results')
        
        screening_table.put_item(
            Item={
                'candidate_id': candidate_id,
                'screening_timestamp': int(time.time()),
                'screening_result': screening_result,
                'graph_context_summary': summarize_graph_context(graph_context)
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(screening_result),
            'screening_result': screening_result
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'screening_result': {'recommendation': 'ERROR', 'error': str(e)}
        }

def analyze_evidence_with_bedrock(bedrock_client, core_value, evidence_data):
    """Use Bedrock to analyze core value evidence quality"""
    
    analysis_prompt = f"""
    Analyze the following evidence for core value alignment: {core_value['name']}
    
    Core Value Description: {core_value['description']}
    Expected Behaviors: {json.dumps(core_value['examples'])}
    Anti-Patterns to Avoid: {json.dumps(core_value.get('anti_patterns', []))}
    
    Candidate Evidence: {json.dumps(evidence_data, indent=2)}
    
    Provide analysis in JSON format:
    {{
        "strength_score": <float 0-10>,
        "examples": [<list of concrete evidence examples>],
        "recommendation": "<STRONG|MODERATE|WEAK|INSUFFICIENT>",
        "reasoning": "<detailed explanation>"
    }}
    """
    
    response = bedrock_client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {"role": "user", "content": analysis_prompt}
            ]
        })
    )
    
    result = json.loads(response['body'].read())
    return json.loads(result['content'][0]['text'])

CORE_VALUES = [
    {
        "name": "Technical Excellence & Scalable Elegance",
        "description": "Readable, domain-driven code that scales horizontally",
        "keywords": ["architecture", "scalability", "performance", "clean code", "maintainability"],
        "examples": ["System design improvements", "Performance optimization", "Code refactoring"],
        "anti_patterns": ["Quick fixes", "Technical debt accumulation", "Monolithic thinking"]
    },
    # ... other 9 core values with similar structure
]
```

**Success Criteria:**
- [ ] Step Functions workflow handling complete hiring pipeline within 4 hours
- [ ] Core values screening achieving 90%+ accuracy vs manual evaluation
- [ ] Technical assessment generation personalized per candidate profile
- [ ] Interview kit generation meeting quality standards (>8.5/10 approval threshold)
- [ ] Dooray task integration creating structured interview workflow

### Task 4.1: Interview Kit Generation with Claude Sonnet 4

**Bedrock-Powered Interview Kit Generator:**
```python
def lambda_interview_kit_generation(event, context):
    """
    Generate comprehensive interview kit using Claude Sonnet 4 and Graph RAG context
    """
    candidate_id = event['candidate_id']
    graph_context = event['graph_context']
    role_requirements = event['role_requirements']
    
    bedrock_runtime = boto3.client('bedrock-runtime')
    
    # Generate comprehensive interview kit using Claude's enhanced reasoning
    interview_kit_prompt = f"""
    You are an expert hiring manager creating a comprehensive interview kit. Use the Graph RAG 
    context to generate personalized interview materials.
    
    Candidate Context (from Graph RAG):
    {json.dumps(graph_context, indent=2)}
    
    Role Requirements:
    {json.dumps(role_requirements, indent=2)}
    
    Generate a comprehensive interview kit with three components:
    
    1. CANDIDATE_CONTEXT.md - Executive briefing (2-3 paragraphs)
       - Key strengths with specific evidence from their background
       - Core value alignment with concrete examples
       - Red flags or areas requiring deeper exploration
       - Similar successful candidates from our team
    
    2. INTERVIEW_GUIDE.md - Detailed interview plan
       - 90-minute structured interview timeline
       - BEI questions tied to specific core values with candidate-specific examples
       - Technical deep-dive questions addressing their claimed expertise
       - System design problem tailored to their experience level
       - Pair programming problem from appropriate difficulty level
    
    3. INTERVIEW_SCRIPT.md - Verbatim script for interviewers
       - Complete question scripts with follow-up prompts
       - Scoring rubrics for each section
       - Time management guidance
       - Transition phrases and closing statements
    
    Requirements:
    - Reference specific projects and achievements from candidate's background
    - Include evidence-based core value questions
    - Provide clear scoring criteria
    - Maintain consistent quality with previous interview kits
    
    Output format: JSON with three markdown content sections
    """
    
    response = bedrock_runtime.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 8000,  # Large token budget for comprehensive kit
            "temperature": 0.3,   # Balanced creativity and consistency
            "messages": [
                {"role": "user", "content": interview_kit_prompt}
            ]
        })
    )
    
    result = json.loads(response['body'].read())
    interview_kit_content = json.loads(result['content'][0]['text'])
    
    # Store interview kit in S3 for interviewer access
    s3_client = boto3.client('s3')
    bucket_name = "gefjon-growth-interview-kits"
    
    for component, content in interview_kit_content.items():
        s3_key = f"candidates/{candidate_id}/{component.lower()}.md"
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=content,
            ContentType="text/markdown",
            Metadata={
                'candidate_id': candidate_id,
                'generated_timestamp': str(int(time.time())),
                'generator_model': 'claude-3-sonnet',
                'context_source': 'graph_rag'
            }
        )
    
    # Create shareable URLs for interviewers
    interview_kit_urls = {}
    for component in interview_kit_content.keys():
        s3_key = f"candidates/{candidate_id}/{component.lower()}.md"
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': s3_key},
            ExpiresIn=604800  # 7 days
        )
        interview_kit_urls[component] = presigned_url
    
    return {
        'statusCode': 200,
        'candidate_id': candidate_id,
        'interview_kit': {
            'content': interview_kit_content,
            's3_urls': interview_kit_urls,
            'generation_metadata': {
                'model_used': 'claude-3-sonnet-20240229-v1:0',
                'tokens_consumed': result.get('usage', {}).get('output_tokens', 0),
                'generation_time': context.get_remaining_time_in_millis()
            }
        }
    }
```

**Success Criteria:**
- [ ] Interview kits generated within 4-hour target timeframe
- [ ] Content quality achieving >8.5/10 Platform Lead approval rating
- [ ] S3 storage with secure presigned URLs for interviewer access
- [ ] Cost per interview kit generation <$2.00 using Claude Sonnet optimization

---

## Phase 5: Monitoring and Cost Optimization (Weeks 13-16)

### Task 5: Comprehensive CloudWatch Monitoring

**CloudWatch Dashboard Configuration:**
```python
import boto3
import json

def create_context_service_dashboard():
    """Create comprehensive CloudWatch dashboard for Graph RAG context service"""
    
    cloudwatch = boto3.client('cloudwatch')
    
    dashboard_body = {
        "widgets": [
            {
                "type": "metric",
                "properties": {
                    "metrics": [
                        ["AWS/Lambda", "Duration", "FunctionName", "context-generator"],
                        ["AWS/Lambda", "Invocations", "FunctionName", "context-generator"],
                        ["AWS/Lambda", "Errors", "FunctionName", "context-generator"]
                    ],
                    "period": 300,
                    "stat": "Average",
                    "region": "us-east-1", 
                    "title": "Context Generation Performance"
                }
            },
            {
                "type": "metric",
                "properties": {
                    "metrics": [
                        ["AWS/Neptune", "DatabaseConnections", "DBClusterIdentifier", "context-graph-cluster"],
                        ["AWS/Neptune", "VolumeReadIOPs", "DBClusterIdentifier", "context-graph-cluster"],
                        ["AWS/Neptune", "VolumeWriteIOPs", "DBClusterIdentifier", "context-graph-cluster"]
                    ],
                    "period": 300,
                    "stat": "Average",
                    "region": "us-east-1",
                    "title": "Neptune Graph Database Performance"
                }
            },
            {
                "type": "metric", 
                "properties": {
                    "metrics": [
                        ["AWS/ES", "SearchLatency", "DomainName", "context-vector-search"],
                        ["AWS/ES", "IndexingLatency", "DomainName", "context-vector-search"],
                        ["AWS/ES", "ClusterStatus.yellow", "DomainName", "context-vector-search"],
                        ["AWS/ES", "ClusterStatus.red", "DomainName", "context-vector-search"]
                    ],
                    "period": 300,
                    "stat": "Average", 
                    "region": "us-east-1",
                    "title": "OpenSearch Vector Database Health"
                }
            },
            {
                "type": "metric",
                "properties": {
                    "metrics": [
                        ["CostOptimization/ContextService", "CandidateProcessingCost"],
                        ["CostOptimization/ContextService", "TokensConsumed"],
                        ["CostOptimization/ContextService", "CacheHitRatio"],
                        ["CostOptimization/ContextService", "MonthlyBudgetUtilization"]
                    ],
                    "period": 3600,
                    "stat": "Average",
                    "region": "us-east-1", 
                    "title": "Cost Optimization Metrics"
                }
            },
            {
                "type": "log",
                "properties": {
                    "query": "SOURCE '/aws/lambda/context-generator'\n| fields @timestamp, candidate_id, processing_time_ms, cost_breakdown\n| filter processing_time_ms > 4000\n| sort @timestamp desc\n| limit 20",
                    "region": "us-east-1",
                    "title": "Slow Context Generation Analysis",
                    "view": "table"
                }
            }
        ]
    }
    
    cloudwatch.put_dashboard(
        DashboardName="ContextGraphRAGService",
        DashboardBody=json.dumps(dashboard_body)
    )

# Custom CloudWatch metrics for cost tracking
def publish_cost_metrics(candidate_id: str, processing_costs: dict):
    """Publish custom metrics for cost optimization tracking"""
    
    cloudwatch = boto3.client('cloudwatch')
    
    # Per-candidate cost tracking
    cloudwatch.put_metric_data(
        Namespace='CostOptimization/ContextService',
        MetricData=[
            {
                'MetricName': 'CandidateProcessingCost',
                'Value': processing_costs['total_cost'],
                'Unit': 'None',
                'Dimensions': [
                    {
                        'Name': 'CandidateId',
                        'Value': candidate_id
                    }
                ]
            },
            {
                'MetricName': 'TokensConsumed',
                'Value': processing_costs['total_tokens'],
                'Unit': 'Count'
            },
            {
                'MetricName': 'CacheHitRatio',
                'Value': processing_costs['cache_hit_ratio'],
                'Unit': 'Percent'
            }
        ]
    )
    
    # Budget utilization tracking
    monthly_budget = 3000  # $3,000 budget constraint
    current_utilization = get_monthly_cost_utilization()
    
    cloudwatch.put_metric_data(
        Namespace='CostOptimization/ContextService',
        MetricData=[
            {
                'MetricName': 'MonthlyBudgetUtilization',
                'Value': (current_utilization / monthly_budget) * 100,
                'Unit': 'Percent'
            }
        ]
    )

# CloudWatch Alarms for cost and performance
def create_cost_optimization_alarms():
    """Create CloudWatch alarms for cost and performance monitoring"""
    
    cloudwatch = boto3.client('cloudwatch')
    
    # High cost per candidate alarm
    cloudwatch.put_metric_alarm(
        AlarmName='HighCandidateProcessingCost',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CandidateProcessingCost',
        Namespace='CostOptimization/ContextService',
        Period=300,
        Statistic='Maximum',
        Threshold=10.0,  # Alert if >$10 per candidate
        ActionsEnabled=True,
        AlarmActions=[
            'arn:aws:sns:us-east-1:319470692494:cost-optimization-alerts'
        ],
        AlarmDescription='Alert when candidate processing cost exceeds $10',
        Unit='None'
    )
    
    # Low cache hit ratio alarm
    cloudwatch.put_metric_alarm(
        AlarmName='LowCacheHitRatio', 
        ComparisonOperator='LessThanThreshold',
        EvaluationPeriods=2,
        MetricName='CacheHitRatio',
        Namespace='CostOptimization/ContextService', 
        Period=900,
        Statistic='Average',
        Threshold=85.0,  # Alert if <85% cache hit ratio
        ActionsEnabled=True,
        AlarmActions=[
            'arn:aws:sns:us-east-1:319470692494:performance-alerts'
        ],
        AlarmDescription='Alert when cache hit ratio drops below 85%',
        Unit='Percent'
    )
    
    # Monthly budget utilization alarm
    cloudwatch.put_metric_alarm(
        AlarmName='MonthlyBudgetExceeded',
        ComparisonOperator='GreaterThanThreshold', 
        EvaluationPeriods=1,
        MetricName='MonthlyBudgetUtilization',
        Namespace='CostOptimization/ContextService',
        Period=3600,
        Statistic='Maximum',
        Threshold=90.0,  # Alert at 90% budget utilization
        ActionsEnabled=True,
        AlarmActions=[
            'arn:aws:sns:us-east-1:319470692494:budget-alerts'
        ],
        AlarmDescription='Alert when monthly budget utilization exceeds 90%',
        Unit='Percent'
    )
```

**Success Criteria:**
- [ ] CloudWatch dashboard providing real-time visibility into all system metrics
- [ ] Cost tracking achieving <$10 per candidate with detailed breakdown
- [ ] Performance monitoring showing <200ms context retrieval (p95)
- [ ] Cache hit ratio monitoring maintaining >85% efficiency
- [ ] Automated alerting for cost and performance thresholds

### Task 5.1: Real-Time Cost Optimization

**AWS Cost Explorer Integration:**
```python
import boto3
from datetime import datetime, timedelta

class CostOptimizationEngine:
    def __init__(self):
        self.cost_explorer = boto3.client('ce')
        self.cloudwatch = boto3.client('cloudwatch')
        
    async def analyze_service_costs(self):
        """Analyze costs across all AWS services used by the context system"""
        
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=30)
        
        # Get costs for all services used by context system
        cost_response = self.cost_explorer.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['BlendedCost', 'UsageQuantity'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'},
                {'Type': 'TAG', 'Key': 'Project'}
            ],
            Filter={
                'Tags': {
                    'Key': 'Project',
                    'Values': ['gefjon-growth-context-service']
                }
            }
        )
        
        # Analyze cost breakdown by service
        service_costs = {}
        total_monthly_cost = 0
        
        for result_by_time in cost_response['ResultsByTime']:
            for group in result_by_time['Groups']:
                service_name = group['Keys'][0]
                cost = float(group['Metrics']['BlendedCost']['Amount'])
                
                if service_name not in service_costs:
                    service_costs[service_name] = []
                service_costs[service_name].append(cost)
                total_monthly_cost += cost
        
        # Calculate cost per candidate processed
        candidates_processed = await self.get_monthly_candidate_count()
        cost_per_candidate = total_monthly_cost / max(candidates_processed, 1)
        
        # Identify cost optimization opportunities
        optimization_recommendations = []
        
        if service_costs.get('Amazon Bedrock', 0) > (total_monthly_cost * 0.4):
            optimization_recommendations.append({
                'service': 'Amazon Bedrock',
                'issue': 'High LLM costs',
                'recommendation': 'Increase caching, use model routing',
                'potential_savings': service_costs.get('Amazon Bedrock', 0) * 0.3
            })
        
        if service_costs.get('Amazon Neptune', 0) > (total_monthly_cost * 0.3):
            optimization_recommendations.append({
                'service': 'Amazon Neptune',
                'issue': 'High graph database costs',
                'recommendation': 'Optimize query patterns, implement connection pooling',
                'potential_savings': service_costs.get('Amazon Neptune', 0) * 0.2
            })
        
        return {
            'total_monthly_cost': total_monthly_cost,
            'cost_per_candidate': cost_per_candidate,
            'service_breakdown': service_costs,
            'candidates_processed': candidates_processed,
            'optimization_recommendations': optimization_recommendations,
            'budget_utilization': (total_monthly_cost / 3000) * 100  # $3,000 budget
        }
    
    async def implement_cost_optimization(self, recommendations: list):
        """Automatically implement approved cost optimization measures"""
        
        for rec in recommendations:
            if rec['service'] == 'Amazon Bedrock' and rec['potential_savings'] > 100:
                # Implement more aggressive caching
                await self.increase_cache_duration()
                await self.implement_model_routing()
                
            elif rec['service'] == 'Amazon Neptune' and rec['potential_savings'] > 50:
                # Optimize graph queries
                await self.optimize_neptune_queries()
                await self.implement_connection_pooling()
        
        # Update CloudWatch metrics with optimization actions
        await self.publish_optimization_metrics(recommendations)
    
    async def increase_cache_duration(self):
        """Increase cache TTL for frequently accessed context"""
        elasticache = boto3.client('elasticache')
        
        # Update cache configuration to increase TTL for stable context
        cache_config = {
            'candidate_profiles': 7200,    # 2 hours -> reduce API calls
            'core_values_analysis': 86400, # 24 hours -> stable content
            'interview_templates': 604800   # 1 week -> rarely changing
        }
        
        for cache_type, ttl in cache_config.items():
            await self.redis_client.config_set(f'{cache_type}_ttl', ttl)
    
    async def implement_model_routing(self):
        """Route requests to most cost-effective models based on complexity"""
        
        model_routing_config = {
            'simple_formatting': 'anthropic.claude-3-haiku-20240307-v1:0',    # $0.25/1K tokens
            'complex_analysis': 'anthropic.claude-3-sonnet-20240229-v1:0',    # $3.00/1K tokens  
            'critical_decisions': 'anthropic.claude-3-opus-20240229-v1:0'     # $15.00/1K tokens
        }
        
        # Update Lambda environment variables for model routing
        lambda_client = boto3.client('lambda')
        
        lambda_client.update_function_configuration(
            FunctionName='context-generator',
            Environment={
                'Variables': {
                    'MODEL_ROUTING_CONFIG': json.dumps(model_routing_config),
                    'COST_OPTIMIZATION_ENABLED': 'true'
                }
            }
        )
```

**AWS Cost Budget Integration:**
```python
def create_cost_budget_with_alerts():
    """Create AWS Budget for the context service with automated alerts"""
    
    budgets_client = boto3.client('budgets')
    
    # Create monthly budget for context service
    budget_response = budgets_client.create_budget(
        AccountId='319470692494',
        Budget={
            'BudgetName': 'ContextGraphRAGServiceBudget',
            'BudgetLimit': {
                'Amount': '3000.00',
                'Unit': 'USD'
            },
            'TimeUnit': 'MONTHLY',
            'TimePeriod': {
                'Start': datetime(2024, 1, 1),
                'End': datetime(2030, 12, 31)
            },
            'BudgetType': 'COST',
            'CostFilters': {
                'TagKey': ['Project'],
                'TagValue': ['gefjon-growth-context-service']
            }
        },
        NotificationsWithSubscribers=[
            {
                'Notification': {
                    'NotificationType': 'ACTUAL',
                    'ComparisonOperator': 'GREATER_THAN',
                    'Threshold': 80.0,  # Alert at 80% budget utilization
                    'ThresholdType': 'PERCENTAGE'
                },
                'Subscribers': [
                    {
                        'SubscriptionType': 'SNS',
                        'Address': 'arn:aws:sns:us-east-1:319470692494:budget-alerts'
                    }
                ]
            },
            {
                'Notification': {
                    'NotificationType': 'FORECASTED',
                    'ComparisonOperator': 'GREATER_THAN', 
                    'Threshold': 100.0,  # Alert if forecasted to exceed budget
                    'ThresholdType': 'PERCENTAGE'
                },
                'Subscribers': [
                    {
                        'SubscriptionType': 'SNS',
                        'Address': 'arn:aws:sns:us-east-1:319470692494:budget-alerts'
                    }
                ]
            }
        ]
    )
    
    return budget_response
```

**Success Criteria:**
- [ ] Monthly cost tracking staying within $3,000 budget constraint
- [ ] Per-candidate cost optimization achieving <$10 target (ideal $2-5)
- [ ] AWS Budget with automated alerts at 80% utilization
- [ ] Cost optimization engine reducing expenses by 20-30%
- [ ] Service cost breakdown providing actionable optimization insights

---

## Implementation Timeline Summary

### Week-by-Week AWS Implementation Plan

**Weeks 1-3: AWS Infrastructure Foundation**
- Deploy Neptune cluster with Multi-AZ configuration
- Set up OpenSearch domain with vector search capabilities  
- Configure ECS Fargate services with auto-scaling
- Implement RDS PostgreSQL, DynamoDB, ElastiCache integration
- Establish security foundation with Secrets Manager and IAM

**Weeks 4-5: Graph RAG Intelligence**
- Build Neptune knowledge graph schema and relationships
- Implement OpenSearch vector similarity search
- Deploy Bedrock-powered context optimization
- Create intelligent relationship prioritization algorithms
- Achieve 50-70% token reduction with preserved semantic quality

**Weeks 6-8: Universal API Platform**
- Deploy API Gateway with Lambda backend
- Implement agent-specific context formatting
- Build universal JSON API for 5 agent types
- Create caching layer with >85% hit ratio target
- Integrate all agent types (Gemini CLI, Claude Code, Amazon Q, KIRO, OpenAI)

**Weeks 9-12: Hiring Workflow Automation**
- Build Step Functions workflow for complete hiring pipeline
- Implement core values screening with Graph RAG discovery
- Deploy interview kit generation with Claude Sonnet 4
- Create Dooray task integration for workflow management
- Achieve <4 hour interview kit generation target

**Weeks 13-16: Monitoring & Optimization**
- Deploy CloudWatch comprehensive monitoring dashboard
- Implement cost optimization with Budget alerts
- Create performance monitoring with SLA tracking
- Build automated cost optimization engine
- Validate all success criteria and performance targets

**Final Validation Targets:**
- **Cost**: <$10 per candidate (target $2-5) ✅
- **Performance**: <200ms context retrieval (p95) ✅  
- **Quality**: >8.5/10 Platform Lead approval rating ✅
- **Scalability**: 40+ candidates/month, 15/week peak ✅
- **Availability**: >99.5% uptime with <11 minute MTTR ✅
- **Budget**: Total operational costs <$3,000/month ✅

This comprehensive AWS-native implementation roadmap ensures complete integration of all .kiro specification requirements with AWS cloud services, providing detailed task breakdown, cost optimization strategies, and success validation criteria for upcoming AWS Solution Architect consultations.