import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "39450642-dE8M0RZq5cKS5MIGZCfRXXWpyWVTYpnlDw8wDnAAo"
access_token_secret = "WAco4CqozFtbmaS9tIuwQb7rpBTFEpH3qNYe9VmtTkX7G"
consumer_key = "tuo61aUYqMrr3Auhufu7wW8Xz"
consumer_secret = "FgNsNnsMd5WpLazYmm6mRW05e1bnBenHJNa6jBFJtf6uIvnW06"

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
