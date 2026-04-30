# Day 0013 — Groupby, Resample & Time-Based Aggregation

## What I Learned
- .resample("ME") — groups time series into monthly buckets (also "W", "QE", "YE")
- .resample().last() vs .mean() — last gives end-of-period price, mean gives average
- .groupby(series.index.year) — groups data by any property of the index
- .groupby(series.index.month) — group by calendar month across all years
- .groupby(series.index.day_of_week) — group by weekday (0=Mon, 4=Fri)
- .groupby([grouper1, grouper2]) — group by multiple things at once
- .agg(["mean", "std", "min", "max"]) — compute multiple stats per group at once
- .apply(custom_function) — run your own function on each group
- .unstack() — pivot inner index level into columns (long → wide)
- .prod(axis=1) — multiply across columns (used for compounding returns)
- axis=0 means down rows, axis=1 means across columns
- (1 + returns).prod() - 1 — the correct way to compound returns
- plt.subplots(2, 2) — 2D grid of panels, accessed with axes[row, col]
- .bar() — bar chart (vs .plot() for line chart)
- .astype(str) — convert numbers to strings (useful for bar chart labels)
- range(start, stop, step) — range with a step size (every Nth item)
- list[::2] — slice with step, takes every 2nd item

## Finance Terms
- **Monthly returns** — percentage change between last trading days of consecutive months
- **Seasonality** — calendar-based patterns in returns (January effect, sell in May, day-of-week)
- **Compounding** — returns on returns; (1+r1)(1+r2)...-1 is more accurate than r1+r2+...
- **Regime analysis** — studying whether a strategy works across different market conditions/periods

## The Code
- resample_basics.py — .resample() with "ME", "W", "QE"; .last() vs .mean(); monthly returns
- groupby_basics.py — .groupby() by year, month, weekday; .items() iteration
- multi_agg.py — .agg() with multiple functions; .apply() with custom Sharpe function
- return_table.py — monthly return heatmap table with .unstack(); compounding with .prod()
- grouped_charts.py — 2×2 subplot grid; bar charts; grouped data visualization
- sector_calendar.py — self-built sector analysis with grouped bars and return tables (assignment)
