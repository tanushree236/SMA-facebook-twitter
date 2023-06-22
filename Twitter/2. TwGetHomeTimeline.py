import json
from tweepy import Cursor
from tweepy import API
from tweepy import OAuthHandler

consumer_key = "Y5f62Ow0jKjmnYl02RuyA1ReB"
consumer_secret = "w4ZEPPTfJUVNi95o7cwvUGjWK9WbbQpPlG67CvZnexSO7mi3fj"
access_token = "1598228520764776448-Ltx3raB1NZ5liCRyxJJhaVeRWtz8Nw"
access_secret = "c4SFyO4niQpPuosjf2g6KcTQfj4peoK9Ttk7yi8hAsocW"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
client = API(auth)

with open('home_timeline.jsonl', 'w') as f:
    for page in Cursor(client.home_timeline, count = 200).pages(4):
        for status in page:
            f.write(json.dumps(status._json)+"\n")
