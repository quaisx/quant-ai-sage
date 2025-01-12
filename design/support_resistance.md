# Trading Support and Resistance
Support and resistance levels are fundamental concepts in technical analysis, representing price points where an asset tends to stop and reverse its direction. Support levels indicate a price point where a downtrend can be expected to pause due to a concentration of demand, while resistance levels are where an uptrend can pause due to a concentration of selling interest. 

The article emphasizes the significance of these levels in trading strategies, particularly focusing on the psychological aspects that drive market participants to make decisions at these critical points. By understanding and identifying these levels, traders can make more informed decisions, potentially increasing their chances of success.

To effectively trade using support and resistance levels, it's essential to accurately identify these zones on a price chart. This involves analyzing historical price data to pinpoint areas where the price has consistently reversed or stalled. Once these levels are identified, traders can develop strategies to enter or exit trades based on the price's interaction with these zones.

Backtesting is a crucial step in validating any trading strategy. By applying the strategy to historical data, traders can assess its effectiveness and make necessary adjustments before applying it in live markets. This process helps in understanding the potential risks and rewards associated with the strategy. 

It's important to note that while support and resistance levels can provide valuable insights, they are not foolproof. Market conditions can change, and unexpected events can cause price movements that break through these levels. Therefore, it's advisable to use support and resistance levels in conjunction with other technical analysis tools and to remain adaptable to changing market dynamics.

For a more in-depth understanding and practical demonstration of trading strategies involving support and resistance levels, you might find the following video helpful:
[How to backtest S/R levels](https://youtu.be/tEqumHq6gBY)

## Why it works
Levels work and will always work for one simple reason: When price forms levels, the price is allocated between buyers and sellers within that range. That is the mechanics of the market. Its very essence. Because of this, support and resistance levels are formed. At the moment when who wanted to buy bought, and who wanted to sell sold, the price goes out of this range, goes beyond the formed levels. And, as a consequence, there is a breakdown of stoplosses, liquidation, and at the same time an organic movement to one side of the market.

> "Pareto’s Law: 20% of the effort yields 80% of the result and the other 80% of the effort yields only 20% of the result"


# Calculate Support and Resistance Levels

**Support** and **resistance** lines are key concepts in technical analysis used by traders to identify potential turning points in the price movement of a stock or other asset. 

_A **support** line_ represents a price level where a downtrend tends to pause or reverse due to a concentration of buying interest. 

Conversely, _a __resistance__ line_ indicates a level where an uptrend might halt or reverse because of selling pressure. 

These levels are used by traders to make decisions about entering or exiting trades, estimating risk, and predicting future price movements.

Installation:
```bash
pip install yahooquery pandas scipy mplfinance
```

Imports:
```bash
import yahooquery as yq
import pandas as pd
import scipy as sp
import mplfinance as mpf
```

Load historical data for a trading period:
```python
bars = yq.Ticker('AAPL').history(start='2022-01-01', interval='1d').reset_index(level=0, drop=True)
```

Visualize the data:
```python
bars.index = pd.to_datetime(bars.index)
mpf.plot(bars, type='candle', style='charles', title='(AAPL) Candlestick Chart', volume=True)
```

## Identifying Peaks and Troughs with SciPy

The *find_peaks* function from the **scipy.signal** module detects local maxima (peaks) in data. 

In the context of stock prices, these peaks can serve as potential _resistance levels_. Let’s take a look at the key parameters we use:

• **distance**: Specifies the minimum number of data points between consecutive peaks. This helps avoid detecting too many peaks too close to each other.

• **prominence**: A peak’s prominence represents how much it stands out from the surrounding data. The higher the prominence, the more significant the peak.

## Strong Peaks
**“strong”** peaks as those with high prominence and greater separation (distance), as well as significant price levels like the 52-week high.

### How to find strong peaks:
```python
# Define the distance between strong peaks (in days).
strong_peak_distance = 60

# Define the prominence (how high the peaks are compared to their surroundings).
strong_peak_prominence = 20

# Find the strong peaks in the 'high' price data
strong_peaks, _ = sp.signal.find_peaks(
  bars['high'],
  distance=strong_peak_distance,
  prominence=strong_peak_prominence
)

# Extract the corresponding high values of the strong peaks
strong_peaks_values = bars.iloc[strong_peaks]["high"].values.tolist()

# Include the yearly high as an additional strong peak
yearly_high = bars["high"].iloc[-252:].max()
strong_peaks_values.append(yearly_high)
```

### Visualize resistance levels
```python
# Create a list of horizontal lines to plot as resistance levels
add_plot = [mpf.make_addplot(np.full(bars.shape[0], resistance), color='r', linestyle='--') for resistance in strong_peaks_values]

# Plot the candlestick chart with resistance lines
mpf.plot(
    bars, 
    type='candle', 
    style='charles', 
    title='AAPL Candlestick Chart with Strong Resistance Lines',
    volume=True, 
    addplot=add_plot
)
```

### General Peaks
**General peaks** as those with weaker prominence and shorter distance compared to strong peaks. However, for a price level to qualify as a **general peak**, the stock must reach and be rejected from that level multiple times.

To achieve this, we will have to set both a minimum width and a minimum rank thresholds. These thresholds help group weaker peaks into bins, merging nearby peaks that are too close to one another. 

If a peak level reaches the minimum rank (i.e., the stock price has been rejected at that level enough times), it is added to **the list of resistance levels**.

This approach helps identify shorter-term resistance levels, which are particularly useful for **swing tradering** with the focus on smaller price movements over shorter time periods. 

These general peaks complement the strong peaks to provide a more comprehensive view of resistance levels in the stock’s price history.

### How to calculate the general peaks

```python
# Define the shorter distance between general peaks (in days)
# This controls how far apart peaks need to be to be considered separate.
peak_distance = 5

# Define the width (vertical distance) where peaks within this range will be grouped together.
# If the high prices of two peaks are closer than this value, they will be merged into a single resistance level.
peak_rank_width = 2

# Define the threshold for how many times the stock has to reject a level
# Before it becomes a resistance level
resistance_min_pivot_rank = 3

# Find general peaks in the stock's 'high' prices based on the defined distance between them.
# The peaks variable will store the indices of the high points in the 'high' price data.
peaks, _ = sp.signal.find_peaks(bars['high'], distance=peak_distance)

# Initialize a dictionary to track the rank of each peak
peak_to_rank = {peak: 0 for peak in peaks}

# Loop through all general peaks to compare their proximity and rank them
for i, current_peak in enumerate(peaks):
    # Get the current peak's high price
    current_high = bars.iloc[current_peak]["high"]
    
    # Compare the current peak with previous peaks to calculate rank based on proximity
    for previous_peak in peaks[:i]:
        if abs(current_high - bars.iloc[previous_peak]["high"]) <= peak_rank_width:
            # Increase rank if the current peak is close to a previous peak
            peak_to_rank[current_peak] += 1
```

```python
# Initialize the list of resistance levels with the strong peaks already identified.
resistances = strong_peaks_values

# Now, go through each general peak and add it to the resistance list if its rank meets the minimum threshold.
for peak, rank in peak_to_rank.items():
    # If the peak's rank is greater than or equal to the resistance_min_pivot_rank, 
    # it means this peak level has been rejected enough times to be considered a resistance level.
    if rank >= resistance_min_pivot_rank:
        # Append the peak's high price to the resistances list, adding a small offset (1e-3) 
        # to avoid floating-point precision issues during the comparison.
        resistances.append(bars.iloc[peak]["high"] + 1e-3)

# Sort the list of resistance levels so that they are in ascending order.
resistances.sort()
```

```python
# Initialize a list to hold bins of resistance levels that are close to each other.
resistance_bins = []

# Start the first bin with the first resistance level.
current_bin = [resistances[0]]

# Loop through the sorted resistance levels.
for r in resistances:
    # If the difference between the current resistance level and the last one in the current bin 
    # is smaller than a certain threshold (defined by peak_rank_w_pct), add it to the current bin.
    if r - current_bin[-1] < peak_rank_width:
        current_bin.append(r)
    else:
        # If the current resistance level is far enough from the last one, close the current bin
        # and start a new one.
        resistance_bins.append(current_bin)
        current_bin = [r]

# Append the last bin.
resistance_bins.append(current_bin)

# For each bin, calculate the average of the resistances within that bin.
# This will produce a clean list of resistance levels where nearby peaks have been merged.
resistances = [np.mean(bin) for bin in resistance_bins]
```

### Support levels - Troughs
Support levels can be calculated exactly like resistance levels, except we pass in the negative values of our lows:

```python
troughs, _ = sp.signal.find_peaks(-bars['low'], distance=peak_distance)
```

