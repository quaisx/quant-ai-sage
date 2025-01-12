# How to Choose the Right Entries, Filters, and Exits?
## Entry and Exit
Deciding when to enter and exit trades is the foundation of any algorithmic strategy. Here’s how to define these parameters:

### Entry
Entry Criteria: Determine the exact conditions to enter a trade. For example:

* Use technical indicators like moving averages, RSI (Relative Strength Index), or MACD (Moving Average Convergence Divergence) to identify potential entries.
* Use price action patterns like after 3 bullish days or when the recent close is higher than the day before.


**RSI (Relative Strength Index)**
Relative Strength Index (RSI), a pivotal momentum oscillator in technical analysis. Developed by J. Welles Wilder in 1978, the RSI measures the speed and change of price movements, oscillating between 0 and 100. 

- **Calculation of RSI**: The RSI is calculated using the formula:

  \[ \text{RSI} = 100 - \left( \frac{100}{1 + RS} \right) \]

  Where RS (Relative Strength) is the average of 'n' days' up closes divided by the average of 'n' days' down closes. 

- **Interpretation of RSI Values**:

  - An RSI above 70 indicates that the asset is overbought, suggesting a potential for a price pullback.

  - An RSI below 30 indicates that the asset is oversold, suggesting a potential for a price increase. 

- **Divergence Analysis**:

  - Bullish divergence occurs when the price makes a new low, but the RSI forms a higher low, indicating potential upward momentum.

  - Bearish divergence occurs when the price makes a new high, but the RSI forms a lower high, indicating potential downward momentum. 

- **Failure Swings**:

  - A failure swing occurs when the RSI moves above 70, pulls back, and then rises again, failing to surpass the previous peak, suggesting a potential reversal to the downside.

  - Conversely, a failure swing below 30, where the RSI moves below 30, rises, and then falls again without surpassing the previous low, suggests a potential reversal to the upside. 

- **Centerline Crossover**:

  - The 50 level on the RSI is considered a neutral zone.

  - A move above 50 indicates increasing bullish momentum, while a move below 50 indicates increasing bearish momentum. 

While the RSI is a powerful tool for identifying potential price reversals and momentum shifts, it should be used in conjunction with other technical indicators and fundamental analysis to enhance trading decisions.

You might find the following video helpful:
[Relative Strength Index Explained](https://youtu.be/hbcCykbX14U)


The article "MACD (Moving Average Convergence/Divergence)" from Algomatic Trading offers a comprehensive overview of the MACD indicator, a fundamental tool in technical analysis for assessing market momentum and trend direction.

**Key Components of MACD:**

- **MACD Line**: Calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA. 

- **Signal Line**: A 9-period EMA of the MACD Line, serving as a trigger for buy and sell signals. 

- **Histogram**: Represents the difference between the MACD Line and the Signal Line, visually indicating the strength of the trend.

**Interpretation and Trading Signals:**

- **Crossover Signals**:
  - *Bullish Signal*: Occurs when the MACD Line crosses above the Signal Line, suggesting potential upward momentum.
  - *Bearish Signal*: Occurs when the MACD Line crosses below the Signal Line, indicating potential downward momentum.

- **Divergence**:
  - *Bullish Divergence*: Happens when the price forms a new low, but the MACD forms a higher low, indicating weakening downward momentum.
  - *Bearish Divergence*: Occurs when the price forms a new high, but the MACD forms a lower high, suggesting weakening upward momentum.

- **Zero Line Crossovers**:
  - When the MACD Line crosses above zero, it indicates that the 12-period EMA is above the 26-period EMA, signaling potential bullish momentum.
  - Conversely, when the MACD Line crosses below zero, it suggests that the 12-period EMA is below the 26-period EMA, indicating potential bearish momentum.

**Limitations and Considerations:**

- **Lagging Indicator**: As a lagging indicator, MACD may not predict future price movements but rather confirms trends after they have begun.

- **False Signals**: In choppy or sideways markets, MACD can produce false signals, leading to potential losses.

- **Complementary Use**: For enhanced reliability, MACD should be used in conjunction with other technical analysis tools and indicators.

Let's highlight the necessity of combining MACD with other analytical methods to improve decision-making and mitigate risks.

You might find the following video helpful:

[How to Use the MACD Indicator](https://www.youtube.com/watch?v=8VJ0VxVx0Jw) 
 
[Entries for MRS](https://www.algomatictrading.com/post/12-essential-entries-for-mean-reversion-strategies)

### Exit
Exit Criteria: Decide when to take profits or cut losses. Some examples include:

Setting a fixed profit target or percentage gain.
Stop-loss orders to limit losses if the market moves against your position.
Trailing stops to lock in profits as the trade moves in your favor.

[Exits for MRS](https://www.algomatictrading.com/post/13-essential-exits-for-mean-reversion-strategies)

## When Not to Trade
One of the most overlooked aspects of algorithmic trading is knowing when not to trade. Market conditions aren’t always favorable, and trading during the wrong times can delete profits. Consider the following filters:

* Low Volatility Periods: Avoid trading when market volatility is unusually low, as price movements may not provide sufficient opportunities for profit.
* High-Impact News Events: Unless specifically designed for news trading, avoid trading during major events like central bank announcements, earnings reports, or geopolitical crises. These can cause unpredictable market swings.
* Overbought or Oversold Markets: Some algorithms are ineffective in extreme market conditions. Implementing filters to avoid trades when indicators like RSI show overbought or oversold signals can reduce unnecessary risk.

[Trend Filters](https://www.algomatictrading.com/post/11-key-trend-filters-for-trading)
[Essential MA](https://www.algomatictrading.com/post/11-essential-moving-averages-for-trading)
[Volatility Filters](https://www.algomatictrading.com/post/10-volatility-filters-you-need-in-your-trading-toolbox)
[Indicators](https://www.algomatictrading.com/blog/categories/indicators)
[Strategies](https://www.algomatictrading.com/blog/categories/strategies)