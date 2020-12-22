import numpy as np
import pandas as pd
from sklearn.linear_model import BayesianRidge, LinearRegression, ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor   # 集成算法
from sklearn.model_selection import cross_val_score    # 交叉验证
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score  
import matplotlib.pyplot as plt
import seaborn as sns

from add_data import gen_reg_data
# %matplotlib inline


gen_reg_data('TSLA')
df = pd.read_csv(
    'test.csv',
    usecols=[
        'Daily Return',
        'neg',
        'neu',
        'pos',
        'comp'
    ]
)

# 可视化数据关系
sns.set(style='whitegrid', context='notebook')   #style控制默认样式,context控制着默认的画幅大小
sns.pairplot(df, size=3)
plt.savefig('x.png')

corr = df.corr()
# 相关度热力图
sns.heatmap(corr, cmap='GnBu_r', square=True, annot=True)
plt.savefig('xx.png')