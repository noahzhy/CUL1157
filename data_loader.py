import os
# import sys
import glob
import numpy as np
import pandas as pd
import gensim
import datetime

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    # ['neg', 'neu', 'pos', 'compound']
    return score['compound']


def match_date(stock_code:str):
    code = stock_code.upper()
    news_f = glob.glob("news/{}_*.csv".format(code))[0]
    news_df = pd.read_csv(news_f)

    print(news_f, '\t', news_df.shape)
    vecs = list()

    for idx, row in news_df.iterrows():
        t0 = datetime.datetime.strptime(row['datetime'], "%Y-%m-%d %H:%M:%S %z")
        row['datetime'] = str(t0)[:10]
        title_content = ". ".join([row['title'], row['content']])
        vec = sentiment_analyzer_scores(title_content)
        vecs.append(vec)

    news_df.insert(news_df.shape[1], 'compound_score', vecs)
    news_df.to_csv(news_f, index=False)


if __name__ == "__main__":
    for t in glob.glob("stock/*.csv"):
        code = os.path.basename(t).split('_')[0]
        match_date(code)

