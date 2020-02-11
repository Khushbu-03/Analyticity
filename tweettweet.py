import tweepy
import json
import csv

consumerkey = "UVi7AriRjq77qkDwrZR3KB7PA"
consureSecret = "n8iYeS2LYkS87sTjeD6bhpn7OPqZQYmRyha3mW7G152eG76ctf"
accessToken = "2912257634-wPWg2vggF9SUsVLACp2B5UOfo5tox8qCxKqyi1T"
accessTokenSecret = "0fuALeCXEwStrLGlbHQXxRB97CnI0XZhKrra3lY98L8Uz"

auth = tweepy.OAuthHandler(consumerkey, consureSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

searchItem = input("Please enter keyword/ hashtag to search about: ")
noOfSearchItems = int(input("Please enter how many tweets you want: "))

print(noOfSearchItems)

tweets =  tweepy.Cursor(api.search,q=searchItem,since="2018-05-01").items(noOfSearchItems)
data =[]

for status in tweets:
        print(status.text)
        tweet_details = {}
        tweet_details['id'] = status.id
        tweet_details['created'] = status.created_at.strftime("%d-%b-%Y")
        tweet_details['tweet_text'] = status.text
        data.append(tweet_details)

print(data)
with open('tweet.json', 'w') as f:
    json.dump(data, f)


#search_tweets = [tweet fpor tweet in tweepy.Cursor(api.search, q=searchItem).items(noOfSearchItems)]
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