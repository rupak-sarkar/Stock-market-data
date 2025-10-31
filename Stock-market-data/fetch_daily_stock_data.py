import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Define the list of tickers
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
date_str = yesterday.strftime('%Y-%m-%d')

# Define the output file name
output_file = 'bsestock.csv'

# Determine write mode and header based on file existence and content
if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    mode = 'a'
    header = False
else:
    mode = 'w'
    header = True

# Fetch data for all tickers
print(f"Fetching data for {date_str}")
all_data = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=date_str, end=date_str)
    if not data.empty:
        data['Ticker'] = ticker
        all_data = pd.concat([all_data, data])

# Save the data to the CSV file
if not all_data.empty:
    all_data.to_csv(output_file, mode=mode, header=header)
    print(f"Successfully saved {len(all_data)} rows to {output_file}.")
else:
    print("No data fetched for the specified date.")
