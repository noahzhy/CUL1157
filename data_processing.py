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


def news_to_vec(doc:list):
    d2v_model = Doc2Vec.load("models/doc2vec.bin")
    return d2v_model.infer_vector(doc)

def create_words_frequency(features, features_name):
    features_df=pd.DataFrame(features)
    features_df.columns=features_name
    sorted_features = features_df.sum(axis=0).sort_values(ascending=False)
    sorted_features=pd.DataFrame(sorted_features)
    sorted_features=sorted_features.reset_index()
    sorted_features.columns=['Top Words','Counts']
    return sorted_features


def tf_idf_method(doc:list):

    # initilize 
    vec = TfidfVectorizer(
        sublinear_tf=True,
        min_df=1,
        norm='l2',
        ngram_range=(1,3),
        stop_words="english",
        max_features=2000
    )
    features = vec.fit_transform(doc).toarray()
    features_tfidf_names = vec.get_feature_names()
    tfidf_sorted_table = create_words_frequency(features, features_tfidf_names)

    sid = SentimentIntensityAnalyzer()
    title_score = [sid.polarity_scores(sent) for sent in df.title]
    title_score = [sid.polarity_scores(sent) for sent in df.title]


    # compound=[]
    # neg=[]
    # neu=[]
    # pos=[]

    # for i in range(len(title_score)):
    #     compound.append(title_score[i]['compound'])
    #     neg.append(title_score[i]['neg'])
    #     neu.append(title_score[i]['neu'])
    #     pos.append(title_score[i]['pos'])

    # df['compound'] = compound
    # df['neg'] = neg
    # df['neu'] = neu
    # df['pos'] = pos

    # df.head()
    # print(df)


def match_date(stock_code:str):

    X = list()
    Y = list()

    code = stock_code.upper()
    stock_f = glob.glob("stock/{}_*.csv".format(code))[0]
    news_f = glob.glob("news/{}_*.csv".format(code))[0]

    stock_df = pd.read_csv(stock_f)
    news_df = pd.read_csv(news_f)

    print("{}\t{}\n{}\t{}".format(stock_f, stock_df.shape, news_f, news_df.shape))

    for idx, row in stock_df.iterrows():
        # print(row['Date'])
        t0 = datetime.datetime.strptime(row['Date'], "%Y-%m-%d")

        t1 = (t0 - datetime.timedelta(1)).strftime("%Y-%m-%d")
        t1_news = news_df[(news_df['datetime'].str.contains(t1))]
        # print(t1_news.shape)
        
        if not (t1_news.shape[0] == 0):
            # print(t1_news, t1_news.shape)
            print(t1_news.shape)
            dr = row['Daily Return']

            for idx_n, (n, i) in enumerate(t1_news.iterrows()):
                tmp = [i['title'], i['content']]
                fs = tf_idf_method(tmp)
                print(fs.shape)
                # each_day[idx_n] = fs

                X.append(fs)
                Y.append(dr)
            # vec_arry = np.array(vec_arry)
            # print("vec_arry", vec_arry.shape)

    np.savez(
        "{}.npz".format(stock_code),
        x=np.array(X),
        y=np.array(Y)
    )


if __name__ == "__main__":
    text = [
        "8 Wild Numbers From Amazon's Third-Quarter Earnings Report",
        "Here are some of the most amazing figures I found in Amazon's third-quarter report and earnings call.  The third quarter is normally a fairly quiet period for Amazon, seasonally speaking.  Amazon's bottom line nearly tripled compared to the year-ago period, landing at $12.37 per diluted share."
    ]
    # text = "Here are some of the most amazing figures I found in Amazon's third-quarter report and earnings call.  The third quarter is normally a fairly quiet period for Amazon, seasonally speaking.  Amazon's bottom line nearly tripled compared to the year-ago period, landing at $12.37 per diluted share."
    # n2v = tf_idf_method(text)
    # print(n2v)
    # print(n2v.shape)

    # match_date("AMZN", "")
    for t in glob.glob("stock/*.csv"):
        code = os.path.basename(t).split('_')[0]
        match_date(code)

