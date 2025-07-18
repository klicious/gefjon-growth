# **Unified Ticker Normaliser**

## **1 Timeline & Submission**

| **Item** | **Requirement** |
| --- | --- |
| **Time-box** | **72 hours** from email receipt **or** once you reach **8 hours of effort**—stop and submit even if incomplete. |
| **Repo** | Private GitHub repo; add **klicious** as collaborator. |
| **What to send** | Email **hr@dunamiscap.com** with:• Repo URL• GitHub handle• TIME_SPENT.md (hh:mm log). |
| **Commits** | Push frequently with clear, descriptive messages; branching optional but encouraged. |

---

## **2 Tech Stack & Tooling**

- **Python 3.12** (install deps with uv pip install -r requirements.txt).
- HTTP client: httpx or requests.
- Data classes / validation: pydantic.
- Testing: pytest, **responses** for HTTP stubs .
- Lint/format: ruff, black, pre-commit hooks encouraged .
- **No secrets required** – endpoints are public.

---

## **3 Functional Requirements**

| **#** | **Task** | **Endpoint Reference** |
| --- | --- | --- |
| 1 | **Fetch last-trade price** for BTC/USD from **Binance Spot** | GET /api/v3/ticker/price?symbol=BTCUSDT |
| 2 | **Fetch last-trade price** for BTC-USD from **Coinbase Exchange** | GET /products/BTC-USD/ticker (Advanced Trade API) |
| 3 | **Normalise** each payload into a shared JSON schema:`{ “exchange”: str, “timestamp”: iso8601, “bid”: float | None, “ask”: float |
| 4 | **Output** the merged list (List[dict]) to **stdout** as pretty-printed JSON. |  |
| 5 | **CLI flags** --exchanges and --symbol (default BTCUSD) for extensibility. |  |

### **Stretch Goal (Ownership 15 %)**

- Compute the cross-exchange **spread** (abs(price_a - price_b) / mid) and print an **alert** if it exceeds **0.5 %**.

---

## **4 Non-Functional Requirements**

- **Modularity** – separate binance_client.py, coinbase_client.py, and normaliser.py.
- **Type-safety** – full type hints; mypy --strict clean.
- **Logging** – structured INFO logs (timestamp, exchange, latency_ms).
- **Testing** – at least one happy-path and one failure test per client; target ≥ 45 % coverage (LambdaTest junior baseline) .
- **Retry policy** – honour HTTP 5xx with exponential back-off (optional stretch).

---

## **5 Deliverables**

1. **Code** – working CLI (python cli.py --exchanges binance,coinbase).
2. **Tests** – pytest -q must pass; all external calls mocked with responses .
3. **README.md** (≤ 400 words) – setup, env-vars (if any), CLI examples, and a tiny architecture diagram.
4. **TIME_SPENT.md** – honest hh:mm log.
5. **(Stretch)** – spread alert or retry logic.

---

## **6 Evaluation Mapping (to Enhanced Rubric)**

| **Rubric Criterion** | **Where It Appears in Task** |
| --- | --- |
| **Functional 25 %** | Successful fetch → normalise → JSON out. |
| **Code Quality 20 %** | Modular clients, pydantic schema, lint clean. |
| **Testing 15 %** | Mocked HTTP + coverage report. |
| **Docs 10 %** | Clear README & diagram. |
| **Ownership 15 %** | Spread alert, retries, logging. |
| **Scalability 10 %** | Abstract BaseTickerClient to add more exchanges. |
| **Quant 5 %** | Correct numeric handling, spread calc. |

Gate ≥ 2/5 on Functional, Code, Tests; overall ≥ 3.0/5 (60 %) advances.

---

## **7 Helpful Resources**

- **Binance Spot API ticker docs** – /api/v3/ticker/price
- **Binance rate-limit headers** – X-MBX-USED-WEIGHT
- **Coinbase Exchange API overview**
- Example REST “product” endpoint spec (price fields)
- StackOverflow discussion of legacy spot-price endpoint (context)
- Python responses mocking library
- Example mock snippet (requests.get monkey-patch)
- LambdaTest article on coverage expectations
- Talent Board CandE program – candidate-experience benchmarks
- CareerPlug 2024 Candidate Experience Report (lengthy tasks → dropout)
- Cronofy Candidate Expectations 2024 (42 % drop if slow/long)
- ruff-pre-commit hook guide

---

**Remember** – quality over quantity. If you hit 8 hours first, commit with TODOs for remaining work, push, and submit. Good luck!