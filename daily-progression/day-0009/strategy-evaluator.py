import numpy as np
import pandas as pd
import yfinance as yf

def evaluate(tickers, start="2020-01-01", end="2025-01-01"):
    results = {}

    for ticker in tickers:
        try:
            df = yf.download(ticker, start=start, end=end,
                             auto_adjust=True, progress=False)
            if df.empty:
                continue
            r = df["Close"].pct_change().dropna().squeeze()
        except:
            print(f"{ticker} failed")
            continue

        ann_return = r.mean() * 252
        ann_vol    = r.std() * np.sqrt(252)
        sharpe     = (r.mean() / r.std()) * np.sqrt(252)
        t_stat     = r.mean() / (r.std() / np.sqrt(len(r)))

        equity = (1 + r).cumprod()
        max_dd = ((equity - equity.cummax()) / equity.cummax()).min()

        results[ticker] = {
            "Ann Return": ann_return,
            "Ann Vol":    ann_vol,
            "Sharpe":     sharpe,
            "T-Stat":     t_stat,
            "Max DD":     max_dd,
        }

    return pd.DataFrame.from_dict(results, orient="index").round(3)

table = evaluate(["AAPL", "MSFT", "NVDA", "TLT", "GLD"])
print(table)
