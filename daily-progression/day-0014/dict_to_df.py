# Both DataFrames have a "close" column
spy_data = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=5),
    "close": [470, 472, 475, 473, 478],
    "volume": [1e8, 1.1e8, 1.2e8, 1e8, 1.3e8]
})

qqq_data = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=5),
    "close": [400, 401, 405, 403, 410],
    "volume": [8e7, 8.5e7, 9e7, 8.2e7, 9.5e7]
})

# Default suffixes are _x and _y — usually unhelpful
merged_bad = spy_data.merge(qqq_data, on="date")
# columns: close_x, volume_x, close_y, volume_y  ← gross

# Specify suffixes explicitly
merged = spy_data.merge(qqq_data, on="date", suffixes=("_spy", "_qqq"))
# columns: close_spy, volume_spy, close_qqq, volume_qqq  ← clean
