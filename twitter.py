import tweepy
import loc
from time import sleep
import pandas as pd
import numpy as np
import math
#loc
#Add your credentials here
from wiki import country_bike
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
import seaborn as sns


# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '195257267-gRf3Z4LzQxi1Rsd7JzSzX6z5AynGILx9Gau7athR'
ACCESS_SECRET = 'mTM4Y2nYSc9F2AWdz2gE3ZTETxGIZIlqaU2bE8LK7PFbV'
CONSUMER_KEY = 'o9OwWjiOukxq0FUGxkiQBfYIG'
CONSUMER_SECRET = 'ETAVneQWZKl8P92E8hMM6nRjX2PjUxjZbbbbp8DQx1XOtT0vJ6'

#Setup access to API
# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


api = connect_to_twitter_OAuth()

gc = list(loc.lat_lon[loc.your_place])
gc = (str(gc[0])+ "," +str(gc[1])+ "," + "1000km")

df_1 = {}

# fuction to extract data from tweet object

def extract_tweet_attributes(tweet_object):
    # create empty list
    tweet_list =[]
    # loop through tweet objects
    for tweet in tweet_object:
        tweet_id = tweet.id # unique integer identifier for tweet
        text = tweet.full_text # utf-8 text of tweet
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at # utc time tweet created
        source = tweet.source # utility used to post tweet
        reply_to_status = tweet.in_reply_to_status_id # if reply int of orginal tweet id
        reply_to_user = tweet.in_reply_to_screen_name # if reply original tweetes screenname
        retweets = tweet.retweet_count # number of times this tweet retweeted
        favorites = tweet.favorite_count # number of time this tweet liked
        # append attributes to list
        tweet_list.append({'tweet_id':tweet_id,
                          'text':text,
                          'favorite_count':favorite_count,
                          'retweet_count':retweet_count,
                          'created_at':created_at,
                          'source':source,
                          'reply_to_status':reply_to_status,
                          'reply_to_user':reply_to_user,
                          'retweets':retweets,
                          'favorites':favorites})
    # create dataframe
    df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                           'text',
                                           'favorite_count',
                                           'retweet_count',
                                           'created_at',
                                           'source',
                                           'reply_to_status',
                                           'reply_to_user',
                                           'retweets',
                                           'favorites'])
    return df



for v in country_bike[loc.your_location]:
    #print(v)
    sleep(1)
    searchString = v.split()[0] + " bike" + '-filter:retweets'  # + " bike" #+ '-filter:retweets'
    cursor = tweepy.Cursor(api.search, geocode=gc, q=searchString, count=200, lang="en", tweet_mode='extended')
    # df = "bike " + v
    df_1[v] = extract_tweet_attributes(cursor.items())

def remove_url(txt):
    """Replace URLs found in a text string with nothing
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


tweets_no_urls = [remove_url(text) for text in df_1['AJS']['text']]
sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]

print(tweets_no_urls)

# Create dataframe containing the polarity value and tweet text
# Create list of polarity valuesx and tweet text
sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]
sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])

all_sentiments = pd.DataFrame(columns=['polarity','tweet','bike'])



for k in df_1:
    print("getting sentiments for : " + str(k))
    tweets_no_urls = [remove_url(text) for text in df_1[k]['text']]
    sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]
    sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]
    sentiment_df = pd.DataFrame(sentiment_values, columns=['polarity','tweet'])
    sentiment_df['bike'] = k
    print("shape.......",sentiment_df.shape[0])
    all_sentiments=all_sentiments.append(sentiment_df)
    print("shape.......!!!!!!!",all_sentiments.shape[0])



print(sentiment_df)
all_sentiments.append(sentiment_df)
print(all_sentiments)
# Remove polarity values equal to zero
sentiment_df = sentiment_df#[sentiment_df.polarity != 0]




def pol_to_senti(p):
    if p == 0:
        return 'neutral'
    elif p > 0:
        return 'positive'
    else :
        return 'negative'

s = [pol_to_senti(pol) for pol in all_sentiments['polarity']]

all_sentiments['sentiments'] = s
print(all_sentiments.sentiments.value_counts())
print(all_sentiments.sentiments.value_counts(normalize=True) * 100)
#fig, ax = plt.subplots(figsize=(8, 8))
print(all_sentiments)



b = np.unique(all_sentiments.bike)






print(np.unique(all_sentiments.bike))




###final 
'''
print(len(b))

x1 = all_sentiments[all_sentiments.bike==b[0]][['bike','polarity']]
x2 = all_sentiments[all_sentiments.bike==b[1]][['bike','polarity']]
x3 = all_sentiments[all_sentiments.bike==b[2]][['bike','polarity']]
x4 = all_sentiments[all_sentiments.bike==b[3]][['bike','polarity']]
x5 = all_sentiments[all_sentiments.bike==b[4]][['bike','polarity']]
x6 = all_sentiments[all_sentiments.bike==b[5]][['bike','polarity']]

fig,ax = plt.subplots(3,2)

x1.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax[0,0],
             color="purple")

x2.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax[0,1],
             color="purple")
x3.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax[1,0],
             color="purple")
x4.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax[1,1],
             color="purple")
x5.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax[2,0],
             color="purple")
x6.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax[2,1],
             color="purple")

ax[0,0].set_title(b[0])
ax[0,1].set_title(b[1])
ax[1,0].set_title(b[2])
ax[1,1].set_title(b[3])
ax[2,0].set_title(b[4])
ax[2,1].set_title(b[5])
#plt.title("Sentiments distribution from Tweets")
plt.show()

print(x1)

bike_frames = {}

for bike in b:
    print(bike)
    bike_frames[bike] = all_sentiments[all_sentiments.bike==bike][['bike','polarity']]

print(bike_frames[b[0]])
r = 0

if len(b)/2 == 0:
    r = int(math.floor(len(b)/2))
else:
    r = int(math.floor(len(b)/2) + 1)
print(r)

which_bike = len(b)


'''

bike_frames = {}

for bike in b:
    print(bike)
    bike_frames[bike] = all_sentiments[all_sentiments.bike==bike][['bike','polarity']]

####and again

#  SUBPLOTS - FOR Loop
rowCnt = len(b)
colCnt = 1     # cols:  overall, no disease, disease
subCnt = 1     # initialize plot number
print(rowCnt,colCnt,subCnt)
plt.close('all')
fig = plt.figure(figsize=(3,8))

for i,x in zip(bike_frames.values(),bike_frames.keys()):
    # OVERALL subplots
    print(x,"at index: ", subCnt)
    fig.add_subplot(rowCnt, colCnt, subCnt)
    plt.title("sentiments on " + x, fontsize=8,color='purple')
    plt.xlabel('polarity (> 0 is positive)', fontsize=8)
    sns.distplot(i['polarity'],bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1])
    subCnt = subCnt + 1
plt.tight_layout()
plt.show()
