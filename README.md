# Onelogica_Assignment
This is the library made for onelogica and consists of fuctions for common algorithmic trading. 

#### SMABacktester

SMABacktester is a Python class for backtesting SMA-based trading strategies. It provides functionality to retrieve historical price data from Yahoo Finance, preprocess the data, backtest the SMA-based trading strategy, compute performance metrics, and visualize the backtesting results.


Now lets dive into the Modules one by one in this class!!

def __init__(self, symbol, SMA_S=50, SMA_L=200, start=None, end=None):

 It Initializes the SMABacktester object and initializes all the parameters required(stock symbol, SMA_S, SMA_L, start date and the end date required)

