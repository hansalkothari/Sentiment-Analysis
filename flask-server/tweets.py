import tweepy

# Twitter API1 credentials

consumer_key = "i7ZoAPOib35dU7MMJJBYsE2G5"
consumer_secret = "Y6BAoprof7Xb0g0irAMiYXtbhdjAyvLulSBrvpwFpaI5VwZL5v"
access_token = "833244248980017152-NKxHaTtBskKbg499w9sRksQq1KvsR3p"
access_secret = "mdE7alpC1puYYaenOpSsQDDFvgNrMhKzo2eQzYzIFA2lu"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAD8vmgEAAAAAZoKZZWxRyrVNiLw2oXjKsLd%2FQGI%3DJP7p83P7G3rGFGm7qah7diU3LaeCwYDtq2zEIuQfDIfO4nid9e'

# auth = tweepy.OAuth1UserHandler(
#     consumer_key=consumer_key,
#     consumer_secret=consumer_secret,
#     access_token=access_token,
#     access_token_secret=access_secret
# )

auth = tweepy.OAuth2BearerHandler(bearer_token=bearer_token)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Define the search term and number of tweets to fetch
search_term = "python"
num_tweets = 10

# Fetch the tweets using the Twitter API v2 and Tweepy
tweets = api.search_tweets(
    q=search_term,
    max_results=num_tweets,
    
)

# Print out the full text of each tweet
for tweet in tweets:
    print(tweet)