import re
from datetime import datetime, timezone
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS


def get_news(query):
    timestamp = datetime.now().strftime("%Y%m%d")
    print("[{}] start collecting '{}'...".format(timestamp, query))
    datas = list()

    page = 1
    max_page = 1

    ## nd -> days

    while True:
        url = (
            'https://wallmine.com/screener/async?'
            'd=d&'
            'fo=s&'
            'nd=186&'
            'o=m&'
            'page={}&'.format(page)+
            'r=n&'
            's={}&'.format(query)+
            'symbols={}'.format(query)
        )
        req = requests.get(url)
        html_text = req.text
        # print(html_text)
        bs = BS(html_text, 'html5lib')
        rows = bs.findAll('tr', {'class': "js-clickable-row clickable-row"})

        print("page: {}".format(page))
        for i in rows:
            data_dict = dict()

            title = i.findAll('a', {'target': "_blank"})[0].getText()
            content = i.findAll('td', {'class': "js-tooltip"})[0]['title']
            small = BS(content, 'html5lib')
            tmp = small.findAll('time', {'class': "timeago"})[0]['title']
            content = re.compile('<small>.*\n<br />\n').sub('', content.strip())

            data_dict = {"datetime":tmp, "title":title, "content":content}
            datas.append(data_dict)

        page += 1
        try:
            # raise the error to make sure break the loop
            bs.findAll('li', {'class': "page-item"})[-1].getText()
        except IndexError as ie:
            break

    df = pd.DataFrame(datas)
    df.to_csv("news/{}_{}.csv".format(query, timestamp), index=None)


if __name__ == "__main__":
    ## focus on
    candidates = ['MSFT', 'AMZN', 'GOOGL', 'AAPL', 'FB', 'ZM', 'VMW', 'NVDA', 'AMD', 'TSLA']
    for c in candidates:
        get_news(c)
