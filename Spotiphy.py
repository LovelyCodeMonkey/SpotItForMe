
import spotipy
import spotipy.util as util

class Spotiphy:

    SPOTIPY_CLIENT_ID = '57cb04fee761493cbcd31ab4274a5a39'

    SPOTIPY_CLIENT_SECRET = '67d9f48c5f604e0da8ad347cffda1361'

    SPOTIPY_REDIRECT_URI = 'http://hangoutapp.tech'

    username = input('Please Enter Your Spotify Username: ')
    playlistName = input('Please Enter the Name of your Spotify Playlist: ')
    playlist_id = ''
    track_id = list()
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,
                                       SPOTIPY_REDIRECT_URI)
    sp = spotipy.Spotify(auth=token)

    def __init__(self):

        self.set_playListID()

    def set_playListID(self):

        if self.token:
            playlists = self.sp.user_playlists(self.username)

            for playlist in playlists['items']:
                if str(playlist['name']) == self.playlistName:
                    self.playlist_id = playlist['uri']

    def set_trackID(self, songSet):

        if self.token:

            # print('song set {}'.format(songSet))
            for song in songSet:
                lst = song.split(' - ')
                artistName = lst[0]
                results = self.sp.search(q=artistName)

                for i in results['tracks']['items']:
                    if i['name'] == lst[1]:
                        self.track_id.append(i['id'])
                        print('track id: {}'.format(self.track_id))

    def add_song(self):

        if self.token:
            self.sp.trace = False
            # print('{}\t{}\t{}'.format(self.username, self.playlist_id, self.track_id))
            if len(self.track_id) > 0:
                self.sp.user_playlist_add_tracks(self.username, self.playlist_id, self.track_id)
            else:
                print('Sorry no tracks where found at this time')