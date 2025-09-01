### DAY 4: PANDAS BASICS

# MAIN GOALS:
# 1) Creating a Dataframe with 3 assets with Close and Volume values of the last 60 days
# 2) Calculating daily returns using pandas, in a new column to add in the dataframe (using .pct_change())
# 3) Printing the first 10 values of the new column
# 4) Creating a new column with 7-day moving average

# Step 1: importing data and creatinga  dataset
# !pip install yfinance pandas     
import yfinance as yf, pandas as pd, numpy as np   # Importing them in a single row

tickers = ['IWM', 'GLD', 'IGOV']                                   # Defined tickets
data = yf.download(tickers, period = '60d')                        # Selected assets: Apple, Microsoft, and Google for a period of 60 days
close_prices = data['Close'][['IWM', 'GLD', 'IGOV']]               # Only Closing prices
volume = data['Volume'][['IWM', 'GLD', 'IGOV']]                    # Volume Column

print(f"Last Prices Available: {close_prices.iloc[-1]}")           # Print last prices available
print(f"Last Volumes Available: {volume.iloc[-1]}")                # Print Volume for Each Asset


# Step 2-3-4: daily returns and analysis with pandas
def calc_daily_returns(prices):
  """Calculate Daily Returns with pct_change()"""                               # Function for daily return calculation
  returns = prices.pct_change()                                                 # Function ready using pandas
  return returns

calc_daily_returns(close_prices).dropna().head(10)                              # Print frist 10 rows


### EXTRA STEP: GRAPH


import matplotlib.pyplot as plt

returns = calc_daily_returns(close_prices).dropna()
returns.plot(figsize=(10,6), title="Daily Returns of IWM, GLD, IGOV")
plt.show()
