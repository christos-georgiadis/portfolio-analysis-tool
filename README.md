# Portfolio Analysis Tool

This project provides a Python tool for analyzing and visualizing the cumulative returns of a stock portfolio over time. The tool uses historical stock data fetched from Yahoo Finance via the `yfinance` library and generates plots to visualize the portfolio's performance.

## Features

- **Portfolio Class:** Manages a collection of stocks, calculates their respective weights, and computes the overall portfolio returns.
- **Stock Class:** Represents individual stocks, retrieves historical price data, and calculates daily returns.
- **Dynamic Weight Calculation:** The portfolio automatically updates the weights of stocks whenever a new stock is added or removed.
- **Cumulative Return Plot:** Visualize the cumulative returns of your portfolio over a specified time period.
