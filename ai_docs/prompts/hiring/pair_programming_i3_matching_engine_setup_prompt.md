You are a senior software engineer responsible for setting up and conducting a pair programming interview. Your task is to create the necessary files and directory structure for the "I-3 Mini Matching Engine" problem.

**Problem Description:**

**I-3 Mini Matching Engine:** This problem requires implementing a simplified order matching engine for a financial exchange. The engine must handle market orders and limit orders, applying price-time priority for matching. This exercise assesses understanding of core data structures (like order books), event handling, and algorithmic logic crucial in fintech environments.

**Company Context:**

*   **Mission:** To empower investors with intelligent, AI-driven tools that provide a decisive edge in the market.
*   **Vision:** To become the leading provider of AI-powered investment solutions, making sophisticated trading strategies accessible to everyone.
*   **Values:**
    *   **Data-Driven:** Decisions are based on empirical evidence and rigorous analysis.
    *   **Excellence:** Strive for the highest quality in our products, services, and operations.
    *   **Innovation:** Continuously explore new technologies and ideas to stay ahead of the curve.
    *   **Integrity:** Uphold the highest ethical standards in all our dealings.
    *   **Collaboration:** Foster a culture of teamwork, communication, and mutual respect.

**Hiring Process:**

The pair programming session is a key stage in our hiring process, following the initial screening and preceding a system design interview. The goal is to evaluate a candidate's real-time coding, problem-solving, and collaboration skills in a setting that mirrors our day-to-day work.

**Instructions:**

1.  **Create a root directory** for the pair programming session. Name it `pair_programming_i3_matching_engine`.
2.  **Inside the root directory, create the following subdirectories:**
    *   `src`: For the main application source code.
    *   `tests`: For the unit and integration tests.
    *   `docs`: For a brief explanation of the problem and the project structure.
3.  **Populate the directories with the following files:**

    *   **`docs/README.md`:**
        *   A clear and concise description of the "I-3 Mini Matching Engine" problem.
        *   Instructions on how to set up the project, run the application, and execute the tests.
        *   An explanation of the project structure.

    *   **`src/matching_engine.py`:**
        *   A skeleton for the matching engine logic, including class and method stubs.
        *   Comments indicating where the candidate should fill in the implementation.
        *   Placeholders for core data structures (e.g., order book).

    *   **`src/order.py`:**
        *   A data class or simple class to represent a trading order, with attributes like `order_id`, `side` (buy/sell), `type` (market/limit), `price`, and `quantity`.

    *   **`tests/test_matching_engine.py`:**
        *   A set of unit tests covering the basic functionalities of the matching engine.
        *   Include test cases for:
            *   Adding a new order to the book.
            *   Matching a market order with an existing limit order.
            *   Matching two limit orders.
            *   Handling partial fills.
            *   Ensuring price-time priority.
        *   Leave some test cases unimplemented for the candidate to complete.

    *   **`.gitignore`:**
        *   A standard Python `.gitignore` file to exclude common files and directories (e.g., `__pycache__`, `.venv`, `*.pyc`).

    *   **`requirements.txt`:**
        *   A file listing the necessary Python packages. For this problem, it might be empty or include a testing framework like `pytest`.

Ensure the created files and directories are well-structured and follow best practices for a Python project. The code should be clean, readable, and provide a solid foundation for the pair programming session.
