from operator import index
from threadpoolctl import _main
import pandas as pd
import os


def daily_stock_return(path):

    def formula(t, t_1):
        return 0 if t_1 == 0 else (t - t_1) / t_1

    pre = 0
    df = pd.read_csv(path)
    print(type(df))
    df.insert(df.shape[1], "Daily Return", 0)
    for idx, row in df.iterrows():
        curr = row["Close"]
        df.loc[idx, "Daily Return"] = formula(curr, pre)
        pre = curr

    df = df.loc[1:, :]
    df.to_csv("after_{}".format(os.path.basename(path)), index=None)




if __name__ == "__main__":
    daily_stock_return(r"TSLA_20200503_20201106.csv")