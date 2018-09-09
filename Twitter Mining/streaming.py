from tweepy import Stream,OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECERT'
access_key = 'ACCESS KEY'
access_secret = 'ACCESS SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

class streamer(StreamListener):

    def streamer(self,data):
        try:
            with open('data.json','a') as f:
                f.write(data)
                return True

        except BaseException as  e:
            print('Invalid data: []').format(str(e))
            return True

    def for_error(self,status):
        print(status)
        return True

streamer_twitter = Stream(auth,streamer())
# Now filtering with certain keyword
streamer_twitter.filter(track=['#python'])




