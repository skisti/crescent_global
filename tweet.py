import tweepy
import csv
import datetime
import json

# Load credentials from json file
with open("credentials.json", "r") as f:
    cred = json.load(f)

# Authorizing for credentials
auth = tweepy.OAuthHandler(cred['user_id'], cred['user_pass'])
auth.set_access_token(cred['access_token'], cred['access_secret'])

api = tweepy.API(auth)

username = "#blm"
startDate = datetime.datetime(2020, 12, 4, 0, 0, 0)
endDate = datetime.datetime(2020, 11, 27, 0, 0, 0)

tweets = []
tmp = api.user_timeline(username)
for tweet in tmp:
    if endDate > tweet.created_at > startDate:
        tweets.append(tweet)

# Filename we will write into
with open('output_twitter.csv', 'wb') as file:
    f = csv.writer(file)

    # header row for spreadsheet
    f.writerow(['username', 'timestamp'])

    # searching for the matching hashtags from tweets
    for tweet in tweepy.Cursor(api.search, q='#blm' + '-filter:retweets', lang="en").items(100):
        f.writerow([tweet.created_at, tweet.username])
