Here's a refined version of the data ingestion system that satisfies your requirements:

### Key Features:
1. **Scheduled Data Fetching**:
   - Runs from **6 PM Friday** to **9:30 AM Monday** for historical data fetching.
   - Switches to fetching data every **5 minutes** after 9:30 AM on Monday.
   
2. **Database Locking Mechanism**:
   - Ensures safe read/write operations to avoid conflicts using `threading.Lock`.

3. **Master DataFrame**:
   - Loads from the database on initialization and merges new data as it arrives.

4. **Scheduling**:
   - Uses the `schedule` package to manage periodic tasks.

---

### Explanation of the Code

1. **Historical Data Collection**:
   - Runs between Friday 6 PM and Monday 9:30 AM, fetching 5 years of historical data for NASDAQ tickers.
   - Saves data to the SQLite database.

2. **Intraday Data Collection**:
   - Starts Monday at 9:30 AM and fetches data every 5 minutes.
   - Appends new data to the database and updates the `MASTER_DF`.

3. **Database Locking**:
   - Ensures safe concurrent access using a `threading.Lock`.

4. **Master DataFrame**:
   - Loaded from the database at startup.
   - Updated with new data whenever the database is written to.

5. **Scheduling**:
   - Uses the `schedule` package to set up periodic tasks.
   - Runs historical fetching on weekends and switches to intraday fetching on Monday.

6. **Error Handling**:
   - Ensures robust handling of API or database errors.

---

### How It Works:
1. **Weekend**:
   - Historical data is fetched incrementally, saving as much as possible.
2. **Monday Onwards**:
   - Intraday data is fetched every 5 minutes and merged with the master dataset.
3. **Database Writes**:
   - Use a lock to ensure no concurrent writes or reads interfere.

This setup ensures robust and scalable data ingestion for your trading system.