
import spotipy
import spotipy.util as util

class Spotiphy:

    SPOTIPY_CLIENT_ID = '57cb04fee761493cbcd31ab4274a5a39'

    SPOTIPY_CLIENT_SECRET = '0f0fb4b004134a60ab59d33d3481f352'

    SPOTIPY_REDIRECT_URI = 'http://hangoutapp.tech'

    username = input('Please Enter Your Username: ')
    playlistName = input('Please Enter the Name of your Playlist: ')
    playlist_id = ''
    track_id = list()
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,
                                       SPOTIPY_REDIRECT_URI)

    def __init__(self):

        self.set_playListID()

    def set_playListID(self):

        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            playlists = sp.user_playlists(self.username)

            for playlist in playlists['items']:
                if str(playlist['name']) == self.playlistName:
                    self.playlist_id = playlist['uri']

    def set_trackID(self, songSet):

        if self.token:
            sp = spotipy.Spotify(auth=self.token)

            for song in songSet:
                lst = song.split(' - ')
                artistName = lst[0]
                results = sp.search(q=artistName, limit=20)

                for i in results['tracks']['items']:
                    if i['name'] == lst[1]:
                        self.track_id.append(i['id'])

    def add_song(self):

        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            sp.trace = False
            sp.user_playlist_add_tracks(self.username, self.playlist_id, self.track_id)