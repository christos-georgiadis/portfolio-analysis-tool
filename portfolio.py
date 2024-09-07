import yfinance as yf
from datetime import date as dt, timedelta, datetime
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks
        self.weights = self.calculate_weights(self.stocks)
    
    @staticmethod
    def calculate_weights(list_of_stocks):
        total_invested = 0
        for stock in list_of_stocks:
            total_invested += stock.amount
            
        weights = []
        for stock in list_of_stocks:
            weights.append(round(stock.amount/total_invested, 3))
        return weights
        
    @staticmethod
    def calculate_portfolio_daily_return(date, list_of_stocks, weights):
        date = date.strftime("%Y-%m-%d")
        portfolioReturns = 0
        for i in range(len(list_of_stocks)):
            portfolioReturns += weights[i]*list_of_stocks[i].daily_returns[date]
        return round(portfolioReturns,4)
             
    def add_stock(self, new_stock):
        self.stocks.append(new_stock)
        self.weights = self.calculate_weights(self.stocks)
        
    def remove_stock(self, pos):
        self.stocks.pop(pos)
        self.weights = self.calculate_weights(self.stocks)
        
    def calculate_returns(self, startDate, endDate):
        
        data = yf.download('AAPL', startDate, endDate) # Temporary to get dates
        dates = [date.date() for date in data.index]
        
        daily_returns = []
        curr_stocks = []
        for date in dates:
            for i, stock in enumerate(self.stocks):
                if stock.openDate <= date <= stock.closeDate and stock not in curr_stocks:
                    curr_stocks.append(stock)
                elif date > stock.closeDate:
                    curr_stocks.pop(i)
            weights = self.calculate_weights(curr_stocks)
            daily_returns.append(self.calculate_portfolio_daily_return(date, curr_stocks, weights))
        return daily_returns
    
    def plot_cumulative_returns(self, startDate, endDate):
        returns = self.calculate_returns(startDate, endDate)
        cumulative_returns = []
        s = 0
        for daily_return in returns:
            s += daily_return
            cumulative_returns.append(s*100)
        
        plt.plot(cumulative_returns, linewidth=1)
        plt.xlabel("Days")
        plt.ylabel("Cumulative Return (%)")
        plt.title("Portfolio Cumulative Returns")
        plt.show()
        
    def __str__(self):
        st = "\n"
        for i in range(len(self.stocks)):
            st += f"{self.stocks[i].ticker}: {self.weights[i]*100}% \n"
        return st


class Stock:
    def __init__(self, ticker, amount, openDate, closeDate = None):
        self.ticker = ticker
        self.amount = amount
        if closeDate is None:
            self.closeDate = dt.today()
        else:
            self.closeDate = closeDate
            
        self.openDate = datetime.strptime(openDate, '%Y-%m-%d').date()
        prev_date = self.openDate - timedelta(days=1)
        
        data = yf.download(self.ticker, prev_date, self.closeDate)
        self.dates = [date.date() for date in data.index]
        while prev_date not in self.dates:
            prev_date -= timedelta(days=1)
            data = yf.download(self.ticker, prev_date, self.closeDate)
            self.dates = [date.date() for date in data.index]
            
        self.daily_returns = data['Adj Close'].pct_change()
        self.daily_returns = self.daily_returns.dropna()
        self.dates.pop(0)