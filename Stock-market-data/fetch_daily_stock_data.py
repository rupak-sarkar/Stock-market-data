import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Define the list of tickers
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
date_str = yesterday.strftime('%Y-%m-%d')

# Define the output directory and file name
output_dir = 'stock_data'
output_file = os.path.join(output_dir, f'historical_stock_data_{date_str}.csv')

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Fetch data for all tickers
print(f"Fetching data for {date_str}")
all_data = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=date_str, end=date_str)
    if not data.empty:
        data['Ticker'] = ticker
        all_data = pd.concat([all_data, data])

# Save the data to a new CSV file
if not all_data.empty:
    all_data.to_csv(output_file)
    print(f"Successfully saved {len(all_data)} rows to {output_file}.")
else:
    print("No data fetched for the specified date.")
