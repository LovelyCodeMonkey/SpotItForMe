
from TweeterMachine import TweeterMachine
from Spotiphy import Spotiphy
import time

class SpotItForMe:

    tweetApi = TweeterMachine()
    spotAPi = Spotiphy()

    def __init__(self):
        pass

    def config_playlist(self):

        print("Getting the Tweets...")
        self.tweetApi.get_tweets()

        print("Getting Tracks...")
        self.spotAPi.set_trackID(self.tweetApi.get_songs())

        print("Adding Tracks To Playlist")
        self.spotAPi.add_song()

        self.tweetApi.reset_songSet()

def main():

    spot = SpotItForMe()

    while True:
        spot.config_playlist()

        print('program waiting until next iteration...')
        time.sleep(600)

        if input('Do you want to continue? Y/N: ') == 'Y':
            break



if __name__ == '__main__': main()