# Graph RAG Context Infrastructure for AWS Bedrock
**Ultra-Low-Cost Multi-Database Architecture with Independent Context Service**

## Executive Summary

This document presents a comprehensive AWS-native implementation of the Graph RAG-based context infrastructure designed to serve as an independent microservice for all AI agents. The architecture leverages Amazon Neptune for knowledge graphs, Amazon OpenSearch for vector similarity, and existing AWS production infrastructure to create an ultra-low-cost, high-performance context delivery platform.

## Architecture Principles

### 1. Independent Context Service (MSA)
- **Service Name**: `context-graph-service`
- **Purpose**: Universal context service for current and future AI agents
- **Deployment**: Independent ECS Fargate service with auto-scaling
- **API**: RESTful JSON endpoints for agent-agnostic compatibility
- **Cost Target**: <$10 per candidate (target: $2-5)

### 2. Graph RAG Intelligence
- **Knowledge Graph**: Amazon Neptune for semantic relationships
- **Vector Database**: Amazon OpenSearch for semantic similarity
- **Context Fusion**: Intelligent combination of graph and vector results
- **Relationship Discovery**: Multi-hop graph traversal for context assembly

### 3. Ultra-Low-Cost Optimization
- **Subscription Model**: CLI agents instead of expensive API tokens
- **Shared Infrastructure**: Leverage existing AWS production resources (Account: 319470692494)
- **Aggressive Caching**: >95% cache hit ratio for cost minimization
- **Token Optimization**: Empirically-determined optimal ranges for quality preservation

## AWS-Native Graph RAG Architecture

### Core AWS Services Integration

```yaml
AWS_Infrastructure:
  Knowledge_Graph:
    service: "Amazon Neptune Serverless"
    instance_type: "db.r5.large" # Cost-optimized for development
    storage: "gp3 with automatic scaling"
    backup: "Point-in-time recovery enabled"
    cost_estimate: "$200-400/month"
    
  Vector_Database:
    service: "Amazon OpenSearch Serverless"
    engine: "Vector engine with k-NN"
    embedding_model: "Amazon Titan Embeddings G1 - Text"
    indexing: "HNSW for semantic similarity"
    cost_estimate: "$100-200/month"
    
  Context_Storage:
    primary: "DynamoDB with Global Tables"
    cache: "ElastiCache Redis (shared cluster)"
    files: "S3 with Intelligent Tiering"
    cost_estimate: "$50-100/month (shared)"
    
  Compute_Platform:
    service: "ECS Fargate (shared cluster)"
    scaling: "Auto-scaling based on context requests"
    cost: "$0 additional (shared infrastructure)"
    
  Message_Queue:
    primary: "Amazon MSK Serverless"
    backup: "SQS with Dead Letter Queues"
    processing: "Lambda functions for webhook handling"
    cost_estimate: "$100-200/month"
```

### Graph Schema for AWS Neptune

```cypher
# Knowledge Graph Schema for Amazon Neptune (Gremlin/SPARQL)

# Core entities with rich properties
CREATE VERTEX candidates {
    id: string (primary key),
    name: string,
    email: string,
    experience_years: int,
    current_role: string,
    core_values_score: decimal,
    created_at: datetime,
    updated_at: datetime
}

CREATE VERTEX skills {
    name: string (primary key),
    category: string,
    market_demand: decimal,
    complexity_level: int,
    description: text
}

CREATE VERTEX core_values {
    name: string (primary key),
    description: text,
    weight: decimal,
    examples: text[],
    anti_patterns: text[]
}

CREATE VERTEX roles {
    title: string,
    level: string,
    department: string,
    requirements: text,
    okr_alignment: string[]
}

CREATE VERTEX projects {
    name: string (primary key),
    domain: string,
    technologies: string[],
    impact: string,
    duration: string
}

# Rich relationships with properties and weights
CREATE EDGE has_skill {
    proficiency: decimal,     # 0.0-1.0 skill proficiency
    years_experience: int,    # Years of experience
    verified: boolean,        # Skill verification status
    evidence: text,           # Supporting evidence
    confidence: decimal       # Confidence in assessment
} FROM candidates TO skills

CREATE EDGE demonstrates {
    evidence: text,           # Specific behavioral evidence
    score: decimal,           # Alignment score 0.0-1.0
    frequency: string,        # How often demonstrated
    context: string,          # Situational context
    validated_by: string      # Who validated the evidence
} FROM candidates TO core_values

CREATE EDGE worked_on {
    duration: string,         # Project duration
    role: string,             # Role in project
    impact: string,           # Measurable impact
    technologies_used: string[], # Technical stack
    outcomes: text            # Project outcomes
} FROM candidates TO projects

CREATE EDGE required_for {
    importance: decimal,      # Importance weight 0.0-1.0
    level: string,           # Required proficiency level
    essential: boolean,       # Whether skill is essential
    alternatives: string[]    # Alternative skills
} FROM skills TO roles

CREATE EDGE critical_for {
    weight: decimal,          # Weight in role evaluation
    evaluation_method: string, # How to evaluate (BEI, etc.)
    examples: text[],         # Role-specific examples
    threshold: decimal        # Minimum required score
} FROM core_values TO roles

CREATE EDGE similar_to {
    similarity: decimal,      # Similarity score 0.0-1.0
    basis: string[],         # Basis for similarity
    computed_at: datetime,    # When similarity calculated
    confidence: decimal       # Confidence in similarity
} FROM candidates TO candidates
```

### Vector Database Schema for OpenSearch

```json
// OpenSearch index mappings for vector similarity
{
  "mappings": {
    "properties": {
      "entity_id": {"type": "keyword"},
      "entity_type": {"type": "keyword"},
      "content": {"type": "text"},
      "embedding": {
        "type": "knn_vector",
        "dimension": 1536,
        "method": {
          "name": "hnsw",
          "engine": "nmslib",
          "parameters": {
            "ef_construction": 128,
            "m": 24
          }
        }
      },
      "metadata": {
        "properties": {
          "domain": {"type": "keyword"},
          "quality_score": {"type": "float"},
          "created_at": {"type": "date"},
          "task_type": {"type": "keyword"},
          "token_count": {"type": "integer"}
        }
      }
    }
  },
  "settings": {
    "index": {
      "knn": true,
      "knn.algo_param.ef_search": 100
    }
  }
}
```

## Graph RAG Context Generation Engine

### AWS Lambda Function for Context Assembly

```python
import boto3
import json
from typing import Dict, List, Any
from gremlin_python.driver import client
from opensearchpy import OpenSearch, RequestsHttpConnection
from aws_requests_auth.aws_auth import AWSRequestsAuth

class AWSGraphRAGEngine:
    """AWS-native Graph RAG context generation engine"""
    
    def __init__(self):
        # Neptune configuration
        self.neptune_endpoint = os.environ['NEPTUNE_ENDPOINT']
        self.gremlin_client = client.Client(
            f"wss://{self.neptune_endpoint}:8182/gremlin",
            'g'
        )
        
        # OpenSearch configuration
        self.opensearch_client = OpenSearch(
            hosts=[{'host': os.environ['OPENSEARCH_ENDPOINT'], 'port': 443}],
            http_auth=AWSRequestsAuth(
                aws_access_key=os.environ['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                aws_token=os.environ['AWS_SESSION_TOKEN'],
                aws_host=os.environ['OPENSEARCH_ENDPOINT'],
                aws_region=os.environ['AWS_REGION'],
                aws_service='es'
            ),
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )
        
        # AWS services
        self.dynamodb = boto3.resource('dynamodb')
        self.bedrock = boto3.client('bedrock-runtime')
        
    def generate_context_graph_rag(self, 
                                   candidate_id: str, 
                                   task_type: str, 
                                   agent_type: str) -> Dict:
        """Generate intelligent context using Graph RAG methodology"""
        
        # 1. Multi-hop graph traversal for relationship discovery
        graph_context = self._discover_relationships(candidate_id, task_type)
        
        # 2. Vector similarity search for semantic context
        vector_context = self._find_similar_patterns(candidate_id, task_type)
        
        # 3. Intelligent context fusion
        fused_context = self._fuse_multi_source_context(
            graph_context, 
            vector_context
        )
        
        # 4. Relevance-based ranking and filtering
        ranked_context = self._rank_by_relevance(fused_context, task_type)
        
        # 5. Token optimization for target model
        optimized_context = self._optimize_for_agent(
            ranked_context, 
            agent_type
        )
        
        return optimized_context
    
    def _discover_relationships(self, candidate_id: str, task_type: str) -> Dict:
        """Multi-hop graph traversal using Amazon Neptune"""
        
        if task_type == "screening":
            # Focus on core values and skill relationships
            query = """
            g.V().has('candidates', 'id', candidate_id)
                .outE('demonstrates').as('demo_edge')
                .inV().as('values')
                .select('demo_edge', 'values')
                .by(valueMap())
                .union(
                    g.V().has('candidates', 'id', candidate_id)
                        .outE('has_skill').as('skill_edge')
                        .inV().as('skills')
                        .outE('required_for')
                        .inV().as('roles')
                        .select('skill_edge', 'skills', 'roles')
                        .by(valueMap())
                )
                .limit(50)
            """
            
        elif task_type == "interview_kit":
            # Focus on evidence and examples for BEI questions
            query = """
            g.V().has('candidates', 'id', candidate_id)
                .outE('worked_on').as('project_edge')
                .inV().as('projects')
                .outE('demonstrates')
                .inV().as('project_values')
                .select('project_edge', 'projects', 'project_values')
                .by(valueMap())
                .union(
                    g.V().has('candidates', 'id', candidate_id)
                        .outE('similar_to')
                        .inV().as('similar_candidates')
                        .outE('demonstrates')
                        .inV().as('similar_values')
                        .select('similar_candidates', 'similar_values')
                        .by(valueMap())
                )
                .limit(30)
            """
        
        try:
            result = self.gremlin_client.submit(query, {
                'candidate_id': candidate_id
            })
            return self._process_graph_results(result.all().result())
        except Exception as e:
            print(f"Graph query error: {e}")
            return {}
    
    def _find_similar_patterns(self, candidate_id: str, task_type: str) -> List[Dict]:
        """Vector similarity search using Amazon OpenSearch"""
        
        # Get candidate embedding
        candidate_embedding = self._get_candidate_embedding(candidate_id)
        
        # Construct search query
        search_query = {
            "size": 10,
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"metadata.task_type": task_type}},
                        {"range": {"metadata.quality_score": {"gte": 0.8}}}
                    ]
                }
            },
            "knn": {
                "embedding": {
                    "vector": candidate_embedding,
                    "k": 10
                }
            },
            "_source": {
                "includes": ["content", "metadata"]
            }
        }
        
        try:
            response = self.opensearch_client.search(
                index="candidate_contexts",
                body=search_query
            )
            return self._process_vector_results(response['hits']['hits'])
        except Exception as e:
            print(f"Vector search error: {e}")
            return []
    
    def _fuse_multi_source_context(self, 
                                  graph_context: Dict, 
                                  vector_context: List[Dict]) -> Dict:
        """Intelligent fusion of graph and vector results"""
        
        fused_context = {
            "graph_relationships": graph_context,
            "similar_patterns": vector_context,
            "fusion_metadata": {
                "graph_entities": len(graph_context.get("entities", [])),
                "vector_matches": len(vector_context),
                "fusion_timestamp": datetime.utcnow().isoformat()
            }
        }
        
        # Identify overlapping entities between graph and vector results
        overlaps = self._find_entity_overlaps(graph_context, vector_context)
        if overlaps:
            fused_context["entity_overlaps"] = overlaps
            fused_context["confidence_boost"] = len(overlaps) * 0.1
        
        return fused_context
    
    def _optimize_for_agent(self, context: Dict, agent_type: str) -> Dict:
        """Optimize context for specific agent type with token limits"""
        
        # Agent-specific optimization parameters
        optimization_config = {
            "aws_bedrock": {
                "max_tokens": 8000,
                "format": "knowledge_base_chunks",
                "priority": "semantic_relationships"
            },
            "claude_code": {
                "max_tokens": 6000,
                "format": "markdown_structured",
                "priority": "technical_accuracy"
            },
            "gemini_cli": {
                "max_tokens": 5000,
                "format": "yaml_hierarchical",
                "priority": "process_workflows"
            },
            "openai_mini": {
                "max_tokens": 4000,
                "format": "compressed_json",
                "priority": "cost_efficiency"
            }
        }
        
        config = optimization_config.get(agent_type, {
            "max_tokens": 5000,
            "format": "json",
            "priority": "general"
        })
        
        # Apply token optimization
        optimized = self._apply_token_limits(context, config["max_tokens"])
        optimized["agent_config"] = config
        optimized["optimization_applied"] = True
        
        return optimized

# AWS Lambda handler
def lambda_handler(event, context):
    """AWS Lambda function handler for Graph RAG context generation"""
    
    engine = AWSGraphRAGEngine()
    
    candidate_id = event.get('candidate_id')
    task_type = event.get('task_type', 'screening')
    agent_type = event.get('agent_type', 'aws_bedrock')
    
    try:
        result = engine.generate_context_graph_rag(
            candidate_id=candidate_id,
            task_type=task_type,
            agent_type=agent_type
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(result),
            'headers': {
                'Content-Type': 'application/json',
                'X-Context-Tokens': str(result.get('token_count', 0))
            }
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Context generation failed'
            })
        }
```

## Cost Optimization Strategy

### Ultra-Low-Cost Implementation

```yaml
Cost_Optimization:
  Subscription_Model:
    gemini_cli: "$20-30/month subscription"
    claude_code: "$20-30/month subscription"
    amazon_q: "$19/month subscription"
    openai_mini: "$20-30/month subscription"
    total_subscriptions: "$79-109/month"
    
  Shared_Infrastructure:
    existing_ecs: "$0 additional cost"
    existing_rds: "$0 additional cost"
    existing_s3: "$0 additional cost"
    existing_redis: "$0 additional cost"
    
  New_AWS_Services:
    neptune_serverless: "$200-400/month"
    opensearch_serverless: "$100-200/month"
    msk_serverless: "$100-200/month"
    lambda_compute: "$50-100/month"
    total_new: "$450-900/month"
    
  Total_Monthly_Cost: "$529-1009/month"
  Cost_Per_Candidate: "$13-25 (at 40 candidates/month)"
  
Cost_Reduction_Strategies:
  cache_optimization:
    target_hit_ratio: ">95%"
    api_call_reduction: "90-95%"
    estimated_savings: "$300-500/month"
    
  subscription_amortization:
    fixed_cost_spread: "Across all candidates"
    volume_efficiency: "Higher volume = lower per-candidate cost"
    target_cost: "$2-5 per candidate at scale"
    
  resource_sharing:
    infrastructure_reuse: "100% shared with existing systems"
    marginal_cost: "Near zero for compute resources"
    efficiency_gain: "Significant cost leverage"
```

### Intelligent Caching for Cost Reduction

```python
class AWSCostOptimizedCache:
    """Ultra-high performance caching for cost minimization"""
    
    def __init__(self):
        self.redis_client = boto3.client('elasticache')
        self.cache_patterns = {
            "candidate_profile": 3600,      # 1 hour TTL
            "graph_relationships": 7200,    # 2 hour TTL
            "vector_similarities": 14400,   # 4 hour TTL
            "optimized_context": 1800,      # 30 minute TTL
            "agent_responses": 86400,       # 24 hour TTL
        }
        
    def get_cached_context(self, cache_key: str) -> Dict:
        """Retrieve cached context with high hit ratio optimization"""
        try:
            cached = self.redis_client.get(cache_key)
            if cached:
                self._record_cache_hit(cache_key)
                return json.loads(cached)
        except Exception as e:
            print(f"Cache retrieval error: {e}")
        
        self._record_cache_miss(cache_key)
        return None
    
    def cache_context_pattern(self, 
                             pattern_type: str, 
                             context_data: Dict,
                             similarity_threshold: float = 0.8) -> str:
        """Cache reusable context patterns for similar candidates"""
        
        # Generate pattern-based cache key
        pattern_key = self._generate_pattern_key(
            pattern_type, 
            context_data,
            similarity_threshold
        )
        
        # Store with pattern-specific TTL
        ttl = self.cache_patterns.get(pattern_type, 3600)
        
        try:
            self.redis_client.setex(
                pattern_key,
                ttl,
                json.dumps(context_data)
            )
        except Exception as e:
            print(f"Cache storage error: {e}")
        
        return pattern_key
    
    def get_cache_efficiency_metrics(self) -> Dict:
        """Monitor cache efficiency for cost optimization"""
        return {
            "hit_ratio": self._calculate_hit_ratio(),
            "cost_savings": self._estimate_cost_savings(),
            "api_calls_avoided": self._count_avoided_calls(),
            "monthly_efficiency": self._project_monthly_savings()
        }
```

## Multi-Agent Integration with AWS Bedrock

### Bedrock Agent Configuration

```json
{
  "agentName": "contextGraphRAGAgent",
  "description": "Graph RAG-powered context assembly agent",
  "foundationModel": "anthropic.claude-3-sonnet-20240229-v1:0",
  "instruction": "You are a context assembly specialist that uses Graph RAG methodology to provide intelligent, relationship-aware context to other AI agents. You combine knowledge graph relationships with vector similarity to create comprehensive, token-optimized context for specific tasks.",
  "knowledgeBases": [
    {
      "knowledgeBaseId": "company_values_kb",
      "description": "Dunamis Capital core values and cultural context",
      "retrievalConfiguration": {
        "vectorSearchConfiguration": {
          "numberOfResults": 10,
          "overrideSearchType": "HYBRID"
        }
      }
    },
    {
      "knowledgeBaseId": "platform_team_kb",
      "description": "Platform development team composition and processes",
      "retrievalConfiguration": {
        "vectorSearchConfiguration": {
          "numberOfResults": 8,
          "overrideSearchType": "SEMANTIC"
        }
      }
    },
    {
      "knowledgeBaseId": "technical_assets_kb",
      "description": "Interview problems, rubrics, and technical assessments",
      "retrievalConfiguration": {
        "vectorSearchConfiguration": {
          "numberOfResults": 15,
          "overrideSearchType": "HYBRID"
        }
      }
    }
  ],
  "actionGroups": [
    {
      "actionGroupName": "graphContextRetrieval",
      "description": "Retrieve context using graph traversal",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:us-east-1:319470692494:function:graph-context-retrieval"
      },
      "apiSchema": {
        "payload": {
          "type": "object",
          "properties": {
            "candidate_id": {"type": "string"},
            "task_type": {"type": "string"},
            "relationship_depth": {"type": "integer"}
          }
        }
      }
    },
    {
      "actionGroupName": "vectorSimilaritySearch",
      "description": "Find similar patterns using vector search",
      "actionGroupExecutor": {
        "lambda": "arn:aws:lambda:us-east-1:319470692494:function:vector-similarity-search"
      },
      "apiSchema": {
        "payload": {
          "type": "object",
          "properties": {
            "entity_id": {"type": "string"},
            "similarity_threshold": {"type": "number"},
            "max_results": {"type": "integer"}
          }
        }
      }
    }
  ],
  "promptOverrideConfiguration": {
    "promptConfigurations": [
      {
        "promptType": "PRE_PROCESSING",
        "promptState": "ENABLED",
        "promptCreationMode": "OVERRIDDEN",
        "basePromptTemplate": "You are about to generate context for an AI agent. First, analyze the task requirements and determine what types of relationships and patterns would be most relevant. Consider: 1) Direct relationships (candidate -> skills -> roles), 2) Evidence patterns (projects -> values -> behaviors), 3) Similar successful examples, 4) Token optimization requirements."
      },
      {
        "promptType": "POST_PROCESSING", 
        "promptState": "ENABLED",
        "promptCreationMode": "OVERRIDDEN",
        "basePromptTemplate": "Review the generated context to ensure: 1) Token count is within optimal range for target agent, 2) Most relevant relationships are prioritized, 3) Context maintains semantic coherence, 4) Quality score meets minimum threshold of 8.5/10."
      }
    ]
  }
}
```

## Implementation Roadmap

### Phase 1: AWS Infrastructure Setup (Weeks 1-4)
```yaml
Week_1:
  - Deploy Neptune Serverless cluster
  - Create knowledge graph schema
  - Set up basic Gremlin queries
  - Configure IAM roles and security
  
Week_2:
  - Deploy OpenSearch Serverless
  - Create vector index mappings
  - Implement embedding generation
  - Test semantic similarity search
  
Week_3:
  - Set up MSK Serverless for webhooks
  - Create Lambda functions for processing
  - Implement DynamoDB context storage
  - Configure Redis cache optimization
  
Week_4:
  - Deploy ECS Fargate context service
  - Create API Gateway endpoints
  - Implement authentication and rate limiting
  - Load existing Gefjon Growth data
```

### Phase 2: Graph RAG Engine (Weeks 5-8)
```yaml
Week_5:
  - Implement graph traversal algorithms
  - Create relationship discovery functions
  - Build context fusion engine
  - Test multi-hop queries
  
Week_6:
  - Implement vector similarity search
  - Create pattern recognition algorithms
  - Build relevance ranking system
  - Test semantic matching
  
Week_7:
  - Implement token optimization
  - Create agent-specific formatting
  - Build intelligent context selection
  - Test quality preservation
  
Week_8:
  - Deploy cost monitoring system
  - Implement cache optimization
  - Create performance metrics
  - Validate ultra-low-cost targets
```

### Phase 3: Multi-Agent Integration (Weeks 9-12)
```yaml
Week_9:
  - Configure AWS Bedrock agents
  - Create knowledge base integrations
  - Implement action group functions
  - Test Bedrock context delivery
  
Week_10:
  - Integrate external agents (Claude Code, Gemini)
  - Create universal API interface
  - Implement agent-specific optimizations
  - Test cross-agent consistency
  
Week_11:
  - Deploy context update pipelines
  - Create webhook processing
  - Implement AI validation system
  - Test real-time synchronization
  
Week_12:
  - Production optimization and tuning
  - Performance monitoring setup
  - Cost efficiency validation
  - Quality assurance testing
```

## Success Metrics & Monitoring

### AWS CloudWatch Metrics
```yaml
Performance_Metrics:
  context_retrieval_latency:
    target: "<200ms (p95)"
    alarm_threshold: ">500ms"
    
  cache_hit_ratio:
    target: ">95%"
    alarm_threshold: "<85%"
    
  graph_query_performance:
    target: "<100ms average"
    alarm_threshold: ">300ms"
    
  vector_search_latency:
    target: "<150ms (p95)"
    alarm_threshold: ">400ms"

Cost_Metrics:
  cost_per_candidate:
    target: "<$10"
    stretch_goal: "$2-5"
    alarm_threshold: ">$15"
    
  monthly_infrastructure_cost:
    budget: "$529-1009"
    alarm_threshold: ">$1200"
    
  api_cost_savings:
    target: "90-95% reduction"
    measurement: "vs. pure API token model"

Quality_Metrics:
  context_quality_score:
    target: ">8.5/10"
    measurement: "AI agent validation"
    
  relationship_discovery_accuracy:
    target: ">90%"
    measurement: "Manual validation sample"
    
  token_optimization_effectiveness:
    target: "50-70% reduction"
    measurement: "vs. unoptimized context"
```

## Security and Compliance

### AWS Security Configuration
```yaml
Security_Measures:
  Network_Security:
    vpc: "Isolated VPC with private subnets"
    security_groups: "Least-privilege access rules"
    nacls: "Network-level access control"
    
  Data_Encryption:
    at_rest: "AES-256 encryption for all storage"
    in_transit: "TLS 1.2+ for all communications"
    key_management: "AWS KMS with automatic rotation"
    
  Access_Control:
    iam: "Role-based access with least privilege"
    authentication: "AWS Cognito + API keys"
    audit_logging: "CloudTrail + structured logs"
    
  Compliance:
    gdpr: "Data retention and deletion policies"
    audit_trail: "Immutable event logging"
    data_privacy: "Candidate data encryption"
```

This AWS-native Graph RAG implementation provides the comprehensive context infrastructure needed for ultra-low-cost, high-performance AI agent empowerment while leveraging existing production infrastructure and achieving the target <$10 per candidate cost.
