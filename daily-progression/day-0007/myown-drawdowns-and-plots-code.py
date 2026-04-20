import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = 'SPY'

data = yf.download(ticker, start='2020-01-01', end='2026-01-01', auto_adjust=True)

data.columns = data.columns.droplevel(1)

data['SMA_50'] = data['Close'].rolling(50).mean()
data['SMA_20'] = data['Close'].rolling(20).mean()
data['signal'] = np.where(data['SMA_20'] > data['SMA_50'], 1, 0)
data['position'] = data['signal'].shift(1)
data['daily_return'] = data['Close'].pct_change()

data['strategy_return'] = data['daily_return'] * data['position']

data['buyhold_equity'] = (1 + data['daily_return']).cumprod()
data['strategy_equity'] = (1 + data['strategy_return']).cumprod()


data['buyhold_peak'] = data['buyhold_equity'].cummax()
data['buyhold_dd'] = (data['buyhold_equity'] - data['buyhold_peak']) / data['buyhold_peak']
data['strategy_peak'] = data['strategy_equity'].cummax()
data['strategy_dd'] = (data['strategy_equity'] - data['strategy_peak']) / data['strategy_peak']

def summarize(name, equity, dd, daily_ret):
  total_return = equity.iloc[-1] - 1
  years = len(equity) / 252     
  cagr = (equity.iloc[-1] ** (1/years)) - 1    # Last line (last amount on account) ** (1/years) - 1 
  ann_vol = daily_ret.std() * np.sqrt(252)    # daily ret standard dev. * sqrt 252 to get annual.
  sharpe = (daily_ret.mean() * 252) / ann_vol     # mean daily ret / ann vol
  max_dd = dd.min()   # Finds min value
  calmar = cagr / abs(max_dd)    # cagr ratio / absolute value of max dd
  print(f"\n=== {name} ===")
  print(f"Total return:       {total_return:.2%}")
  print(f"CAGR:               {cagr:.2%}")      
  print(f"Annual Volatility:  {ann_vol:.2%}")
  print(f"Sharpe:             {sharpe:.2f}")    # risk-adjusted return of an investment
  print(f"Max Drawdown:       {max_dd:.2%}")    
  print(f"Calmar:             {calmar:.2f}")    # Pain dodged to missed returns ratio: is it worth the loss?


summarize("Buy & Hold", data['buyhold_equity'], data['buyhold_dd'], data['daily_return'])
summarize("SMA Crossover", data['strategy_equity'], data['strategy_dd'], data['strategy_return'])


fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

axes[0].plot(data.index, data['buyhold_equity'], label='Buy & Hold', color='steelblue')
axes[0].plot(data.index, data['strategy_equity'], label='Strategy', color='darkorange')
axes[0].set_title('Growth of $1')
axes[0].set_ylabel('Portfolio Value ($)')
axes[0].legend()   # Shows legend
axes[0].grid(True, alpha=0.3)      # Draws a grid. Faint, invisible.

axes[1].fill_between(data.index, data['buyhold_dd'], 0, color='steelblue', alpha=0.4, label='Buy & Hold DD')     # Fill between means that it will fill it between 2 things.
axes[1].fill_between(data.index, data['strategy_dd'], 0, color='darkorange', alpha=0.4, label='Strategy DD')
axes[1].set_title('Drawdown')
axes[1].set_ylabel('Drawdown %')
axes[1].legend()   
axes[1].grid(True, alpha=0.3)     

plt.tight_layout()   # auto adjusts spacing
plt.savefig('drawdown_chart.png', dpi=100)   # dots per inch
plt.show()
