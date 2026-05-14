# Day 0014 — Merging, Joining & Combining DataFrames

## What I Learned
- pd.concat([df1, df2], axis=0) — stack rows (more dates, same columns)
- pd.concat([df1, df2], axis=1) — stack columns (more tickers, same dates)
- pd.concat() auto-aligns by index — mismatched rows get NaN
- .merge(other, on="key", how="...") — SQL-style join
- how="inner" — keep only rows in BOTH (default)
- how="left" — keep all left rows, NaN where right missing
- how="right" — keep all right rows, NaN where left missing
- how="outer" — keep all rows from either side
- left_index=True, right_index=True — merge on index instead of column
- suffixes=("_a", "_b") — disambiguate overlapping column names
- .join() — shortcut for index-based merge, defaults to left join
- pd.concat(dict_of_series, axis=1) — convert dict-of-DataFrames pattern into one wide DataFrame
- The canonical quant layout: rows=dates, columns=tickers

## Finance Terms
- **Spread (pairs trading)** — price difference between two related assets (e.g., KO − PEP)
- **Ratio (pairs trading)** — price ratio between two related assets, used when prices differ in scale
- **Factor data** — characteristics describing a security (momentum, value, quality, size) used to predict returns
- **Survivorship in merges** — when you inner-join on dates, you implicitly drop any asset that wasn't trading on a given day; can bias backtests

## The Code
- concat_basics.py — pd.concat() with axis=0 and axis=1; index auto-alignment
- merge_basics.py — all four how= types demonstrated on hand-built data
- date_merge.py — merging two assets with different trading calendars on date index
- pairs_setup.py — KO/PEP spread and ratio, saved to CSV (pairs trading prep)
- dict_to_df.py — converting dict pattern to wide DataFrame; average pairwise correlation
- factor_join.py — joining factor scores onto returns; sorting by score
