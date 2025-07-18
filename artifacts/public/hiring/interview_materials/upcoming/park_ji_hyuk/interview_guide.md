# Interview Guide: Park Ji-Hyuk

## 1. General Guidance for Interviewers
The primary goal for this interview is to assess the depth of Park Ji-Hyuk's practical backend and cloud skills, moving beyond his academic and internship experiences. He has a strong, innovative project portfolio, so we need to gauge his ability to apply that creativity to our production systems. Focus on his problem-solving process, his understanding of engineering trade-offs, and his direct experience with the technologies listed.

---

## 2. Session-Specific Plans

### **Stage 1: Behavioral & Technical Deep-Dive (60 mins)**

#### **Behavioral (BEI) Questions (Personalized)**
*   **Question 1 (Ownership & Technical Challenge):** "Your resume mentions you led the backend API and DB schema for the 'Chung-an Downtown Revitalization App'. Walk me through the process. What was the most challenging technical decision you had to make, and what was the outcome?"
*   **Question 2 (Innovation & Problem-Solving):** "Winning the 'Heart & Lung Sound AI Challenge' is impressive. Tell me about the moment you decided to use an SRGAN model. What was the problem you were trying to solve, and why was that the right approach compared to other models?"
*   **Question 3 (Versatility & Collaboration):** "On the 'Pet-Care AI Web-platform', you handled frontend, backend, and deployment. Describe a situation where a decision on the backend had a significant impact on the frontend, and how you managed that trade-off."

#### **Technical Deep-Dive Questions**
*   **Follow-up on ITEL internship:** "Let's talk about the data-pipeline automation for the patent-fee manager. What specific AWS services did you use? What was the data flow? How did you ensure the pipeline was reliable?"
*   **Django/Python:** "In your Django projects, how have you handled asynchronous tasks? What are the benefits and drawbacks of Django's ORM?"
*   **API Design:** "When you designed the weather API for the revitalization app, what principles did you follow to make it a well-designed REST API?"

---

### **Stage 2: Pair-Programming (45 mins)**

#### **Problem Selection**
- **Problem:** `Intermediate: API Rate Limiter`
- **Rationale:** This problem is a good fit for Park Ji-Hyuk's experience with API design and backend systems. It will allow us to assess his problem-solving skills, data structure knowledge (e.g., using hash maps and timestamps), and his ability to write clean, efficient Python code under time constraints.

---

### **Stage 3: System Design (45 mins)**

#### **Problem Statement**
- **Problem:** "Design a system that collects real-time data from thousands of IoT-enabled pet feeders, allows users to view their pet's feeding history via a mobile app, and sends an alert if a scheduled feeding is missed. The system should be scalable, reliable, and cost-effective."
- **Rationale:** This problem is tailored to his experience with the "Pet-Care AI Web-platform" and his listed skills in AWS and backend development. It will test his ability to think about scalability, data ingestion, API design for mobile clients, and reliability (alerting). We can see how he applies his knowledge to a practical, large-scale problem.
