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
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Top panel: equity curves
axes[0].plot(data.index, data['buyhold_equity'],  label='Buy & Hold', color='steelblue')
axes[0].plot(data.index, data['strategy_equity'], label='SMA Crossover', color='darkorange')
axes[0].set_title('Equity Curves')
axes[0].set_ylabel('Growth of $1')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Bottom panel: drawdowns (underwater curve)
axes[1].fill_between(data.index, data['buyhold_dd'],  0, color='steelblue',  alpha=0.4, label='Buy & Hold DD')
axes[1].fill_between(data.index, data['strategy_dd'], 0, color='darkorange', alpha=0.4, label='Strategy DD')
axes[1].set_title('Drawdowns (Underwater Curve)')
axes[1].set_ylabel('Drawdown')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('drawdown_chart.png', dpi=100)
plt.show()


# Written by Claude. I'll do something myself.
