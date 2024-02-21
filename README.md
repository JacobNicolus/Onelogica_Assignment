# Onelogica_Assignment
This is the library made for onelogica and consists of fuctions for common algorithmic trading.

##welldocumented lib..

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


Next is to evaluate strategy...

def evaluate_strategy():


This Python function evaluates a trading strategy using three key performance metrics:

1. Sharpe Ratio: Measures risk-adjusted returns.

2. Sortino Ratio: Focuses on downside risk.

3. Calmar Ratio: Evaluates returns relative to maximum drawdown.

The function calculates these metrics and returns them as a dictionary. They provide insights into the strategy's performance and risk profile.


The Final is the analysis part....

def analysis():

This methodis designed to plot the backtesting results of a trading strategy.


>>> If `self.results` is `None`, indicating that the backtesting hasn't been performed yet, it prints a message prompting the user to run the test.

>>> If `self.results` contains backtesting results:
  
  - It constructs a title for the plot based on the symbol (`self.symbol`), short moving average (`self.SMA_S`), and long moving average (`self.SMA_L`) parameters.
  
  - It plots two columns of `self.results` DataFrame: `"returnsbuy&hold"` and `"returnsstrategy"`.
  
  - The plot title includes information about the symbol and the moving average parameters.
  
  - The plot is displayed with a size of 12x8 inches.

This method is intended to provide a visual representation of the backtesting results, comparing the returns of the strategy against a buy-and-hold approach.


In the main.py, I have done and evaluated the library for RELIANCE INDUSTRIES you can try for any companies you wish to check...


And finally you should be having the doubt of SMA, SMA_S and SMA_L 

###### SMA(SIMPLE MOVING AVERAGE)

It's a technical analysis indicator commonly used in finance and trading to analyze and smooth out price data over a specific time period. The Simple Moving Average is calculated by adding up the closing prices of a security or asset over a certain number of periods (e.g., days) and then dividing that sum by the number of periods.

For example, a 50-day SMA is calculated by summing up the closing prices of the last 50 days and then dividing that sum by 50. The result is a single data point on the chart, representing the average price over the last 50 days. As new data becomes available, the oldest data point is dropped from the calculation, and the newest data point is included, thus creating a moving average line that moves with the price action.

SMA is used for various purposes in trading and technical analysis, including identifying trends, determining support and resistance levels, and generating trading signals. It helps traders smooth out price fluctuations and identify the underlying trend in the price movement of an asset. Different SMA periods (e.g., 50-day, 100-day, 200-day) are commonly used depending on the trader's strategy and time horizon.

SMA_S is simple moving average short like for  short period (In code we took 50)

SMA_L is simple moving average long like for long period(In code we took 200)


### Done 

##### Thanks! for going through this README file
