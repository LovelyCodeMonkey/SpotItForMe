from TweeterMachine import TweeterMachine
from Spotiphy import Spotiphy

class SpotItForMe:

    tweetApi = TweeterMachine()
    spotAPi = Spotiphy()

    def __init__(self):
        pass

def main():
    spot = SpotItForMe()
    spot.tweetApi.set_Hashtag(input('Please Enter Host\'s name: '))
    print(spot.tweetApi.get_Hashtag())

if __name__ == '__main__': main()