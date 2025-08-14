### DAY 1: DOWNLOAD AND EXERCIZE ON FINANCIAL DATA
================
# MAIN GOALS
# Learning how to use Python's functions
# Calculating annualized returns from daily returns - Formula = (1 + Daily return)^252 - 1
# Applying the function to more Tickers
================

# Step 1: Installing & importaing Libraries (Yahoo Finance, Pandas)
!pip install yfinance, pandas            # Installing both with a single command
import yfinance as yf, pandas as pd      # Importing them in a single row

# Step 2: Download last 60 days of at least 3 Tickers 
data = yf.download('GOOGL', 'AAPL', 'META')      # Selected assets: Apple, Google and Meta
close_prices = list(data['Close'])               # Only Closing prices
print(close_prices[-1])                          # Last prices available

### EXERCISE 1: CALCULATING DAILY RETURNS (AS AT DAY 1) & ANNAUALISED RETURNS USING A SINGLE FORMULA
def calc_annualized_return(daily_returns):
  daily_returns = []
  for n in close_prices:
    ret = (close_prices[n] / close_prices[n-1]) * 100      # The loop uses the formula to calculate the daily returns, comparing the percentage of the first with the previous one
    daily_returns.append(round(ret, 2))
  for n in daily_returns:
    formula = ((1 + daily_returns) ** 252) - 1
  print(daily_returns[:5])

  
