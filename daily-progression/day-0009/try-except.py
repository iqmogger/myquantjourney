try:
    x = 10 / 0
except:
    print("oops, moving on")
    x = 0

for ticker in ["AAPL", "FAKE123", "MSFT"]:
    try:
        data = yf.download(ticker, progress=False)
        if data.empty:
            continue
        print(f"{ticker} loaded")
    except:
        print(f"{ticker} failed")

  #skips to the next loop iteration without stopping the loop.
