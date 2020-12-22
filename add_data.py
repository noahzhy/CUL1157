import pandas as pd
import os


def gen_reg_data(code):
    score_df = pd.read_csv('news\{}_20201220.csv'.format(code))
    stock_df = pd.read_csv('stock\{}_20200618_20201220.csv'.format(code))

    _neg = list()
    _neu = list()
    _pos = list()
    _comp = list()
    _scores = score_df['datetime'].to_list()
    # print(_scores)

    for i in range(len(stock_df)):
        if stock_df['Date'].iloc[i] in _scores:
            print(stock_df['Date'].iloc[i])
            _neg.append(score_df['neg'].iloc[i])
            _neu.append(score_df['neu'].iloc[i])
            _pos.append(score_df['pos'].iloc[i])
            _comp.append(score_df['comp'].iloc[i])

        else:
            _neg.append('n/a')
            _neu.append('n/a')
            _pos.append('n/a')
            _comp.append('n/a')

    # print(_mean)
    xy_data = {
        'datetime': stock_df['Date'],
        'neg': _neg,
        'neu': _neu,
        'pos': _pos,
        'comp': _comp,
        'Daily Return': stock_df['Daily Return']
    }

    xy_df = pd.DataFrame(xy_data)
    print(xy_df)
    xy_df.to_csv('test.csv', index=None)
