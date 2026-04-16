# Day 0005 — Functions: Building Reusable Tools

## What I Learned

### Terms / Concepts:
- **Function** — A named, reusable block of code. You define it once with `def`, then call it whenever you need it.
- **Parameter (argument)** — A placeholder variable inside the parentheses of `def`. Gets filled in when you call the function.
- **`return`** — How a function sends a value back to whoever called it. Without it, the function gives back `None`.
- **Default parameter** — A parameter with a pre-set value (like `risk_free_annual=0.04`). You can override it or leave it as-is.
- **Tuple** — A group of values separated by commas. Used when a function returns multiple things at once.
- **Unpacking** — Assigning multiple returned values to multiple variables in one line (e.g., `v, s, best, worst = analyze_stock(returns)`).
- **Boolean** — A data type with only two values: `True` or `False`. Used for on/off switches in code.
- **`if` conditional** — Runs a block of code only when a condition is `True`. Skips it otherwise.
- **`for` loop** — Repeats code once for each item in a list. The loop variable changes each time.
- **Alpha** — The return earned above the market benchmark. If SPY returns 10% and your strategy returns 15%, alpha is 5%. Sharpe measures risk-adjusted return; alpha measures how much you beat the market.
- **`.squeeze()`** — Converts a single-column DataFrame into a Series. Fixes formatting issues caused by yfinance's multi-level columns.
- **`.max()` / `.min()`** — Pandas methods that find the largest/smallest value in a Series.

### Coding:
- How to define functions with `def`, parameters, and `return`
- How to use default parameters to make functions flexible
- How to return multiple values from a function and unpack them
- How to use `if` conditionals with boolean switches
- How to use `for` loops to iterate through a list of tickers
- Why you must save function outputs with `=` (otherwise the result disappears)
- Why `return` inside a loop exits the entire function on the first iteration
- Consistent function naming (typo in `def` vs call = `NameError`)

## The Code
1 file: `toolkit.py`

Defines reusable functions for downloading returns, calculating Sharpe ratio, calculating volatility, and comparing multiple stocks in a loop.

## Questions I Answered

**Q1: What's the difference between defining a function and calling it?**
[Your answer here]

**Q2: Why is `return` important? What happens if you forget it?**
[Your answer here]

**Q3: What's a default parameter and when would you use one?**
[Your answer here]

**Q4: What is alpha? How is it different from Sharpe ratio?**
[Your answer here]

**Q5: In your `compare_stocks` function, what does the `for` loop do?**
[Your answer here]

## Key Takeaway
Functions turn repeated code into reusable tools. Define once, call anywhere. This is how real quant codebases are organized — small, focused functions that combine into powerful analysis pipelines.
