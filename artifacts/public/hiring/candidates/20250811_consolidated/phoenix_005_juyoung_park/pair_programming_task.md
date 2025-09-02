---
id: pair_programming_juyoung_park_2025-08-20
type: pair_programming_task
domain: hiring
created_date: 2025-08-20
candidate: phoenix_005_juyoung_park
difficulty: intermediate
duration: 45_minutes
author: Claude Code
tags: ['resilience', 'testing', 'security', 'production_readiness']
visibility: public
version: 1.0
---

# Pair Programming Task - Park Juyoung

**Candidate**: phoenix_005_juyoung_park  
**Difficulty**: Intermediate  
**Target Duration**: 45 minutes  
**Focus Areas**: Production resilience, testing strategy, security practices

## Problem: Resilient Exchange Client with Comprehensive Testing

### Summary / Objective

Build a production-ready cryptocurrency exchange price fetcher that demonstrates resilience patterns, comprehensive testing, and security best practices. This extends your take-home project's concepts into production-grade engineering.

### Core Requirements

| **Component** | **Specification** |
|---------------|------------------|
| **Base Class** | Abstract `ExchangeClient` with extensible architecture |
| **Resilience** | Implement retry with exponential backoff, circuit breaker pattern |
| **Security** | Secure API key management, input validation |
| **Testing** | Unit, integration, and contract tests |
| **Observability** | Structured logging, metrics, health checks |

### Implementation Phases (45 minutes)

#### Phase 1: Architecture & Resilience (15 mins)
```python
class ExchangeClient(ABC):
    def __init__(self, api_key: str, base_url: str):
        # TODO: Implement secure key handling
        pass
    
    @abstractmethod
    async def get_price(self, symbol: str) -> dict:
        pass
    
    async def _make_request(self, endpoint: str, params: dict) -> dict:
        # TODO: Implement with retry logic and circuit breaker
        pass

class BitMEXClient(ExchangeClient):
    # TODO: Implement concrete client
    pass
```

**Key Discussion Points**:
- How would you implement exponential backoff with jitter?
- When should the circuit breaker open/close?
- What errors warrant retries vs immediate failure?

#### Phase 2: Testing Strategy (20 mins)
```python
# tests/test_exchange_client.py
class TestBitMEXClient:
    def test_successful_price_fetch(self):
        # TODO: Unit test with mocked HTTP client
        pass
    
    async def test_retry_on_transient_error(self):
        # TODO: Test retry logic with controlled failures
        pass
    
    def test_circuit_breaker_opens_on_failures(self):
        # TODO: Test circuit breaker behavior
        pass

# tests/integration/test_exchange_integration.py  
class TestExchangeIntegration:
    async def test_real_api_call_with_valid_symbol(self):
        # TODO: Integration test with real API
        pass
```

**Key Discussion Points**:
- What's the difference between unit, integration, and contract tests?
- How would you test the circuit breaker without waiting for real timeouts?
- What would a proper contract test look like for this API?

#### Phase 3: Security & Production Readiness (10 mins)
```python
# config.py
class Config:
    def __init__(self):
        # TODO: Secure API key loading from environment/secrets manager
        pass

# monitoring.py  
class Metrics:
    def __init__(self):
        # TODO: Implement request count, latency, error rate metrics
        pass
```

**Key Discussion Points**:
- How would you handle API keys in production vs development?
- What metrics would you track for this service?
- How would you implement health checks?

### Success Criteria

**Technical Excellence (Primary Focus)**:
- [ ] Implements proper retry logic with exponential backoff
- [ ] Circuit breaker pattern correctly implemented
- [ ] Demonstrates understanding of when to use each resilience pattern

**Testing Strategy (Primary Focus)**:
- [ ] Can articulate difference between test types
- [ ] Writes meaningful test cases that verify behavior, not implementation
- [ ] Understands how to test resilience patterns

**Security Awareness (Primary Focus)**:
- [ ] Demonstrates secure secret handling practices
- [ ] Input validation and sanitization
- [ ] Understands principle of least privilege

**Production Thinking**:
- [ ] Considers observability and monitoring
- [ ] Discusses deployment and operational concerns
- [ ] Shows awareness of configuration management

### Interviewer Guidance

**Assessment Strategy**:
1. **Start with architecture**: Let candidate design the class structure first
2. **Focus on resilience**: Deep dive on retry/circuit breaker implementation
3. **Testing discussion**: More talking than coding - assess understanding of testing strategy
4. **Security check**: How they handle API keys reveals security mindset

**Red Flags to Watch For**:
- Hardcoded API keys or secrets
- Infinite retry loops without backoff
- Tests that only verify happy path
- No consideration for production deployment

**Positive Signals**:
- Asks clarifying questions about requirements
- Considers edge cases and failure scenarios  
- Demonstrates understanding of testing pyramid
- Shows awareness of operational concerns

### Connection to Take-Home Evaluation

This task directly addresses the gaps identified in the candidate's take-home submission:
- **Missing resilience patterns** → Implement retry/circuit breaker
- **Insufficient testing** → Design comprehensive test strategy  
- **Security concerns** → Proper secret management
- **Production readiness** → Consider observability and deployment

The goal is to determine if these gaps were due to time constraints or lack of foundational knowledge.