# YFINANCE
## Retrieving Stock Data with yfinance

The `yfinance` library offers Python users a seamless way to retrieve stock data from Yahoo Finance. Whether you're a beginner or a seasoned analyst, this library provides a range of functionalities to help you gather and analyze stock information. In this tutorial, we'll explore 10 fundamental ways to retrieve stock data using `yfinance`.

---

## Table of Contents
- [YFINANCE](#yfinance)
  - [Retrieving Stock Data with yfinance](#retrieving-stock-data-with-yfinance)
  - [Table of Contents](#table-of-contents)
    - [1. Fetching Historical Data](#1-fetching-historical-data)
    - [2. Ticker Object](#2-ticker-object)
    - [3. Getting Recent Data](#3-getting-recent-data)
    - [4. Fetching Data for Multiple Tickers](#4-fetching-data-for-multiple-tickers)
    - [5. Adjusted Data Retrieval](#5-adjusted-data-retrieval)
    - [6. Interval-based Data Retrieval](#6-interval-based-data-retrieval)
    - [7. Retrieving Dividends and Splits](#7-retrieving-dividends-and-splits)
    - [8. Real-time Data](#8-real-time-data)
    - [9. Data for Specific Dates](#9-data-for-specific-dates)
    - [10. Visualization with yfinance](#10-visualization-with-yfinance)

---

### 1. Fetching Historical Data
The `download` method is your go-to for obtaining historical data for any stock.

```python
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
print(data.head())
```

This retrieves Apple’s stock data between January 1, 2020, and January 1, 2021.

---

### 2. Ticker Object
The `Ticker` class allows you to access various data for a specific stock.

```python
apple = yf.Ticker("AAPL")
print(apple.info)  # General information about Apple Inc.
```

This provides detailed information about the stock, including market cap, sector, and more.

---

### 3. Getting Recent Data
Want data for the most recent trading days? Use the `period` parameter.

```python
recent_data = yf.download("AAPL", period="5d")
print(recent_data)
```

This retrieves the last 5 days of trading data for Apple.

---

### 4. Fetching Data for Multiple Tickers
Retrieve data for multiple stocks in one go.

```python
multi_data = yf.download(["AAPL", "MSFT"], start="2020-01-01", end="2021-01-01")
print(multi_data)
```

This downloads historical data for both Apple and Microsoft.

---

### 5. Adjusted Data Retrieval
Obtain adjusted data, which accounts for stock splits, dividends, etc.

```python
data = yf.download("AAPL", start="2020-01-01", end="2021-01-01", auto_adjust=True)
print(data['Close'])  # This will show the adjusted close prices
```

The `auto_adjust` parameter ensures prices are adjusted for corporate actions.

---

### 6. Interval-based Data Retrieval
Retrieve data based on specific intervals, like daily or weekly.

```python
weekly_data = yf.download("AAPL", start="2020-01-01", end="2021-01-01", interval="1wk")
print(weekly_data)
```

This fetches weekly aggregated data for Apple.

---

### 7. Retrieving Dividends and Splits
Access dividend and stock split history for a stock.

```python
apple = yf.Ticker("AAPL")
dividends = apple.dividends
splits = apple.splits
print(dividends, splits)
```

You can analyze Apple’s dividend payouts and stock split history using this data.

---

### 8. Real-time Data
Fetch the most up-to-date stock price.

```python
apple = yf.Ticker("AAPL")
print(apple.history(period="1d"))
```

This retrieves the latest available data for Apple’s stock.

---

### 9. Data for Specific Dates
Obtain data for a specific date range.

```python
data = yf.download("AAPL", start="2022-01-01", end="2022-12-31")
print(data)
```

This downloads Apple’s stock data for the year 2022.

---

### 10. Visualization with yfinance
Visualize historical data with ease.

```python
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
data['Close'].plot()
plt.title("Apple Stock Prices")
plt.show()
```

This creates a simple line plot of Apple’s closing stock prices.

---

With `yfinance`, accessing and analyzing stock data has never been easier. Use these methods to enhance your financial analysis workflows and build robust data-driven strategies.

