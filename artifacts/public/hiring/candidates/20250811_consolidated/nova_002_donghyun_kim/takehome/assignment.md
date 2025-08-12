# Take-Home Assignment: nova_002

## Assignment Overview
**Challenge**: High-Reliability Financial Trading System  
**Time Allocation**: 4-6 hours  
**Due Date**: 72 hours from assignment  
**Evaluator GitHub**: klicious

## Background Context
Based on your exceptional system reliability focus, AWS expertise, and proven experience with observability (Prometheus/Loki), this assignment is designed to assess your ability to build robust, monitored financial systems. Your experience reducing incident detection time from 30m to 2m and implementing comprehensive testing strategies will be particularly relevant.

## Technical Requirements

### Core Challenge: Resilient Trading API with Observability
Implement a fault-tolerant REST API service for cryptocurrency trading that emphasizes reliability, monitoring, and graceful error handling.

### Required Features
1. **Order Management with Reliability Focus**:
   - Get orders by IDs, date range, and state (NEW, PARTIALLY_FILLED, FILLED, CANCELED)
   - Get active orders with caching and fallback mechanisms
   - Place market and limit orders with retry logic
   - Amend order quantity/price with validation
   - Cancel orders with confirmation tracking

2. **Multi-Exchange Integration**:
   - BitMex integration with circuit breaker pattern
   - Binance integration with rate limiting
   - Unified interface with exchange failover capabilities

3. **Instrument Support**:
   - BTC, ETH, SOL
   - SPOT markets
   - USD-M Futures (perpetual and delivery)
   - USD-C Futures (perpetual and delivery)

### Technical Stack Requirements
- **Language**: Python 3.10+ (transition from your Java background)
- **Framework**: FastAPI (new framework to demonstrate adaptability)
- **Testing**: pytest with comprehensive test coverage (leveraging your 250-test experience)
- **Observability**: Structured logging, metrics, and health checks
- **Reliability**: Circuit breakers, retries, and graceful degradation

### Reliability & Observability (Your Core Strengths)
- **Monitoring**: Implement metrics collection (drawing from your Prometheus experience)
- **Logging**: Structured logging with correlation IDs
- **Health Checks**: Comprehensive health endpoints for each exchange
- **Circuit Breakers**: Implement circuit breaker pattern for external API calls
- **Retry Logic**: Exponential backoff with jitter for failed requests
- **Graceful Degradation**: Fallback mechanisms when exchanges are unavailable

### AWS Integration (Leveraging Your Experience)
Given your AWS ECS/Lambda expertise:
- Containerized deployment ready for ECS
- Environment-based configuration for different stages
- Basic CloudWatch integration for monitoring
- Parameter Store integration for sensitive configuration

## Evaluation Criteria

### System Reliability (35%)
- Circuit breaker implementation for external APIs
- Comprehensive error handling with proper recovery
- Retry mechanisms with exponential backoff
- Health check endpoints and monitoring integration
- Graceful degradation when services are unavailable

### Technical Implementation (25%)
- Clean Python implementation (demonstrating Java→Python transition)
- Proper async/await usage for concurrent API calls
- Efficient caching and state management
- Modular design with clear separation of concerns

### Observability & Monitoring (20%)
- Structured logging with correlation tracking
- Metrics collection and exposure
- Health check implementation
- Error tracking and alerting considerations
- Performance monitoring integration

### Code Quality & Testing (15%)
- Comprehensive test suite with meaningful test cases
- Proper mocking strategies for external dependencies
- Clean code principles and documentation
- Security best practices implementation

### Innovation (5%)
- Creative reliability solutions
- Performance optimizations
- Additional monitoring features
- Advanced error handling patterns

## Submission Guidelines

### Repository Setup
1. Create a private GitHub repository
2. Add `klicious` as a collaborator
3. Use clear commit messages showing development progression
4. Include comprehensive README.md with reliability considerations

### Required Deliverables
- Fault-tolerant FastAPI application with observability
- Comprehensive test suite with >85% coverage
- Docker configuration for containerized deployment
- Monitoring and health check implementation
- Documentation covering reliability patterns and monitoring

### Repository Structure
```
reliable-trading-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── exchanges/
│   ├── reliability/  # Circuit breakers, retries
│   ├── monitoring/   # Metrics, health checks
│   ├── models/
│   └── utils/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── reliability/  # Failure scenario tests
├── docker/
├── monitoring/       # Prometheus configs, dashboards
├── requirements.txt
├── Dockerfile
└── README.md
```

## Success Criteria
- All API endpoints functional with comprehensive error handling
- Circuit breaker pattern implemented for external API calls
- Health checks providing detailed system status
- Test coverage >85% including failure scenario testing
- Structured logging with correlation IDs
- Metrics collection ready for Prometheus integration

## Evaluation Focus Areas
Given your background, we'll particularly assess:
1. **Reliability Patterns**: Circuit breakers, retries, graceful degradation
2. **Observability Implementation**: Logging, metrics, health checks
3. **Testing Strategy**: Comprehensive testing including failure scenarios
4. **Python Transition**: Clean Python code demonstrating adaptability from Java
5. **AWS Readiness**: Configuration and deployment considerations

## Specific Reliability Requirements

### Circuit Breaker Implementation
- Implement circuit breaker for each exchange API
- Configurable failure thresholds and recovery timeouts
- Proper state transitions (Closed → Open → Half-Open)
- Metrics tracking for circuit breaker state changes

### Health Check System
- Individual health checks for each exchange
- Aggregate system health endpoint
- Dependency health tracking
- Health check caching to prevent overload

### Retry Logic
- Exponential backoff with jitter
- Configurable retry attempts per operation type
- Different retry strategies for different error types
- Retry metrics and logging

### Monitoring Integration
- Prometheus-compatible metrics endpoint
- Key business metrics (order success rate, latency percentiles)
- System metrics (circuit breaker states, retry counts)
- Error rate tracking by exchange and operation

## Time Management Suggestions
- **Hour 1**: Project setup, FastAPI skeleton, basic reliability patterns
- **Hours 2-3**: Core exchange integrations with circuit breakers
- **Hour 4**: Comprehensive testing including failure scenarios
- **Hours 5-6**: Observability implementation and documentation

## Questions or Clarifications
If you have any questions during implementation, feel free to reach out. We're particularly interested in seeing how you apply your reliability engineering expertise to financial system integration while demonstrating adaptability to new technologies.

This assignment is designed to showcase your strengths in system reliability while assessing your ability to learn new frameworks and apply your observability expertise to financial platforms.

---
**Assignment Generated**: 2025-08-11T12:15:00Z  
**Personalization Level**: High (Reliability, Observability, AWS focus)  
**Difficulty Level**: Entry-Level with Reliability Focus  
**Expected Completion**: 4-6 hours