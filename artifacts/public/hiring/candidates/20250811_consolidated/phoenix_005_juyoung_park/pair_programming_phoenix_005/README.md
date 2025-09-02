# Pair Programming Task - Resilient Exchange Client

**Candidate**: Park Juyoung  
**Duration**: 45 minutes  
**Difficulty**: Intermediate  

## Overview

You'll be building a production-ready cryptocurrency exchange price fetcher that demonstrates resilience patterns, comprehensive testing, and security best practices. This builds on concepts from your take-home project but focuses on production-grade engineering practices.

## Quick Start

### Prerequisites
- Python 3.12+
- Basic familiarity with async/await
- Understanding of HTTP APIs

### Setup (2 minutes)

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify setup**:
   ```bash
   python -m pytest tests/ -v
   # Should show 0 tests initially - we'll build them together
   ```

3. **Check linting**:
   ```bash
   ruff check src/ tests/
   # Should show no issues initially
   ```

## Task Structure (45 minutes total)

### Phase 1: Architecture & Resilience (15 minutes)
**Goal**: Build the foundation with resilience patterns

**Files to work on**:
- `src/exchange_client.py` - Abstract base class
- `src/bitmex_client.py` - Concrete implementation
- `src/resilience.py` - Retry and circuit breaker logic

**Key concepts to implement**:
- Exponential backoff with jitter
- Circuit breaker pattern
- Proper error handling

### Phase 2: Testing Strategy (20 minutes)
**Goal**: Design and implement comprehensive tests

**Files to work on**:
- `tests/unit/test_bitmex_client.py` - Unit tests with mocks
- `tests/unit/test_resilience.py` - Test resilience patterns
- `tests/integration/test_exchange_integration.py` - Integration tests

**Key concepts to discuss**:
- Testing pyramid (unit → integration → contract)
- Mocking external dependencies
- Testing failure scenarios

### Phase 3: Security & Production (10 minutes)
**Goal**: Add production-ready features

**Files to work on**:
- `config/settings.py` - Secure configuration
- `src/monitoring.py` - Metrics and observability
- `src/health.py` - Health checks

## Project Structure

```
pair_programming/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
├── src/
│   ├── __init__.py
│   ├── exchange_client.py    # Abstract base class [Phase 1]
│   ├── bitmex_client.py      # BitMEX implementation [Phase 1]  
│   ├── resilience.py         # Retry/circuit breaker [Phase 1]
│   ├── monitoring.py         # Metrics [Phase 3]
│   └── health.py            # Health checks [Phase 3]
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_bitmex_client.py     # Unit tests [Phase 2]
│   │   └── test_resilience.py        # Resilience tests [Phase 2]
│   └── integration/
│       ├── __init__.py
│       └── test_exchange_integration.py  # Integration tests [Phase 2]
└── config/
    ├── __init__.py
    └── settings.py          # Configuration [Phase 3]
```

## Implementation Guidelines

### Code Style
- Follow PEP 8 (enforced by `ruff`)
- Use type hints throughout
- Write docstrings for public methods
- Keep methods focused and testable

### Error Handling
- Use custom exceptions for different error types
- Log errors with structured logging
- Distinguish between retryable and non-retryable errors

### Testing Approach
- **Unit tests**: Fast, isolated, test one thing
- **Integration tests**: Test real API interactions (with care)
- **Mocking**: Use for external dependencies in unit tests

### Security Considerations
- Never hardcode API keys
- Use environment variables or secure config
- Validate all inputs
- Implement proper timeout handling

## Running Tests During Development

```bash
# Run all tests
python -m pytest tests/ -v

# Run only unit tests
python -m pytest tests/unit/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=term-missing

# Run linting
ruff check src/ tests/

# Format code
ruff format src/ tests/
```

## Expected Deliverables

By the end of 45 minutes, you should have:

1. **Working base architecture** with abstract class and concrete implementation
2. **Resilience patterns** implemented (retry + circuit breaker)
3. **Test structure** demonstrating understanding of testing strategy
4. **Security awareness** in configuration and secret handling
5. **Production thinking** around monitoring and health checks

## Discussion Points

Be prepared to discuss:

- **Why** you chose specific resilience patterns
- **Trade-offs** between different approaches
- **Testing strategy** and what each test type validates
- **Production concerns** like monitoring, deployment, scaling
- **Security practices** for handling secrets and validating inputs

## Success Criteria

- [ ] Code runs without errors
- [ ] Demonstrates understanding of resilience patterns
- [ ] Shows thoughtful approach to testing
- [ ] Considers security and production concerns
- [ ] Can explain architectural decisions

## Getting Help

If you get stuck:
1. Ask questions - this is collaborative!
2. Focus on demonstrating understanding over perfect implementation
3. It's okay to pseudocode complex parts and discuss approach

**Remember**: This is about demonstrating your thinking process and production engineering mindset, not about perfect code in 45 minutes.

Good luck! 🚀