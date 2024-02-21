import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SMABacktester():
    """
    A class for backtesting SMA-based trading strategies.

    Attributes:
        symbol (str): The symbol of the asset to backtest.
        SMA_S (int): The short-term SMA period (default: 50, adjust to 5 or to your convenience if start and end dates are within a month).
        SMA_L (int): The long-term SMA period (default: 200, adjust to 10 or to your convenience if start and end dates are within a month).
        start (str): Start date for data retrieval (YYYY-MM-DD).
        end (str): End date for data retrieval (YYYY-MM-DD).
        results (DataFrame): The backtesting results.
    """
    def __init__(self,symbol,SMA_S=50, SMA_L=200,start=None,end=None):
        """
        Initializes the SMABacktester object.

        Parameters:
            symbol (str): The symbol of the asset to backtest.
            SMA_S (int): The short-term SMA period (default: 50, adjust to 5 or to your convenience if start and end dates are within a month).
            SMA_L (int): The long-term SMA period (default: 200, adjust to 10 or to your convenience if start and end dates are within a month).
            start (str): Start date for data retrieval (YYYY-MM-DD).
            end (str): End date for data retrieval (YYYY-MM-DD).
        """

        self.symbol=symbol
        self.SMA_S=SMA_S
        self.SMA_L=SMA_L
        self.start=start
        self.end=end
        self.results=None
        self.get_data()
        self.test_results()

    def get_data(self):
        """
        Retrieves historical price data from Yahoo Finance and preprocesses it.

        Returns:
            DataFrame: Processed historical price data.
        """
        df=yf.download(self.symbol,start=self.start,end=self.end)
        data=df.Close.to_frame()
        data["returns"]=np.log(data.Close.div(data.Close.shift(1)))
        data["SMA_S"]=data.Close.rolling(self.SMA_S).mean()
        data["SMA_L"]=data.Close.rolling(self.SMA_L).mean()
        data.dropna(inplace=True)
        self.data2=data


        return data

    def test_results(self):

        """
        Backtests the SMA-based trading strategy and computes performance metrics.

        Returns:
            dict: A dictionary containing performance metrics.
        """
        data=self.data2.copy().dropna()
        data["position"]=np.where(data["SMA_S"]>data["SMA_L"],1,-1)
        data["strategy"]=data["returns"]*data.position.shift(1)
        data.dropna(inplace=True)
        data["returnsbuy&hold"]=data["returns"].cumsum().apply(np.exp)
        data["returnsstrategy"]=data["strategy"].cumsum().apply(np.exp)
        perf=data["returnsstrategy"].iloc[-1]
        outperf=perf-data["returnsbuy&hold"].iloc[-1]
        self.results=data

        ret=np.exp(data["strategy"].sum())
        std= data["strategy"].std()*np.sqrt(252)

        #return ret,std
        return {"performance":round(perf,6),"Outperformance" :round(outperf,6)}


    def evaluate_strategy(self):
        """
        Evaluate the strategy using Sharpe ratio, Sortino ratio, and Calmar ratio.

        Returns:
        dict: A dictionary containing the evaluation metrics.
        """
        returns_strategy = self.results["strategy"]

        # Calculate Sharpe ratio
        sharpe = np.sqrt(252) * (returns_strategy.mean() / returns_strategy.std())

        # Calculate Sortino ratio
        downside_returns = returns_strategy[returns_strategy < 0]
        downside_std = downside_returns.std()
        sortino = np.sqrt(252) * (returns_strategy.mean() / downside_std)

        # Calculate Calmar ratio
        max_drawdown = (returns_strategy / returns_strategy.cummax() - 1).min()
        calmar = returns_strategy.mean() / abs(max_drawdown)

        return {"Sharpe Ratio": sharpe, "Sortino Ratio": sortino, "Calmar Ratio": calmar}

    def analysis(self):
        """
        Plot the backtesting results.
        """
        if self.results is None:
            print("Run the test please")
        else:
            title="{}| SMA_S={} | SMA_L{}".format(self.symbol,self.SMA_S, self.SMA_L)
            self.results[["returnsbuy&hold","returnsstrategy"]].plot(title=title, figsize=(12,8))

