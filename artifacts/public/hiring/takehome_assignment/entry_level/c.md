# **Moving-Average Crossover Back-tester**

## **1 Timeline & Submission**

| **Item** | **Requirement** |
| --- | --- |
| **Time-box** | **72 hours** from email receipt **or** once you reach **8 hours of effort**—stop and submit even if incomplete. (Aligns with best-practice candidate-experience findings). |
| **Repo** | Private GitHub repo; add **klicious** as collaborator. |
| **Send** | Email **hr@dunamiscap.com** with:• repo URL• GitHub handle• TIME_SPENT.md (hh:mm log). |
| **Commits** | Push frequently with descriptive messages; branching optional but encouraged. |

---

## **2 Tech Stack & Tooling**

- **Python 3.12** (install libs via uv pip install -r requirements.txt).
- Data wrangling: pandas.
- Numeric: numpy, decimal for P&L accuracy.
- Charts (optional): matplotlib.
- Testing: pytest, pytest-parametrize.
- Lint/format: ruff, black.
- No external APIs—work with local CSV.

---

## **3 Functional Requirements**

| **#** | **Task** | **Details / References** |
| --- | --- | --- |
| 1 | **Read candles CSV** | Format: timestamp,open,high,low,close,volume (1-minute bars). |
| 2 | **Compute 9/21 SMA** | Use simple moving averages per QuantStart example. |
| 3 | **Generate trades** | • **Long entry** when fast SMA crosses **above** slow.• **Flat** when fast crosses **below** slow. |
| 4 | **P&L calculation** | Running equity curve & final metrics: gross P&L, max drawdown, win %. Tutorial inspiration on P&L math. |
| 5 | **CLI outputs** | a) trades.csv blotter; b) summary.json with stats. |
| 6 | **Edge-case handling** | Missing candles, zero volume rows, duplicate timestamps must not crash. (Forum discussions highlight common pitfalls). |

### **Stretch Goal (Ownership 15 %)**

- Add a CLI flag --grid that runs a grid-search over (fast, slow) pairs (e.g., 5–30) and prints the top three Sharpe ratios. Optimisation guidance from Medium tutorial.

---

## **4 Non-Functional Requirements**

- **Modularity** – separate data_loader.py, strategy.py, backtester.py, cli.py.
- **Type-safety** – full type hints; mypy --strict clean.
- **Logging** – INFO logs for start/finish and key metrics.
- **Test coverage ≥ 45 %** (LambdaTest junior baseline).
- **Performance** – process 1-month (≈ 40 k rows) CSV in < 5 s on mid-tier laptop.

---

## **5 Deliverables**

1. **Code** – runnable via python cli.py --csv candles.csv.
2. **Tests** – pytest -q green; include parametrised tests for SMA crossover logic.
3. **README.md** – ≤ 400 words: setup, CLI examples, file specs, diagram optional.
4. **TIME_SPENT.md** – honest hh:mm log.
5. **(Stretch)** – grid-search optimisation results.

---

## **6 Evaluation Mapping**

| **Rubric Criterion** | **Evidence in Task** |
| --- | --- |
| Functional 25 % | Correct trade generation & P&L calc. |
| Code Quality 20 % | Modular files, typing, lint clean. |
| Testing 15 % | Unit tests for SMA calc & trade engine. |
| Docs 10 % | Clear README, schema diagram. |
| Ownership 15 % | Grid-search, logging, drawdown calc. |
| Scalability 10 % | Strategy/Backtester class separation. |
| Quant 5 % | Accurate P&L & drawdown maths. |

Gate ≥ 2/5 on Functional, Code, Tests; overall ≥ 3.0/5 (60 %) advances.

---

## **7 Helpful Resources**

1. QuantStart SMA crossover back-test in Python
2. Charles Schwab primer on moving-average crossovers
3. Vestinda 2024 back-testing best-practice guide
4. YouTube tutorial on P&L calculation in MA strategies
5. Medium guide to optimising MA parameters in Python
6. StackOverflow OHLC CSV handling thread
7. Reddit discussion on back-testing lessons learned (edge cases)
8. TrendSpider learning-center article on MA crossover variants
9. Investopedia primer on MACD (context for crossovers)
10. Wall Street Journal piece on back-testing pitfalls (good to mention in README)

---

### **Final Note**

Focus on **clarity, correctness, and testability**—if you hit eight hours, add TODO comments for unfinished ideas and submit. Good luck!