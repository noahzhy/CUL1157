# Manual

> Manual for each .ipynb file, all .ipynb script in folder '[Final Project](https://drive.google.com/drive/folders/1dUj8PMuTDCvmBDygvMs86EpHqxwBNjqE?usp=sharing)'.

```powershell
.
│  data_generate.ipynb
│  data_visualization.ipynb
├─news
└─stock
```

## Requirements

* BeautifulSoup
* yfinance
* pandas-datareader

**Install requirements via pip3**

```powershell
pip3 install -U bs4 yfinance pandas-datareader
```

## Guide

### Quick start

### data_generate.ipynb

Collecting the related historical finance news and stock price data via given stock code.

```python
## only support stock code
candidates = [
    'MSFT', 'AMZN', 'GOOGL', 'AAPL', 'FB', 'TSLA', 'PFE', 'MRNA', 'AAL', 'DAL'
]
days = 180
save = True
## instance StockDataGen object
data_gen = StockDataGen(candidates, days, save)
data_gen.data_gen()
```

Modify the `days`, `save`, `candidates` as what you want to collected in last code cell, then run all code cells or just press `Ctrl+F9`.











#### StockDataGen object

```python
StockDataGen(candidates, days, save)
```

Set parameters:

* `candidates` The stock code of companies, should be a list type

* `days` Historical finance news of the number of days before today, default is 180
* `save` Save to the .csv file or not, collected data will be saved in 'news' and 'stock' folders, default is True

```python
## only support stock code
candidates = [
    'MSFT', 'AMZN', 'GOOGL', 'AAPL', 'FB', 'TSLA', 'PFE', 'MRNA', 'AAL', 'DAL'
]
days = 180
save = True
## instance StockDataGen object
data_gen = StockDataGen(candidates, days, save)
data_gen.data_gen()
```

Modify the `days`, `save`, `candidates` as what you want to collected in last code cell, then run all code cells or just press `Ctrl+F9`.




There are three methods in `StockDataGen` objects as following

* `get_stock_price()` get the historical stock data from yahoo finance via given stock code
* `get_news()` get finance news from [wallmine](https://wallmine.com/market/us) via given stock code
* `data_gen()` get stock data and related finance news both

### [data_visualization.ipynb]()

#### [tf-idf_kmeans.ipynb](https://drive.google.com/file/d/1I6yZPe9jIKGHxGVnd6AUmMRbOYWF3QYC/view?usp=sharing)

Modify the second code cell to load data, some supported finance news data in folder `news/`. 

```python
## load data
df = pd.read_csv(r"news\AMZN_20201106.csv")
X = df["content"].values
```

The word frequency could be viewed in the last code cell.

```python
words_frequency = vec.vocabulary_
words_frequency = sorted(words_frequency.items(), key=lambda v: v[1], reverse=True)
words_frequency
```

The TF-IDF vectors in 3D space as following, (cluster=4)

![001](C:\Users\e-it\Desktop\001.png)

#### [doc2vec_kmeans.ipynb](https://drive.google.com/file/d/1wKkOj9cx8OsASUVcZqquAcz8fHHZVYhp/view?usp=sharing)

As same as above, modify the second code cell to load news data.

The document embedding vectors in 3D space as following, (cluster=4)

![002](C:\Users\e-it\Desktop\002.png)