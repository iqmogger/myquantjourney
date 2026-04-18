import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt    # plot thing. 

# ---- 1. Download data ----
data = yf.download('SPY', start='2020-01-01', end='2026-01-01', auto_adjust=True)
data.columns = data.columns.droplevel(1)
data = data[['Close']].copy()

# ---- 2. Build the Day 6 strategy ----
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['signal'] = np.where(data['SMA_20'] > data['SMA_50'], 1, 0)
data['position'] = data['signal'].shift(1)
data['daily_return'] = data['Close'].pct_change()
data['strategy_return'] = data['position'] * data['daily_return']

# ---- 3. Build equity curves ----
data['buyhold_equity']  = (1 + data['daily_return']).cumprod()
data['strategy_equity'] = (1 + data['strategy_return']).cumprod()

# ---- 4. Calculate drawdowns for both ----
data['buyhold_peak']     = data['buyhold_equity'].cummax()
data['buyhold_dd']       = (data['buyhold_equity'] - data['buyhold_peak']) / data['buyhold_peak']

data['strategy_peak']    = data['strategy_equity'].cummax()
data['strategy_dd']      = (data['strategy_equity'] - data['strategy_peak']) / data['strategy_peak']

# ---- 5. Summary metrics ----
def summarize(name, equity, dd, daily_ret):
    total_return = equity.iloc[-1] - 1
    n_years = len(equity) / 252
    cagr = (equity.iloc[-1]) ** (1 / n_years) - 1
    ann_vol = daily_ret.std() * np.sqrt(252)
    sharpe = (daily_ret.mean() * 252) / ann_vol
    max_dd = dd.min()
    calmar = cagr / abs(max_dd)

    print(f"\n=== {name} ===")
    print(f"Total return:  {total_return:.2%}")
    print(f"CAGR:          {cagr:.2%}")
    print(f"Ann. vol:      {ann_vol:.2%}")
    print(f"Sharpe:        {sharpe:.2f}")
    print(f"Max drawdown:  {max_dd:.2%}")
    print(f"Calmar ratio:  {calmar:.2f}")

summarize("Buy & Hold",    data['buyhold_equity'],  data['buyhold_dd'],  data['daily_return'])
summarize("SMA Crossover", data['strategy_equity'], data['strategy_dd'], data['strategy_return'])

# ---- 6. Chart it ----
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)        # figsize=(12, 8) is the size in inches, 12 wide × 8 tall
# sharex=True means both panels share the same x-axis (the dates line up)
#plt.subplots(2, 1) means "make a figure with 2 rows and 1 column of panels"

#So axes[0].plot(...) means "draw a line on the top panel" and axes[1].plot(...) means "draw on the bottom panel."

# Top panel: equity curves
axes[0].plot(data.index, data['buyhold_equity'],  label='Buy & Hold', color='steelblue')     # When you make a chart with multiple panels (like a top chart and a bottom chart stacked), each panel is called an "axes"
axes[0].plot(data.index, data['strategy_equity'], label='SMA Crossover', color='darkorange')
axes[0].set_title('Equity Curves')
axes[0].set_ylabel('Growth of $1')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
#.grid(True, alpha=0.3) — Adds faint gridlines. alpha is transparency, 0.3 = 30% opaque (faint).

# Bottom panel: drawdowns (underwater curve)
axes[1].fill_between(data.index, data['buyhold_dd'],  0, color='steelblue',  alpha=0.4, label='Buy & Hold DD')
axes[1].fill_between(data.index, data['strategy_dd'], 0, color='darkorange', alpha=0.4, label='Strategy DD')
#.fill_between(x, y, 0)  Shades the area between the line and zero. Perfect for drawdowns because drawdowns are always negative, so it fills downward from zero.
axes[1].set_title('Drawdowns (Underwater Curve)')
axes[1].set_ylabel('Drawdown')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('drawdown_chart.png', dpi=100)
plt.show() #Actually displays the chart on screen.

#Saves the chart as a PNG file. dpi=100 is the resolution (dots per inch). Higher = sharper but bigger file.


#Equity — The value of your account. If you started with $1 and it's now $1.47, your equity is $1.47.
#Equity curve — The line showing equity over time. Just a chart of "how much is my money worth each day."

#CAGR (Compound Annual Growth Rate) — Your annualized return, accounting for compounding. 
#If you turned $1 into $2 over 5 years, your CAGR isn't 20% per year — 
#it's about 14.87%, because 1.1487 × 1.1487 × 1.1487 × 1.1487 × 1.1487 ≈ 2. 
#It's the "steady yearly rate that would get you from start to end if it compounded."

#Calmar ratio — CAGR divided by the absolute value of max drawdown. Measures "return per unit of pain."
#Calmar of 0.5 = you earn 0.5% per year for every 1% of max drawdown → mediocre
#Calmar of 2.0 = you earn 2% per year for every 1% of max drawdown → excellent

# Written by Claude. I'll do something myself.
