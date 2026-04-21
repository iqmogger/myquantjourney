# Day 0009 — Statistical Significance

## What I Learned
- try/except: catch errors without crashing the script
- continue: skip to the next loop iteration
- T-stat: mean / (std / sqrt(N)); tells you if a return is real or noise
- Rule of thumb: |t| >= 3 to trust a strategy
- Rolling Sharpe: Sharpe over a moving window, shows if performance is stable
- np.sqrt() for square roots

## The Code
- try_except demo
- t_stat calc on SPY
- rolling sharpe on SPY
- evaluate(): full stats table across multiple tickers

## Questions

**Q1: What's the difference between a high Sharpe and a high t-stat?**
Sharpe is return-to-risk. T-stat is confidence the return isn't noise. A strategy 
with Sharpe 2.0 on 2 months of data has a low t-stat (not enough samples). A 
strategy with Sharpe 0.5 on 30 years has a high t-stat. Rough link: t ≈ Sharpe * sqrt(years).

**Q2: Why use try/except in the evaluator instead of letting it crash?**
In real quant code, tickers get delisted, APIs rate-limit, data goes missing. 
If one bad ticker crashes the loop, you lose all the other results. try/except + 
continue lets the script skip the broken one and finish the rest.

**Q3: Rolling Sharpe is 2.5 from 2015-2019 and -0.3 from 2020-2024. Deploy it?**
No. The edge is dead. The overall Sharpe averages the two periods and looks 
okay, but that's hiding the fact that the strategy stopped working. Trading it 
now means betting the old regime comes back — expensive bet.

**Q4: Your tearsheet shows NVDA has the highest Sharpe AND highest t-stat. 
Does that mean it's the best strategy to deploy?**
Not necessarily — those are returns from *holding* NVDA, not from a strategy. 
And it's one stock over one specific period during an AI boom. Past performance 
on a single asset says nothing about whether buying NVDA NOW will keep working.

## Reflection
Today was the shift from "build a backtest" to "decide if the backtest means 
anything." T-stat is the question I should ask before anything else — a 
good-looking Sharpe on a short backtest is basically worthless.
