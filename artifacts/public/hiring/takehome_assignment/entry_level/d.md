## **1 Timeline & Submission**

| **Item** | **Requirement** |
| --- | --- |
| **Time-box** | **72 hours** from email receipt **or** once you reach **8 hours of effort**—whichever comes first. |
| **Repo** | Private GitHub repo; add **klicious** as collaborator. |
| **Send** | Email **hr@dunamiscap.com** with the repo URL, your GitHub handle, and TIME_SPENT.md (hh:mm log). |
| **Commits** | Push frequently with clear messages; branches optional but welcome. |

---

## **2 Tech Stack & Tooling**

- **Python 3.12** – install deps with uv pip install -r requirements.txt.
- **FastAPI + Uvicorn** for the web layer .
- **Pydantic v2** for request/response models and automatic OpenAPI docs .
- **pytest** + **httpx TestClient** for local unit tests .
- **Prometheus-FastAPI-Instrumentator** (stretch) for metrics .
- **ruff** / **black** pre-commit hooks for lint/format .

---

## **3 Functional Requirements**

| **#** | **Endpoint** | **Behaviour** |
| --- | --- | --- |
| 1 | POST /orders | Create an order {id:str, symbol:str, qty:int, price:Decimal}. Return the order JSON. |
| 2 | POST /amend | Body `{id:str, qty:int |
| 3 | GET /orders/{id} | Return current order JSON or 404 if not found. |
| 4 | **OpenAPI docs** auto-generated at /docs (FastAPI default)  . |  |

**Constraints**

- Store orders in a process-level dict (thread-safe for demo purposes) .
- Prices/qty must use decimal.Decimal to avoid float error .
- Return validation errors (422) for negative qty or price .

### **Stretch Goal (Ownership 15 %)**

- Expose Prometheus metrics at /metrics with request count & latency .

---

## **4 Non-Functional Requirements**

- **Modularity** – separate models.py, storage.py, api.py.
- **Type-safety** – full type hints; mypy --strict passes.
- **Logging** – INFO logs per request (method, path, latency).
- **Testing** – at least two happy-path and one edge-case test; use FastAPI TestClient and pytest best-practice .
- **Coverage ≥ 45 %** (junior baseline) .

---

## **5 Deliverables**

1. **Code** – runnable with uvicorn api:app.
2. **Tests** – pytest -q must pass; no external calls.
3. **README.md** (≤ 400 words) – setup, API examples, env vars (none), diagram optional.
4. **TIME_SPENT.md** – honest hh:mm log.
5. **(Stretch)** – Prometheus metrics & Grafana link example .

---

## **6 Evaluation Mapping**

| **Rubric Criterion** | **Evidence in Task** |
| --- | --- |
| Functional 25 % | Endpoints create / amend / fetch orders. |
| Code Quality 20 % | Modular files, lint clean, type-safe. |
| Testing 15 % | Unit tests for happy & invalid cases. |
| Docs 10 % | README + auto OpenAPI. |
| Ownership 15 % | Metrics, structured logs. |
| Scalability 10 % | Storage & service layers separable. |
| Quant 5 % | Decimal accuracy, validation logic. |

(Gate ≥ 2/5 on Functional, Code, Tests; overall ≥ 3.0/5 = pass.)

---

## **7 Helpful Resources**

1. FastAPI testing tutorial (official)
2. FastAPI Pydantic schema examples
3. In-memory store discussion for FastAPI (#5045)
4. Prometheus-FastAPI-Instrumentator GitHub
5. Grafana+Prometheus monitoring guide
6. decimal module docs for money calc
7. responses / mocking requests pattern
8. CRUD tutorial video (patterns)
9. FastAPI OpenAPI models reference
10. FastAPI rate-limit thread-safety Q&A

---

**Reminder** – focus on clarity and tests; if you hit eight hours, commit TODOs for unfinished ideas and submit. We value thoughtful trade-offs over unfinished polish.