import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDIRECT_URI = os.environ["REDIRECT_URI"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                              client_secret=CLIENT_SECRET,
                                              redirect_uri = REDIRECT_URI,
                                              scope = "playlist-modify-private"
                                              )
                    )

user_id = sp.current_user()["id"]
# print(sp.current_user()["id"])

uris_list = []

with open("songs.txt") as file:
    songs = file.readlines()

songs = [song.replace("\n", "") for song in songs]

for song in songs[1:]:
    result = sp.search(q=f"track:{song} year:2000", type="track")

    try:
        uris_list.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"'{song}' doesn't exist in spotify")


print(uris_list)
print(len(uris_list))

playlist = sp.user_playlist_create(user_id, name=f"{songs[0]} Billboard 100", public="False")
playlist_id = playlist['id']

sp.playlist_add_items(playlist_id=playlist_id, items=uris_list)
