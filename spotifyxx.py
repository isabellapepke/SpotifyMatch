### Created by Daniel Brisen, Nic Fergie, and Bella Pepke

import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util


def auth(user):
    "Function obtains authorization from spotify, returns authorization token"

    try:
        #Set Auth variables
        SPOTIFY_CLIENT_ID = '4814686cacd44e65ab9561e8744726ee'
        SPOTIPY_CLIENT_SECRET = 'e23f210b1e0d4e6da5dbe263a7add7af'
        SPOTIPY_REDIRECT_URI = 'http://localhost:/callback'
        scope = 'user-read-private user-read-email user-library-read'
        #Get Auth token
        token = util.prompt_for_user_token(user,scope ,SPOTIFY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI)
        return token
    except:
        #if auth fails ... may be due to out-dated cache
        print("Could not obtain token for , " + user)
        print("Clearing Cache, please run again")
        #clear cache, exit gracefully
        #os.remove(f".cache-{user}")
        sys.exit(0)

def getTracks(token):
    "Function returns list containing song library"

    sp = spotipy.Spotify(auth=token)#create Spotify object
    songs = []
    offset = 0 #this variable determines index in song library at which to begin song fetch

    #begin fetching songs from library
    results = sp.current_user_saved_tracks(20,offset)
    while( not (results['items'] == []) ): #while there are still songs left in library
        for item in results['items']:
            track= item['track']
            songs.append(track)

        #increase offset to fetch next batch of songs, then fetch
        offset+=20
        results = sp.current_user_saved_tracks(20,offset)
    return songs

def printTracks(songs):
    for song in songs:
        print(song['name']+ ' - ' + song['artists'][0]['name']).encode("utf-8")


username = sys.argv[1]
token = auth(username)
songs= getTracks(token)
printTracks(songs)
