### DAY 4: PANDAS BASICS

# MAIN GOALS:
# 1) Creating a Dataframe with 3 assets with Close and Volume values of the last 60 days
# 2) Calculating daily returns using pandas, in a new column to add in the dataframe (using .pct_change())
# 3) Printing the first 10 values of the new column
# 4) Creating a new column with 7 days moving average

# Step 1: importing data and creating dataset
# !pip install yfinance pandas     
import yfinance as yf, pandas as pd, numpy as np

tickers = ['IWM', 'GLD', 'IGOV']                      # Defined tickets
data = yf.download(tickers, period = '60d')           # downloading lst 60 days of data
print(data.head())                                    # print the first values
new_data = data['Close', 'Volume'][tickers]           # select close column
print(new_data.head())                                # print first 5 rows of prices and market volumes values

# Step 2-3-4: daily returns and analysis with pandas
def analyse_returns(new_data, close_prices):
    returns = new_data['Close'].pct_change()          # Function for daily returns from pandas
    returns = returns.dropna()                        # remove first NaN value
    avg_daily_return = returns.mean()                 # Average daily return
    daily_volatility = returns.std()                           # Volatily
    annualized_return = (1 + avg_daily_return) ** 252 -1       # Annlualized return
    annualized_volatility = daily_volatility * np.sqrt(252)    # Annlualized volatility
    moving_average = new_data['Close'].rolling(window = 7).mean()                                      # Moving Average (7 days)
    # Results Dictionary
    results = {
        'Annualized Return': round(annualized_return, 4),
        'Annualized Volatility': round(annualized_volatility, 4)
    }
    # Print Output
    print(results)
    print({'Daily Returns': returns.head(10)})
    print({'Moving Average 7-Days': moving_average.head(10)})
    
    return returns, results, moving_average
    
