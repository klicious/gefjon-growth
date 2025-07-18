# 📝  1-Week Take-Home Evaluation Sheet — Entry-Level SWE
*Candidate:* __________________  *Evaluator:* __________________  *Date:* ___________

### 🕒 Context & Quick Rules
1. **Scope & Effort**: Candidate was allotted **7 calendar days**; typical effort ≈ 15 h. Expect broader feature coverage than the 72-h tasks.  
2. **Gate Criteria**: Functional Correctness, Code Quality, and Testing must each score ≥ 2/5.  
3. **Pass Guideline**: Weighted ≥ 3.0 / 5 (60 %) → proceed. 3.0 – 3.4 = Lean Hire 3.5 – 4.4 = Hire ≥ 4.5 = Strong Hire.  
4. **Evidence Rule**: Any score ≤ 3 **or** any Red Flag ⇒ cite ≥ 1 code reference (`path/file.py:line`).  
5. **Bias Guard**: Deduct **only** for items explicitly in this sheet; missing senior-only concerns (K8s, DI, micro-services) should **not** affect scores.

---

## 0️⃣ Overall Recommendation
- [ ] **Strong Hire** (≥ 4.5)  
- [ ] **Hire** (3.5 – 4.4)  
- [ ] **Lean Hire** (3.0 – 3.4)  
- [ ] **No Hire** (< 3.0)

---

## 1️⃣ Functional Correctness & Completeness *(Weight 25 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor (behaviour) |
|:--:|---|
| **5** | All required BitMEX & Binance endpoints implemented (get/list, place, amend, cancel); works on **test & prod**; supports SPOT + USD-M + USD-C for BTC/ETH/SOL; graceful errors. |
| **4** | 90 % of endpoints work; minor feature or market missing; sensible error handling. |
| **3** | Core (place, list, cancel) work on both exchanges; gaps in amend or one market type. |
| **2** | Multiple required flows missing or crash on invalid input. |
| **1** | Cannot place or fetch orders reliably. |

**Check-List**  
- BitMEX **and** Binance?  
- `GET /orders` filters (IDs, date range, state)?  
- Both market & limit orders?  
- Amend qty/price works?  
- Test vs prod base-URL switch?  
- Error mapping (HTTP 4xx/5xx)?

**Red Flags** ▢ Silent crash ▢ Hard-coded prod keys ▢ Wrong symbol mapping  
**Green Flags** ▢ Idempotent retries ▢ Pagination support  

---

## 2️⃣ Code Quality & Best Practices *(Weight 20 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Idiomatic, modular; SOLID; secrets via env/SM; 0 `ruff` errors; cyclomatic complexity ≤ 15. |
| **4** | Readable; small functions; minor style nits; secrets via env. |
| **3** | Mostly readable but long functions (> 75 LOC) or mixed styles. |
| **2** | Spaghetti, duplication, hard-coded creds. |
| **1** | Monolithic blobs, global state abuse. |

**Check-List**  
- Separation of concerns (`exchange_client`, `order_service`)?  
- Consistent naming & PEP 8?  
- Type hints + `mypy --strict` clean?  
- No sensitive data committed?

**Red Flags** ▢ `print` debugging in prod path ▢ Credentials in repo  
**Green Flags** ▢ Pre-commit (`ruff`, `black`) ▢ Docstrings with examples  

---

## 3️⃣ Testing Approach & Coverage *(Weight 15 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Unit + ≥ 1 integration suite; coverage ≥ 60 %; mocks isolate APIs; regression fails captured. |
| **4** | Good unit tests; coverage 45–59 %. |
| **3** | Happy-path tests only; 25–44 % coverage. |
| **2** | Sparse tests; < 25 % coverage. |
| **1** | No runnable tests. |

**Check-List**  
- `pytest -q` green?  
- Edge-case assertions?  
- `responses` / `httpx_mock` used?  
- Coverage report?

**Red Flags** ▢ Tests hit live API ▢ Failing test suite  
**Green Flags** ▢ Parametrised edge tests ▢ Factory fixtures  

---

## 4️⃣ Documentation *(Weight 10 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | README ≤ 600 wds: setup, env vars table, repo map, rich usage examples, flow diagram. |
| **4** | README clear; minor omissions. |
| **3** | Basic setup & usage; unclear structure. |
| **2** | Minimal README; missing steps. |
| **1** | No docs. |

**Check-List**  
- Quick-start commands?  
- Env var table / `.env.example`?  
- Sequence / architecture diagram?  
- Troubleshooting FAQ?

---

## 5️⃣ Ownership / Above-&-Beyond *(Weight 15 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Adds logging, metrics, config file; clear TODO roadmap; ADRs; basic CI workflow. |
| **4** | Implements 1–2 extras (structured logs, retry policy). |
| **3** | Some thoughtful TODOs; minor extras. |
| **2** | Little initiative. |
| **1** | None. |

**Red Flags** ▢ No extra thought ▢ Copied sample code w/o changes  
**Green Flags** ▢ Structured logging ▢ Prometheus stub ▢ GitHub CI yaml  

---

## 6️⃣ Scalability & Design Patterns *(Weight 10 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Clear `ExchangeClient`/`OrderService` interfaces; Strategy/Factory; add new exchange ≤ 50 LOC. |
| **4** | Decent abstractions; minor duplication. |
| **3** | Works but tightly coupled; copy-paste in places. |
| **2** | Copy-paste per exchange everywhere. |
| **1** | Monolithic, rigid. |

**Check-List**  
- Interface or ABC for exchanges?  
- Symbol mapping dictionary?  
- Config-driven order types?

---

## 7️⃣ Quantitative & Logical Reasoning *(Weight 5 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Robust param validation; numeric edge checks; clearly explains any math (price tick, qty step). |
| **4** | Correct calculations; concise algorithms. |
| **3** | Straightforward logic. |
| **2** | Inefficient or naive loops; magic numbers. |
| **1** | Logical errors or wrong price/qty handling. |

---

## 8️⃣ Agentic Thinking & Future Potential *(Weight 10%)*
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Proactively identifies opportunities for automation or agent-based solutions in their documentation. Code is structured in a way that would facilitate future agent integration. |
| **4** | Demonstrates a clear understanding of how their solution could be extended or automated. |
| **3** | Shows some awareness of the broader system and potential for future improvements. |
| **2** | Code is functional but shows little consideration for future development or automation. |
| **1** | No evidence of forward-thinking or consideration of the broader system. |

---

## 9️⃣ Score Calculation  

| Criterion | Weight | Raw | Weighted |
|-----------|-------:|----:|---------:|
| Functional Correctness | 25 | | |
| Code Quality | 20 | | |
| Testing | 15 | | |
| Documentation | 10 | | |
| Ownership | 15 | | |
| Scalability | 10 | | |
| Quant Reasoning | 5 | | |
| Agentic Thinking | 10 | | |
| **Total** | 100 | — | **__/5** |

---

## 1️⃣0️⃣ Strengths
- …

## 1️⃣1️⃣ Areas for Improvement
- …

## 1️⃣2️⃣ Alignment with Core Values
*(brief mapping to “Technical Excellence”, “Ownership & Proactivity”, “Scalable Elegance”, etc.)*

---

## 1️⃣3️⃣ Next Steps
- [ ] Proceed to interview – Reason: __________  
- [ ] Keep in pipeline for other role – Reason: __________  
- [ ] Do not proceed – Reason: __________  

> **Reminder:** Weighted score ≥ 3.0 / 5 and no gate < 2 ⇒ Lean Hire or above.