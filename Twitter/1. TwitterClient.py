from tweepy import API
from tweepy import OAuthHandler

consumer_key = "Y5f62Ow0jKjmnYl02RuyA1ReB"
consumer_secret = "w4ZEPPTfJUVNi95o7cwvUGjWK9WbbQpPlG67CvZnexSO7mi3fj"
access_token = "1598228520764776448-Ltx3raB1NZ5liCRyxJJhaVeRWtz8Nw"
access_secret = "c4SFyO4niQpPuosjf2g6KcTQfj4peoK9Ttk7yi8hAsocW"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
client = API(auth)

print("Auth: ", auth)
print("Client: ", client)