# Portfolio Analysis Tool

This project provides a Python tool for analyzing and visualizing the cumulative returns of a stock portfolio over time. The tool uses historical stock data fetched from Yahoo Finance via the `yfinance` library and generates plots to visualize the portfolio's performance.

## Features

- **Portfolio Class:** Manages a collection of stocks, calculates their respective weights, and computes the overall portfolio returns.
- **Stock Class:** Represents individual stocks, retrieves historical price data, and calculates daily returns.
- **Dynamic Weight Calculation:** The portfolio automatically updates the weights of stocks whenever a new stock is added or removed.
- **Cumulative Return Plot:** Visualize the cumulative returns of your portfolio over a specified time period.

## Usage
```python
from portfolio import Portfolio, Stock

# Create a portfolio with some stocks
portfolio = Portfolio([Stock("AAPL", 300, "2023-03-23"), Stock("AVGO", 200, "2023-03-27")])

# Display the portfolio
print(portfolio)

# Plot cumulative returns
portfolio.plot_cumulative_returns("2023-03-23", "2024-09-05")

# Add a new stock to the portfolio
portfolio.add_stock(Stock('NVDA', 100, "2023-04-21"))

# Display the updated portfolio
print(portfolio)

# Plot cumulative returns after adding the new stock
portfolio.plot_cumulative_returns("2023-03-23", "2024-09-05")

```
## Example Plots
![cumulative_returns](https://github.com/user-attachments/assets/22ec59c2-bdfa-4974-be8b-59acd368dd43)
