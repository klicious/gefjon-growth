
# Candidate Context: Park Kyung Ho

## 1. Executive Summary

Park Kyung Ho is a highly proactive and skilled Backend & DevOps engineer with approximately 2 years of experience. He demonstrates exceptional ownership, a strong foundation in cloud-native technologies (Kotlin/Spring, Kubernetes), and practical experience with AI/LLM systems. His public contribution to a major open-source library (`spring-ai`) is a standout indicator of his technical depth and commitment to quality. He appears to be a strong fit for our team and culture, with the potential to grow into a senior role.

---

## 2. Key Information

*   **Applying for:** Mid-Level Backend Engineer
*   **Experience:** ~2 years
*   **Education:** B.S. in Software Engineering, Kyungsung University
*   **Certifications:** CKA (Certified Kubernetes Administrator)
*   **Key Skills:** Kotlin, Java, Spring Boot, Spring AI, Python, AWS, Kubernetes, Docker, Terraform, CI/CD, MySQL, ChromaDB, Prometheus, Grafana

---

## 3. Experience & Project Highlights

### **WaveDeck (Startup) - Backend & DevOps Engineer**

*   **Scope:** Owned end-to-end backend development, AWS EKS infrastructure design, and CI/CD.
*   **Key Achievements:**
    *   **Efficiency:** Reduced deployment time from 30 minutes to 5 minutes by building a GitHub Actions-based pipeline.
    *   **Performance:** Improved key query performance by over 200% through index refactoring.
    *   **Cost Savings:** Built a mock AI server to reduce non-production GPU spend.

### **Project: `why_price` ("이거왜오름?")**

*   **Description:** An AI service that explains price volatility for Korean stocks.
*   **Technology:** Implemented a RAG pipeline using Spring AI and ChromaDB. Used batch generation and HTTP caching to lower LLM costs.
*   **Relevance:** Demonstrates practical experience with the agentic AI concepts we value.

### **Project: `Warehouse Reservation` System**

*   **Description:** A reservation system built with Kotlin/Spring.
*   **Technology:** Used pessimistic locking to ensure concurrency safety and prevent double-bookings. Implemented a binary-search algorithm for efficient slot lookup.
*   **Relevance:** Shows a deep understanding of backend concurrency and algorithmic problem-solving.

### **Contribution: Spring AI ChromaDB Issue #2648**

*   **Description:** Identified, documented, and submitted a fix for a breaking-change bug in the `spring-ai` library.
*   **Technology:** Used the Adapter pattern to isolate the risk before the fix was merged.
*   **Relevance:** This is a powerful signal of **Ownership**, **Technical Excellence**, and **Integrity**. He didn't just find a problem; he solved it for the entire community.

---

## 4. Core Value Alignment

This section maps the candidate's experience to our core values, providing you with concrete examples to discuss during the interview.

*   **Technical Excellence & Scalable Elegance:**
    *   **Evidence:** Applied Hexagonal Architecture and the Adapter pattern to isolate external risk in the `spring-ai` issue.

*   **Ownership & Proactivity:**
    *   **Evidence:** The `spring-ai` contribution is a prime example. He also designed the AWS VPC-to-EKS infrastructure from scratch and maintained it 24/7.

*   **Observability & Guardrails:**
    *   **Evidence:** Direct experience with Prometheus, Grafana, and Loki.

*   **Data-Informed Iteration:**
    *   **Evidence:** Eliminated low-usage features after query analysis, cutting project costs by 20%.

*   **Integrity & Reliability:**
    *   **Evidence:** His proactive and public handling of the `spring-ai` bug demonstrates high integrity. His use of pessimistic locks and exhaustive tests in the reservation system shows a commitment to reliability.

*   **Continuous Learning & Mentorship:**
    *   **Evidence:** Over 1,400 learning-focused commits and a regularly updated technical blog on Tistory.

*   **Innovative Spirit:**
    *   **Evidence:** Extended the Spring AI OpenAIChatModel to communicate with the Perplexity API, showing a desire to experiment and improve existing tools.

*   **Automation & Efficiency:**
    *   **Evidence:** Reduced deployment time from 30 to 5 minutes by building a CI/CD pipeline.

---

## 5. Points to Clarify (Red Flags)

*   **Testing Philosophy:** While he mentions testing, his resume lacks specific details on unit test coverage or his approach to quality assurance. This is a key area to probe in the technical deep-dive.
*   **Career Timeline:** His resume is missing exact employment dates. This should be clarified during the final leadership interview.
