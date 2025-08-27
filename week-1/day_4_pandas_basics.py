### DAY 4: PANDAS BASICS

# MAIN GOALS:
# Creating a Dataframe with Close and Volume values of the last 30 days
# Calculating daily returns using pandas, in a new column to add in the dataframe
# Printing the first 10 values of the new column
# Creating a new column with 7 days moving average

# Step 1: importing data and creating dataset
# !pip install yfinance pandas     
import yfinance as yf, pandas as pd

data = yf.download('AAPL', period = '30d')      # downloading lst 30 days of data
print(data.head())                              # print the first values

close_prices = data['Close']                    # select close column
print(close_prices.head())                      # print first values



