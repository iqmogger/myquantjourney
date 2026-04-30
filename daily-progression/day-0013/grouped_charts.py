import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
close = df["Close"].squeeze()
returns = close.pct_change().dropna()

# ── Chart 1: Monthly average return — bar chart ──
monthly_avg = returns.groupby(returns.index.month).mean() * 21  # rough monthly
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
# 2 rows, 2 columns = 4 panels
# axes is now a 2D array:  axes[0, 0] = top-left, axes[0, 1] = top-right
#                           axes[1, 0] = bottom-left, axes[1, 1] = bottom-right

# ── Panel 1 (top-left): seasonality bar chart ──
colors = ["green" if x > 0 else "red" for x in monthly_avg]
# ^ list comprehension from Day 11! Green for positive, red for negative

axes[0, 0].bar(month_names, monthly_avg * 100, color=colors, alpha=0.8)
axes[0, 0].set_title("AAPL Average Monthly Return (%)")
axes[0, 0].set_ylabel("Return (%)")
axes[0, 0].axhline(y=0, color="black", linewidth=0.5)
axes[0, 0].grid(axis="y", alpha=0.3)

# ── Panel 2 (top-right): yearly Sharpe ──
def sharpe(r):
    if r.std() == 0:
        return 0.0
    return (r.mean() / r.std()) * np.sqrt(252)

yearly_sharpe = returns.groupby(returns.index.year).apply(sharpe)
sharpe_colors = ["green" if s > 0 else "red" for s in yearly_sharpe]

axes[0, 1].bar(yearly_sharpe.index.astype(str), yearly_sharpe, color=sharpe_colors, alpha=0.8)
axes[0, 1].set_title("AAPL Sharpe Ratio by Year")
axes[0, 1].set_ylabel("Sharpe")
axes[0, 1].axhline(y=0, color="black", linewidth=0.5)
axes[0, 1].grid(axis="y", alpha=0.3)

# ── Panel 3 (bottom-left): quarterly cumulative returns ──
quarterly_ret = close.resample("QE").last().pct_change().dropna()
q_labels = [f"{d.year}Q{d.quarter}" for d in quarterly_ret.index]
q_colors = ["green" if r > 0 else "red" for r in quarterly_ret]

axes[1, 0].bar(range(len(q_labels)), quarterly_ret * 100, color=q_colors, alpha=0.8)
axes[1, 0].set_title("AAPL Quarterly Returns (%)")
axes[1, 0].set_ylabel("Return (%)")
axes[1, 0].set_xticks(range(0, len(q_labels), 2))
axes[1, 0].set_xticklabels(q_labels[::2], rotation=45, fontsize=7)
axes[1, 0].axhline(y=0, color="black", linewidth=0.5)

# ── Panel 4 (bottom-right): day-of-week effect ──
dow_avg = returns.groupby(returns.index.day_of_week).mean() * 252  # annualized
day_labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]
dow_colors = ["green" if d > 0 else "red" for d in dow_avg]

axes[1, 1].bar(day_labels, dow_avg * 100, color=dow_colors, alpha=0.8)
axes[1, 1].set_title("AAPL Day-of-Week Effect (Annualized %)")
axes[1, 1].set_ylabel("Return (%)")
axes[1, 1].axhline(y=0, color="black", linewidth=0.5)
axes[1, 1].grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("grouped_analysis.png", dpi=150)
plt.show()
print("Saved grouped_analysis.png")
