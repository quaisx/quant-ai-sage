"""
    Module: poc.py
"""

import env
import os
from typing import Dict
from datetime import datetime
import requests

import pandas as pd
import logging
import config
from quant_ai_sage.utils.market import manage
import yfinance as yf
from quant_ai_sage.analysis import insights
from quant_ai_sage.prediction import llm_wrapper as llm

def setup_logging():
    logger = logging.getLogger(config.APP_NAME)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

def fetch_data(start: datetime, end: datetime) -> pd.DataFrame:
    instrument_id = os.getenv('INSTRUMENT_ID', config.DEFAULT_INSTRUMENT_ID)
    file_path = f'{instrument_id}_{start.strftime("%Y-%m-%d")}_{end.strftime("%Y-%m-%d")}.csv'
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        # Set the 'Date' column as the index
        df.set_index('Date', inplace=True)
        return df
    instrument_info = yf.Ticker(instrument_id)
    # 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    data = instrument_info.history(start=start, end=end, interval='15m')
    data.index.name = 'Date'
    data.to_csv(file_path)

    return data


def main():
    logger = setup_logging()
    logger.info('main')

    data = manage.fetch_market_data(fetch_data)
    prices = insights.daily_price(data)
    trends = insights.daily_insights(data)
    indicators = { **prices, **trends }
    indicators['instrument_id'] = os.getenv('INSTRUMENT_ID', config.DEFAULT_INSTRUMENT_ID)
    response = llm.get_natural_language_insights(**indicators)
    print(response)
    logger.info('DONE')

if __name__ == "__main__":
    main()