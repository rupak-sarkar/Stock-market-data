import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Define tickers
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]

# Date range
today = datetime.now()
end_date = today.strftime('%Y-%m-%d')
start_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')

# Output file
output_file = 'stock_data/historical_stock_data1.csv'
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Determine write mode and header
if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    mode = 'a'
    header = False
else:
    mode = 'w'
    header = True

print(f"Fetching data from {start_date} to {end_date}")

# Fetch and format data
all_data = []
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        data.reset_index(inplace=True)
        data['date'] = data['Date'].dt.strftime('%m/%d/%Y')
        data['Ticker'] = ticker
        # Keep only required columns and round
        data = data[['date', 'Close', 'High', 'Low', 'Open', 'Volume', 'Ticker']]
        data = data.round(2)
        all_data.append(data)

# Combine all tickers
final_df = pd.concat(all_data, ignore_index=True)

# Save to CSV
if not final_df.empty:
    final_df.to_csv(output_file, mode=mode, header=header, index=False)
    print(f"✅ Saved {len(final_df)} rows to {output_file}")
else:
    print("⚠️ No data fetched for the specified date range")

# Display for debugging
print(final_df)
