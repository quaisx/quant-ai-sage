import ollama

def get_natural_language_insights(**kwargs) -> str:
    
    instrument_id = kwargs['instrument_id']
    rolling_avg = kwargs['rolling_avg'] 
    ema = kwargs['ema'] 
    rsi = kwargs['rsi'] 
    bollinger_upper = kwargs['bollinger_upper']
    bollinger_lower = kwargs['bollinger_lower']
    price_change = kwargs['price_change']
    volume_change = kwargs['volume_change']
    market_open_duration = kwargs['market_open_duration'] 
    daily_high = kwargs['daily_high'] 
    daily_low = kwargs['daily_low'] 
    buying_momentum = kwargs['buying_momentum']
    selling_momentum = kwargs['selling_momentum']

    prompt = f"""
    You are a professional stock broker. {instrument_id} stock has a daily rolling average of {rolling_avg:.2f}.
    The Exponential Moving Average (EMA) is {ema:.2f}, and the Relative Strength Index (RSI) is {rsi:.2f}.
    The Bollinger Bands are set with an upper band of {bollinger_upper:.2f} and a lower band of {bollinger_lower:.2f}.
    The price has changed by {price_change:.2f}, and the volume has shifted by {volume_change}.
    The market has been open for {market_open_duration:.2f} minutes.
    Today's high was {daily_high:.2f} and low was {daily_low:.2f}.
    The buying momentum is {buying_momentum:.2f} and selling momentum is {selling_momentum:.2f}.
    Based on this data, provide insights into the current stock trend and the general market sentiment.
    The insights should not be longer than 280 characters to fit into a single tweet, so be as concise as possible and only
    capture the most important parts of the stock trend.
    """
    response = ollama.chat(
            model="llama3.1",
            messages=[{"role": "user", "content": prompt}]
        )
    return response['message']['content'].strip()
    