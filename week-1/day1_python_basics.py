### DAY 1: DOWNLOAD AND EXERCIZE ON FINANCIAL DATA
# MAIN GOALS
# Understanding data types, and first approach

# Step 1: Importing Yahoo Finance
#!pip install yfinance pandas         # Command to download the Yahoo Finance and Pandas library tool
import yfinance as yf, pandas as pd      # import the library to be used on the script


# Step 2: Download last 30 days of APPL Inc. Stock
ticker = 'AAPL'                                 # Apple ticker selected
data = yf.download(ticker, period = '30d')      # Select Asset and period
close_prices = data['Close']                  # Closing prince selected
print(close_prices[:4])                       # Showing the first 5 rows / daily prices of the stock

### EXERCISE 1: SAVING PRICES AND PRINT FIRST STATS
min_price = close_prices.min()                     # Calculatin min, max and mean price
max_price = close_prices.max()
avg_price = close_prices.mean()
std_price = close_prices.std()

stats = {"Ticker": ticker,
          "Min": min_price,
          "Max": max_price,
          "Average": avg_price,
          "Standard Deviation": std_price}
print(stats)

### EXERCISE 2: COMPUTING DAILY RETURNS OF THE ASSET
daily_returns = []
for i in range(1, len(close_prices)):
  today = close_prices.iloc[i]
  yesterday = close_prices.iloc[i-1]
  ret = (((today - yesterday) / yesterday) * 100)
  daily_returns.append(round(ret, 2))

print('Daily Returns', daily_returns[:5])              # It shows the result of the first 5 values

print('Daily Returns', daily_returns[:5])              # It shows the result of the first 5 values
