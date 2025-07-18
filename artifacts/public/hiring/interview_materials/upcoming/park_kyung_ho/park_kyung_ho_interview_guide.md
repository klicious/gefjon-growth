
# Personalized Interview Guide: Park Kyung Ho

## 1. General Guidance for Interviewers

This candidate is strong, with a high degree of ownership and practical experience. The goal of this interview is to go deep and understand the *why* behind his decisions. Avoid simple knowledge-based questions and focus on open-ended, situational, and design-oriented questions.

---

## 2. Interview Timeline & Structure

**Total Duration:** ~4 hours (including breaks)

| Session                               | Duration    | Focus                                           |
| ------------------------------------- | ----------- | ----------------------------------------------- |
| 1. Behavioral & Technical Deep-Dive   | 60 minutes  | Culture fit, past experience, technical depth   |
| *Break*                               | *15 minutes*|                                                 |
| 2. Pair-Programming Session           | 75 minutes  | Real-time coding, problem-solving, collaboration|
| *Break*                               | *15 minutes*|                                                 |
| 3. System Design & Agentic AI         | 75 minutes  | Scalability, architecture, AI-native thinking   |
| 4. Final Leadership Interview         | 30 minutes  | Career goals, vision alignment                  |

---

## 3. Session-Specific Plans

### **A. Behavioral Interview (BEI)**

**Focus:** Collaboration, influencing others, and handling ambiguity.

**Suggested Questions:**

1.  **Based on your `spring-ai` contribution:** "Tell me about a time you had to influence a team or individual that you didn't have any formal authority over. How did you convince them to adopt your recommendation? What was the outcome?"
2.  **Based on your DevOps experience:** "Describe a situation where you had to make a significant technical decision with incomplete information. How did you approach the problem, and what was the result?"
3.  "Tell me about a time you had a disagreement with a colleague about a technical approach. How did you handle it, and what was the outcome?"
4.  **Probing for Integrity & Observability:** "Tell me about a time you made a significant technical mistake that impacted users or the system. How did you handle the situation, what was the immediate aftermath, and what did you learn from it?"
    *   **Rationale:** While his `spring-ai` contribution shows he is proactive about external bugs, this question directly assesses how he handles his *own* errors, which is crucial for building a culture of trust and immediate fault reporting.

### **B. Pair-Programming Session**

**Focus:** Real-time coding, problem-solving, and collaboration.

**Selected Problem:**
*   **Intermediate: I-3 Mini Matching Engine**
    *   **Rationale:** This problem is highly relevant to our fintech domain and will allow us to assess his understanding of core data structures, event handling, and price-time priority logic. It is also a good test of his ability to write clean, maintainable code under pressure.

### **C. System Design Interview**

**Focus:** Real-time data processing, scalability, and agentic design.

**Selected Problem:**
*   **Design a Real-Time Fraud Detection System for a High-Frequency Trading Platform.**
    *   **Rationale:** This problem is complex, open-ended, and directly relevant to our work. It will require him to think about:
        *   **Data Ingestion:** How to handle a high volume of real-time trade data.
        *   **Feature Engineering:** What features would be useful for detecting fraudulent activity.
        *   **Model Deployment:** How to deploy and update a machine learning model in a low-latency environment.
        *   **Agentic Component:** How an AI agent could be used to monitor the system, flag suspicious activity, and even take automated action.

### **D. Agentic AI & System Design**

**Focus:** Deep dive into agent orchestration, evaluation, and practical challenges.

**Suggested Questions:**

1.  "In your `why_price` project, you used RAG to explain stock price volatility. How would you evolve this into a more autonomous agent that could not only explain volatility but also predict it and suggest trading strategies? What new components would you need?"
2.  "Let's talk about agent evaluation. How would you measure the performance of an AI agent in a live trading environment? What are the key metrics you would track?"
3.  "Describe a situation where an AI agent might fail or produce unexpected results. How would you design a system to handle these failures gracefully?"

### **E. Technical Deep-Dive**

**Focus:** Testing philosophy and practices, and the "why" behind his technical decisions.

**Suggested Questions:**

1.  **On the `Warehouse Reservation` project:** "You used pessimistic locking to handle concurrency. What other approaches did you consider, and why did you choose pessimistic locking? What are the trade-offs of this approach?"
2.  **On testing:** "Can you walk me through your testing strategy for the `why_price` project? What types of tests did you write, and how did you ensure the quality of your code? What is your philosophy on unit testing, and what do you think is a reasonable level of test coverage?"

### **F. Final Leadership Interview**

**Focus:** Career aspirations, alignment with our vision, and clarifying his career timeline.

**Suggested Questions:**

1.  "Where do you see yourself in the next 3-5 years? What are your long-term career goals?"
2.  "Based on what you've learned about our team and our mission, how do you see yourself contributing to our success?"
3.  "To help us understand your journey better, could you walk us through your career path and the duration of your previous roles?"
