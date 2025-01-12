from typing import Dict
import pandas as pd
from datetime import datetime, timedelta

def get_market_open_duration(window: pd.DataFrame) -> float:
    current_time = window.index[-1].time()  # Returns a datetime.time object
    previous_trading_day = datetime.today() - timedelta(days=1)
    current_datetime = datetime.combine(previous_trading_day, current_time)
    market_start_time = datetime.combine(previous_trading_day, datetime.strptime("09:30:00", "%H:%M:%S").time())
    market_open_duration = (current_datetime - market_start_time).total_seconds() / 60  # in minutes
    
    return market_open_duration

def daily_price(data: pd.DataFrame) -> Dict:
    daily_high: float = float('-inf')
    daily_low: float  = float('inf')
    buying_momentum: int = 0
    selling_momentum: int = 0
    price_change: float = 0.
    if not data.empty:
        daily_high = data['Close'].max()
        daily_low = data['Close'].min()
        first_close = data['Close'].iloc[0]
        last_close = data['Close'].iloc[-1]
        price_change = last_close - first_close

        if price_change > 0:
            buying_momentum += price_change
        else:
            selling_momentum += abs(price_change)

    results = {
        'daily_high': daily_high,
        'daily_low': daily_low,
        'buying_momentum': buying_momentum,
        'selling_momentum': selling_momentum,
        'price_change': price_change
    }

    return  results           

def daily_insights(window: pd.DataFrame) -> Dict:
        window_size = window.shape[0]
        rolling_avg = window['Close'].rolling(window=window_size).mean().iloc[-1]
        price_change = window['Close'].iloc[-1] - window['Close'].iloc[0]
        volume_change = window['Volume'].iloc[-1] - window['Volume'].iloc[0]
        ema = window['Close'].ewm(span=window_size, adjust=False).mean().iloc[-1]
        std = window['Close'].rolling(window=window_size).std().iloc[-1]
        bollinger_upper = rolling_avg + (2 * std)
        bollinger_lower = rolling_avg - (2 * std)
        delta = window['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14, min_periods=1).mean().iloc[-1]
        avg_loss = loss.rolling(window=14, min_periods=1).mean().iloc[-1]
        rs = avg_gain / avg_loss if avg_loss != 0 else float('nan')
        rsi = 100 - (100 / (1 + rs))
        
        market_open_duration = get_market_open_duration(window)

        results = {
            'rolling_avg': rolling_avg,
            'ema': ema,
            'rsi': rsi,
            'bollinger_upper': bollinger_upper,
            'bollinger_lower': bollinger_lower,
            'price_change': price_change,
            'market_open_duration': market_open_duration,
            'volume_change': volume_change
        }

        return results
        