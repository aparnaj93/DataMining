import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "enter your access token"
access_token_secret = "enter your access token key"
consumer_key = "enter your consumer key"
consumer_secret = "enter your consumer secret"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Donald Trump', '#POTUS', 'Fake News'])
