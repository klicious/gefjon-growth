# Take-Home Assignment: Atlas (Da Bin Nam)

## Assignment Overview
**Complexity Level**: Standard (Mid-Level)  
**Estimated Time**: 4-6 hours  
**Due Date**: 5 days from assignment delivery  

## Background Context
You're joining our Platform Development Team to help build a fully-automated, self-healing fintech platform. This assignment evaluates your ability to design and implement backend services that could integrate with our trading and portfolio management systems.

## Assignment: Portfolio Risk Monitoring Service

### Problem Statement
Design and implement a backend service that monitors portfolio positions and calculates risk metrics in real-time. The service should handle position updates, calculate various risk measures, and provide alerts when risk thresholds are exceeded.

### Core Requirements

#### 1. Data Models & API Design
Create a RESTful API service with the following endpoints:

```
POST /api/positions - Add or update a position
GET /api/positions - List all positions
GET /api/positions/{id} - Get specific position details
GET /api/risk/portfolio - Get portfolio-level risk metrics
GET /api/risk/alerts - Get active risk alerts
POST /api/risk/thresholds - Configure risk thresholds
```

#### 2. Position Management
- **Position Model**: symbol, quantity, entry_price, current_price, timestamp
- **Position Updates**: Handle real-time position updates
- **Data Validation**: Ensure data integrity and proper error handling

#### 3. Risk Calculations
Implement the following risk metrics:
- **Portfolio Value**: Total current value of all positions
- **Unrealized P&L**: Profit/loss for each position and portfolio total
- **Position Concentration**: Percentage of portfolio in each position
- **Risk Alerts**: Trigger alerts when positions exceed configured thresholds

#### 4. Real-time Updates
- Implement WebSocket endpoint for real-time risk metric updates
- Push notifications when risk thresholds are breached
- Maintain connection state and handle reconnections

### Technical Requirements

#### Technology Stack
- **Backend**: Java (Spring Boot) or Node.js (Express) - your choice
- **Database**: PostgreSQL or MySQL
- **Real-time**: WebSockets
- **Testing**: Unit tests with reasonable coverage
- **Documentation**: API documentation (Swagger/OpenAPI preferred)

#### Architecture Considerations
- **Scalability**: Design for horizontal scaling
- **Performance**: Optimize for low-latency risk calculations
- **Reliability**: Handle failures gracefully
- **Observability**: Include logging and basic metrics

### Evaluation Criteria

#### Technical Implementation (40%)
- Code quality, structure, and maintainability
- Proper error handling and validation
- Database design and query optimization
- API design following REST principles

#### System Design (25%)
- Architecture decisions and trade-offs
- Scalability and performance considerations
- Real-time update implementation
- Data consistency and integrity

#### Problem-Solving (20%)
- Risk calculation accuracy and efficiency
- Alert system design and implementation
- Edge case handling
- Creative solutions to technical challenges

#### Documentation & Testing (15%)
- Clear API documentation
- Comprehensive unit tests
- Setup and deployment instructions
- Code comments and README quality

### Deliverables

1. **Source Code**: Complete implementation with Git history
2. **Database Schema**: SQL scripts or migration files
3. **API Documentation**: Swagger/OpenAPI specification or equivalent
4. **README**: Setup instructions, architecture overview, design decisions
5. **Tests**: Unit tests with coverage report
6. **Docker Setup**: Containerized application (bonus points)

### Sample Data
```json
{
  "positions": [
    {"symbol": "BTC-USD", "quantity": 0.5, "entry_price": 45000, "current_price": 47000},
    {"symbol": "ETH-USD", "quantity": 2.0, "entry_price": 3000, "current_price": 3200},
    {"symbol": "AAPL", "quantity": 10, "entry_price": 150, "current_price": 155}
  ],
  "risk_thresholds": {
    "max_position_concentration": 0.3,
    "max_portfolio_loss": 0.1,
    "max_position_loss": 0.05
  }
}
```

### Bonus Challenges (Optional)
- **Historical Data**: Store and query historical risk metrics
- **Advanced Metrics**: Implement VaR (Value at Risk) calculations
- **Performance Optimization**: Implement caching for frequently accessed data
- **Monitoring**: Add health checks and metrics endpoints
- **CI/CD**: GitHub Actions workflow for testing and deployment

### Submission Instructions
1. Create a private GitHub repository
2. Implement the solution with clear commit messages
3. Include comprehensive README with setup instructions
4. Add `klicious` as a collaborator to the repository
5. Send repository link via email

### Questions & Clarifications
If you have questions about the requirements, please email us. We encourage asking clarifying questions as it demonstrates good communication skills.

---

**Personalization Notes for Atlas:**
- Leverages your full-stack experience with backend focus
- Builds on your PostgreSQL and API development expertise
- Incorporates real-time features similar to your MQTT/WebSocket experience
- Allows choice between Java (your strength) and Node.js (your expertise)
- Risk calculations align with your data processing background
- Docker containerization matches your migration experience

**Success Indicators:**
- Clean, maintainable code structure
- Proper database design and optimization
- Effective real-time update implementation
- Good error handling and validation
- Clear documentation and testing approach