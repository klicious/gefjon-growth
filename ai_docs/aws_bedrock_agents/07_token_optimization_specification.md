# Token Optimization Specification for Gefjon Growth
**Research-Driven Context Chunking for Optimal LLM Performance**

## Research Foundation

Based on the research indicating LLM quality degradation with increased token count, this specification defines optimal context delivery strategies that maximize agent effectiveness while staying within research-validated token limits.

## Token Budget Framework

### Research-Based Token Limits

```yaml
TokenLimits:
  OptimalPerformanceZone:
    total_context: 7000      # Maximum for maintaining high quality
    task_specific: 4000      # Primary task-relevant information  
    domain_context: 2000     # Supporting knowledge
    background: 1000         # Essential company/team context
    
  QualityThresholds:
    high_quality: "<5000 tokens"     # Optimal performance range
    good_quality: "5000-8000 tokens" # Acceptable with slight degradation
    degraded: ">8000 tokens"         # Noticeable quality loss
    
  AgentSpecificBudgets:
    claude_code: 7000        # Complex reasoning tasks
    gemini_cli: 6000         # Process-focused workflows
    kiro: 5000               # Decision-making contexts
    bedrock_agents: 4000     # Specialized task agents
```

### Dynamic Token Allocation

```python
class DynamicTokenAllocator:
    """
    Allocates token budget based on task complexity and agent capabilities
    Ensures optimal performance within research-validated limits
    """
    
    COMPLEXITY_MULTIPLIERS = {
        'simple': 0.7,      # Basic tasks (candidate intake, simple screening)
        'moderate': 1.0,    # Standard tasks (interview kit generation)
        'complex': 1.3,     # Advanced tasks (comprehensive evaluation)
        'critical': 1.5     # High-stakes decisions (final hiring recommendations)
    }
    
    def __init__(self):
        self.base_budgets = {
            'task_context': 4000,
            'domain_context': 2000, 
            'background_context': 1000
        }
        
    def allocate_tokens(self, 
                       task_complexity: str,
                       agent_type: str,
                       priority_domains: List[str]) -> dict:
        """
        Allocate token budget based on task requirements
        Returns optimized allocation within performance limits
        """
        
        # Get base allocation for agent type
        base_budget = self._get_agent_budget(agent_type)
        
        # Apply complexity multiplier
        multiplier = self.COMPLEXITY_MULTIPLIERS.get(task_complexity, 1.0)
        adjusted_budget = int(base_budget * multiplier)
        
        # Ensure we don't exceed optimal performance zone
        final_budget = min(adjusted_budget, 7000)
        
        # Allocate across context categories
        return self._distribute_budget(final_budget, priority_domains)
    
    def _distribute_budget(self, total_budget: int, priority_domains: List[str]) -> dict:
        """
        Distribute token budget across context categories based on priorities
        """
        # Base allocation percentages
        base_allocation = {
            'task_specific': 0.57,    # ~4000/7000
            'domain_knowledge': 0.29,  # ~2000/7000
            'background': 0.14        # ~1000/7000
        }
        
        # Adjust based on priority domains
        if 'technical' in priority_domains:
            base_allocation['task_specific'] += 0.1
            base_allocation['domain_knowledge'] -= 0.1
        elif 'company_culture' in priority_domains:
            base_allocation['background'] += 0.1
            base_allocation['task_specific'] -= 0.1
            
        # Calculate final allocations
        return {
            category: int(total_budget * percentage)
            for category, percentage in base_allocation.items()
        }
```

### Context Chunking Algorithms

```python
class SemanticContextChunker:
    """
    Chunks context while preserving semantic meaning and relationships
    Critical for maintaining context quality within token limits
    """
    
    def __init__(self):
        self.tiktoken_encoder = tiktoken.encoding_for_model("gpt-4")
        self.semantic_boundaries = [
            'company_values_block',
            'team_composition_section', 
            'process_step',
            'candidate_experience_item',
            'technical_requirement'
        ]
        
    def chunk_context_semantically(self,
                                 raw_context: dict,
                                 token_budget: int,
                                 preserve_priority: List[str]) -> dict:
        """
        Create semantic chunks that preserve meaning within token limits
        """
        
        # Prioritize context elements
        prioritized_context = self._prioritize_context(raw_context, preserve_priority)
        
        # Create semantic chunks
        semantic_chunks = self._create_semantic_chunks(prioritized_context)
        
        # Select optimal chunks within budget
        selected_chunks = self._select_within_budget(semantic_chunks, token_budget)
        
        # Reconstruct coherent context
        return self._reconstruct_context(selected_chunks)
    
    def _create_semantic_chunks(self, context: dict) -> List[dict]:
        """
        Break context into semantically coherent chunks
        Each chunk maintains complete meaning for its domain
        """
        chunks = []
        
        for domain, content in context.items():
            if domain == 'company_values':
                # Each core value becomes its own chunk
                for i, value in enumerate(content.get('values', [])):
                    chunks.append({
                        'type': 'company_value',
                        'priority': 'high',
                        'domain': domain,
                        'content': {
                            'value_number': i + 1,
                            'value_name': value['name'],
                            'description': value['description'],
                            'good_examples': value.get('examples', []),
                            'anti_patterns': value.get('anti_patterns', [])
                        },
                        'tokens': self._count_tokens(value)
                    })
                    
            elif domain == 'candidate_profile':
                # Group related candidate information
                experience_chunk = {
                    'type': 'candidate_experience',
                    'priority': 'high',
                    'domain': domain,
                    'content': {
                        'work_history': content.get('experience', {}),
                        'technical_skills': content.get('skills', {}),
                        'projects': content.get('projects', [])
                    }
                }
                experience_chunk['tokens'] = self._count_tokens(experience_chunk['content'])
                chunks.append(experience_chunk)
                
                personal_chunk = {
                    'type': 'candidate_personal',
                    'priority': 'medium',
                    'domain': domain,
                    'content': {
                        'name': content.get('name'),
                        'contact': content.get('contact', {}),
                        'education': content.get('education', {})
                    }
                }
                personal_chunk['tokens'] = self._count_tokens(personal_chunk['content'])
                chunks.append(personal_chunk)
                
            elif domain == 'team_context':
                # Create chunks for different team aspects
                structure_chunk = {
                    'type': 'team_structure',
                    'priority': 'high',
                    'domain': domain,
                    'content': {
                        'composition': content.get('team_composition', {}),
                        'roles': content.get('roles', {}),
                        'tech_stack': content.get('technology_stack', {})
                    }
                }
                structure_chunk['tokens'] = self._count_tokens(structure_chunk['content'])
                chunks.append(structure_chunk)
                
        return chunks
    
    def _select_within_budget(self, chunks: List[dict], token_budget: int) -> List[dict]:
        """
        Select optimal combination of chunks within token budget
        Uses priority-based greedy selection with quality preservation
        """
        
        # Sort chunks by priority and token efficiency
        prioritized_chunks = sorted(
            chunks,
            key=lambda x: (
                {'high': 3, 'medium': 2, 'low': 1}[x['priority']],
                -x['tokens']  # Prefer smaller chunks for efficiency
            ),
            reverse=True
        )
        
        selected_chunks = []
        remaining_budget = token_budget
        
        # Greedy selection with priority weighting
        for chunk in prioritized_chunks:
            if chunk['tokens'] <= remaining_budget:
                selected_chunks.append(chunk)
                remaining_budget -= chunk['tokens']
            elif chunk['priority'] == 'high' and remaining_budget > chunk['tokens'] * 0.8:
                # For high-priority chunks, allow slight budget overflow
                truncated_chunk = self._truncate_chunk(chunk, remaining_budget)
                selected_chunks.append(truncated_chunk)
                remaining_budget = 0
                break
                
        return selected_chunks
```

### Quality-Preserving Compression

```python
class ContextQualityPreserver:
    """
    Compresses context while maintaining essential quality and relationships
    Ensures agents receive complete, actionable information within token limits
    """
    
    def __init__(self):
        self.essential_fields = {
            'company_values': ['name', 'description', 'examples'],
            'candidate': ['name', 'experience', 'key_projects'],
            'team': ['composition', 'tech_stack', 'responsibilities'],
            'process': ['stages', 'criteria', 'deliverables']
        }
        
    def compress_while_preserving_quality(self,
                                        context_chunks: List[dict],
                                        target_tokens: int) -> dict:
        """
        Compress context chunks to target token count while preserving quality
        Uses intelligent summarization and relationship preservation
        """
        
        current_tokens = sum(chunk['tokens'] for chunk in context_chunks)
        
        if current_tokens <= target_tokens:
            return self._reconstruct_context(context_chunks)
        
        compression_ratio = target_tokens / current_tokens
        
        compressed_chunks = []
        for chunk in context_chunks:
            if chunk['priority'] == 'high':
                # Minimal compression for high-priority content
                target_chunk_tokens = int(chunk['tokens'] * max(0.8, compression_ratio))
            else:
                # More aggressive compression for lower priority
                target_chunk_tokens = int(chunk['tokens'] * compression_ratio)
                
            compressed_chunk = self._compress_chunk(chunk, target_chunk_tokens)
            compressed_chunks.append(compressed_chunk)
            
        return self._reconstruct_context(compressed_chunks)
    
    def _compress_chunk(self, chunk: dict, target_tokens: int) -> dict:
        """
        Compress individual chunk while preserving essential information
        """
        content = chunk['content']
        chunk_type = chunk['type']
        
        if chunk_type == 'company_value':
            # For company values, preserve core meaning but compress examples
            compressed_content = {
                'value_name': content['value_name'],
                'description': self._compress_text(
                    content['description'], 
                    target_tokens * 0.6
                ),
                'key_example': self._select_best_example(
                    content.get('good_examples', []),
                    target_tokens * 0.3
                ),
                'anti_pattern': self._select_best_example(
                    content.get('anti_patterns', []),
                    target_tokens * 0.1
                )
            }
            
        elif chunk_type == 'candidate_experience':
            # Preserve most relevant experience items
            compressed_content = {
                'recent_experience': self._compress_work_history(
                    content.get('work_history', {}),
                    target_tokens * 0.5
                ),
                'key_skills': self._select_top_skills(
                    content.get('technical_skills', {}),
                    target_tokens * 0.3
                ),
                'notable_projects': self._select_top_projects(
                    content.get('projects', []),
                    target_tokens * 0.2
                )
            }
            
        else:
            # Default compression strategy
            compressed_content = self._generic_compress(content, target_tokens)
            
        chunk['content'] = compressed_content
        chunk['tokens'] = self._count_tokens(compressed_content)
        chunk['compressed'] = True
        
        return chunk
```

---

## Context Update Mechanisms

### Kafka-Based Message Queue Architecture

```python
class KafkaContextUpdateQueue:
    """
    Zero-data-loss webhook buffering using Apache Kafka
    Ensures all context updates are captured and processed
    """
    
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['kafka-cluster:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8'),
            acks='all',  # Ensure zero data loss
            retries=3,
            retry_backoff_ms=1000
        )
        
        self.topics = {
            'webhook_updates': 'gefjon-webhook-updates',
            'manual_updates': 'gefjon-manual-updates',
            'system_updates': 'gefjon-system-updates',
            'validation_results': 'gefjon-validation-results'
        }
        
    def buffer_webhook_update(self,
                             source: str,
                             update_type: str, 
                             data: dict,
                             metadata: dict = None) -> str:
        """
        Buffer webhook updates for processing
        Guarantees no data loss even during system failures
        """
        
        update_id = self._generate_update_id()
        
        message = {
            'update_id': update_id,
            'timestamp': datetime.utcnow().isoformat(),
            'source': source,
            'update_type': update_type,
            'data': data,
            'metadata': metadata or {},
            'status': 'pending'
        }
        
        # Send to Kafka with retry logic
        future = self.producer.send(
            self.topics['webhook_updates'],
            key=update_id,
            value=message
        )
        
        # Ensure message is sent successfully
        try:
            record_metadata = future.get(timeout=10)
            logger.info(f"Update {update_id} buffered successfully: {record_metadata}")
            return update_id
        except Exception as e:
            logger.error(f"Failed to buffer update {update_id}: {e}")
            raise
    
    def process_update_queue(self):
        """
        Process buffered updates with AI validation
        Ensures high-quality context updates
        """
        consumer = KafkaConsumer(
            self.topics['webhook_updates'],
            bootstrap_servers=['kafka-cluster:9092'],
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            enable_auto_commit=False,  # Manual commit after successful processing
            max_poll_records=10       # Process in small batches
        )
        
        for message in consumer:
            update_data = message.value
            
            try:
                # Validate update with AI agents
                validation_result = await self._validate_with_ai(update_data)
                
                if validation_result['valid']:
                    # Apply update to context store
                    await self._apply_context_update(update_data)
                    
                    # Invalidate relevant caches
                    await self._invalidate_caches(update_data['update_type'])
                    
                    # Notify dependent systems
                    await self._notify_update_applied(update_data)
                    
                else:
                    # Handle validation failure
                    await self._handle_validation_failure(
                        update_data, 
                        validation_result
                    )
                
                # Commit offset after successful processing
                consumer.commit()
                
            except Exception as e:
                logger.error(f"Error processing update {update_data['update_id']}: {e}")
                # Do not commit offset - message will be reprocessed
                continue
```

### Manual Update Channels

```python
class ManualUpdateAPI:
    """
    HTTP API for manual context updates with validation
    Supports various input formats and AI-powered quality assurance
    """
    
    def __init__(self):
        self.app = FastAPI(title="Gefjon Context Update API")
        self.validator = AIContextValidator()
        self.setup_routes()
        
    def setup_routes(self):
        
        @self.app.post("/api/v1/context/update/{domain}")
        async def update_context(
            domain: str,
            update_data: dict,
            api_key: str = Depends(self.verify_api_key),
            background_tasks: BackgroundTasks
        ):
            """
            Manual context update endpoint
            Validates and applies context updates with AI quality assurance
            """
            
            # Generate update ID for tracking
            update_id = str(uuid.uuid4())
            
            try:
                # Validate domain
                if domain not in ['company', 'team', 'hr_processes', 'technical']:
                    raise HTTPException(400, f"Invalid domain: {domain}")
                
                # Schema validation
                self._validate_update_schema(domain, update_data)
                
                # Queue for AI validation
                background_tasks.add_task(
                    self._process_manual_update,
                    update_id,
                    domain,
                    update_data
                )
                
                return {
                    'update_id': update_id,
                    'status': 'queued_for_validation',
                    'estimated_processing_time': '2-5 minutes'
                }
                
            except Exception as e:
                logger.error(f"Manual update failed: {e}")
                raise HTTPException(500, str(e))
        
        @self.app.post("/api/v1/context/upload")
        async def upload_context_file(
            file: UploadFile = File(...),
            domain: str = Form(...),
            api_key: str = Depends(self.verify_api_key)
        ):
            """
            File upload endpoint for batch context updates
            Supports JSON, YAML, CSV formats
            """
            
            # Validate file type
            allowed_types = ['application/json', 'text/yaml', 'text/csv']
            if file.content_type not in allowed_types:
                raise HTTPException(400, f"Unsupported file type: {file.content_type}")
            
            # Process file based on type
            try:
                content = await file.read()
                
                if file.content_type == 'application/json':
                    update_data = json.loads(content)
                elif file.content_type == 'text/yaml':
                    update_data = yaml.safe_load(content)
                elif file.content_type == 'text/csv':
                    update_data = self._process_csv_update(content, domain)
                
                # Queue for processing
                update_id = await self._queue_file_update(domain, update_data, file.filename)
                
                return {
                    'update_id': update_id,
                    'filename': file.filename,
                    'status': 'uploaded_and_queued'
                }
                
            except Exception as e:
                raise HTTPException(500, f"File processing failed: {e}")
    
    async def _process_manual_update(self,
                                   update_id: str,
                                   domain: str, 
                                   update_data: dict):
        """
        Process manual update with full AI validation pipeline
        """
        
        try:
            # AI validation with multiple agents
            validation_result = await self.validator.comprehensive_validation(
                update_data, 
                domain
            )
            
            if validation_result.valid:
                # Create context snapshot before update
                snapshot_id = await self._create_context_snapshot(domain)
                
                # Apply update
                await self._apply_context_update(domain, update_data)
                
                # Update status
                await self._update_status(update_id, 'completed', {
                    'validation_score': validation_result.score,
                    'snapshot_id': snapshot_id
                })
                
            else:
                # Validation failed
                await self._update_status(update_id, 'validation_failed', {
                    'errors': validation_result.errors,
                    'suggestions': validation_result.suggestions
                })
                
        except Exception as e:
            await self._update_status(update_id, 'processing_failed', {
                'error': str(e)
            })
```

<function_calls>
<invoke name="TodoWrite">
<parameter name="todos">[{"id": "1", "content": "Review existing AWS Bedrock agents documentation", "status": "completed"}, {"id": "2", "content": "Analyze context architecture requirements for multi-agent server access", "status": "completed"}, {"id": "3", "content": "Design token-optimized context chunking strategy", "status": "completed"}, {"id": "4", "content": "Plan context update mechanisms (Kafka + manual channels)", "status": "in_progress"}, {"id": "5", "content": "Update AWS Bedrock agents plan with context-centric architecture", "status": "pending"}]