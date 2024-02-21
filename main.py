import Library as Li

tester = Li.SMABacktester("RELIANCE.NS",SMA_S=5,SMA_L=10,start="2020-01-01",end="2020-02-01")
print(tester.sharpe_ratio())