### Day 8 – Structuring the Dashboard
#    Create a reusable function to download data for selected tickers and period
#    Handle missing values (forward fill or drop)
#    Return a clean DataFrame as the basis for the dashboard


### 1) Preparatory Exercise - Creating a Simple Function


import matplotlib.pyplot as plt, pandas as pd, numpy as np


# Example: create a function that takes a list of numbers and returns their squares
def number_root(numbers):
    return [i**0.5 for i in numbers]

print(number_root([9, 25, 36, 10000]))
     

### 2) Main Task – Data Download & Cleaning

import yfinance as yf, pandas as pd, numpy as np, matplotlib.pyplot as plt

# Step 1: Define a function to download and clean data

def get_data(tickers, period="90d"):

    data = yf.download(tickers, period=period)
    close_prices = data["Close"]
    clean_data = close_prices.ffill()   # forward fill missing values

    return clean_data

# Step 2: Test the function
tickers = ["IWM", "GLD", "IGOV", "AAPL"]
prices = get_data(tickers, period="90d")

print(prices.head(4))


### 3) Consolidation Exercise - Managing NaN and Time Series Period

# Step 3: Create a function to managing NaN and time series Period

def get_customised_data(tickers, start, end, missing_method="ffill"):

    data = yf.download(tickers, start = start, end = end)
    close_prices = data["Close"]

    if missing_method == "ffill":
      clean_data = close_prices.ffill()   # forward fill missing values
    elif missing_method =="bfill":
      clean_data = close_prices.bfill()   # backward fill missing values
    elif missing_method == "drop":
      clean_data = close_prices.dropna()  # drop missing values
    else:
      raise ValueError("missing_method must be 'ffill', 'bfill' or 'drop'")
    return clean_data

# Step 4: Test the function
tickers = ["IWM", "GLD", "IGOV", "AAPL"]
prices = get_customised_data(
    tickers = tickers,
    start = "2025-01-01",
    end = "2025-03-01",
    missing_method = "bfill"
)

print(prices.tail(4))
