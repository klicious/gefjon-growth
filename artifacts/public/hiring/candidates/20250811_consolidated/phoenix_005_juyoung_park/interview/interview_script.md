---
id: interview_script_2025-08-20
type: interview_script
domain: hiring
created_date: 2025-08-20
last_updated: 2025-08-20
author: Junie
quality_score: __TBD__
tags: ['interview', 'bei', 'phoenix_005_juyoung_park']
visibility: public
version: 1.0
---


# Interview Script (BEI & Technical Deep-Dive)

**Candidate**: Juyoung Park (phoenix_005_juyoung_park)
**Project**: `dunamis` (https://github.com/jyp-on/dunamis)

**Instructions for Interviewer**:
This is not a typical BEI. Use the candidate's code as the "Situation" and "Task" for the STAR method. Your goal is to probe their "Action" and "Result" by asking about the code they wrote and the choices they made. Dig deep into the *why*.

---

## Part 1: Introduction & Opening (5 mins)

- **Interviewer**: "Hi Juyoung, thanks for joining us today. We were all able to review your take-home submission, the `dunamis` project, and we'll be using that as a foundation for our conversation today. The goal here is to understand your thought process and your approach to building software."
- **Interviewer**: "Before we dive in, I was impressed with your prior experience building a festival platform for 25,000 users. That sounds like a great experience with scaling. We'll likely touch on some of those lessons today as well."

---

## Part 2: Code-Centric Behavioral & Technical Deep-Dive (80 mins)

### Topic 1: Testing and Reliability (Value: Integrity & Reliability)

1.  **Interviewer**: "Let's start with testing. I saw you created unit tests for your logger in `tests/test_logger_simple.py`. Can you tell me about your thought process for testing that component?"
    - **Follow-up**: "That makes sense. Now, looking at the core logic in `src/exchanges/bitmex.py`, there aren't any tests. If you had another day to work on this, how would you have built a test suite to ensure the BitMEX client was truly reliable? What kinds of tests (unit, integration, contract) would you write, and why?"
    - **Follow-up**: "How would you handle testing the private, authenticated endpoints? What challenges would you expect?"

### Topic 2: Architecture and Scalability (Value: Technical Excellence & Scalable Elegance)

1.  **Interviewer**: "In `src/exchanges/base.py`, you created an abstract `BaseExchange` class. This is a solid pattern. Can you walk me through why you chose this design? How did you see this helping the project scale to support other exchanges in the future?"
    - **Follow-up**: "On line 24, you set a timeout for the `httpx.Client`. This is a good first step for resilience. What other issues could this client face when talking to an external API in a production environment?"
    - **Follow-up**: "How would you evolve this client to be more resilient? Let's talk about patterns like exponential backoff retries or circuit breakers. How might you implement one of those here?"

### Topic 3: Security (Value: Security & Compliance First)

1.  **Interviewer**: "Your `BaseExchange` class has several `_validate_` methods, which is great for catching bad inputs. Let's focus on security. The config in your project seems to imply API keys would be stored in a file. Can you walk me through how you would handle these secrets securely in a real production environment on AWS? What tools or services would you use?"
    - **Follow-up**: "What are the risks of committing secrets to a repository, even a private one?"
    - **Follow-up**: "Your project uses `httpx`. What kind of security vulnerabilities do you need to consider when using third-party libraries, and how would you mitigate them?"

### Topic 4: Production Readiness (Values: Observability & Guardrails, Ownership & Proactivity)

1.  **Interviewer**: "You've implemented structured logging, which is excellent for `Observability`. What's the next step? If this service were running in production, what other signals would you want to emit to understand its health? Let's talk about metrics."
    - **Follow-up**: "What key metrics would you track for the `place_order` function, for example?"
2.  **Interviewer**: "The evaluation noted there was no CI pipeline. Can you describe how you would set up a CI pipeline for this project using GitHub Actions? What would be the essential stages in that pipeline to enforce our standards for `Technical Excellence`?"
    - **Follow-up**: "What is linting, and why is it an important gate in a CI pipeline?"
3.  **Interviewer**: "The project didn't include a `Dockerfile`. Why is containerization important for modern services? How would you go about containerizing this Python application?"

---

## Part 3: Candidate Q&A and Closing (10 mins)

- **Interviewer**: "That was a great discussion. I appreciate you walking me through your project in such detail. Now, what questions do you have for me about the role, the team, or our engineering culture at Gefjon?"
- **Interviewer**: (After Q&A) "Thank you again for your time and for the effort you put into the assignment. We'll be in touch with the next steps within a few days."
