import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('stock\GOOGL_20171218_20201217.csv')

df['3_SMA'] = df['Close'].rolling(window=3).mean()
df['5_SMA'] = df['Close'].rolling(window=5).mean()

df = df[df['5_SMA'].notna()]

# SMA trade calls
Trade_Buy=[]
Trade_Sell=[]
for i in range(len(df)-1):
    if ((df['3_SMA'].values[i] < df['5_SMA'].values[i]) & (df['3_SMA'].values[i+1] > df['5_SMA'].values[i+1])):
        print("Trade Call for {row} is Buy.".format(row=df.index[i]))
        Trade_Buy.append(i)
    elif ((df['3_SMA'].values[i] > df['5_SMA'].values[i]) & (df['3_SMA'].values[i+1] < df['5_SMA'].values[i+1])):
        print("Trade Call for {row} is Sell.".format(row=df.index[i]))
        Trade_Sell.append(i)

plt.figure(figsize=(20, 10),dpi=80)
plt.plot(df.index, df['Close'])
plt.plot(df.index, df['3_SMA'], markevery=Trade_Buy, color='green')
plt.plot(df.index, df['5_SMA'], markevery=Trade_Sell, color='red')
plt.xlabel('Date',fontsize=14)
plt.ylabel('Price in Dollars', fontsize = 14)
plt.xticks(rotation='60',fontsize=12)
plt.yticks(fontsize=12)
plt.title('Trade Calls - Moving Averages Crossover', fontsize = 16)
plt.legend(['Close','3_SMA','5_SMA'])
plt.grid()
plt.show() 