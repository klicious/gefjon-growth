# 📝  Take-Home Evaluation Sheet — Entry-Level Software Engineer
*Candidate:* __________________  *Evaluator:* __________________  *Date:* ___________

### 🔑 Quick Rules
1. **Time-box assumption:** Candidate invested ≤ 8 h ⇒ do **not** penalize absent pro-level extras.  
2. **Gate criteria:** Functional Correctness, Code Quality, Testing must each score ≥ 2/5.  
3. **Pass guideline:** Weighted ≥ 3.0 / 5 (60 %) ⇒ proceed. 3.0–3.4 = Lean Hire 3.5–4.4 = Hire ≥ 4.5 = Strong Hire.  
4. **Evidence requirement:** Any score ≤ 3 **or** any Red Flag ⇒ cite ≥ 1 code reference (`path/file.py:line`).  
5. **Bias guard:** Only deduct for items explicitly in this sheet. Missing observability, DI, etc. should **not** lower scores unless specified.

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
| **5** | All required flows + edge cases work; zero crashes; graceful errors. |
| **4** | Core flows solid; ≤ 2 minor bugs; sensible error messages. |
| **3** | Core works but ≥ 1 major feature missing **or** poor edge handling. |
| **2** | Multiple flows missing; crashes on invalid input. |
| **1** | Fails happy path or cannot run. |

**Check-List**  
- BitMEX **and** Binance APIs implemented?  
- SPOT, USD-M, USD-C markets supported?  
- BTC / ETH / SOL instruments tradable?  
- Handles test **vs.** prod endpoints?  
- Validates inputs & maps API errors?  

**Red Flags** ▢ Silent crash ▢ Hard-coded prod URL ▢ Wrong side/qty mapping  
**Green Flags** ▢ Idempotent retries ▢ Min/max sanity checks  

---

## 2️⃣ Code Quality & Best Practices *(Weight 20 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Idiomatic, modular; ≤ 15 cyclomatic complexity; secrets via env/SM; 0 `ruff` errors. |
| **4** | Readable, small funcs; minor style nits; secrets via env. |
| **3** | Mostly readable but long funcs (> 75 LOC) **or** mixed style. |
| **2** | Spaghetti, duplicated code, hard-coded creds. |
| **1** | Large blobs, global state abuse. |

**Check-List**  
- Consistent naming & PEP 8?  
- Separation of concerns (API vs domain)?  
- Type hints + `mypy --strict` pass?  
- No sensitive data committed?  

**Red Flags** ▢ `print` debugging left ▢ Credentials in repo  
**Green Flags** ▢ Pre-commit (`ruff` / `black`) ▢ Docstrings w/ examples  

---

## 3️⃣ Testing Approach & Coverage *(Weight 15 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Unit + ≥ 1 integration suite; coverage ≥ 60 %; mocks isolate APIs. |
| **4** | Good unit tests; coverage 45–59 %. |
| **3** | Happy-path tests only; coverage 25–44 %. |
| **2** | Sparse tests; coverage < 25 %. |
| **1** | No runnable tests. |

**Check-List**  
- `pytest` green?  
- Edge-case assertions?  
- Mocking external calls?  
- Coverage report?  

**Red Flags** ▢ Tests fail on clean clone ▢ Real API hits in tests  
**Green Flags** ▢ Parametrized edge tests ▢ Fixture/factory pattern  

---

## 4️⃣ Documentation *(Weight 10 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | README ≤ 400 wds: setup, CLI usage, env vars; arch diagram. |
| **4** | README clear; minor omissions. |
| **3** | Basic setup but unclear usage. |
| **2** | Minimal README; missing steps. |
| **1** | No docs. |

**Check-List**  
- Quick-start commands?  
- Env var table / `.env.example`?  
- Diagrams / flowcharts?  
- Troubleshooting FAQ?  

---

## 5️⃣ Ownership / Above-&-Beyond *(Weight 15 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Adds logging/metrics, config file, clear TODO roadmap, ADRs. |
| **4** | Implements 1–2 extras (retry / metrics). |
| **3** | Some thoughtful TODOs. |
| **2** | Little initiative. |
| **1** | None. |

**Red Flags** ▢ No extra thought ▢ Copy-paste configs  
**Green Flags** ▢ Structured logging ▢ Prometheus stub  

---

## 6️⃣ Scalability & Design Patterns *(Weight 10 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Clear `ExchangeClient` interface; Strategy/Factory; add new exchange ≤ 30 LOC. |
| **4** | Decent abstractions; some duplication. |
| **3** | Works but tightly coupled. |
| **2** | Copy-paste per exchange. |
| **1** | Monolithic. |

**Check-List**  
- Abstract base or protocol?  
- Symbol mapping dict?  
- Config-driven order types?  

---

## 7️⃣ Quantitative & Logical Reasoning *(Weight 5 %)*  
**Raw:** __/5  **Weighted:** ____

| Score | Anchor |
|:--:|---|
| **5** | Complexity analysis, numeric edge checks; math explained. |
| **4** | Correct, concise algorithms. |
| **3** | Straightforward logic. |
| **2** | Inefficient or naive. |
| **1** | Logical errors. |

---

## 8️⃣ Score Calculation  

| Criterion | Weight | Raw | Weighted |
|-----------|-------:|----:|---------:|
| Functional Correctness | 25 | | |
| Code Quality | 20 | | |
| Testing | 15 | | |
| Documentation | 10 | | |
| Ownership | 15 | | |
| Scalability | 10 | | |
| Quant Reasoning | 5 | | |
| **Total** | 100 | — | **__/5** |

---

## 9️⃣ Strengths
- …

## 🔟 Areas for Improvement
- …

## 1️⃣1️⃣ Alignment with Core Values
*(brief bullet mapping to “Ownership & Proactivity”, “Scalable Elegance”, etc.)*

---

## 1️⃣2️⃣ Next Steps
- [ ] Proceed to interview – Reason: __________  
- [ ] Consider for other role – Reason: __________  
- [ ] Do not proceed – Reason: __________  

> **Reminder:** Weighted score ≥ 3.0 **and** no gate < 2 ⇒ Lean Hire or above.