import re
import tweepy
import datetime
import pandas as pd
from tweepy import OAuthHandler


# for recording each tweets' data
class Record(object):
    def __init__(self, query:str, date:str, id_str:str, text:str, followers:int):
        self.query = query
        self.created_at = self.to_utc_time(date)
        self.id_str = id_str
        self.text = text
        self.followers = followers

    @staticmethod
    def to_utc_time(obj:datetime.datetime)->str:
        """ 
        Converting datetime to format as '2020-01-01 23:59:59 Wed'
        """
        return obj.strftime("%Y-%m-%d %H:%M:%S %a")


class TwitterClient(object):
    def __init__(self, start="20200930", end="20201029", min_followers=1000):
        api_key = 'q1YQBU6DWIHzb1XkAkR8aKM7q'
        api_key_secret = 'PCPzec9Vj4oHzYL1iuN97qbmDWIR7PpJAJnzJOkLOsOUj4f3cd'
        access_token = '1167956868-dA2N5In606l7jllX6Hex99s85OUaSSOUG3Dq5iv'
        access_token_secret = 'gYrXi9dyzMYshA4zHYSAKoVKXL6pFRVZYWkedqYODR6dZ'

        # limit threshold
        # self.min_ret = 0
        self.min_followers = min_followers

        # date limited
        self.start_date = start
        self.end_date = end

        try:
            self.auth = OAuthHandler(api_key, api_key_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except: 
            print("!!! Authentication Failed")

    # only using for cleaning data or predict the sentiment via textBot, vaderSentiment could handle with special symbols
    # @staticmethod
    # def clean_tweet(tweet):
    #   return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweets(self, query, count=100, output=False)->list:
        tweets = list()
        try:
            # res_tweets = self.api.search(
            #     q=query,
            #     count=count,
            #     lang='en',
            # )
            res_tweets = self.api.search_30_day(
                environment_name="stock",
                query=query,
                # do not support choose language in premium search
                # lang="en",
                fromDate="{}0000".format(self.start_date),
                toDate="{}2359".format(self.end_date),
            )

            for tweet in res_tweets:
                parsed_tweet = tweet.text
                # reserved for missing values or preprocessing of sentiment analyze

                created_at = tweet.created_at
                id_str = tweet.id_str
                num_followers = tweet.user.followers_count

                if num_followers >= self.min_followers:
                    record_dict = Record(query, created_at, id_str, parsed_tweet, num_followers).__dict__
                    # # avoid duplication
                    # if record_dict not in tweets:
                    tweets.append(record_dict)
                    if output:
                        print(record_dict)

        except Exception as e:
            print("Error:", e)
        return tweets


if __name__ == "__main__":
    start = "20200930"
    end = "20201001"
    tc = TwitterClient(start, end)
    # free premium search not allow to query with '$' hashtag
    # query = "$AMZN"
    query = "AMZN"
    res = tc.get_tweets(query, output=False)

    # list of dict -> DataFrame
    df = pd.DataFrame(res)
    # avoid duplication, keep only the tweets of who have most followers
    df = df.sort_values(by="followers" , ascending=False)
    df.drop_duplicates(subset={"text", "followers"}, keep='first', inplace=True)
    # restore the sort
    df = df.sort_values(by="created_at" , ascending=False)

    df.to_csv("{}_{}_{}.csv".format(query, start, end), index=None)
