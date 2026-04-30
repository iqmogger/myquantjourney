# Day 0012 — Matplotlib Deep Dive: Subplots & Multi-Panel Charts

## What I Learned
- `fig, ax = plt.subplots()` — the proper way to create charts (fig = canvas, ax = chart area)
- `plt.subplots(rows, cols)` — creates multiple panels; returns a list of axes
- `figsize=(width, height)` — sets the figure size in inches
- `sharex=True` — makes panels share the same x-axis so dates align vertically
- `gridspec_kw={"height_ratios": [...]}` — controls relative panel heights
- `ax.plot()` vs `plt.plot()` — ax version targets a specific panel
- `ax.bar()` — bar charts (good for daily returns)
- `ax.hist(data, bins=N)` — histograms showing value distributions
- `ax.fill_between()` — shades area between two curves (used for drawdowns)
- `ax.axhline(y=...)` — horizontal reference line
- `ax.axvline(x=...)` — vertical reference line
- `ax.annotate(text, xy=..., xytext=..., arrowprops=...)` — labeled arrows pointing to data
- `ax.text(x, y, text, transform=ax.transAxes)` — text at chart-fraction coordinates
- `ax.legend()` — draws a legend; needs `label=` in plot calls
- `ax.grid(True, alpha=...)` — grid lines with transparency
- `plt.rcParams` — dictionary of global style defaults
- `alpha` — transparency (0 = invisible, 1 = solid)
- `color`, `linewidth`, `linestyle` — line appearance controls
- `:.1%` format specifier — displays as percentage with 1 decimal
- `.idxmin()` / `.idxmax()` — returns the index (date) of the min/max value
- `dpi=150` — dots per inch for saved images (higher = sharper)
- `plt.tight_layout()` — auto-adjusts spacing to prevent label cutoff

## Finance Terms
- **Distribution** — the pattern of how values are spread out; histograms visualize this
- **Tearsheet** — a one-page multi-panel summary of a strategy or asset's performance

## The Code
- `fig_and_ax.py` — basic fig/ax pattern, single chart with grid and styling
- `subplots.py` — two-panel chart (price + returns) with list comprehension coloring
- `tearsheet.py` — three-panel tearsheet: cumulative return, drawdown, rolling volatility
- `styling.py` — rcParams theme, legends, histograms, vertical reference lines
- `annotate.py` — annotating best/worst days with arrows, text placement
- `mini_tearsheet.py` — self-built 4-panel tearsheet (assignment)

## Questions

**Q1: Why does sharex=True matter for financial charts? What goes wrong without it?**
Without sharex, each panel has its own independent x-axis. That means March 2020 on the price chart might not line up vertically with March 2020 on the drawdown chart — you can't visually connect "the price dropped here" with "this is how deep the drawdown was." Shared axes keep everything aligned so your eyes can scan straight down across panels and see the same moment in time.

**Q2: When would you use a histogram instead of a time series line chart? Give a real example from quant work.**
A histogram when you care about the *shape* of the data rather than *when* things happened. For example, plotting the distribution of daily returns for SPY to check if returns are normally distributed or have fat tails. A line chart shows you returns over time (what happened on which day), but a histogram answers "how often does a 3% daily move happen?" — that's the question risk managers care about when sizing positions.

**Q3: You build a tearsheet where Panel 1 is cumulative return and Panel 4 is a histogram of returns. Should Panel 4 share the x-axis with the others? Why or why not?**
No. Panels 1–3 all have dates on the x-axis, so sharing makes sense — they're all time series. But a histogram's x-axis is return values (like -0.05 to +0.05), not dates. If you force it to share with date panels, the histogram breaks because it's trying to plot return buckets on a date axis. Panel 4 needs its own independent x-axis.

**Q4: Your chart has a drawdown that hits -33% in March 2020, but visually it looks small compared to a -15% drawdown in 2022. What setting might be causing this?**
The y-axis might be auto-scaling to the wrong range, or more likely the height_ratios are making the drawdown panel too short vertically. If the panel is squished, a -33% and -15% will look similar because there aren't enough pixels to show the difference. Fix it by giving the drawdown panel more height in the ratios, or by explicitly setting the y-axis limits with `ax.set_ylim()` so the scale is consistent and the -33% gets the visual weight it deserves.

**Q5: Why set matplotlib style with rcParams at the top of your script instead of styling each chart individually?**
Same reason you write functions (Day 5) instead of copy-pasting code — DRY (Don't Repeat Yourself). If you have 5 panels and you want the same font size, grid transparency, and background on all of them, setting rcParams once applies it everywhere. If you style each panel individually, you're writing the same 6 lines of styling code 5 times, and if you want to change the font size later, you have to change it in 5 places instead of 1.

## Reflection
Today was the jump from "I can make a chart" to "I can make a chart that actually communicates something." The fig/ax pattern and subplots give you real control — stacking panels with shared axes turns a bunch of separate charts into one coherent story. The biggest unlock was seeing how everything from previous days (cumulative returns, drawdowns, rolling volatility, list comprehensions for coloring) feeds directly into building a professional-looking tearsheet.
