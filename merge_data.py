import pandas as pd
import os

score_df = pd.read_csv('news\FB_20201220.csv')
stock_df = pd.read_csv('stock\FB_20200618_20201220.csv')

_mean = list()
_final = list()
_sum = list()
_scores = score_df['datetime'].to_list()
# print(_scores)

for i in range(len(stock_df)):
    if stock_df['Date'].iloc[i] in _scores:
        print(stock_df['Date'].iloc[i])
        _mean.append(score_df['mean_scores'].iloc[i])

        if score_df['final_scores'].iloc[i] > .2:
            _final.append(score_df['final_scores'].iloc[i])
        elif score_df['final_scores'].iloc[i] < -.2:
            _final.append(score_df['final_scores'].iloc[i])
        else:
            _final.append(0)

        _sum.append(score_df['sum_scores'].iloc[i])
    else:
        _mean.append(0)
        _final.append(0)
        _sum.append(0)

# print(_mean)
xy_data = {
    'datetime': stock_df['Date'],
    'mean_scores': _mean,
    'final_scores': _final,
    'sum_scores': _sum,
    'Daily Return': stock_df['Daily Return']
}

xy_df = pd.DataFrame(xy_data)
print(xy_df)
xy_df.to_csv('test.csv', index=None)
