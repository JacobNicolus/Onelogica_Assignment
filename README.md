# Onelogica_Assignment
This is the library made for onelogica and consists of fuctions for common algorithmic trading. 

#### SMABacktester

SMABacktester is a Python class for backtesting SMA-based trading strategies. It provides functionality to retrieve historical price data from Yahoo Finance, preprocess the data, backtest the SMA-based trading strategy, compute performance metrics, and visualize the backtesting results.


Now lets dive into the Modules one by one in this class!!

def __init__(self, symbol, SMA_S=50, SMA_L=200, start=None, end=None):
        """
        Initializes the SMABacktester object.
        
        Parameters:
            symbol (str): The symbol of the asset to backtest.
            SMA_S (int): The short-term SMA period (default: 50, adjusted to 5 if start and end dates are within a month).
            SMA_L (int): The long-term SMA period (default: 200, adjusted to 10 if start and end dates are within a month).
            start (str): Start date for data retrieval (YYYY-MM-DD).
            end (str): End date for data retrieval (YYYY-MM-DD).
        """
        self.symbol = symbol
        self.SMA_S = SMA_S if SMA_S >= 5 else 5  # Adjust to default if within a month
        self.SMA_L = SMA_L if SMA_L >= 10 else 10  # Adjust to default if within a month
        self.start = start
        self.end = end
        self.results = None
        self.get_data()
        self.test_results()


