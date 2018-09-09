import tweepy as tw
import  json

consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECERT'
access_key = 'ACCESS KEY'
access_secret = 'ACCESS SECRET'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tw.API(auth)

#Defining a method to print and save
def process(tweet):
    print(json.dumps(tweet))
    data = json.dumps(tweet)
    return data
def store(data):
    with open('name.json','w') as outfile:
        json.dump(data,outfile)

# Printing from our timeline
for friend in tw.Cursor(api.friends).items(10):
    z = process(friend._json)
    store(z)



