import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SMABacktester():

    def __init__(self,symbol,SMA_S=50, SMA_L=200,start=None,end=None):
        self.symbol=symbol
        self.SMA_S=SMA_S
        self.SMA_L=SMA_L
        self.start=start
        self.end=end
        self.results=None
        self.get_data()
        self.test_results()
        
    def get_data(self):
        df=yf.download(self.symbol,start=self.start,end=self.end)
        data=df.Close.to_frame()
        data["returns"]=np.log(data.Close.div(data.Close.shift(1)))
        data["SMA_S"]=data.Close.rolling(self.SMA_S).mean()
        data["SMA_L"]=data.Close.rolling(self.SMA_L).mean()
        data.dropna(inplace=True)
        self.data2=data
        
        return data
    
    def test_results(self):
        data=self.data2.copy().dropna()
        data["position"]=np.where(data["SMA_S"]>data["SMA_L"],1,-1)
        data["strategy"]=data["returns"]*data.position.shift(1)
        data.dropna(inplace=True)
        data["returnsbh"]=data["returns"].cumsum().apply(np.exp)
        data["returnsstrategy"]=data["strategy"].cumsum().apply(np.exp)
        perf=data["returnsstrategy"].iloc[-1]
        outperf=perf-data["returnsbh"].iloc[-1]
        self.results=data
        
        ret=np.exp(data["strategy"].sum())
        std= data["strategy"].std()*np.sqrt(252)
    
        return ret,std
        #return round(perf,6), round(outperf,6)

    def sharpe_ratio(self):
        returns_strategy = self.results["strategy"]
        sharpe = np.sqrt(252) * (returns_strategy.mean() / returns_strategy.std())
        return sharpe

    def sortino_ratio(self):
        returns_strategy = self.results["strategy"]
        downside_returns = returns_strategy[returns_strategy < 0]
        downside_std = downside_returns.std()
        sortino = np.sqrt(252) * (returns_strategy.mean() / downside_std)
        return sortino

    def calmar_ratio(self):
        returns_strategy = self.results["strategy"]
        max_drawdown = (returns_strategy / returns_strategy.cummax() - 1).min()
        calmar = returns_strategy.mean() / abs(max_drawdown)
        return calmar
    
    def plot_results(self):
        if self.results is None:
            print("Run the test please")
        else:
            title="{}| SMA_S={} | SMA_L{}".format(self.symbol,self.SMA_S, self.SMA_L)
            self.results[["returnsbh","returnsstrategy"]].plot(title=title, figsize=(12,8))
        
        


# In[ ]:




