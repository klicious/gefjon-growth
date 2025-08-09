# Comprehensive Architecture Diagrams for AWS Bedrock Multi-Agent System
**Draw.io XML Diagrams for Graph RAG Context-Centric Architecture**

## Executive Summary

This document contains comprehensive draw.io XML diagrams that illustrate the Graph RAG-based context-centric multi-agent architecture at multiple levels of detail. These diagrams are designed to help builders and AWS meeting participants understand the complete system architecture, data flows, and component interactions.

---

## High-Level System Architecture

### Overall System Architecture (draw.io XML)

```xml
<mxfile host="app.diagrams.net" modified="2025-01-08T16:00:00.000Z" agent="Graph-RAG-Multi-Agent-System" etag="architecture-v2.0" version="24.7.17">
  <diagram name="High-Level Graph RAG Architecture" id="graph-rag-high-level">
    <mxGraphModel dx="1800" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Title and Legend -->
        <mxCell id="title" value="Graph RAG Context-Centric Multi-Agent System&#xa;AWS Bedrock + Subscription CLI Agents + Ultra-Low-Cost Architecture" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1300" height="40" as="geometry" />
        </mxCell>
        
        <!-- Cost Indicator -->
        <mxCell id="cost-target" value="💰 COST TARGET&#xa;<$10 per candidate&#xa;(Target: $2-5)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;fontStyle=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="1200" y="80" width="150" height="60" as="geometry" />
        </mxCell>
        
        <!-- External Interfaces Layer -->
        <mxCell id="external-layer" value="External Interfaces & Data Sources" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="80" width="1100" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="dooray-api" value="Dooray Task API&#xa;(PyDooray)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="80" y="150" width="120" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="outlook-integration" value="Outlook/Exchange&#xa;Email Integration" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="220" y="150" width="120" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="manual-uploads" value="Manual Updates&#xa;JSON/YAML/CSV" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="360" y="150" width="120" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="git-webhooks" value="Git Webhooks&#xa;Context Updates" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="500" y="150" width="120" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="hr-systems" value="HR Systems&#xa;Candidate Data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="640" y="150" width="120" height="50" as="geometry" />
        </mxCell>
        
        <!-- Message Queue Layer -->
        <mxCell id="message-queue-layer" value="Message Queue & Event Processing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="240" width="1100" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="kafka-cluster" value="Amazon MSK&#xa;(Kafka Serverless)&#xa;Zero Data Loss" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="100" y="310" width="150" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="sqs-dlq" value="SQS + DLQ&#xa;Fallback Queue" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="280" y="310" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="lambda-processors" value="Lambda Functions&#xa;Event Processing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="430" y="310" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- Graph RAG Context Infrastructure -->
        <mxCell id="context-infrastructure" value="Graph RAG Context Infrastructure (Independent Microservice)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="420" width="1100" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="context-service" value="context-graph-service&#xa;FastAPI + ECS Fargate&#xa;Independent MSA" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="490" width="140" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="neptune-graph" value="Amazon Neptune&#xa;Knowledge Graph&#xa;Gremlin Queries" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="250" y="490" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="opensearch-vector" value="Amazon OpenSearch&#xa;Vector Similarity&#xa;k-NN Search" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="390" y="490" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="context-fusion" value="Context Fusion&#xa;Graph + Vector&#xa;Relevance Ranking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="530" y="490" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="token-optimizer" value="Token Optimizer&#xa;Model-Specific&#xa;Quality-Optimal" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="670" y="490" width="120" height="80" as="geometry" />
        </mxCell>
        
        <!-- Caching Layer -->
        <mxCell id="caching-layer" value="Ultra-High Performance Caching (>95% Hit Ratio)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="610" width="1100" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="redis-cluster" value="ElastiCache Redis&#xa;L2 Cache&#xa;30min TTL" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="100" y="680" width="120" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="dynamodb-cache" value="DynamoDB&#xa;L3 Cache + Storage&#xa;24h TTL" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="250" y="680" width="120" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="s3-storage" value="S3 Intelligent&#xa;Tiering + Lifecycle" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="400" y="680" width="120" height="60" as="geometry" />
        </mxCell>
        
        <!-- Multi-Agent Platform -->
        <mxCell id="agent-platform" value="Multi-Agent Platform (Subscription + AWS Bedrock)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="780" width="1100" height="50" as="geometry" />
        </mxCell>
        
        <!-- Subscription CLI Agents -->
        <mxCell id="subscription-agents" value="Subscription CLI Agents ($94/month total)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="850" width="300" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="gemini-cli" value="Gemini CLI&#xa;Primary Workflow&#xa;$25/month" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="80" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="claude-code" value="Claude Code CLI&#xa;Technical Accuracy&#xa;$25/month" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="200" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="amazon-q" value="Amazon Q Dev&#xa;AWS Integration&#xa;$19/month" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="320" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="openai-mini" value="OpenAI o4-mini&#xa;Cost-Efficient&#xa;$25/month" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="440" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <!-- AWS Bedrock Strategic Agents -->
        <mxCell id="bedrock-agents" value="AWS Bedrock Strategic Agents (Pay-per-token)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="600" y="850" width="300" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="context-assembler" value="Context Assembler&#xa;Claude-3-Sonnet&#xa;Graph RAG" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="600" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="quality-validator" value="Quality Validator&#xa;Claude-3-Haiku&#xa;Bias Detection" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="720" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="decision-synthesizer" value="Decision Synthesis&#xa;Claude-3-Sonnet&#xa;Multi-Agent" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="840" y="900" width="100" height="60" as="geometry" />
        </mxCell>
        
        <!-- Data Flow Arrows -->
        <mxCell id="flow-external-to-kafka" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="dooray-api" target="kafka-cluster">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="140" y="220" as="sourcePoint" />
            <mxPoint x="175" y="310" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-kafka-to-context" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="kafka-cluster" target="context-service">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="175" y="380" as="sourcePoint" />
            <mxPoint x="150" y="490" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-context-to-agents" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="context-service" target="gemini-cli">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="150" y="570" as="sourcePoint" />
            <mxPoint x="130" y="900" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-graph-to-fusion" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="neptune-graph" target="context-fusion">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="530" as="sourcePoint" />
            <mxPoint x="530" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-vector-to-fusion" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="opensearch-vector" target="context-fusion">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="510" y="530" as="sourcePoint" />
            <mxPoint x="530" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-fusion-to-optimizer" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="context-fusion" target="token-optimizer">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="650" y="530" as="sourcePoint" />
            <mxPoint x="670" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- Cache Integration -->
        <mxCell id="flow-context-to-cache" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="token-optimizer" target="redis-cluster">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="730" y="570" as="sourcePoint" />
            <mxPoint x="160" y="680" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- Performance Metrics Box -->
        <mxCell id="metrics-box" value="📊 KEY METRICS&#xa;• Context Delivery: <200ms (p95)&#xa;• Cache Hit Ratio: >95%&#xa;• Cost per Candidate: <$10&#xa;• Quality Score: >8.5/10&#xa;• System Availability: >99.5%" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="980" y="680" width="200" height="120" as="geometry" />
        </mxCell>
        
        <!-- Architecture Benefits Box -->
        <mxCell id="benefits-box" value="🎯 ARCHITECTURE BENEFITS&#xa;• Independent context service (MSA)&#xa;• Graph RAG intelligent discovery&#xa;• Ultra-low-cost via subscriptions&#xa;• Multi-agent ecosystem support&#xa;• Real-time context updates&#xa;• Enterprise-grade security" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="980" y="490" width="200" height="120" as="geometry" />
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Graph RAG Context Infrastructure Detail

### Context Infrastructure Detailed Architecture (draw.io XML)

```xml
<mxfile host="app.diagrams.net" modified="2025-01-08T16:00:00.000Z" agent="Graph-RAG-Context-Detail" etag="context-detail-v2.0" version="24.7.17">
  <diagram name="Graph RAG Context Infrastructure Detail" id="context-infrastructure-detail">
    <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1300" pageHeight="800" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Title -->
        <mxCell id="title-context" value="Graph RAG Context Infrastructure - Detailed Architecture" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1200" height="30" as="geometry" />
        </mxCell>
        
        <!-- Input Layer -->
        <mxCell id="input-layer" value="Context Request & Input Processing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="70" width="1200" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="api-gateway" value="API Gateway&#xa;Rate Limiting&#xa;Authentication" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="80" y="130" width="120" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="context-router" value="Context Router&#xa;Agent-Specific&#xa;Task-Aware" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="220" y="130" width="120" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="request-validator" value="Request Validator&#xa;Schema Check&#xa;Permission Check" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="360" y="130" width="120" height="60" as="geometry" />
        </mxCell>
        
        <!-- Graph RAG Processing Core -->
        <mxCell id="graph-rag-core" value="Graph RAG Processing Core" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="230" width="1200" height="40" as="geometry" />
        </mxCell>
        
        <!-- Knowledge Graph Processing -->
        <mxCell id="graph-processing" value="Knowledge Graph Processing (Amazon Neptune)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="290" width="350" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="entity-resolver" value="Entity Resolver&#xa;Candidate/Skill/Value&#xa;ID Resolution" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="80" y="340" width="100" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="graph-traversal" value="Graph Traversal&#xa;Multi-hop Queries&#xa;Relationship Discovery" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="200" y="340" width="100" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="relationship-scorer" value="Relationship Scorer&#xa;Path Strength&#xa;Relevance Ranking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="320" y="340" width="100" height="80" as="geometry" />
        </mxCell>
        
        <!-- Vector Processing -->
        <mxCell id="vector-processing" value="Vector Similarity Processing (Amazon OpenSearch)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="470" y="290" width="350" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="embedding-generator" value="Embedding Generator&#xa;Titan Embeddings&#xa;1536 Dimensions" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="470" y="340" width="100" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="vector-search" value="Vector Search&#xa;k-NN Similarity&#xa;HNSW Index" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="590" y="340" width="100" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="pattern-matcher" value="Pattern Matcher&#xa;Similar Candidates&#xa;Success Patterns" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="710" y="340" width="100" height="80" as="geometry" />
        </mxCell>
        
        <!-- Context Fusion Engine -->
        <mxCell id="fusion-engine" value="Context Fusion & Optimization Engine" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="460" width="1200" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="context-merger" value="Context Merger&#xa;Graph + Vector&#xa;Semantic Fusion" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="100" y="520" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="relevance-ranker" value="Relevance Ranker&#xa;Task-Specific&#xa;Importance Weighting" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="250" y="520" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="semantic-compressor" value="Semantic Compressor&#xa;Meaning Preservation&#xa;Token Optimization" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="400" y="520" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="agent-formatter" value="Agent Formatter&#xa;JSON/YAML/Markdown&#xa;Agent-Specific" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="550" y="520" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="quality-validator-detail" value="Quality Validator&#xa;Coherence Check&#xa;Bias Detection" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="700" y="520" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- Caching & Storage Layer -->
        <mxCell id="caching-storage" value="Multi-Layer Caching & Storage" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="630" width="1200" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="l1-cache" value="L1 Cache&#xa;In-Memory LRU&#xa;512MB, 5min TTL" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="100" y="690" width="100" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="l2-redis" value="L2 Cache&#xa;Redis Cluster&#xa;2GB, 1h TTL" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="220" y="690" width="100" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="l3-dynamodb" value="L3 Storage&#xa;DynamoDB TTL&#xa;24h, Unlimited" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="340" y="690" width="100" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="l4-s3" value="L4 Archive&#xa;S3 Intelligent&#xa;30d, Unlimited" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="460" y="690" width="100" height="70" as="geometry" />
        </mxCell>
        
        <!-- Performance Monitoring -->
        <mxCell id="monitoring-detail" value="Real-Time Performance Monitoring" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="600" y="690" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="latency-monitor" value="Latency Monitor&#xa;<200ms (p95)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;" vertex="1" parent="1">
          <mxGeometry x="600" y="730" width="90" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="cache-monitor" value="Cache Monitor&#xa;>95% Hit Ratio" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;" vertex="1" parent="1">
          <mxGeometry x="710" y="730" width="90" height="50" as="geometry" />
        </mxCell>
        
        <!-- Cost Tracking -->
        <mxCell id="cost-tracking" value="💰 Ultra-Low-Cost Tracking&#xa;Target: <$10 per candidate&#xa;Real-time alerts at $12" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;fontStyle=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="850" y="690" width="180" height="90" as="geometry" />
        </mxCell>
        
        <!-- Data Flow Arrows -->
        <mxCell id="flow-api-to-router" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="api-gateway" target="context-router">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="200" y="160" as="sourcePoint" />
            <mxPoint x="220" y="160" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-router-to-validator" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="context-router" target="request-validator">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="340" y="160" as="sourcePoint" />
            <mxPoint x="360" y="160" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-validator-to-graph" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="request-validator" target="entity-resolver">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="420" y="190" as="sourcePoint" />
            <mxPoint x="130" y="340" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-graph-chain" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="entity-resolver" target="graph-traversal">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="180" y="380" as="sourcePoint" />
            <mxPoint x="200" y="380" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-traversal-to-scorer" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="graph-traversal" target="relationship-scorer">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="300" y="380" as="sourcePoint" />
            <mxPoint x="320" y="380" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-vector-chain" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="embedding-generator" target="vector-search">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="570" y="380" as="sourcePoint" />
            <mxPoint x="590" y="380" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-search-to-pattern" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="vector-search" target="pattern-matcher">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="690" y="380" as="sourcePoint" />
            <mxPoint x="710" y="380" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-to-fusion" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="relationship-scorer" target="context-merger">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="420" as="sourcePoint" />
            <mxPoint x="160" y="520" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-fusion-chain" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="context-merger" target="relevance-ranker">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="220" y="555" as="sourcePoint" />
            <mxPoint x="250" y="555" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-ranker-to-compressor" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="relevance-ranker" target="semantic-compressor">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="555" as="sourcePoint" />
            <mxPoint x="400" y="555" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-compressor-to-formatter" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="semantic-compressor" target="agent-formatter">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="520" y="555" as="sourcePoint" />
            <mxPoint x="550" y="555" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-formatter-to-validator" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="agent-formatter" target="quality-validator-detail">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="670" y="555" as="sourcePoint" />
            <mxPoint x="700" y="555" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-to-cache" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="quality-validator-detail" target="l1-cache">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="760" y="590" as="sourcePoint" />
            <mxPoint x="150" y="690" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-cache-hierarchy" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="l1-cache" target="l2-redis">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="200" y="725" as="sourcePoint" />
            <mxPoint x="220" y="725" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-redis-to-dynamo" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="l2-redis" target="l3-dynamodb">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="320" y="725" as="sourcePoint" />
            <mxPoint x="340" y="725" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-dynamo-to-s3" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="l3-dynamodb" target="l4-s3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="440" y="725" as="sourcePoint" />
            <mxPoint x="460" y="725" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Multi-Agent Communication Flow

### Agent Interaction and Communication Flow (draw.io XML)

```xml
<mxfile host="app.diagrams.net" modified="2025-01-08T16:00:00.000Z" agent="Multi-Agent-Flow" etag="agent-flow-v2.0" version="24.7.17">
  <diagram name="Multi-Agent Communication Flow" id="multi-agent-flow">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="800" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Title -->
        <mxCell id="title-flow" value="Multi-Agent Communication Flow - Subscription CLI + AWS Bedrock Integration" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1100" height="30" as="geometry" />
        </mxCell>
        
        <!-- Sequence Participants -->
        <mxCell id="user" value="User/System" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="70" width="100" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="orchestrator" value="Agent Orchestrator" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="70" width="120" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="context-service-flow" value="Context Graph Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="380" y="70" width="120" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="subscription-agent" value="Subscription CLI Agent" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="540" y="70" width="120" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="bedrock-agent" value="AWS Bedrock Agent" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="700" y="70" width="120" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="external-system" value="External System" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fce5cd;strokeColor=#d6b656;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="860" y="70" width="120" height="40" as="geometry" />
        </mxCell>
        
        <!-- Vertical Lifelines -->
        <mxCell id="user-line" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="130" y="110" as="sourcePoint" />
            <mxPoint x="130" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="orchestrator-line" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="280" y="110" as="sourcePoint" />
            <mxPoint x="280" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="context-line" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="440" y="110" as="sourcePoint" />
            <mxPoint x="440" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="subscription-line" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="600" y="110" as="sourcePoint" />
            <mxPoint x="600" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="bedrock-line" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="760" y="110" as="sourcePoint" />
            <mxPoint x="760" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="external-line" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="920" y="110" as="sourcePoint" />
            <mxPoint x="920" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- Message Flow Sequence -->
        <mxCell id="msg1" value="1. Task Request (candidate screening)" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="130" y="140" as="sourcePoint" />
            <mxPoint x="280" y="140" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg2" value="2. Request Graph RAG context" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="280" y="160" as="sourcePoint" />
            <mxPoint x="440" y="160" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg3" value="3. Multi-hop graph traversal + vector similarity" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="440" y="180" as="sourcePoint" />
            <mxPoint x="440" y="210" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="process-box" value="Graph RAG Processing:&#xa;• Neptune graph traversal&#xa;• OpenSearch vector search&#xa;• Context fusion & ranking&#xa;• Token optimization" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;align=left;verticalAlign=top;fontSize=9;" vertex="1" parent="1">
          <mxGeometry x="360" y="180" width="160" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="msg4" value="4. Return optimized context (JSON/YAML)" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="440" y="280" as="sourcePoint" />
            <mxPoint x="280" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg5" value="5. Route to optimal agent (cost-aware)" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="280" y="300" as="sourcePoint" />
            <mxPoint x="600" y="300" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg6" value="6. Execute task with context (CLI subscription)" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="600" y="320" as="sourcePoint" />
            <mxPoint x="600" y="350" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="cli-process-box" value="CLI Agent Processing:&#xa;• Gemini/Claude/Amazon Q&#xa;• Subscription-based (unlimited)&#xa;• Agent-specific formatting&#xa;• Server-side automation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;align=left;verticalAlign=top;fontSize=9;" vertex="1" parent="1">
          <mxGeometry x="520" y="320" width="160" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="msg7" value="7. Quality validation request" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="600" y="420" as="sourcePoint" />
            <mxPoint x="760" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg8" value="8. Bedrock validation (Claude-3-Haiku)" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="760" y="440" as="sourcePoint" />
            <mxPoint x="760" y="470" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="bedrock-process-box" value="Bedrock Validation:&#xa;• Content quality check&#xa;• Bias detection&#xa;• Compliance validation&#xa;• Pay-per-token usage" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;align=left;verticalAlign=top;fontSize=9;" vertex="1" parent="1">
          <mxGeometry x="680" y="440" width="160" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="msg9" value="9. Validation results" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="760" y="540" as="sourcePoint" />
            <mxPoint x="600" y="540" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg10" value="10. Execute external actions (Dooray, Email)" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="600" y="560" as="sourcePoint" />
            <mxPoint x="920" y="560" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg11" value="11. Return task results + metrics" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="600" y="580" as="sourcePoint" />
            <mxPoint x="280" y="580" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg12" value="12. Cache results for reuse" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="280" y="600" as="sourcePoint" />
            <mxPoint x="440" y="600" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="msg13" value="13. Task completion notification" style="endArrow=classic;html=1;rounded=0;fontSize=10;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="280" y="620" as="sourcePoint" />
            <mxPoint x="130" y="620" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- Cost and Performance Metrics -->
        <mxCell id="cost-metrics" value="💰 Cost Metrics per Task:&#xa;• Subscription agent: $0.05 (amortized)&#xa;• Context generation: $0.02&#xa;• Bedrock validation: $0.03&#xa;• Total cost: $0.10 per task&#xa;• Target: <$10 per candidate" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="660" width="200" height="120" as="geometry" />
        </mxCell>
        
        <mxCell id="performance-metrics" value="⚡ Performance Metrics:&#xa;• Context delivery: <200ms&#xa;• CLI agent processing: 2-5min&#xa;• Quality validation: 30-60sec&#xa;• Cache hit ratio: >95%&#xa;• End-to-end: <10 minutes" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="660" width="200" height="120" as="geometry" />
        </mxCell>
        
        <mxCell id="agent-selection" value="🎯 Agent Selection Logic:&#xa;• Screening: Gemini CLI (cost-efficient)&#xa;• Interview kits: Claude Code (accuracy)&#xa;• Technical tasks: Amazon Q (AWS native)&#xa;• Analysis: OpenAI o4-mini (reasoning)&#xa;• Validation: Bedrock (strategic)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="490" y="660" width="200" height="120" as="geometry" />
        </mxCell>
        
        <mxCell id="quality-gates" value="✅ Quality Gates:&#xa;• Context relevance: >8.5/10&#xa;• Bias detection: automated&#xa;• Human approval: required&#xa;• Error rate: <2%&#xa;• SLA compliance: 99.5%" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="710" y="660" width="200" height="120" as="geometry" />
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## AWS Infrastructure Components Detail

### AWS Infrastructure Component Architecture (draw.io XML)

```xml
<mxfile host="app.diagrams.net" modified="2025-01-08T16:00:00.000Z" agent="AWS-Infrastructure-Detail" etag="aws-infra-v2.0" version="24.7.17">
  <diagram name="AWS Infrastructure Components" id="aws-infrastructure-components">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1000" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Title -->
        <mxCell id="title-aws" value="AWS Infrastructure Components - Context-Centric Multi-Agent System" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1300" height="30" as="geometry" />
        </mxCell>
        
        <!-- AWS Account Info -->
        <mxCell id="aws-account" value="🏢 AWS Production Account: 319470692494&#xa;Region: us-east-1 (primary) + us-west-2 (backup)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0f0f0;strokeColor=#666666;fontStyle=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="50" y="60" width="400" height="50" as="geometry" />
        </mxCell>
        
        <!-- VPC and Networking -->
        <mxCell id="vpc-layer" value="VPC and Networking Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="140" width="1300" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="production-vpc" value="Production VPC&#xa;10.0.0.0/16&#xa;Multi-AZ Setup" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="80" y="200" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="private-subnets" value="Private Subnets&#xa;ECS + Databases&#xa;3 AZs" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="220" y="200" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="public-subnets" value="Public Subnets&#xa;Load Balancers&#xa;NAT Gateways" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="360" y="200" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="security-groups" value="Security Groups&#xa;Least-Privilege&#xa;Port-Specific" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="500" y="200" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- Compute Layer -->
        <mxCell id="compute-layer" value="Compute and Container Orchestration" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="300" width="1300" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="ecs-cluster" value="ECS Fargate Cluster&#xa;context-graph-service&#xa;Auto-scaling enabled" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="80" y="360" width="150" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="lambda-functions" value="Lambda Functions&#xa;Event Processing&#xa;Webhook Handlers" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="250" y="360" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="step-functions" value="Step Functions&#xa;Workflow Orchestration&#xa;Multi-Agent Coordination" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="390" y="360" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="eventbridge" value="EventBridge&#xa;Event Routing&#xa;Agent Communication" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="530" y="360" width="120" height="80" as="geometry" />
        </mxCell>
        
        <!-- Database and Storage Layer -->
        <mxCell id="database-layer" value="Database and Storage Layer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="470" width="1300" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="neptune-cluster" value="Neptune Serverless&#xa;Knowledge Graph&#xa;Multi-AZ, Auto-scaling" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="80" y="530" width="130" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="opensearch-cluster" value="OpenSearch Serverless&#xa;Vector Engine&#xa;k-NN Optimized" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="230" y="530" width="130" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="rds-postgresql" value="RDS PostgreSQL&#xa;Structured Data&#xa;Multi-AZ, Read Replicas" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="380" y="530" width="130" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="dynamodb-tables" value="DynamoDB&#xa;Session Data&#xa;Global Tables" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="530" y="530" width="130" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="elasticache-redis" value="ElastiCache Redis&#xa;Multi-layer Cache&#xa;Cluster Mode" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="680" y="530" width="130" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="s3-storage" value="S3 Buckets&#xa;Intelligent Tiering&#xa;Lifecycle Policies" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="830" y="530" width="130" height="80" as="geometry" />
        </mxCell>
        
        <!-- Message Queue and Streaming -->
        <mxCell id="messaging-layer" value="Message Queue and Event Streaming" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="640" width="1300" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="msk-kafka" value="MSK Serverless&#xa;Kafka Streaming&#xa;Zero Data Loss" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="80" y="700" width="150" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="sqs-queues" value="SQS Queues&#xa;Dead Letter Queues&#xa;Fallback Processing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="250" y="700" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="sns-topics" value="SNS Topics&#xa;Alert Distribution&#xa;Multi-channel" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="390" y="700" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- AI and ML Services -->
        <mxCell id="ai-ml-layer" value="AI and ML Services" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="800" width="1300" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="bedrock-agents" value="Bedrock Agents&#xa;Claude-3-Sonnet/Haiku&#xa;Context Assembly" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="80" y="860" width="140" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="bedrock-kb" value="Bedrock KB&#xa;Company Knowledge&#xa;Vector Search" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="240" y="860" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="titan-embeddings" value="Titan Embeddings&#xa;Text-to-Vector&#xa;1536 Dimensions" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="380" y="860" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- Monitoring and Security -->
        <mxCell id="ops-layer" value="Monitoring, Security, and Operations" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="700" y="200" width="650" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="cloudwatch" value="CloudWatch&#xa;Metrics & Logs&#xa;Custom Dashboards" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="720" y="260" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="xray" value="X-Ray&#xa;Distributed Tracing&#xa;Performance Analysis" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="860" y="260" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="secrets-manager" value="Secrets Manager&#xa;Credential Storage&#xa;90-day Rotation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1000" y="260" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="iam-roles" value="IAM Roles&#xa;Least-Privilege&#xa;Service-to-Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1140" y="260" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="cost-explorer" value="Cost Explorer&#xa;Budget Alerts&#xa;Resource Optimization" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="720" y="350" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="config" value="AWS Config&#xa;Compliance Monitoring&#xa;Resource Tracking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="860" y="350" width="120" height="70" as="geometry" />
        </mxCell>
        
        <mxCell id="cloudtrail" value="CloudTrail&#xa;Audit Logging&#xa;Immutable Records" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1000" y="350" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- Data Flow Connections -->
        <mxCell id="flow-ecs-to-neptune" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="ecs-cluster" target="neptune-cluster">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="155" y="440" as="sourcePoint" />
            <mxPoint x="145" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-ecs-to-opensearch" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="ecs-cluster" target="opensearch-cluster">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="155" y="440" as="sourcePoint" />
            <mxPoint x="295" y="530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-lambda-to-msk" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="lambda-functions" target="msk-kafka">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="310" y="440" as="sourcePoint" />
            <mxPoint x="155" y="700" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="flow-bedrock-to-opensearch" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;strokeWidth=2;" edge="1" parent="1" source="bedrock-agents" target="opensearch-cluster">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="150" y="860" as="sourcePoint" />
            <mxPoint x="295" y="610" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- Cost and Performance Indicators -->
        <mxCell id="cost-breakdown" value="💰 Monthly Cost Breakdown:&#xa;• Neptune Serverless: $200-400&#xa;• OpenSearch Serverless: $100-200&#xa;• ECS Fargate (shared): $0&#xa;• MSK Serverless: $100-200&#xa;• Redis (shared): $0&#xa;• Total Infrastructure: $400-800&#xa;&#xa;• Subscription CLI Agents: $94&#xa;• Total Monthly: $494-894&#xa;• Cost per candidate: $12-22" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffcccc;strokeColor=#ff0000;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1000" y="530" width="300" height="200" as="geometry" />
        </mxCell>
        
        <mxCell id="performance-targets" value="⚡ Performance Targets:&#xa;• Neptune queries: <100ms avg&#xa;• OpenSearch k-NN: <150ms p95&#xa;• Context assembly: <200ms p95&#xa;• ECS auto-scale: <30sec&#xa;• Cache hit ratio: >95%&#xa;• System availability: >99.5%" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="530" y="700" width="200" height="120" as="geometry" />
        </mxCell>
        
        <mxCell id="scaling-strategy" value="📈 Auto-Scaling Strategy:&#xa;• ECS tasks: CPU >70%&#xa;• Neptune: Connection >80%&#xa;• OpenSearch: Query latency&#xa;• Lambda: Concurrent executions&#xa;• Target: Handle 60+ candidates/week" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;align=left;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="750" y="700" width="200" height="120" as="geometry" />
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Usage Instructions

### How to Use These Diagrams

1. **Copy XML Content**: Copy any of the XML code blocks above
2. **Open draw.io**: Go to https://app.diagrams.net/
3. **Import XML**: 
   - Click "File" → "Import from" → "Text"
   - Paste the XML content
   - Click "Import"
4. **Edit and Customize**: Modify colors, text, or layout as needed
5. **Export**: Save as PNG, PDF, or SVG for presentations

### Diagram Purposes

1. **High-Level Architecture**: Overall system view for executives and stakeholders
2. **Context Infrastructure Detail**: Technical deep-dive for developers and architects
3. **Multi-Agent Flow**: Communication patterns for understanding agent interactions
4. **AWS Infrastructure**: Detailed AWS service configuration for cloud architects

These diagrams provide comprehensive visual documentation of the Graph RAG-based context-centric multi-agent architecture, making it easy for builders and AWS meeting participants to understand the complete system design, costs, and implementation approach.
