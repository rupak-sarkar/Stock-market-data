import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Define the list of tickers
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"] # Customize this list

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
end_date = yesterday.strftime('%Y-%m-%d')
start_date = end_date

# Define the output CSV file
output_file = 'stock_data/historical_stock_data.csv'

# Check if file exists to determine if it's the first run
if os.path.exists(output_file):
    existing_data = pd.read_csv(output_file, index_col=0, parse_dates=True)
    # Find the last date with data
    last_date = existing_data.index.max().strftime('%Y-%m-%d')
    # Fetch data starting from the day after the last date
    start_date = (pd.to_datetime(last_date) + timedelta(days=1)).strftime('%Y-%m-%d')
    mode = 'a' # Append mode
    header = False # Don't write header again
else:
    existing_data = pd.DataFrame() # Empty dataframe for first run
    mode = 'w' # Write mode
    header = True # Write header

print(f"Fetching data from {start_date} to {end_date}")

# Fetch data for all tickers
all_data = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        data['Ticker'] = ticker
        all_data = pd.concat([all_data, data])

# Append new data to the CSV file
if not all_data.empty:
    all_data.to_csv(output_file, mode=mode, header=header)
    print(f"Successfully appended {len(all_data)} new rows.")
else:
    print("No new data to append.")
