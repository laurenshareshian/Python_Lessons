import twurl2
import hidden
import tweet_generator
import string
import binascii

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/update.json'

num_of_tweets = 20

for i in range(num_of_tweets):

    tweet=tweet_generator.get_tweet()

    new_tweet=''
    for char in tweet:
        if char in string.punctuation or char ==' ':
            code=binascii.hexlify(str.encode(char))
            new_tweet=''.join([new_tweet, '%', code.decode('ascii')])
        else:
            new_tweet = ''.join([new_tweet, char])

    secrets = hidden.oauth()
    full_url=''.join([TWITTER_URL,'?','status=', new_tweet])
    print(full_url)
    twurl2.oauth_req( full_url, secrets['token_key'], secrets['token_secret'], "POST")


