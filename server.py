from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'Z0QgUmbUY4ifhdfaX4sSRsvyv'
consumer_secret = 'IqU7heSldQ7vFqqhbZZjjuYZ6dd59LzggdUYhKAAESGCYvMCfL'

access_token = '391991107-3foNWZmSBXWnaV4k5iU9gBgCpEiwK3paQsB2ewpe'
access_token_secret = 'xLbNg8K6Z7a8eKQS5ZNzF2zSrOUS5wuoRJA2qqqDfRxcA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


