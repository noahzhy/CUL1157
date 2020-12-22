import yfinance as yf
from pandas_datareader import data as pdr

tickers = yf.Tickers('msft aapl')
tickers.tickers.AAPL.history(period="1mo")
# ^ returns a named tuple of Ticker objects

# access each ticker using (example)
# tickers.tickers.MSFT.info

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("aapl", start="2020-01-01", end="2020-04-30")
print(data)