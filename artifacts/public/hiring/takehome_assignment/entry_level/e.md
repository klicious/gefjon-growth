## **1 Timeline & Submission**

| **Item** | **Requirement** |
| --- | --- |
| **Time-box** | **72 hours** from email receipt **or** until you hit **8 hours of effort**—stop and submit even if incomplete. |
| **Repo** | Private GitHub repo; add **klicious** as collaborator. |
| **Send** | Email **hr@dunamiscap.com** with repo URL, GitHub handle, and a TIME_SPENT.md (hh:mm log). |
| **Commits** | Push frequently with clear messages; branching optional but welcome. |

## **2 Tech Stack & Tooling**

- **Python 3.12** – install deps via uv pip install -r requirements.txt.
- **pandas** for aggregation .
- **decimal.Decimal** for monetary accuracy (avoid float drift) .
- **pytest** + parametrize for edge-case tests .
- **ruff / black** pre-commit hooks .

## **3 Functional Requirements**

| **#** | **Task** | **Detail / Reference** |
| --- | --- | --- |
| 1 | **Ingest blotter** | Read trades.json (array of {timestamp, symbol, qty, price} in ISO 8601 & Decimal-friendly strings). |
| 2 | **Risk snapshot** | Return dict {symbol: {"net_qty", "notional_usd", "avg_price"}}. Net qty = Σ qty; notional = Σ |
| 3 | **Edge-case rules** | • Unknown symbol → skip & WARN • Net qty = 0 → omit symbol • Stale trade (> 24 h) → flag in output list stale_trades. Guidance from industry Q&A on exposure calc. |
| 4 | **CLI** | python snapshot.py trades.json --as-md prints Markdown table. |
| 5 | **Precision** | All calcs must use Decimal with getcontext().prec = 10   . |

### **Stretch Goal (Ownership 15 %)**

- Produce a Markdown report grouped by **asset class** (e.g., BTC, ETH, SOL) with subtotal lines.

## **4 Non-Functional Requirements**

- **Modularity** – separate loader.py, calculator.py, cli.py.
- **Type safety** – full type hints; mypy --strict passes.
- **Logging** – INFO logs for file load, calc summary.
- **Test coverage ≥ 45 %** (junior benchmark) .
- **Performance** – handle 50 k trades in < 5 s on mid-tier laptop (pandas groupby is O(N) ).

## **5 Deliverables**

1. **Code** – runnable via python snapshot.py trades.json.
2. **Tests** – pytest -q green; include parametrised edge cases.
3. **README.md** – ≤ 400 words: setup, schema, CLI examples, sample output.
4. **TIME_SPENT.md** – honest hh:mm log.
5. **(Stretch)** – Markdown report with asset-class subtotals.

## **6 Evaluation Mapping (Enhanced Rubric)**

| **Criterion** | **Evidence in Task** |
| --- | --- |
| Functional 25 % | Accurate snapshot dict, edge-case handling. |
| Code Quality 20 % | Modular files, Decimal precision, lint clean. |
| Testing 15 % | Parametrised tests for zero-qty & stale trades. |
| Documentation 10 % | Clear README & schema diagram. |
| Ownership 15 % | Markdown report, structured logs. |
| Scalability 10 % | Separation of loader/calculator allows new data sources. |
| Quant 5 % | Weighted average price, Decimal math. |

(Gate ≥ 2/5 on Functional, Code, Tests; overall ≥ 3.0/5 = pass.)

## **7 Helpful Resources**

1. pandas groupby().sum() tutorial
2. Real Python GroupBy guide
3. Python decimal docs
4. Python float-vs-Decimal case study
5. Python floating-point pitfalls
6. Quant.SE thread on net exposure
7. Coding Finance tutorial on portfolio returns
8. SparkByExamples pandas groupby sum
9. Pytest parametrize article
10. LambdaTest coverage FAQ
11. Medium parametrize edge-tests
12. Crypto Data Download (sample candle & trade data)
13. CareerPlug 2024 Candidate Experience Report
14. Cronofy 2024 candidate expectations (drop-out stats)

---

**Remember:** clarity and correctness matter most. If you hit eight hours, commit TODOs for unfinished ideas and submit. Good luck!