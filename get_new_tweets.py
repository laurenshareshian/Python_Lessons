import twurl2
import json
import hidden

outfile = open('donalddata_new.json', 'w')
wrap_list=[] #since I need to make a twitter API call repeatedly I will wrap the JSON info into a list

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
acct = 'realdonaldtrump'
twittercount=200 #pull 200 tweets at a time (the max)
secrets = hidden.oauth()
full_url=''.join([TWITTER_URL,'?','count=',str(twittercount),'&', 'screen_name=', acct])
user_timeline = twurl2.oauth_req( full_url, secrets['token_key'], secrets['token_secret'], "GET" )
js=json.loads(user_timeline)
print(0, js[0]['text'], js[0]['id'], js[0]['created_at']) #print most recent tweet
wrap_list.append(js)


count=1
old_max_id=0
max_id=js[len(js) - 1]['id']

while old_max_id!=max_id:
    old_max_id=max_id
    full_url=''.join([TWITTER_URL,'?','count=',str(twittercount),'&', 'screen_name=', acct, '&', 'max_id=', str(max_id)])
    user_timeline = twurl2.oauth_req( full_url, secrets['token_key'], secrets['token_secret'], "GET" )
    js = json.loads(user_timeline)
    print(count, js[0]['text'], js[0]['id'], js[0]['created_at']) #print one every 200 tweets
    max_id=js[len(js) - 1]['id']
    wrap_list.append(js)
    count=count+1


json.dump(wrap_list, outfile)
outfile.close()
