### Day 6 – Data Cleaning & Basic Stats with Pandas
#    Learn how to handle missing values in financial data
#    Practice descriptive statistics with pandas (.mean(), .std(), .describe())
#    Normalize data for easier comparison across assets


### 1) Preparatory Exercise - Using a Sample with missing values (NaN)

import pandas as pd, numpy as np

data_sample = {"Asset_1": [np.nan,140,135,142,np.nan],
               "Asset_2": [300,np.nan,310,308,307],
               "Asset_3": [451,455,453,452,450]
}

sample = pd.DataFrame(data_sample)
print("Original sample with Missing Values: \n", sample)

# 2 Alternative dataframes from the original one, filling missing data or removing them all
sample_filled = sample.fillna(method="ffill")
sample_dropped = sample.dropna()
print({"Sample with filled NaN": sample_filled,
       "Sample with dropped NaN": sample_dropped})



### 2) Main Task – Cleaning & Descriptive Stats on Financial Data

import yfinance as yf, pandas as pd, numpy as np                   # Importing them in a single row

# Step 1: Download closing price of the 3 tickers of the last 90 days
tickers = ['IWM', 'GLD', 'IGOV']                                   # Defined tickets
data = yf.download(tickers, period = '90d')                        # Selected Period = 90 days
close_prices = data['Close']

# Step 2: Check and fill missing values
print("Missing values per asset:\n", close_prices.isna().sum())
close_cleaned = close_prices.fillna(method = "ffill")

# Step 3: First Descriptive stats
print("\nDescriptive Statistics:\n", close_cleaned.describe())

# Step 4: Normalise values (starting from first Value = 100)
normalized = close_cleaned / close_cleaned.iloc[0] * 100
print("\nNormalized Prices:\n", normalized.head())


### 3) Consolidation exercise - Rolling Stats

rolling_mean = close_cleaned.rolling(window=30).mean()
rolling_std = close_cleaned.rolling(window=30).std()

print("\n30-Day Rolling Mean:\n", rolling_mean.tail())
print("\n30-Day Rolling Std:\n", rolling_std.tail())

### 4) Plot of normalised prices

import matplotlib.pyplot as plt

normalized.plot(figsize = (10, 6), title = "Comparison between normalised prices")
plt.show()
