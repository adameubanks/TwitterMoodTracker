import tweepy
import csv

#Twitter API credentials
api_key = "oHE7XfwvO3TekFfoqEboGn1tv"
api_secret_key = "Q77xcmzuA2qv2CSOHvFIBVDoAIGbVOWlEYfSQ7v9rERmsqPic4"
access_token = "2586611642-KNdWz6VQ7Lss7TI36tfj007AU0goXRaUhxrS07r"
access_token_secret = "5CbIPjhANXPOVtsTdLxEi9FqVtJorXKc41qtmSKTdu1QJ"


def get_all_tweets(search_term,time):
	#authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
    all_tweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
    tweets = api.search(q=search_term, lang='en', count=2000, tweet_mode='extended')

	#save most recent tweets
    all_tweets.extend(tweets)

	#transform the tweepy tweets into a 2D array that will populate the csv
    out_tweets = [[tweet.created_at, tweet.full_text, tweet.place] for tweet in all_tweets]

	#write the csv
    extension = "covid-19_"+time
    with open('%s_tweets.csv' % extension, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text","place"])
        writer.writerows(out_tweets)
    pass
