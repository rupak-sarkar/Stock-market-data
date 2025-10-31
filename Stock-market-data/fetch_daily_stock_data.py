import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Define the list of tickers
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]  # Customize this list

# Define the output CSV file
output_file = 'stock_data/historical_stock_data.csv'

# Create the directory if it doesn't exist
output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
end_date = yesterday.strftime('%Y-%m-%d')
start_date = end_date

# Check if file exists to determine if it's the first run

if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    existing_data = pd.read_csv(output_file, index_col=0, parse_dates=True)
    last_date = existing_data.index.max().strftime('%Y-%m-%d')
    start_date = (pd.to_datetime(last_date) + timedelta(days=1)).strftime('%Y-%m-%d')
    mode = 'a'
    header = False
else:
    existing_data = pd.DataFrame()
    mode = 'w'
    header = True


print(f"Fetching data from {start_date} to {end_date}")

# Fetch data for all tickers
all_data = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        data['Ticker'] = ticker
        all_data = pd.concat([all_data, data])

# Write new data to the CSV file
if not all_data.empty:
    all_data.to_csv(output_file, mode=mode, header=header)
    print(f"Successfully saved {len(all_data)} rows to {output_file}.")
else:
    print("No data fetched for the specified date range.")
