import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
#from json.decoder import JSONDecodeError

#Get the username from terminal, use argv taking the argument from commandline
username = sys.argv[1]

# brownbearhoopla?si=GTQRYsmTTHivygieza7QbA

#erase cache and prompt for user permission, ask user to accept
try:
    #token  = util.prompt_for_user_token(username)
    clientID = '112fe974da5743d4a85569ae8a4804da'
    clientSecret = 'd82f12a424fa493092654ad56cfad2c5'
    redirectURL = 'http://localhost:8888/callback/'
    token = util.prompt_for_user_token(username,scope='playlist-read-private',client_id='112fe974da5743d4a85569ae8a4804da',client_secret='d82f12a424fa493092654ad56cfad2c5',redirect_uri='http://localhost:8888/callback') # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/
except:
    os.remove(".cache-{brownbearhoopla}")
    token = util.prompt_for_user_token(username,scope='playlist-read-private',client_id='112fe974da5743d4a85569ae8a4804da',client_secret='d82f12a424fa493092654ad56cfad2c5',redirect_uri='http://localhost:8888/callback') # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/

#create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)
