import sqlite3
import yfinance as yf
import pandas as pd
import schedule
import time
from datetime import datetime, timedelta
from threading import Lock

# Global Lock for database operations
db_lock = Lock()

# Constants
DB_NAME = "stock_data.db"
MASTER_DF = pd.DataFrame()  # Initialize master DataFrame
START_DATE = (datetime.now() - timedelta(days=5 * 365)).strftime("%Y-%m-%d")  # 5 years back
END_DATE = None  # Defaults to today in yfinance

# Fetch historical stock data
def fetch_historical_data(ticker, start_date=START_DATE, end_date=END_DATE):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        stock_data.reset_index(inplace=True)  # Convert index to Date column
        stock_data['Ticker'] = ticker
        return stock_data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Save data to SQLite database
def save_to_database(df):
    global db_lock
    with db_lock:  # Ensure database lock for safe writes
        try:
            with sqlite3.connect(DB_NAME) as conn:
                df.to_sql("historical_stock_data", conn, if_exists="append", index=False)
            print(f"Data saved to database: {len(df)} records")
        except Exception as e:
            print(f"Error saving data to database: {e}")

# Load master DataFrame from database
def load_master_dataframe():
    global db_lock
    global MASTER_DF
    with db_lock:  # Ensure database lock for safe reads
        try:
            with sqlite3.connect(DB_NAME) as conn:
                MASTER_DF = pd.read_sql("SELECT * FROM historical_stock_data", conn)
            print("Master DataFrame loaded from database.")
        except Exception as e:
            print(f"Error loading master DataFrame: {e}")

# Fetch data for NASDAQ tickers
def fetch_and_save_nasdaq_data():
    # Replace with actual tickers (this is just an example)
    tickers = ["AAPL", "MSFT", "GOOG"]  # Fetch real tickers from NASDAQ API if needed
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetch_historical_data(ticker)
        if data is not None and not data.empty:
            save_to_database(data)

# Merge new data into the master DataFrame
def merge_new_data_to_master():
    global MASTER_DF
    try:
        with db_lock:  # Ensure database lock
            with sqlite3.connect(DB_NAME) as conn:
                new_data = pd.read_sql("SELECT * FROM historical_stock_data", conn)
            MASTER_DF = pd.concat([MASTER_DF, new_data]).drop_duplicates()
            print("Master DataFrame updated with new data.")
    except Exception as e:
        print(f"Error merging new data: {e}")

# Intraday data fetching
def fetch_intraday_data():
    global MASTER_DF
    tickers = MASTER_DF['Ticker'].unique()  # Get tickers from the master DataFrame
    for ticker in tickers:
        print(f"Fetching intraday data for {ticker}...")
        intraday_data = fetch_historical_data(ticker, start_date=datetime.now().strftime("%Y-%m-%d"))
        if intraday_data is not None and not intraday_data.empty:
            save_to_database(intraday_data)
            merge_new_data_to_master()

# Schedule tasks
def schedule_tasks():
    # Historical data fetching from Friday 6 PM to Monday 9:30 AM
    schedule.every().friday.at("18:00").do(fetch_and_save_nasdaq_data)
    schedule.every().saturday.at("09:00").do(fetch_and_save_nasdaq_data)
    schedule.every().sunday.at("09:00").do(fetch_and_save_nasdaq_data)
    schedule.every().monday.at("09:25").do(merge_new_data_to_master)

    # Intraday fetching every 5 minutes after Monday 9:30 AM
    schedule.every().monday.at("09:30").do(lambda: schedule.every(5).minutes.do(fetch_intraday_data))

# Main loop
def main():
    load_master_dataframe()  # Load master DataFrame on startup
    schedule_tasks()  # Initialize scheduled tasks
    print("Scheduler started.")
    while True:
        schedule.run_pending()  # Run scheduled tasks
        time.sleep(1)

if __name__ == "__main__":
    main()
