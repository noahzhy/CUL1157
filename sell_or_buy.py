import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


df = pd.read_csv('score\TSLA_20201217.csv')
stock_df = pd.read_csv('stock\TSLA_20171218_20201217.csv')

_pos = list()
_neg = list()

for i in range(len(df)):
    data = df['datetime'].iloc[i]
    if df['mean_scores'].values[i] > 0.2:
        print("{row} -> Buy".format(row=data))
        _pos.append(data)
    elif df['mean_scores'].values[i] < -0.2:
        print("{row} -> Sell".format(row=data))
        _neg.append(data)

date_pos = []
for i in range(len(stock_df)):
    if stock_df['Date'].iloc[i] in _pos:
        date_pos.append(i)
        
date_neg = []
for i in range(len(stock_df)):
    if stock_df['Date'].iloc[i] in _neg:
        date_neg.append(i)

# print(date_pos)
# print(date_neg)
        
fig, ax = plt.subplots(1,1)
ax.plot(stock_df['Date'], stock_df['Close'],'-^', markevery=date_pos, color='green')
ax.plot(stock_df['Date'], stock_df['Close'],'-v', markevery=date_neg, color='red')
ax.plot(stock_df['Date'], stock_df['Close'])
# ax.plot(stock_df['Date'], stock_df['Daily Return']*100)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.xticks(rotation='60')

ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
# plt.yticks(fontsize=12)
plt.title('Buy or Sell')
plt.legend(['Buy','Sell','Close'])
plt.grid()
plt.show() 