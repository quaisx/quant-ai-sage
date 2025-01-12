from datetime import datetime, timedelta, time
import pytz  # Install pytz if not already installed
from typing import Callable, Optional
import pandas as pd

from quant_ai_sage.utils.market.timing import is_before_market_open, is_after_market_close

def fetch_market_data(data_processor: Callable[..., None]) -> Optional[pd.DataFrame]:
    """
    Determines the appropriate market data to fetch based on the current date and time.
    """
    eastern = pytz.timezone('US/Eastern')

    # Define the market open and close times
    MARKET_OPEN_TIME = time(9, 30)  # 9:30 AM
    MARKET_CLOSE_TIME = time(16, 0)  # 4:00 PM

    
    today = datetime.now(eastern)
    current_day = today.weekday()  # 0=Monday, ..., 6=Sunday

    if current_day == 6:  # Sunday - Do nothing
        print("It's Sunday. No data fetch.")
        return None

    # if current_day == 5:  # Saturday - Fetch 5 days of data (Monday to Friday of the current week)
    #     print("It's Saturday. Fetching data for the past 5 days.")
    #     start_date = today - timedelta(days=6)  # Last Monday
    #     end_date = today - timedelta(days=1)   # Friday
    #     # date_range = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    #     return data_processor(start=start_date, end=end_date)

    if current_day == 5:  # Saturday - Fetch 5 days of data (Monday to Friday of the current week)
        print("It's Saturday. Fetching data for the previous day.")
        start_date = today - timedelta(days=1)  # Last Monday
        end_date = today - timedelta(days=1)   # Friday
        market_open = eastern.localize(datetime.combine(start_date, MARKET_OPEN_TIME))
        market_close = eastern.localize(datetime.combine(end_date, MARKET_CLOSE_TIME))
        # date_range = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
        return data_processor(start=market_open, end=market_close)
    
    # elif month.is_end_of_month():  # End of month - Fetch a month of data
    #     print("It's the end of the month. Fetching data for the past month.")
    #     # You can use the start of the month as `today.replace(day=1)` and fetch a month of data.
    #     # get_market_data(f"{today.year}-{today.month - 1:02d}-01 to {today.year}-{today.month:02d}-01")
    #     prev_month = month.get_beginning_of_previous_month()
    #     return data_processor(start=prev_month, end=today)

    elif is_before_market_open():  # Before market opens - Fetch previous day's data
        print("It's before market open. Fetching data for the previous day.")
        previous_day = today - timedelta(days=1)
        return data_processor(start=previous_day, end=previous_day)

    elif is_after_market_close():  # After market closes - Fetch today's data
        print("Market is closed. Fetching data for today.")
        data_processor(start=today, end=today)

    else:
        print("Market is open. No data fetch.")
        return None
