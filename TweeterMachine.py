import tweepy
import requests
import json

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

    #Your geolocation
    latitude = 0.0
    longitude = 0.0
    myIP = ''

    def __init__(self):
        self.find_location()

    def find_location(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        self.latitude = j['latitude']
        self.longitude = j['longitude']
        self.myIP = j['ip']

def main():
    twitterApi = TweeterMachine()

    print('{}\t{}\t{}'.format(twitterApi.latitude,twitterApi.longitude,twitterApi.myIP))


if __name__ == '__main__': main()