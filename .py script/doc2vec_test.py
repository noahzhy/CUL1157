import re
import os
import nltk
import random
import pandas as pd
import matplotlib.pyplot as plt
import gensim
from gensim.models import Doc2Vec
from sklearn import metrics
from sklearn.cluster import Birch, KMeans, DBSCAN
from sklearn.decomposition import PCA
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


# nltk.download('stopwords')
# nltk.download('punkt')

from sklearn import metrics
 
import gensim.models as gm
import codecs


## duanju
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import word_tokenize
import numpy as np
# 输入一个段落，分成句子（Punkt句子分割器）

def cut_content(paragraph) -> list:
    paragraph = paragraph.lower()
    #加载punkt句子分割器
    sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
    #对句子进行分割
    sentences = sen_tokenizer.tokenize(paragraph)
    return sentences
 

 
model = "models/doc2vec.bin"
test_docs = "data/test_docs.txt"

#inference hyper-parameters
start_alpha = 0.01
infer_epoch = 1000

#load model
model = gm.Doc2Vec.load(model)

main_data = pd.read_csv('news/TSLA_20201112.csv')
# main_data.head()
# title_content = '. '.join([main_data['title'][0], main_data['content'][0]])
docs = list()
for i in main_data["content"].values:
    tmp = cut_content(i)
    [docs.append(i) for i in tmp]

# print(docs)

doc_words = list()
for doc in docs:
    words = word_tokenize(doc)
    for w in words:
        if len(w) <= 1:
            words.remove(w)
    doc_words.append(words)


# print(doc_words)

# quit()

X = list()
for d in doc_words:
    X.append(
        model.infer_vector(
            d,
            alpha=start_alpha,
            steps=infer_epoch
        )
    )

k = 3
brc = Birch(branching_factor=50, n_clusters=k, threshold=0.1, compute_labels=True)
brc.fit(X)
clusters = brc.predict(X)
labels = brc.labels_
print("Clusters: ")
print(clusters)
silhouette_score = metrics.silhouette_score(X, labels, metric='euclidean')
print("Silhouette_score: ")
print(silhouette_score)

import matplotlib.pyplot as plt
plt.figure()
plt.scatter(datapoint[:, 0], datapoint[:, 1], c=labels, cmap='viridis')
centroidpoint = pca.transform(kmeans_model.cluster_centers_)
plt.scatter(centroidpoint[:, 0], centroidpoint[:, 1], marker="^", s=100, c="black")
plt.show()