import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
#from json.decoder import JSONDecodeError

#Get the username from terminal, use argv taking the argument from commandline
#to run use python spotifyxx.py spotifyusername
username = sys.argv[1]

# brownbearhoopla?si=GTQRYsmTTHivygieza7QbA
#erase cache and prompt for user permission, ask user to accept
try:
    #token  = util.prompt_for_user_token(username)
    clientID = '112fe974da5743d4a85569ae8a4804da'
    clientSecret = 'd82f12a424fa493092654ad56cfad2c5'
    redirectURL = 'http://localhost:8888/callback/'
    token = util.prompt_for_user_token(username,scope='user-read-private user-read-email',client_id='112fe974da5743d4a85569ae8a4804da',client_secret='d82f12a424fa493092654ad56cfad2c5',redirect_uri='http://www.google.com/') # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print track['name'] + ' - ' + track['artists'][0]['name']
    else:
        print "Can't get token for", username
except:
    #os.remove(".cache-{brownbearhoopla}")
    print('in else?')
    token = util.prompt_for_user_token(username,scope='user-read-private user-read-email user-library-read',client_id='112fe974da5743d4a85569ae8a4804da',client_secret='d82f12a424fa493092654ad56cfad2c5',redirect_uri='http://www.google.com/') # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print track['name'] + ' - ' + track['artists'][0]['name']
    else:
        print "Can't get token for", username

#create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)
