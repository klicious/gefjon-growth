# Take-Home Assignment: Titan (Wongyeong Kim)

## Assignment Overview
**Complexity Level**: Advanced (Senior-Level)  
**Estimated Time**: 6-8 hours  
**Due Date**: 7 days from assignment delivery  

## Background Context
You're joining our Platform Development Team to help build a fully-automated, self-healing fintech platform with advanced AI capabilities. This assignment evaluates your ability to design and implement data engineering pipelines with AI/ML integration, building on your proven expertise in data processing and LLM integration.

## Assignment: AI-Powered Trading Signal Processing Pipeline

### Problem Statement
Design and implement an intelligent data processing pipeline that ingests market data, financial news, and social sentiment, processes this information using LLMs for signal extraction, and delivers actionable trading insights through optimized data pipelines with real-time monitoring and alerting.

### Core Requirements

#### 1. Multi-Source Data Ingestion
Create a robust data ingestion system:

```
Data Sources:
- Market data feeds (price, volume, order book)
- Financial news APIs (RSS, REST endpoints)
- Social sentiment data (Twitter-like feeds)
- Economic indicators (scheduled releases)

Requirements:
- Handle 1,000+ messages/minute aggregate
- Support different data formats (JSON, XML, CSV)
- Implement retry logic and error handling
- Data quality validation and cleansing
```

#### 2. LLM-Powered Signal Processing
Implement intelligent signal extraction:
- **News Analysis**: Use LLMs to extract sentiment and key events from financial news
- **Social Sentiment**: Process social media data for market sentiment indicators
- **Event Detection**: Identify significant market events and their potential impact
- **Signal Scoring**: Generate confidence scores for trading signals (0-100 scale)

#### 3. Data Pipeline Optimization
Build high-performance processing pipeline:
- **Apache Airflow**: Orchestrate complex data workflows with dependencies
- **Real-time Processing**: Stream processing for time-sensitive signals
- **Batch Processing**: Historical data analysis and model training
- **Performance Optimization**: Achieve <30 second end-to-end latency for critical signals

#### 4. Storage & Analytics
Design efficient data storage and retrieval:
- **Time-Series Database**: Store market data and signals efficiently
- **Elasticsearch**: Full-text search for news and sentiment analysis
- **Data Warehouse**: Historical data for backtesting and analysis
- **Caching Layer**: Redis for frequently accessed signals and metadata

### Technical Requirements

#### Technology Stack
- **Pipeline Orchestration**: Apache Airflow
- **Stream Processing**: Apache Kafka + Python consumers
- **LLM Integration**: OpenAI API, Anthropic Claude, or local models
- **Databases**: PostgreSQL, Elasticsearch, Redis
- **Containerization**: Docker with docker-compose
- **Monitoring**: Prometheus + Grafana (or similar)
- **Testing**: pytest with data pipeline testing framework

#### Architecture Considerations
- **Scalability**: Design for horizontal scaling of processing nodes
- **Fault Tolerance**: Handle failures gracefully with retry mechanisms
- **Data Quality**: Implement comprehensive data validation and monitoring
- **Cost Optimization**: Efficient LLM usage with caching and batching
- **Observability**: Comprehensive logging, metrics, and alerting

### Evaluation Criteria

#### Data Engineering Excellence (35%)
- Pipeline design and orchestration
- Data quality and validation implementation
- Performance optimization and monitoring
- Error handling and fault tolerance

#### AI/ML Integration (30%)
- LLM integration and prompt engineering
- Signal extraction accuracy and relevance
- Model performance optimization
- Creative use of AI for financial insights

#### System Architecture (20%)
- Component design and interaction
- Scalability and performance considerations
- Data storage and retrieval optimization
- Real-time vs batch processing trade-offs

#### Code Quality & Documentation (15%)
- Clean, maintainable Python code
- Comprehensive testing strategy
- Clear documentation and setup instructions
- Monitoring and observability implementation

### Deliverables

1. **Source Code**: Complete pipeline implementation with Git history
2. **Docker Environment**: Containerized application with docker-compose
3. **Airflow DAGs**: Well-structured workflow definitions
4. **Data Models**: Database schemas and data validation rules
5. **Monitoring Dashboard**: Real-time pipeline health and performance metrics
6. **Documentation**: Architecture overview, setup guide, and design decisions
7. **Test Suite**: Unit tests and integration tests for critical components

### Sample Data Formats

#### Market Data
```json
{
  "symbol": "BTC-USD",
  "timestamp": "2025-08-12T10:30:00Z",
  "price": 47250.50,
  "volume": 1.25,
  "bid": 47249.00,
  "ask": 47252.00
}
```

#### News Data
```json
{
  "title": "Federal Reserve Signals Potential Rate Cut",
  "content": "The Federal Reserve indicated...",
  "source": "Reuters",
  "timestamp": "2025-08-12T09:15:00Z",
  "symbols": ["SPY", "BTC-USD", "EUR-USD"]
}
```

#### Expected Signal Output
```json
{
  "signal_id": "news_sentiment_001",
  "symbol": "BTC-USD",
  "signal_type": "sentiment",
  "score": 75,
  "confidence": 0.85,
  "reasoning": "Positive regulatory news with high market impact",
  "timestamp": "2025-08-12T10:31:00Z",
  "expiry": "2025-08-12T16:00:00Z"
}
```

### Performance Targets
```
Latency Requirements:
- News processing: <30 seconds from ingestion to signal
- Market data processing: <5 seconds
- Social sentiment: <60 seconds
- End-to-end pipeline: <2 minutes for complex signals

Throughput Requirements:
- Market data: 1,000+ messages/minute
- News articles: 100+ articles/hour
- Social posts: 500+ posts/hour
- Signal generation: 50+ signals/hour

Quality Targets:
- Data quality score: >95%
- Pipeline uptime: >99.5%
- Signal accuracy: >70% (backtested)
```

### Advanced Challenges (Required for Advanced Level)
- **Custom LLM Fine-tuning**: Fine-tune a model for financial text analysis
- **Real-time Anomaly Detection**: Detect unusual patterns in data flows
- **Advanced Caching**: Implement intelligent caching for LLM responses
- **A/B Testing Framework**: Compare different signal generation strategies
- **Cost Optimization**: Minimize LLM API costs while maintaining quality

### Bonus Challenges (Optional)
- **Multi-Modal Analysis**: Integrate chart pattern recognition with news analysis
- **Reinforcement Learning**: Implement RL-based signal weighting
- **Distributed Processing**: Multi-node deployment with load balancing
- **Advanced Visualization**: Interactive dashboard for signal exploration
- **Backtesting Framework**: Historical signal performance analysis

### LLM Integration Guidelines
- **Prompt Engineering**: Design effective prompts for financial analysis
- **Response Parsing**: Robust parsing of LLM outputs into structured data
- **Error Handling**: Graceful handling of LLM API failures and rate limits
- **Cost Management**: Implement caching and batching to minimize API costs
- **Quality Assurance**: Validate LLM outputs for consistency and accuracy

### Submission Instructions
1. Create a private GitHub repository with clear commit history
2. Include docker-compose setup for easy deployment
3. Provide comprehensive documentation with architecture diagrams
4. Include sample data and configuration files
5. Add performance benchmarks and optimization notes
6. Add `klicious` as a collaborator to the repository
7. Send repository link with demo video (optional) via email

### Evaluation Environment
Your solution will be tested with:
- Simulated real-time data feeds
- Various LLM API scenarios (success, failure, rate limiting)
- Performance testing under different load conditions
- Data quality validation with edge cases
- Pipeline failure and recovery scenarios

---

**Personalization Notes for Titan:**
- Leverages your exceptional data engineering and pipeline optimization expertise
- Builds on your proven LLM integration experience (87% accuracy improvement)
- Incorporates your Airflow, Elasticsearch, and Docker proficiency
- Challenges your system optimization skills (similar to your 35% runtime reduction)
- Allows demonstration of your Python/Java expertise and architectural thinking
- Aligns with your data processing and performance optimization background

**Success Indicators:**
- Efficient data pipeline design and implementation
- Creative and effective LLM integration
- Measurable performance optimizations
- Robust error handling and monitoring
- Clean, well-documented code architecture