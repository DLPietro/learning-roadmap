### DAY 1: DOWNLOAD AND EXERCIZE ON FINANCIAL DATA

# MAIN GOALS
# Learning how to use Python's functions
# Calculating annualized returns from daily returns - Formula = (1 + Daily return)^252 - 1
# Applying the function to more Tickers


# Step 1: Installing & importaing Libraries (Yahoo Finance, Pandas)
!pip install yfinance pandas            # Installing both with a single command
import yfinance as yf, pandas as pd     # Importing them in a single row

# Step 2: Download last 60 days of at least 3 Tickers 
data = yf.download(['AAPL', 'MSFT', 'GOOGL'], period = '60d')      # Selected assets: Apple, Microsoft and Google for a peirod of 60 days
close_prices = list(data['Close']['GOOGL', 'AAPL', 'META'])              # Only Closing prices
print(close_prices[-1])                                             # Last prices available

### EXERCISE 1: CALCULATING DAILY RETURNS (AS AT DAY 1), ANNAUALISED RETURNS AND VOLATILITY USING A SINGLE FUNCTION
def calc_daily_returns(prices):                # Function for daily return calculation
  returns = []
  for i in prices:                             # The loop uses the formula to calculate the daily returns, comparing the percentage of the first with the previous one
    ret = (prices[i] / prices[i-1]) * 100      
    returns.append(round(ret, 2))

def calc_annualized_return(daily_returns):
  daily_return_avg = sum(daily_returns) / len(daily_returns)
  annualized_return = (1 + daily_return_avg) ** 252 - 1
  volatility = daily_returns.std()
  annualized_volatility = volatility * (252 * 0.5)
  return {
  "annualized_return": annualized_return,
  "annualized_volatility": annualized_volatility
}



