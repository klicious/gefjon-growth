# Take-Home Assignment: Phoenix (Hyungkyu Ahn)

## Assignment Overview
**Complexity Level**: Advanced (Senior-Level)  
**Estimated Time**: 6-8 hours  
**Due Date**: 7 days from assignment delivery  

## Background Context
You're joining our Platform Development Team to help build a fully-automated, self-healing fintech platform that trades digital assets profitably with real-time risk management. This assignment evaluates your ability to design and implement high-performance, low-latency systems critical for algorithmic trading.

## Assignment: High-Frequency Market Data Processing Engine

### Problem Statement
Design and implement a high-performance market data processing engine that ingests real-time price feeds from multiple exchanges, normalizes the data, detects arbitrage opportunities, and distributes processed data to downstream trading algorithms with sub-millisecond latency requirements.

### Core Requirements

#### 1. Market Data Ingestion
Create a multi-exchange data ingestion system:

```
- WebSocket connections to 3+ simulated exchanges
- Real-time price feed normalization across different formats
- Connection management with automatic reconnection
- Message rate handling: 10,000+ messages/second per exchange
```

#### 2. Data Processing Pipeline
Implement a high-performance processing pipeline:
- **Data Normalization**: Convert exchange-specific formats to unified schema
- **Arbitrage Detection**: Identify price discrepancies across exchanges (>0.1% threshold)
- **Market Data Distribution**: Fan-out processed data to multiple consumers
- **Performance Metrics**: Track latency, throughput, and processing statistics

#### 3. Inter-Process Communication
Design efficient IPC mechanism:
- **ZeroMQ Integration**: Use ZeroMQ for low-latency message passing
- **Shared Memory**: Implement shared memory for ultra-low latency data sharing
- **Process Coordination**: Manage multiple worker processes with load balancing
- **Fault Tolerance**: Handle process failures and automatic recovery

#### 4. Performance Optimization
Achieve aggressive performance targets:
- **Latency**: <1ms end-to-end processing latency (95th percentile)
- **Throughput**: Handle 50,000+ messages/second aggregate
- **Memory Efficiency**: Minimize memory allocations and garbage collection
- **CPU Optimization**: Efficient CPU utilization across multiple cores

### Technical Requirements

#### Technology Stack
- **Primary Language**: C++ or Python (with C extensions) - your choice
- **Messaging**: ZeroMQ for IPC
- **Shared Memory**: POSIX shared memory or memory-mapped files
- **Serialization**: Protocol Buffers or MessagePack for efficiency
- **Testing**: Performance benchmarks and unit tests
- **Monitoring**: Real-time performance metrics and alerting

#### Architecture Considerations
- **Multi-Process Design**: Separate processes for ingestion, processing, and distribution
- **Lock-Free Programming**: Minimize synchronization overhead
- **NUMA Awareness**: Consider CPU affinity and memory locality
- **Horizontal Scaling**: Design for adding more processing nodes
- **Observability**: Comprehensive metrics and performance monitoring

### Evaluation Criteria

#### Performance Engineering (35%)
- Latency optimization and measurement
- Throughput maximization techniques
- Memory efficiency and allocation patterns
- CPU utilization and multi-core scaling

#### System Architecture (30%)
- Multi-process design and coordination
- IPC mechanism selection and implementation
- Fault tolerance and recovery strategies
- Scalability and load distribution

#### Financial Domain Knowledge (20%)
- Arbitrage detection algorithm accuracy
- Market data handling best practices
- Risk considerations in high-frequency systems
- Understanding of trading system requirements

#### Code Quality & Testing (15%)
- Clean, maintainable C++/Python code
- Comprehensive performance benchmarks
- Unit tests for critical components
- Documentation and deployment guides

### Deliverables

1. **Source Code**: Complete implementation with build system
2. **Performance Benchmarks**: Latency and throughput measurements
3. **Architecture Documentation**: System design and component interaction
4. **Deployment Guide**: Setup instructions and configuration
5. **Test Suite**: Unit tests and performance validation
6. **Metrics Dashboard**: Real-time performance monitoring (bonus)

### Sample Market Data Format
```json
{
  "exchange": "binance",
  "symbol": "BTC-USDT",
  "timestamp": 1692123456789,
  "bid": 29450.50,
  "ask": 29451.00,
  "last": 29450.75,
  "volume": 1234.56
}
```

### Performance Targets
```
Latency Requirements:
- Data ingestion to normalization: <100μs
- Arbitrage detection: <200μs  
- Distribution to consumers: <300μs
- End-to-end: <1ms (95th percentile)

Throughput Requirements:
- Aggregate message rate: 50,000+ msg/sec
- Per-exchange capacity: 15,000+ msg/sec
- Arbitrage detection rate: 1,000+ opportunities/sec
- Consumer fan-out: 10+ simultaneous consumers
```

### Advanced Challenges (Required for Advanced Level)
- **Lock-Free Data Structures**: Implement lock-free queues or ring buffers
- **SIMD Optimization**: Use vectorized operations for data processing
- **Custom Memory Allocator**: Implement pool-based memory management
- **Kernel Bypass**: Consider user-space networking (DPDK) for ultimate performance
- **Real-Time Monitoring**: Live performance dashboard with sub-second updates

### Bonus Challenges (Optional)
- **Machine Learning Integration**: Add ML-based anomaly detection
- **Historical Replay**: Implement historical data replay for backtesting
- **Distributed Deployment**: Multi-node deployment with coordination
- **Advanced Analytics**: Real-time market microstructure analysis

### Submission Instructions
1. Create a private GitHub repository with clear commit history
2. Include comprehensive build and deployment instructions
3. Provide performance benchmark results with methodology
4. Add detailed architecture documentation
5. Add `klicious` as a collaborator to the repository
6. Send repository link with performance summary via email

### Performance Validation
Your solution will be tested against:
- Simulated high-frequency market data feeds
- Latency measurement under various load conditions
- Stress testing with message bursts and connection failures
- Memory usage profiling and leak detection
- Multi-core scaling efficiency analysis

---

**Personalization Notes for Phoenix:**
- Leverages your exceptional systems programming and performance optimization expertise
- Builds directly on your ZeroMQ, IPC, and distributed systems experience
- Incorporates your financial domain knowledge (capital markets, arbitrage systems)
- Challenges your low-latency optimization skills (similar to your 2x throughput improvement)
- Allows demonstration of your C/Python proficiency and system-level thinking
- Aligns with your proven ability to deliver measurable performance improvements

**Success Indicators:**
- Sub-millisecond latency achievement
- Efficient multi-process architecture
- Sophisticated performance optimization techniques
- Financial domain understanding demonstration
- Clean, high-performance code implementation