# Interview Guide: Lee Im-Hyung

## 1. General Guidance for Interviewers
The interview with Lee Im-Hyung should focus on bridging the gap between his impressive academic/bootcamp projects and the realities of a production engineering environment. His technical skills in LLM/RAG are advanced for his level, so the goal is to evaluate his foundational engineering knowledge, his thought process on scalability and reliability, and his potential to adapt to a professional team setting. Challenge his assumptions about his projects to see how he thinks on his feet.

---

## 2. Session-Specific Plans

### **Stage 1: Behavioral & Technical Deep-Dive (60 mins)**

#### **Behavioral (BEI) Questions (Personalized)**
*   **Question 1 (Technical Excellence & Problem-Solving):** "Your allergy-safe recipe chatbot won the top prize at your bootcamp. Tell me about the decision to build a RAG pipeline. What specific problems were you seeing with the base model, and how did your RAG implementation directly address them?"
*   **Question 2 (Leadership & Collaboration):** "You were the team lead for the AI Golf Assistant project. Describe a time you had a disagreement with a team member about a technical approach. How did you handle it, and what was the outcome?"
*   **Question 3 (Impact & User Focus):** "Many of your projects, like the one for allergy patients, are focused on helping specific groups. What does 'building for impact' mean to you, and how would you apply that principle here, where our customers are often expert financial traders?"

#### **Technical Deep-Dive Questions**
*   **Follow-up on RAG Project:** "Let's imagine your recipe chatbot suddenly gets 100,000 users. What parts of your current architecture would break first? How would you redesign it for scalability and low latency?"
*   **Python/Flask:** "In your Flask applications, how do you manage application configuration and secrets? What are the trade-offs between different approaches?"
*   **API & Data:** "When building the backend for your golf assistant, how did you structure the data models? If the frontend team asked for a new endpoint to show a user's progress over time, how would you design and implement it?"

---

### **Stage 2: Pair-Programming (45 mins)**

#### **Problem Selection**
- **Problem:** `Easy: Implement a Simple Cache`
- **Rationale:** This is a great foundational problem. While he has used complex libraries like LangChain, this task will test his core data structure knowledge (hash maps) and his ability to write clean, logical Python code from scratch. It also opens the door for discussions on caching strategies, which is relevant to the scalability of his projects.

---

### **Stage 3: System Design (45 mins)**

#### **Problem Statement**
- **Problem:** "We want to build a new service called 'Docu-Helper'. It's an internal chatbot that allows our engineers to ask questions about our extensive internal technical documentation. Design the system, paying close attention to how you would ingest the documents, keep the information up-to-date, and ensure the answers are accurate and cite their sources."
- **Rationale:** This problem is directly tailored to his demonstrated expertise in RAG and chatbots. It forces him to think beyond a prototype and consider the full lifecycle of a real-world AI system: data ingestion pipelines, updating knowledge stores, and ensuring accuracy and trust. This will clearly reveal his depth of understanding.
