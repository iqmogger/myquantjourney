# Day 0006 — Trading Signals & Boolean Logic

## What I Learned

### Terms / Concepts:
- **Signal** — A value (True/False or 1/0/-1) generated from data that tells you whether to be in a trade. The output of a trading rule.
- **Position** — What you currently hold in an asset. +1 = long (own it), 0 = flat (no exposure), -1 = short (bet against it). Can also be fractional (+0.5 = half capital deployed) or leveraged (+2 = borrowed money to double exposure).
- **Long** — You own the asset. You profit if it goes up.
- **Flat** — You hold nothing. No profit, no loss, sitting in cash.
- **Short** — You've borrowed and sold an asset, betting it will fall. Profit if it drops.
- **Leverage** — Using borrowed money to increase position size beyond your own capital. Amplifies both gains and losses.
- **Lookahead bias** — Using information in a backtest that wouldn't have been available at the time of the trade. The #1 amateur mistake. Causes backtests to show impossibly high returns.
- **Point-in-time data** — Historical data that only shows what was actually known at each past moment, not what we know now.
- **SMA (Simple Moving Average)** — The unweighted average of the last N closing prices. "Simple" distinguishes it from EMA (exponential) or WMA (weighted).
- **SMA crossover** — A classic trend-following strategy: be long when a fast SMA is above a slow SMA, flat otherwise.
- **Golden cross** — When a fast SMA crosses above a slow SMA (traditionally bullish).
- **Trend-following / momentum** — Strategies that bet current direction will continue. Assume that when prices are rising, they'll keep rising.
- **Cumulative return** — Total compounded return from the start of the period. Built by multiplying `(1 + daily_return)` values together.
- **Daily return** — Percentage change from one day's close to the next.
- **Win rate** — Percentage of trades that made money. Often 40–55% even for great strategies.
- **Expectancy** — Average dollars made per trade, averaged across winners and losers.
- **Regime change** — When market conditions shift and historical patterns stop working. Why quants obsess over robustness testing.
- **Overfitting** — Tuning parameters until the backtest looks great, but the strategy fails in live trading.
- **Market impact / slippage** — Price moves against you when you trade large positions. Matters for illiquid assets and massive orders.
- **MultiIndex columns** — Pandas columns with two or more levels of labels. yfinance returns these by default (Level 0 = field like Close/Open, Level 1 = ticker like AAPL).
- **`np.where()`** — Vectorized if/else. Takes a condition and two outputs; writes one value where True, another where False, across an entire Series.
- **`.shift(n)`** — Slides all values down by n rows. Essential for lining up signals with the day they actually control.
- **`.cumprod()`** — Cumulative product. Multiplies each value by all previous values to compound returns.
- **`.diff()`** — Difference between consecutive values. Used to detect when position changes (count trades).
- **`.iloc[]`** — Access rows by integer position (as opposed to `.loc[]` which uses labels). `.iloc[-1]` = last row.
- **`.droplevel(n)`** — Removes the nth level from a MultiIndex, flattening column labels.

### Coding:
- How to generate boolean Series from conditions across an entire DataFrame
- How to use `np.where()` to convert conditions into numerical positions (+1/0/-1)
- How to use `.shift(1)` to prevent lookahead bias in backtests
- How to build cumulative returns with `(1 + returns).cumprod()`
- How to extract final values with `.iloc[-1]`
- How to flatten yfinance's MultiIndex columns with `.droplevel(1)` (or bypass with `multi_level_index=False`)
- The full backtest pipeline: data → features → signal → position → shifted position × return → cumulative
- Why signal at close of day N controls position for day N+1
- How to count trade signals with `.diff() != 0`

## The Code
1 file: `signals.py`
Builds a complete SMA crossover backtest on SPY: downloads 5 years of data, computes fast/slow moving averages, generates a long/flat signal, shifts to avoid lookahead, calculates strategy returns, and compares performance vs buy-and-hold using total return and Sharpe ratio.

Optional bonus file: `signals_experiment.py`
Tests different SMA window combinations (10/30, 20/50, 50/200, etc.) to see which performs best — and confronts the overfitting trap head-on.

## Questions I Answered

**Q1: In your own words, what is lookahead bias and why does `.shift(1)` fix it?**
It's when it uses info it wouldn't have had at the time of the actual trade. Shift like shifts it so it doesn't know.

**Q2: What's the difference between a signal and a position?**
Signal tell it what to do, position is what position it takes. The context is backtesting.

**Q3: Why do we use `np.where()` instead of just using booleans directly?**
Because it has 3 possible outputs: 1, 0, -1. Booleans have 2. 3 outputs is better because then it tells you when to short and when to long.

**Q4: What does `.cumprod()` do to a Series of daily returns, and why does it compute total return?**
it multiplies each value by all the ones before it. Makes it easier to calculate total returns, aka "how much would a dollar be worth".

**Q5: Did your SMA crossover beat buy-and-hold on SPY? If not, why might a simple strategy underperform?**
No, probably because the strategy wasn't the best (very simple) and a lot happened between 2020 and 2025 (wars, crises, etc.) which might have affected it.

A strategy is just: data → signal → position → shifted position × return. Every backtest in existence — from my SMA crossover to Renaissance's Medallion Fund — follows this same skeleton. The math is easy; the discipline is in being honest about what information you actually had at each moment in time. Strategies don't predict the future — they bet on statistical tendencies continuing, and the job is to stay honest about whether they really will.
