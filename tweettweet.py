from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import csv

consumerkey = "kOOMcRvoQb7HjaaHDgs3Yr4Zv"
consureSecret = "CJUzz551Hhd7XwALAQ2i7PeeQqVd75NQ3cFLrDYLzZ4OojSW4f"
accessToken = "2912257634-bHxlSPe8kGsun0Of84of9tEpVNwmWpAoIR3Absw"
accessTokenSecret = "rShl0psMAAtbPNQLjenMF1GqTp0IsuxSrJ9MkgJhwZawl"

class TwitterAuthenticator():
        def authenticate_twitterAPI(self):
                auth = tweepy.OAuthHandler(consumerkey, consureSecret)
                auth.set_access_token(accessToken, accessTokenSecret)
                return auth


class GetTwitterData():

        def __init__(self, twitter_user=None):
                self.twitter_authenticator = TwitterAuthenticator()
                self.twitter_user = twitter_user

        def getTweets(self, searchItem, noOfSearchItems):

                auth = self.twitter_authenticator.authenticate_twitterAPI()
                api = tweepy.API(auth)

                tweets = tweepy.Cursor(api.search,q=searchItem,since="2018-05-01",id=self.twitter_user).items(noOfSearchItems)

               # print(dir(tweets[0]))
                data = []
                for status in tweets:
                        tweet_details = {}
                        tweet_details['id'] = status.id
                        tweet_details['created'] = status.created_at.strftime("%d-%b-%Y")
                        tweet_details['text'] = status.text
                        tweet_details['source'] = status.source
                        tweet_details['likes'] = status.favorite_count
                        tweet_details['retweets'] = status.retweet_count
                        tweet_details['location'] = status.place

                        data.append(tweet_details)

                print(data)
                try:
                     with open('tweet_data.json', 'w') as f:
                        json.dump(data, f)
                except BaseException as e:
                      print("Error on writing data: %s" % str(e))
                      


if __name__ == "__main__":

        searchItem = "happy"
        noOfSearchItems = 50

        twitterTweet = GetTwitterData()
        twitterTweet.getTweets(searchItem, noOfSearchItems)

'''
tweets = tweepy.Cursor(api.search, q=searchItem, lang="English").items(noOfSearchItems)
#search_tweets = str(search_tweets)
#print(type(tweets))

#with open('americatweet1.json', 'w', encoding='utf-8') as file:
for tweet in tweets:
    print(1)
    print(tweet.text)
     #   json.dump(tweet._json, file)
   


tweets = tweepy.Cursor(api.search, q=searchItem, lang="English").items(noOfSearchItems)

for tweet in tweets:
   print(tweet.text)


with open('tweetamerica_file.json', 'w', encoding='utf-8') as file:
    for tweet in tweets:
        json.dump(tweet._json, file)
'''
'''
public_tweets = api.home_timeline()
user = api.me()
print(user.name)

url = ' https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent'
results = requests.get(url)
better_results = results.json()
print(better_results)

#for post in better_results['results']:
 #   print(post['text'].encode('utf-8'))

#better_results['results'][0]['text'].encode('utf-8')

'''



# Streaming API
'''
consumerkey = "mZaY7ob7aiGMjgy0Lbm8NJbVG"
consureSecret = "GQX0FjPHmD0CBUQKtGPtCO1thzC6580zZUx9osbPcfdC2YJ4aA"
accessToken = "2912257634-vK33G569hGGk5ylfzKZVP4zsDlVDPJv1NDc4ReD"
accessTokenSecret = "m6L1nI73Ar6iNwaqr8imBuk8PcNvU4GxiweaPz0AMZJME"

class StdOutLisener(StreamListener):
        def on_data(self, data):
                print(data)
                return True

        def on_error(self, status_code):
                print(status_code)

        auth = OAuthHandler(consumerkey, consureSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
       # api = tweepy.API(auth)
        stream = Stream(auth, listener)

        stream.filter(track=['donald trump'])
'''