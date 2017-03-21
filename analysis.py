import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = 'twitter_data.txt'

tweets_data = []	
#open the Json file and read every line and store it as a tweet
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
# create an empty data frame and include four columns in it
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['location'] = map(lambda tweet: tweet['user']['location'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_location = tweets['location'].value_counts()
plt.show()

fig, ax = plt.subplots() #generate a plot of number of tweets versus languages
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('location', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_location[:5].plot(ax=ax, kind='bar', color='red')

# function to check if keyword is present in tweet or not

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['obamacare'] = tweets['text'].apply(lambda tweet: word_in_text('#obamacare', tweet))
tweets['trumpcare'] = tweets['text'].apply(lambda tweet: word_in_text('#trumpcare', tweet))

# create a new data frame that contains every tweet containing #obamacare

obama_loc=[]
tweets_obama = pd.DataFrame()
for index, tweet in enumerate(tweets['obamacare']):
	if tweet==True:
		obama_loc.append(tweets['location'][index])

tweets_obama['obama_loc']=obama_loc	
print tweets_obama['obama_loc']

# create a new data frame that contains every tweet containing #trumpcare
trump_loc=[]
tweets_trump = pd.DataFrame()
for index, tweet in enumerate(tweets['trumpcare']):
	if tweet==True:
		trump_loc.append(tweets['location'][index])

tweets_trump['trump_loc']=trump_loc	
print tweets_trump['trump_loc']
	
#print tweets['trumpcare'].value_counts()[True]





