import tweepy
from Locator import Locator

class TweeterMachine:

    #setting the values for the API access

    CONSUMER_KEY = 'FeOfRApXuY4VFiLUN9Y19rGbK'
    CONSUMER_SECRET = 'gPdqBBrhW3OV7eDZc21HXBZW7GlcIJrAN1mF1SELc31wR7LLjo'
    ACCESS_TOKEN = '883048363264004096-dp0Ut1tFvtetzNzpWc6uqhNmpek1sxX'
    ACCESS_TOKEN_SECRET = '4X5CgMtdAb1Qltyh2E0ghblvmpxwvsVezZOfLGhZwiaYa'

    #Create a twitter api instance

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.wait_on_rate_limit = True
    api.wait_on_rate_limit_notify = True



    #tweeted songs
    songSet = set()

    #finding location
    location = Locator()

    #your hashtag

    hashtag = input('Please Enter your selected Hashtag: ')

    def __init__(self):
        pass

    def get_tweets(self):

    #finds and adds the songs that have been tweeted
        for tweet in tweepy.Cursor(self.api.search, q = '{}'.format(self.hashtag), lang = 'en',
                                   geocode = '{},{},10km'.format(self.location.get_latitude(),self.location.get_longitude())).items():
            print(tweet)
            if len(tweet.text.split(' , ')) > 1 :
                self.songSet.add(tweet.text.split(' , ')[1])

    def get_songs(self):
        print(self.songSet)
        return self.songSet

    def reset_songSet(self):
        self.songSet.clear()
        print(self.songSet)