# A dictionary where each VALUE is another dictionary
all_metrics = {
    "AAPL": {"sharpe": 1.2, "max_dd": -0.15, "cagr": 0.10},
    "GOOGL": {"sharpe": 0.9, "max_dd": -0.22, "cagr": 0.08},
    "MSFT": {"sharpe": 1.5, "max_dd": -0.12, "cagr": 0.14}
}

# First bracket gets the outer key, second bracket gets the inner key
print(all_metrics["AAPL"]["sharpe"])     # 1.2
print(all_metrics["MSFT"]["max_dd"])     # -0.12

import pandas as pd

# pd.DataFrame.from_dict() converts a nested dictionary into a DataFrame
# orient="index" means the outer keys (AAPL, GOOGL, MSFT) become row labels
df = pd.DataFrame.from_dict(all_metrics, orient="index")
print(df)

