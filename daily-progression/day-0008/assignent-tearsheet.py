import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_prices(ticker, start='2020-01-01', end='2026-01-01'):
  data = yf.download(ticker, start, end, auto_adjust=True)
  data.columns = data.columns.droplevel(1)
  data['Close']
  return data['Close']

def sma_backtest(prices):
  sma_fast = prices.rolling(20).mean()
  sma_slow = prices.rolling(50).mean()
  signal = np.where(sma_slow < sma_fast, 1, 0)
  signal = pd.Series(signal, index=prices.index)
  position = signal.shift(1)
  daily_ret = prices.pct_change()
  strat_returns = position * daily_ret
  return strat_returns, daily_ret

def calc_metrics(returns):
  equity = (1 + returns).cumprod()
  peak = equity.cummax()
  dd = (equity - peak) / peak
  years = len(equity) / 252
  cagr = (equity.iloc[-1] ** (1/years)) - 1     
  ann_vol = returns.std() * np.sqrt(252)      # uses returns
  sharpe = (returns.mean() * 252) / ann_vol       # uses returns
  max_dd = dd.min()       # uses dd
  calmar = cagr / abs(max_dd) if max_dd != 0 else 0       # uses cagr and max_dd
  return {
  'years' : years, 
  'cagr' : cagr,   
  'ann_vol' : ann_vol,   
  'sharpe' : sharpe,     
  'max_dd' : max_dd,
  'calmar' : calmar   
  }
    

def generate_tearsheet(tickers):
  all_results = {}
  strat_results= {}
  bh_results = {}
  for ticker in tickers:
    prices = get_prices(ticker)       
    strat_returns, bh_returns = sma_backtest(prices)  
    strat_results = calc_metrics(strat_returns)
    bh_results = calc_metrics(bh_returns)
    strat_results[ticker] = strat_metrics 
    bh_results[ticker] = bh_metrics
    all_results[ticker] = metrics       
# METRICS:
for ticker in tickers:
        print(f"Running backtest on {ticker}...")
        prices = get_prices(ticker)
        strat_returns, bh_returns = sma_backtest(prices)
        strat_metrics = calc_metrics(strat_returns)
        bh_metrics = calc_metrics(bh_returns)
        strat_results[ticker] = strat_metrics
        bh_results[ticker] = bh_metrics
        strat_curves[ticker] = (1 + strat_returns).cumprod()
        bh_curves[ticker] = (1 + bh_returns).cumprod()
 
    strat_df = pd.DataFrame.from_dict(strat_results, orient='index')
    bh_df = pd.DataFrame.from_dict(bh_results, orient='index')
 
    print("\n" + "=" * 60)
    print("SMA CROSSOVER (20/50) — STRATEGY RESULTS")
    print("=" * 60)
    print(strat_df.to_string())
 
    print("\n" + "=" * 60)
    print("BUY AND HOLD — BENCHMARK RESULTS")
    print("=" * 60)
    print(bh_df.to_string())
 
    fig, axes = plt.subplots(len(tickers), 1, figsize=(12, 4 * len(tickers)))
    if len(tickers) == 1:
        axes = [axes]
 
    for i, (ticker, ax) in enumerate(zip(tickers, axes)):
        strat_curves[ticker].plot(ax=ax, label="SMA 20/50", color="steelblue")
        bh_curves[ticker].plot(ax=ax, label="Buy & Hold", color="gray", alpha=0.7)
        ax.set_title(f"{ticker} — Equity Curves")
        ax.legend()
        ax.set_ylabel("Growth of $1")
 
    plt.tight_layout()
    plt.savefig("tearsheet.png", dpi=150)
    print("\nChart saved as tearsheet.png")
 
    return strat_df, bh_df
 
tickers = ["SPY", "QQQ", "IWM", "EFA"]
strat_df, bh_df = generate_tearsheet(tickers)
