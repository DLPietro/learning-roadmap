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

# Stock Data Fetcher for JDoodle - Compatible with Restricted Environments
# Uses built-in modules: urllib, json
# Retrieves last 30 days of AAPL stock data from Financial Modeling Prep (FMP) API

from urllib.request import urlopen
import json
from datetime import datetime, timedelta

# === CONFIGURATION ===
api_key = "8XhDNYPOwVWy04CbqbfEFkGpnFBl0BTi"  # Get a free key at https://financialmodelingprep.com/developer/docs/
symbol = "AAPL"                        # Stock symbol
period_days = 30                       # Number of days to fetch

# === BUILD THE API URL ===
url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?timeseries={period_days}&apikey={api_key}"

try:
    # Open URL and read response
    response = urlopen(url)
    data_json = response.read().decode('utf-8')  # Decode bytes to string
    data = json.loads(data_json)                 # Parse JSON

    # Check if data contains historical prices
    if 'historical' not i
        print("❌ Error: No historical data found.")
        print("💡 Check your API key or internet access.")
    else:
        historical = data['historical']  # Extract historical data list

        # Display header for the first 5 rows (like .head())
        print("📈 Historical Data (first 5 entries):")
        print(f"{'Date':<12} {'Open':<8} {'Close':<8} {'Volume':<12}")
        print("-" * 40)

        # List to store closing prices (equivalent to data['Close'])
        close_prices = []

        # Print first 5 days of data
        for i, day in enumerate(historical[:5]):
            date_str = day['date']
            open_price = round(day['open'], 2)
            close_price = round(day['close'], 2)
            volume = day['volume']
            print(f"{date_str:<12} {open_price:<8} {close_price:<8} {volume:<12}")
            # Save closing price
            close_prices.append(close_price)

        # Print all closing prices (first 5 as in original code)
        print("\n📉 Closing Prices (first 5):")
        print(close_prices[:5])

        # Optional: Basic statistics
        print(f"\n📊 Summary (last {len(close_prices)} days):")
        print(f"Highest Close: ${max(close_prices):.2f}")
        print(f"Lowest Close:  ${min(close_prices):.2f}")
        print(f"Average Close: ${sum(close_prices)/len(close_prices):.2f}")

except Exception as e:
    # Handle any error (no internet, invalid key, blocked request, etc.)
    print("❌ Execution Error:", str(e))
    print("💡 Possible causes:")
    print("   - Missing or invalid API key")
    print("   - Internet access disabled on this JDoodle script")
    print("   - API limit reached (free tier allows ~250 requests/day)")
