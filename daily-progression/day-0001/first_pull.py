# before running had to do this: pip3 install yfinance 
# NOT in python but in the terminal.

import yfinance as yf        # import the library and name it yf instead of typing yfinance every time.

# define what we want
ticker = "SPY"
start_date, end_date = "2024-01-01", "2024-12-31" # I hope I didn't mess up the same-line notation lol.

# download the data
data = yf.download(ticker, start=start_date, end=end_date) #The notation is [ticker] then  start=[start date]  then  end=[end date]

# look at what we got
print(data)                      # print the entire table
print()                          # blank line
print(f"rows: {len(data)}")      # how many trading days because the length IS the number of days
print(f"columns: {list(data.columns)}") # Data.columbs is new. it's a property of the table that lists them. wrapping it in list() prints them cleanly. Can only use when there is "list"




# Here's what I got: 
#Price            Close        High         Low        Open     Volume
#Ticker             SPY         SPY         SPY         SPY        SPY
#Date                                                                 
#2024-01-02  459.991150  460.983851  457.888997  459.514283  123623700
#2024-01-03  456.234589  458.570304  455.631199  457.830650  103585900
#2024-01-04  454.765045  458.346478  454.541194  455.757716   84232200
#2024-01-05  455.387909  457.840406  453.937795  454.969403   86118900
#2024-01-08  461.889038  462.035015  455.757750  455.884273   74879100
#...                ...         ...         ...         ...        ...
#2024-12-23  586.186646  586.787909  579.257137  582.440993   57635800
#2024-12-24  592.702026  592.741493  586.955372  587.536963   33160100
#2024-12-26  592.741638  593.865292  589.528242  590.927921   41219100
#2024-12-27  586.502075  589.232487  582.312845  588.995868   64969300
#2024-12-30  579.809143  583.278831  576.053624  579.483905   56578800

#[251 rows x 5 columns]

#rows: 251
#columns: [('Close', 'SPY'), ('High', 'SPY'), ('Low', 'SPY'), ('Open', 'SPY'), ('Volume', 'SPY')]
