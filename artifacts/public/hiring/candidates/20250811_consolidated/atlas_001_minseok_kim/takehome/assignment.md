# Take-Home Assignment: atlas_001

## Assignment Overview
**Challenge**: Financial Trading Platform API Integration  
**Time Allocation**: 4-6 hours  
**Due Date**: 72 hours from assignment  
**Evaluator GitHub**: klicious

## Background Context
Based on your impressive AWS expertise, infrastructure automation experience, and full-stack development background with FastAPI, this assignment is designed to assess your ability to build reliable, scalable financial systems. Your experience with queue-based autoscaling and observability will be particularly relevant.

## Technical Requirements

### Core Challenge: Multi-Exchange Trading API
Implement a unified REST API service that integrates with multiple cryptocurrency exchanges (BitMex and Binance) to support trading operations.

### Required Features
1. **Order Management**:
   - Get orders by IDs, date range, and state (NEW, PARTIALLY_FILLED, FILLED, CANCELED)
   - Get active orders
   - Place market and limit orders
   - Amend order quantity/price
   - Cancel orders

2. **Multi-Exchange Support**:
   - BitMex integration
   - Binance integration
   - Unified interface for both exchanges

3. **Instrument Support**:
   - BTC, ETH, SOL
   - SPOT markets
   - USD-M Futures (perpetual and delivery)
   - USD-C Futures (perpetual and delivery)

### Technical Stack Requirements
- **Language**: Python 3.10+
- **Framework**: FastAPI (leveraging your expertise)
- **Testing**: pytest with comprehensive test coverage
- **Documentation**: OpenAPI/Swagger integration
- **Configuration**: Environment-based configuration management

### Infrastructure & DevOps (Leveraging Your Strengths)
- **Containerization**: Docker implementation
- **CI/CD**: GitHub Actions pipeline (showcase your ECS deployment experience)
- **Observability**: Basic logging and metrics (drawing from your Prometheus/Grafana experience)
- **Error Handling**: Robust error handling with proper HTTP status codes

### AWS Integration (Optional Bonus)
Given your AWS certifications and ECS experience:
- Deploy to AWS ECS or Lambda
- Use AWS Parameter Store for API key management
- Implement basic CloudWatch monitoring

## Evaluation Criteria

### Technical Excellence (30%)
- Clean, maintainable FastAPI implementation
- Proper async/await usage for API calls
- Efficient error handling and retry mechanisms
- Modular design with clear separation of concerns

### System Design (25%)
- Unified interface design for multiple exchanges
- Scalable architecture supporting additional exchanges
- Configuration management and environment handling
- API versioning and backward compatibility considerations

### Code Quality (20%)
- PEP 8 compliance and clean code principles
- Comprehensive docstrings and type hints
- Proper logging and debugging capabilities
- Security best practices for API key handling

### Documentation (15%)
- Clear README with setup instructions
- API documentation via FastAPI/Swagger
- Architecture decisions and trade-offs explanation
- Usage examples and testing guide

### Innovation (10%)
- Creative solutions leveraging your infrastructure background
- Performance optimizations
- Additional features that demonstrate platform thinking
- Integration of observability patterns

## Submission Guidelines

### Repository Setup
1. Create a private GitHub repository
2. Add `klicious` as a collaborator
3. Use clear commit messages showing development progression
4. Include comprehensive README.md

### Required Deliverables
- Fully functional FastAPI application
- Docker configuration for containerized deployment
- Comprehensive test suite with mocking
- CI/CD pipeline configuration (GitHub Actions)
- Documentation covering setup, usage, and architecture

### Repository Structure
```
trading-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── exchanges/
│   ├── models/
│   └── utils/
├── tests/
├── docker/
├── .github/workflows/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Success Criteria
- All API endpoints functional with proper error handling
- Test coverage >80% with meaningful test cases
- Clean, documented code following FastAPI best practices
- Working Docker containerization
- Clear documentation enabling easy setup and usage

## Evaluation Focus Areas
Given your background, we'll particularly assess:
1. **FastAPI Expertise**: Leveraging your framework experience
2. **Infrastructure Thinking**: Docker, CI/CD, and deployment considerations
3. **Scalability Patterns**: Drawing from your autoscaling experience
4. **Observability**: Logging and monitoring implementation
5. **AWS Integration**: Optional but showcases your cloud expertise

## Time Management Suggestions
- **Hour 1**: Project setup, FastAPI skeleton, basic structure
- **Hours 2-3**: Core exchange integrations and unified interface
- **Hour 4**: Testing implementation and error handling
- **Hours 5-6**: Documentation, Docker setup, and CI/CD pipeline

## Questions or Clarifications
If you have any questions during implementation, feel free to reach out. We're interested in seeing how you approach complex system integration challenges while leveraging your infrastructure and full-stack expertise.

Good luck! We're excited to see how you apply your AWS, FastAPI, and infrastructure automation skills to this financial platform challenge.

---
**Assignment Generated**: 2025-08-11T12:00:00Z  
**Personalization Level**: High (FastAPI, AWS, Infrastructure focus)  
**Difficulty Level**: Entry-Level with Infrastructure Bonus  
**Expected Completion**: 4-6 hours