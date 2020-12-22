import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# from sklearn.datasets import load_files

df = pd.read_csv(r"code\news\AMZN_20201106.csv")
# train = pd.read_csv(r"code\news\ZM_20201106.csv")
X = df["content"].values

vec = TfidfVectorizer(stop_words="english")
vec.fit(X)
# print(vec.vocabulary_)
features = vec.transform(X)

cls = KMeans(n_clusters=4)
cls.fit(features)
cls.predict(features)

# to get cluster labels for the dataset used while
# training the model (used for models that does not
# support prediction on new dataset).
# cls.labels_
# reduce the features to 3D
pca = PCA(n_components=3)
reduced_features = pca.fit_transform(features.toarray())

from mpl_toolkits.mplot3d import Axes3D
# reduce the cluster centers to 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
cluster_centers = pca.transform(cls.cluster_centers_)
ax.scatter(
    reduced_features[:,0],
    reduced_features[:,1],
    reduced_features[:,2],
    c=cls.predict(features),
    cmap='viridis'
)
ax.scatter(
    cluster_centers[:,0],
    cluster_centers[:,1],
    cluster_centers[:,2],
    marker='^',
    c='black'
)
plt.show()
