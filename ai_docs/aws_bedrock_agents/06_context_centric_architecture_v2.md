# Context-Centric Architecture for Gefjon Growth v2.0
**Focus: High-Quality Context Server + Token-Optimized Agent Environment**

## Executive Summary

This document outlines a completely revised architecture for Gefjon Growth, prioritizing **context quality and availability** over specific agent implementations. The system creates a robust context infrastructure that empowers any future agent (Claude Code, Gemini CLI, KIRO, AWS Bedrock, etc.) to operate with complete, up-to-date, and appropriately-sized context.

## New Architecture Priorities

### 1. **Context Server as First-Class Infrastructure** 🏗️
- Central context repository accessible by all AI agents
- Domain-separated but comprehensive context stores
- Real-time context updates with zero data loss
- Token-optimized context delivery

### 2. **Token-Aware Context Chunking** 📊  
- Dynamic context segmentation based on task requirements
- Quality-preserved smaller context chunks for optimal LLM performance
- Intelligent context selection algorithms

### 3. **Multi-Channel Context Updates** 🔄
- Kafka-based message queue for webhook buffering
- Manual update channels (HTTP API, file upload)
- AI-agent powered context quality assurance

### 4. **Agent-Agnostic Environment** 🔧
- Infrastructure that supports any agent architecture
- Focus on empowering agents rather than defining them
- Extensible foundation for future innovations

---

## Context Server Architecture

### Core Context Domains

Based on research showing LLM performance degradation with large inputs, we'll organize context into strategic domains:

```yaml
ContextDomains:
  Company:
    scope: "Organizational mission, values, policies, goals"
    size: "~50KB per domain"
    update_frequency: "quarterly"
    access_pattern: "high_frequency"
    
  Platform_Team:
    scope: "Team composition, tech stack, processes, responsibilities"  
    size: "~75KB per domain"
    update_frequency: "monthly"
    access_pattern: "high_frequency"
    
  HR_Processes:
    scope: "Hiring stages, evaluation criteria, BEI frameworks"
    size: "~100KB per domain"
    update_frequency: "monthly" 
    access_pattern: "medium_frequency"
    
  Candidate_Data:
    scope: "Individual candidate profiles and assessments"
    size: "~25KB per candidate"
    update_frequency: "real_time"
    access_pattern: "task_specific"
    
  Technical_Assets:
    scope: "Problem banks, interview guides, evaluation rubrics"
    size: "~150KB per domain"
    update_frequency: "weekly"
    access_pattern: "medium_frequency"
```

### Context Server Technical Stack

```yaml
Infrastructure:
  ContextStore:
    primary: "Amazon DynamoDB" # Fast, scalable, consistent
    secondary: "S3" # Large document storage
    cache: "ElastiCache Redis" # Sub-millisecond context retrieval
    
  MessageQueue:
    primary: "Apache Kafka" # Zero data loss webhook buffering
    backup: "AWS SQS" # Dead letter queue management
    
  ContextAPI:
    framework: "FastAPI" # High-performance Python API
    authentication: "AWS Cognito" # Secure access control
    rate_limiting: "Redis-based" # Prevent abuse
    
  VectorSearch:
    engine: "AWS OpenSearch Serverless" # Semantic context retrieval
    embeddings: "text-embedding-3-large" # High-quality embeddings
    chunking: "semantic_chunking" # Preserve meaning boundaries
```

### Context Quality Guarantees

```yaml
QualityStandards:
  Completeness:
    - All 10 company core values present and current
    - Team composition reflects actual structure (>95% accuracy)
    - HR processes match current implementations
    - Technical assets available at all difficulty levels
    
  Freshness:
    - Company context: <30 days staleness
    - Team context: <7 days staleness  
    - Candidate data: Real-time updates
    - Process documentation: <14 days staleness
    
  Consistency:
    - Cross-domain references validated
    - Naming conventions enforced
    - Metadata completeness verified
    - Agent access patterns optimized
```

---

## Token-Optimized Context Architecture

### Research-Driven Context Sizing

Based on the research you mentioned about LLM performance degradation, we implement intelligent context chunking:

```python
class TokenOptimizedContextManager:
    """
    Manages context delivery optimized for LLM performance
    Key principle: Smaller, high-quality context beats large, comprehensive context
    """
    
    MAX_TOKENS = {
        'task_context': 4000,      # Primary task-relevant context
        'domain_context': 2000,    # Supporting domain knowledge  
        'background_context': 1000, # General company/team context
        'total_budget': 7000       # Total token budget per request
    }
    
    def get_optimized_context(self, task_type: str, candidate_id: str = None) -> dict:
        """
        Returns token-optimized context for specific task
        Prioritizes most relevant information within token budget
        """
        context = {
            'primary': self._get_task_specific_context(task_type, candidate_id),
            'domain': self._get_domain_context(task_type),
            'background': self._get_background_context()
        }
        
        # Ensure we stay within token budget
        return self._enforce_token_limits(context)
    
    def _get_task_specific_context(self, task_type: str, candidate_id: str) -> dict:
        """Get the most relevant context for the specific task"""
        context_map = {
            'interview_kit_generation': [
                'candidate_profile',
                'core_values_detailed',
                'interview_frameworks',
                'technical_problem_bank'
            ],
            'candidate_screening': [
                'candidate_profile', 
                'screening_criteria',
                'core_values_summary',
                'red_flag_indicators'
            ],
            'performance_evaluation': [
                'employee_profile',
                'okr_frameworks',
                'performance_criteria',
                'team_context'
            ]
        }
        
        return self._fetch_context_components(
            context_map.get(task_type, []), 
            candidate_id,
            token_limit=self.MAX_TOKENS['task_context']
        )
```

### Intelligent Context Selection Algorithm

```python
class ContextSelectionAlgorithm:
    """
    Selects optimal context based on:
    1. Task requirements
    2. Token budget constraints  
    3. Context freshness
    4. Historical effectiveness
    """
    
    def select_context(self, task_description: str, agent_type: str) -> dict:
        # Parse task requirements
        required_domains = self._extract_domains(task_description)
        
        # Calculate token budget allocation
        token_budget = self._calculate_budget(agent_type)
        
        # Prioritize context by relevance
        prioritized_context = self._prioritize_by_relevance(
            required_domains, 
            task_description
        )
        
        # Build context within budget
        return self._build_context_within_budget(
            prioritized_context, 
            token_budget
        )
    
    def _extract_domains(self, task_description: str) -> list:
        """Use NLP to identify required context domains"""
        domain_keywords = {
            'company': ['values', 'mission', 'culture', 'goals'],
            'team': ['platform', 'technology', 'roles', 'process'],
            'hr': ['hiring', 'interview', 'evaluation', 'candidate'],
            'technical': ['code', 'system', 'architecture', 'problem']
        }
        
        required_domains = []
        for domain, keywords in domain_keywords.items():
            if any(keyword in task_description.lower() for keyword in keywords):
                required_domains.append(domain)
                
        return required_domains
```

---

## Context Update Infrastructure

### Multi-Channel Update Architecture

```yaml
UpdateChannels:
  WebhookBuffer:
    technology: "Apache Kafka"
    purpose: "Buffer external system webhooks (Dooray, Outlook, HR systems)"
    guarantees: "zero_data_loss"
    processing: "exactly_once_delivery"
    retention: "7_days"
    
  ManualUpdateAPI:
    technology: "FastAPI + Redis Queue"
    purpose: "Manual context updates via HTTP API"
    authentication: "AWS Cognito + API Keys"
    rate_limiting: "100_requests_per_minute"
    validation: "schema_based + ai_quality_check"
    
  FileUploadChannel:
    technology: "S3 + Lambda Triggers"
    purpose: "Batch context updates via file upload"
    supported_formats: ["JSON", "YAML", "CSV", "PDF"]
    processing: "async_with_notifications"
    validation: "automated_ai_review"
    
  GitIntegration:
    technology: "GitHub Webhooks + Actions"
    purpose: "Context updates from code repository changes"
    triggers: ["context_file_changes", "documentation_updates"]
    validation: "pr_based_review"
```

### AI-Powered Context Quality Assurance

```python
class AIContextQualityAssurance:
    """
    Uses existing AI agents (Claude Code, Gemini CLI, KIRO) to ensure
    context updates maintain high quality and consistency
    """
    
    def __init__(self):
        self.agents = {
            'claude_code': self._get_claude_code_client(),
            'gemini_cli': self._get_gemini_client(), 
            'kiro': self._get_kiro_client()
        }
    
    async def validate_context_update(self, 
                                    update_data: dict, 
                                    domain: str) -> ValidationResult:
        """
        Multi-agent validation of context updates
        Each agent validates different aspects for comprehensive quality
        """
        
        validation_tasks = {
            'claude_code': self._validate_technical_accuracy,
            'gemini_cli': self._validate_consistency,
            'kiro': self._validate_completeness
        }
        
        results = await asyncio.gather(*[
            task(update_data, domain) 
            for agent, task in validation_tasks.items()
        ])
        
        return self._aggregate_validation_results(results)
    
    async def _validate_technical_accuracy(self, data: dict, domain: str) -> dict:
        """Claude Code validates technical accuracy and formatting"""
        prompt = f"""
        Review this {domain} context update for technical accuracy:
        - Verify all technical references are correct
        - Check data format compliance
        - Validate cross-references and dependencies
        - Ensure no information conflicts with existing context
        
        Context Update: {json.dumps(data, indent=2)}
        """
        
        return await self.agents['claude_code'].analyze(prompt)
    
    async def _validate_consistency(self, data: dict, domain: str) -> dict:
        """Gemini CLI validates consistency with existing context"""
        prompt = f"""
        Using ReAct methodology, validate this {domain} context update:
        - Load existing {domain} context
        - Compare with proposed update  
        - Identify any inconsistencies or conflicts
        - Suggest improvements or corrections
        
        Proposed Update: {json.dumps(data, indent=2)}
        """
        
        return await self.agents['gemini_cli'].validate(prompt)
    
    async def _validate_completeness(self, data: dict, domain: str) -> dict:
        """KIRO validates completeness and missing information"""
        return await self.agents['kiro'].check_completeness(data, domain)
```

---

## Real-Time Context Synchronization

### Event-Driven Context Updates

```yaml
EventDrivenArchitecture:
  EventSources:
    - name: "candidate_profile_updated"
      trigger: "New candidate data or assessment results"
      action: "Update candidate context + notify active workflows"
      
    - name: "team_composition_changed"  
      trigger: "HR system updates or manual changes"
      action: "Refresh team context + update role mappings"
      
    - name: "process_documentation_updated"
      trigger: "Git commits to process documentation"
      action: "Validate changes + update HR process context"
      
    - name: "technical_assets_modified"
      trigger: "Interview problems or rubrics updated"
      action: "Version assets + update technical context"

  ProcessingPipeline:
    1. EventCapture: "Kafka consumer captures all events"
    2. ValidationQueue: "AI agents validate event data quality"
    3. ContextUpdate: "Apply validated changes to context store"
    4. CacheInvalidation: "Clear relevant cache entries"
    5. NotificationDispatch: "Notify dependent systems/agents"
    6. AuditLogging: "Record all changes for compliance"
```

### Context Versioning and Rollback

```python
class ContextVersionManager:
    """
    Manages context versions with ability to rollback bad updates
    Essential for maintaining system reliability
    """
    
    def __init__(self):
        self.version_store = DynamoDBVersionStore()
        self.rollback_capability = True
        
    def create_context_snapshot(self, domain: str) -> str:
        """Create versioned snapshot before any updates"""
        current_context = self._get_current_context(domain)
        version_id = self._generate_version_id()
        
        self.version_store.store_version(
            domain=domain,
            version_id=version_id,
            context_data=current_context,
            timestamp=datetime.utcnow(),
            metadata={'type': 'auto_snapshot'}
        )
        
        return version_id
    
    def rollback_context(self, domain: str, target_version: str) -> bool:
        """Rollback context to previous known-good state"""
        try:
            target_context = self.version_store.get_version(domain, target_version)
            self._apply_context_update(domain, target_context)
            self._invalidate_caches(domain)
            self._notify_rollback(domain, target_version)
            return True
        except Exception as e:
            logger.error(f"Rollback failed for {domain}: {e}")
            return False
```

---

## Agent Integration Framework

### Universal Agent Interface

```python
class UniversalAgentInterface:
    """
    Provides standardized context access for any AI agent
    Supports Claude Code, Gemini CLI, KIRO, AWS Bedrock, and future agents
    """
    
    def __init__(self, agent_name: str, task_type: str):
        self.agent_name = agent_name
        self.task_type = task_type
        self.context_manager = TokenOptimizedContextManager()
        
    def get_context_for_task(self, 
                           task_description: str, 
                           candidate_id: str = None,
                           custom_requirements: dict = None) -> dict:
        """
        Universal method for agents to request optimized context
        Returns task-appropriate context within token limits
        """
        
        # Get base context optimized for this task
        base_context = self.context_manager.get_optimized_context(
            self.task_type, 
            candidate_id
        )
        
        # Apply agent-specific customizations
        agent_customized = self._apply_agent_customizations(
            base_context, 
            self.agent_name
        )
        
        # Add any custom requirements
        if custom_requirements:
            agent_customized = self._merge_custom_requirements(
                agent_customized,
                custom_requirements
            )
        
        # Final token budget enforcement
        return self._enforce_final_token_limits(agent_customized)
    
    def _apply_agent_customizations(self, context: dict, agent_name: str) -> dict:
        """Apply agent-specific context formatting and priorities"""
        customizations = {
            'claude_code': {
                'format': 'markdown_with_metadata',
                'priority': 'technical_accuracy',
                'include_todos': True
            },
            'gemini_cli': {
                'format': 'yaml_structured',
                'priority': 'process_workflows', 
                'include_react_patterns': True
            },
            'kiro': {
                'format': 'structured_json',
                'priority': 'decision_contexts',
                'include_steering_data': True
            },
            'aws_bedrock': {
                'format': 'knowledge_base_chunks',
                'priority': 'semantic_relationships',
                'include_vector_metadata': True
            }
        }
        
        config = customizations.get(agent_name, {})
        return self._format_context(context, config)
```

### Context Quality Monitoring

```python
class ContextQualityMonitor:
    """
    Continuously monitors context quality and agent effectiveness
    Provides feedback loop for context optimization
    """
    
    def __init__(self):
        self.metrics_collector = CloudWatchMetrics()
        self.quality_thresholds = self._load_quality_thresholds()
        
    def monitor_agent_context_usage(self, 
                                   agent_name: str,
                                   task_type: str, 
                                   context_provided: dict,
                                   task_result: dict) -> None:
        """
        Monitor how effectively agents use provided context
        Track correlation between context quality and task success
        """
        
        metrics = {
            'context_tokens_used': self._count_tokens(context_provided),
            'context_domains_accessed': len(context_provided.keys()),
            'task_success_score': self._evaluate_task_success(task_result),
            'context_freshness_avg': self._calculate_freshness(context_provided),
            'missing_context_flags': self._detect_missing_context(task_result)
        }
        
        # Send metrics to CloudWatch
        self.metrics_collector.put_metrics(
            namespace='GefjonGrowth/ContextQuality',
            metrics=metrics,
            dimensions={
                'Agent': agent_name,
                'TaskType': task_type
            }
        )
        
        # Check for quality degradation
        if metrics['task_success_score'] < self.quality_thresholds['min_success']:
            self._trigger_context_quality_alert(agent_name, task_type, metrics)
    
    def _evaluate_task_success(self, task_result: dict) -> float:
        """
        Evaluate task success based on result quality indicators
        Returns score 0-1 representing task success
        """
        success_indicators = {
            'interview_kit_generation': [
                'candidate_context_completeness',
                'question_personalization_quality',
                'core_values_alignment_accuracy'
            ],
            'candidate_screening': [
                'screening_criteria_coverage',
                'evidence_quality_score',
                'bias_detection_accuracy'
            ]
        }
        
        # Implementation depends on specific task result structure
        # Returns aggregated success score
        pass
```

---

## Implementation Roadmap

### Phase 1: Context Infrastructure (Weeks 1-4)
```yaml
Week1:
  - Deploy Kafka cluster for webhook buffering
  - Set up DynamoDB context store with versioning
  - Create basic FastAPI context server
  - Implement token counting and budget enforcement

Week2:
  - Deploy Redis cache layer for context retrieval
  - Create context update API endpoints
  - Implement basic AI validation pipeline
  - Set up CloudWatch monitoring

Week3:
  - Build context versioning and rollback system
  - Create domain-specific context schemas
  - Implement semantic chunking algorithms
  - Add context freshness tracking

Week4:
  - Deploy universal agent interface
  - Create context quality monitoring dashboard
  - Implement automated context validation
  - Load initial context from existing Gefjon Growth data
```

### Phase 2: Token Optimization (Weeks 5-8)
```yaml
Week5-6:
  - Implement intelligent context selection algorithms
  - Create task-specific context optimization
  - Build agent-specific customization layer
  - Test token budget enforcement

Week7-8:
  - Deploy semantic search for context retrieval
  - Implement context relevance scoring
  - Create adaptive context sizing based on task complexity
  - Optimize cache performance and hit rates
```

### Phase 3: Multi-Channel Updates (Weeks 9-12)
```yaml
Week9-10:
  - Deploy Kafka consumers for external webhooks
  - Create file upload processing pipeline
  - Implement Git integration for context updates
  - Build manual update validation workflows

Week11-12:
  - Deploy AI-powered quality assurance system
  - Create automated context synchronization
  - Implement event-driven update notifications
  - Add comprehensive audit logging
```

### Phase 4: Agent Integration (Weeks 13-16)
```yaml
Week13-14:
  - Integrate Claude Code with context server
  - Connect Gemini CLI to optimized context delivery
  - Set up KIRO agent context access
  - Test multi-agent context consistency

Week15-16:
  - Deploy AWS Bedrock knowledge base integration
  - Create agent performance monitoring
  - Implement context usage analytics
  - Optimize system based on real usage patterns
```

---

## Success Metrics & Quality Assurance

### Context Quality Metrics
```yaml
QualityMetrics:
  Completeness:
    - Company context coverage: 100% (all 10 core values)
    - Team context accuracy: >95%
    - Process documentation current: <14 days staleness
    - Technical assets available: All difficulty levels
    
  Performance:
    - Context retrieval time: <200ms (95th percentile)
    - Token budget adherence: >99%
    - Cache hit ratio: >85%
    - Update propagation time: <30 seconds
    
  Agent_Effectiveness:
    - Interview kit quality score: >8.5/10
    - Context utilization rate: >80%
    - Task completion success: >95%
    - Agent error rate: <2%
```

This context-centric architecture creates the absolute environment you're looking for - one that empowers any current or future AI agent with high-quality, appropriately-sized, and always-current context for optimal performance.