# **BitMEX Testnet Order Client**

## **Summary (read first)**

You will build a minimal Python client / CLI that can **list open orders, place one LIMIT order, and cancel an order by ID on the BitMEX testnet**.

The scope is deliberately narrow so most candidates can finish in **≈ 6 hours**. All functional, quality, testing, documentation and ownership dimensions map 1-to-1 to our evaluation rubric.

---

## **1 Timeline & Submission**

| **Item** | **Requirement** |
| --- | --- |
| **Time-box** | **72 hours** from email receipt **or** once you reach **8 hours of effort**—stop and submit even if incomplete. This follows candidate-experience best practice that longer tasks cause 40-65 % drop-off. |
| **Repo** | Private GitHub repo; add **klicious** as collaborator. |
| **What to send** | Email **hr@dunamiscap.com** with:• Repo URL• GitHub handle• TIME_SPENT.md (hh:mm log). |
| **Commits** | Push frequently with clear messages; branching optional but encouraged. |

---

## **2 Tech Stack & Tooling**

- **Python 3.12** (use uv pip install -r requirements.txt).
- HTTP: requests or httpx.
- Typing/validation: pydantic.
- Testing: pytest, pytest-mock or **responses** for HTTP stubs .
- Lint/format: ruff, black.
- Use only **BitMEX testnet** base URL https://testnet.bitmex.com/api/v1 ; never commit live keys.

---

## **3 Functional Requirements**

| **#** | **Feature** | **Endpoint hints** |
| --- | --- | --- |
| 1 | **List open orders** | GET /order with filter={"open":true} (see BitMEX API Explorer). |
| 2 | **Place LIMIT order** | POST /order with symbol=BTCUSD, ordType=Limit, price, orderQty. |
| 3 | **Cancel order by ID** | DELETE /order with orderID=<id>. |

**Constraints**

- Only **BTCUSD perpetual** contract on testnet.
- CLI flags or a minimal SDK function for each action.
- Respect BitMEX rate-limit headers if you loop (stretch goal).

---

## **4 Non-Functional Requirements**

- **Modularity** – separate API layer (bitmex_client.py) from CLI (cli.py).
- **Security** – load API keys from env vars; never hard-code.
- **Type safety** – annotate and mypy --strict clean.
- **Logging** – at least one structured log line per request (extra credit for structlog).
- **Test coverage ≥ 45 %** is a healthy junior target per LambdaTest norms.

---

## **5 Deliverables**

1. **Code** – working client/CLI with __main__.py entry or python cli.py ….
2. **Tests** – pytest -q must pass; mock HTTP calls.
3. **README.md** – max 400 words; include setup, env-var table, CLI examples, and diagram (optional).
4. **TIME_SPENT.md** – honest time log.
5. **(Stretch)** – Retry/back-off or rate-limit parsing for Ownership points.

---

## **6 Evaluation**

We grade with the **Enhanced Entry-Level SWE rubric** you already received:

- **Functional 25 %** – three actions work on testnet.
- **Code Quality 20 %** – idiomatic, modular, typed.
- **Testing 15 %** – unit + mocked HTTP, coverage report.
- **Docs 10 %** – quick-start and usage clear.
- **Ownership 15 %** – extras like retries/logging.
- **Scalability 10 %** – clean abstraction for future endpoints.
- **Quant/Logic 5 %** – correct numeric handling (qty, price).

Gate ≥ 2/5 on Functional, Code, Tests; overall ≥ 3.0/5 (60 %) advances.

---

## **7 Helpful Resources (optional)**

- BitMEX API overview
- REST endpoint docs
- Official Python Swagger client
- AlgoTrading101 BitMEX intro guide (walk-through of auth & signing)
- Tutorial on mocking external APIs with responses
- Example cancel-all endpoint (handy for future stretch)
- Rate-limit header description (for stretch goal)
- Medium BitMEX Python tutorial (hand-coding requests)

---

**Good luck, and remember: quality over quantity—stop at eight hours and annotate TODOs for anything you’d tackle next!**