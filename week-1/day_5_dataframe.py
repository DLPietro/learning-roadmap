### Day 5: Pandas Basics: DataFrame & Operations
#    Downloading data and tickers for 60 days
#    Creating dataframes with Close and Volume values.
#    Calculationg new column Daily Return using pct_change() from pandas.
#    Print first 10 rows of the new column
#    Plot daily returns and moving average


# Step 1 - Importing libraries and downloading data
import yfinance as yf, pandas as pd, numpy as np, matplotlib.pyplot as plt

tickers = ['IWM', 'GLD', 'IGOV']
data = yf.download(tickers, period="60d")

print(data[['Close', 'Volume']].tail())                       # A way to print 2 different columns in a single row


# Step 2 - Selecting closing prices, volumes, and adding returns to the , calculating moving average as well
close = data['Close']
volume = data['Volume']

returns = close.pct_change().dropna()
mov_avg = close.rolling(window = 7).mean()
std = close.rolling(window = 7).std()

analysis = close.copy()
analysis[["IWM_return", "GLD_return", "IGOV_return"]] = returns[["IWM", "GLD", "IGOV"]]
analysis[["IWM_avg", "GLD_avg", "IGOV_avg"]] = mov_avg[["IWM", "GLD", "IGOV"]]
analysis[["IWM_std", "GLD_std", "IGOV_std"]] = std[["IWM", "GLD", "IGOV"]]

print(analysis.head(10))


# Step 3: Plots showing daily returns and moving averages

returns.plot(figsize=(10,6), title="Daily Returns of IWM, GLD, IGOV")
plt.show()

mov_avg.plot(figsize=(10,6), title="7-Day Moving Average and Volatiliy")
std.plot(ax=plt.gca())                                                    #to add in the same graph
plt.show()
