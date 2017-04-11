import tweepy


consumer_key = 'mi1e5x0VX7m7Us5DTD9vovsJR'
consumer_secret = 'wTKhyMG6KRRpvHRns4LExqhvSim3SF7VcVwgohsNZxa2i08MUf'
access_token = '851465774283841537-mbn9MKlb9aqqeEJrqlGzsQaYkdsY3rc'
access_token_secret = '7wIdoEawI1AYk1gjb6xfWQzuZddyGIKZNV5CdzTsFkXI1'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

myStream.filter(track=['AAPL'])