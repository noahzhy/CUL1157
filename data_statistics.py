import pandas as pd
import os
import glob


def statistics(path):
    for f in glob.glob(path+'/*.csv'):
        f_name = os.path.basename(f).split('_')[0]
        df = pd.read_csv(f)
        total_news = df.shape[0]
        df['datetime'] = df['datetime'].map(lambda x: str(x).split(" ")[0])
        day_news = df.groupby('datetime').size().max()
        print('{}\ttotal: {}\tMax day: {}'.format(f_name, total_news, day_news))


if __name__ == "__main__":
    path = "news"
    statistics(path)