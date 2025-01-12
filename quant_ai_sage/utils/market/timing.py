from datetime import datetime, time, timedelta
import pytz  # Install pytz via pip if not already installed
import pandas as pd

def is_weekend():
    # Get the current date
    today = datetime.now()

    # Check if it's a weekend (Saturday=5, Sunday=6)
    return today.weekday() >= 5  # weekday(): 0=Monday, ..., 6=Sunday
    # Alternatively, using isoweekday(): 6=Saturday, 7=Sunday
    # return today.isoweekday() in (6, 7)

def is_weekday():
    """
    Check if the current day is a weekday (Monday to Friday).
    
    Returns:
        bool: True if today is a weekday, False otherwise.
    """
    today = datetime.now()
    return today.weekday() < 5  # Monday=0 to Friday=4

def is_end_of_month() -> bool:
    """
    Checks if today is the end of the month.
    Returns:
        bool: True if today is the last day of the month, False otherwise.
    """
    today = datetime.now(pytz.timezone('US/Eastern'))
    next_day = today + timedelta(days=1)
    return next_day.day == 1  # If tomorrow is the 1st, today is the last day of the month.

def get_beginning_of_previous_month() -> datetime:
    # Get today's date in Eastern Time
    eastern = pytz.timezone('US/Eastern')
    today = datetime.now(eastern)

    # Since today is the 1st of the new month, subtract 1 day to get to the previous month
    previous_month_date = today - timedelta(days=1)

    # Replace the day with 1 to get the first day of the previous month
    beginning_of_previous_month = previous_month_date.replace(day=1)

    return beginning_of_previous_month

def is_market_open():
    """
    Checks if the market is currently open.
    Market hours: 9:30 AM to 4:00 PM Eastern Time, Monday to Friday.
    
    Returns:
        bool: True if the market is open, False otherwise.
    """
    # Define market open and close times (Eastern Time)
    market_open = time(9, 30)  # 9:30 AM
    market_close = time(16, 0)  # 4:00 PM

    # Get the current time in Eastern Time
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern).time()

    # Check if it's a weekend
    current_day = datetime.now(eastern).weekday()  # 0=Monday, ..., 6=Sunday
    if current_day >= 5:  # Saturday=5, Sunday=6
        return False

    # Check if the current time is within market hours
    if market_open <= current_time <= market_close:
        return True

    return False

def is_before_market_open():
    """
    Checks if the current time is before 9:30 AM Eastern Time.
    
    Returns:
        bool: True if the current time is before 9:30 AM, False otherwise.
    """
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern).time()
    market_open = time(9, 30)

    return current_time < market_open

def is_after_market_close():
    """
    Checks if the current time is after 4:30 PM Eastern Time.
    
    Returns:
        bool: True if the current time is after 4:30 PM, False otherwise.
    """
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern).time()
    market_close = time(16, 30)

    return current_time > market_close

def is_north_american_market_closed():
    """
    Checks if the North American market (Eastern Time) is currently closed.

    Returns:
        bool: True if the market is closed, False otherwise.
    """
    # Define market open and close times (Eastern Time)
    market_open = time(9, 30)  # 9:30 AM
    market_close = time(16, 0)  # 4:00 PM

    # Get the current time in Eastern Time
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern).time()

    # Check if it's a weekend
    current_day = datetime.now(eastern).weekday()  # 0=Monday, ..., 6=Sunday
    if current_day >= 5:  # Saturday=5, Sunday=6
        return True

    # Check if the current time is outside market hours
    if current_time < market_open or current_time > market_close:
        return True

    return False


