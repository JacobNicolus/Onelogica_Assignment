# Onelogica_Assignment
This is the library made for onelogica and consists of fuctions for common algorithmic trading. 

#### SMABacktester

SMABacktester is a Python class for backtesting SMA-based trading strategies. It provides functionality to retrieve historical price data from Yahoo Finance, preprocess the data, backtest the SMA-based trading strategy, compute performance metrics, and visualize the backtesting results.


Now lets dive into the Modules one by one in this class!!

def __init__(self, symbol, SMA_S=50, SMA_L=200, start=None, end=None):

 It Initializes the SMABacktester object and initializes all the parameters required(stock symbol, SMA_S, SMA_L, start date and the end date required)

Moving on to next module 

 def get_data(self):
  
  
  Retrieves historical price data from Yahoo Finance and preprocesses it and Returns a DataFrame containing close of the day, returns for the day , SMA_S and SMA_L. so, the returns of the day is calculated as the logrithmic of todays close to the previous days close and also drops if any NA values..


Now here is the main thing 

def test_results():


The test_results method is responsible for backtesting the SMA-based trading strategy and computing performance metrics. It calculates the returns of the trading strategy, compares them with a buy-and-hold strategy, and computes the outperformance.



1)Copy the preprocessed data (self.data2) and drop any missing values.

2)Compute the trading positions based on the crossover of short-term and long-term SMAs(so if SMA_S>SMA_L then position is 1 else -1)

3)Calculate the strategy returns and cumulative returns.

4)Compute the performance and outperformance.

5)Store the results in self.results.

6)If also it can Compute the total returns and standard deviation of the strategy.


It Returns

performance (float): The final performance of the trading strategy.
Outperformance (float): The outperformance of the trading strategy compared to a buy-and-hold strategy.
Process


