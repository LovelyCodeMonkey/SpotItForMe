import requests
import json

class Locator:

    # Your Geolocation
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

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude