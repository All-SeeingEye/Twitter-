import tweepy
import keys
from pandas import DataFrame

users = [('Christian Ronaldo','Cristiano'), ('Elon Musk','elonmusk'), ('Narendra Modi','narendramodi'), ('Taylor Swift','taylorswift13')]

api_key = keys.API_KEY
api_key_secret = keys.API_KEY_SECRET
bearer_token = keys.BEARER_TOKEN

auth = tweepy.OAuthHandler(api_key, api_key_secret)

api = tweepy.API(auth)

for user,usid in users:
    userID = usid

    tweets = api.user_timeline(screen_name=userID, 
                            count=200, 
                            include_rts = False,
                            exclude_replies = True,
                            tweet_mode = 'extended')

    tweetCollector = []
    tweetCollector.extend(tweets)
    latestTweetId = tweets[-1].id

    while True:
        tweets = api.user_timeline(screen_name=userID, 
                            count=200, 
                            include_rts = False,
                            exclude_replies = True,
                            tweet_mode = 'extended',
                            max_id = latestTweetId - 1)
        
        if len(tweets) == 0:
            print('Tweets = 0')
            break
            
        latestTweetId = tweets[-1].id
        tweetCollector.extend(tweets)
        print('Tweets downloaded so far: {}'.format(len(tweetCollector)))

    tweetsHelper = [[user,
                    tweet.id_str, 
                    tweet.created_at, 
                    tweet.favorite_count, 
                    tweet.retweet_count, 
                    tweet.full_text.encode("utf-8").decode("utf-8").replace('\n', ' ')] 
                    for idx,tweet in enumerate(tweetCollector)]
                    
    df = DataFrame(tweetsHelper,columns=["club","id","createdAt","favorites","retweets","text"])
    df.to_csv('Tweets_%s.csv' % userID,index=False)