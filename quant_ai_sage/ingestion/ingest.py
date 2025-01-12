import sqlite3
import yfinance as yf
import pandas as pd
import requests

# Function to fetch NASDAQ tickers (replace the source URL with a valid NASDAQ tickers list source)
def fetch_nasdaq_tickers():
    url = "https://www.nasdaq.com/api/v1/screener/stocks"  # Example URL (modify as per your source)
    response = requests.get(url)
    if response.status_code == 200:
        # Assuming JSON response contains a list of tickers
        data = response.json()
        tickers = [item['symbol'] for item in data['data']['rows']]
        return tickers
    else:
        raise Exception(f"Failed to fetch NASDAQ tickers: {response.status_code}")

# Function to fetch historical data from Yahoo Finance
def fetch_historical_data(ticker, start_date="2000-01-01", end_date=None):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        stock_data.reset_index(inplace=True)  # Reset index to have 'Date' as a column
        stock_data['Ticker'] = ticker  # Add a Ticker column for identification
        return stock_data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Function to save data to SQLite database
def save_to_database(df, db_name="stock_data.db"):
    try:
        with sqlite3.connect(db_name) as conn:
            df.to_sql("historical_stock_data", conn, if_exists="append", index=False)
        print(f"Data saved to database: {db_name}")
    except Exception as e:
        print(f"Error saving data to database: {e}")

# Main function
def main():
    # Fetch NASDAQ tickers
    try:
        tickers = fetch_nasdaq_tickers()
        print(f"Fetched {len(tickers)} NASDAQ tickers.")
    except Exception as e:
        print(f"Error fetching tickers: {e}")
        return

    # Create an SQLite database connection
    db_name = "stock_data.db"

    # Iterate through tickers and fetch/save their historical data
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetch_historical_data(ticker)
        if data is not None and not data.empty:
            save_to_database(data, db_name=db_name)

if __name__ == "__main__":
    main()
