import sys
import os
import json
import webbrowser
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

SPOTIFY_CLIENT_ID = '4814686cacd44e65ab9561e8744726ee'
SPOTIPY_CLIENT_SECRET = 'e23f210b1e0d4e6da5dbe263a7add7af'
SPOTIPY_REDIRECT_URI = 'http://localhost:/callback' 
scope = 'user-library-read'


username = sys.argv[1]

try:
    token = util.prompt_for_user_token(username, scope, SPOTIFY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

except:
  #  os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, SPOTIFY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

spotifyObject = spotipy.Spotify(auth=token)
user= spotifyObject.current_user()
print(json.dumps(user, sort_keys=True, indent=4))
