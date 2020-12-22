import os
# import sys
import glob
import numpy as np
import pandas as pd
import gensim
import datetime

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from sklearn.cluster import *
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_daily_score(file_name):
    final_news = pd.read_csv(file_name)
    unique_dates = final_news['datetime'].unique()
    grouped_dates = final_news.groupby(['datetime'])
    keys_dates = list(grouped_dates.groups.keys())

    neg_cs = []
    neu_cs = []
    pos_cs = []
    comp_cs = []

    for key in grouped_dates.groups.keys():
        data = grouped_dates.get_group(key)
        # neg,neu,pos,comp
        # _max = data["compound_score"].max()
        # _min = data["compound_score"].min()
        neg = data["neg"].max()
        neu = data["neu"].max()
        pos = data["pos"].max()
        comp = data["comp"].max()

        neg_cs.append(neg)
        neu_cs.append(neu)
        pos_cs.append(pos)
        comp_cs.append(comp)

        # _sum = data["compound_score"].sum()

        # if _max > 0:
        #     max_cs.append(_max)
        # else:
        #     max_cs.append(0)
        
        # if _min < 0:
        #     min_cs.append(_min)
        # else:
        #     min_cs.append(0)

        # mean_cs.append(_mean)
        # sum_cs.append(_sum)
        
    # daily_compound_index = {
    #     'datetime':keys_dates,
    #     'max_scores':max_cs,
    #     'min_scores':min_cs,
    #     'mean_scores':mean_cs,
    #     'sum_scores':sum_cs
    # }
    daily_df = {
        'datetime':keys_dates,
        'neg':neg_cs,
        'neu':neu_cs,
        'pos':pos_cs,
        'comp':comp_cs
    }
    daily_index_df = pd.DataFrame(daily_df)

    # final_scores = []
    # for i in range(len(daily_index_df)):
    #     final_scores.append(daily_index_df['comp'].values[i] + daily_index_df['comp'].values[i])

    # daily_index_df['final_scores'] = final_scores
    # print(daily_index_df.head())
    if not os.path.exists('score'):
        os.mkdir('score')
    daily_index_df.to_csv('score/{}'.format(os.path.basename(file_name)), index=False)


if __name__ == "__main__":
    for i in glob.glob('news/*'):
        get_daily_score(i)