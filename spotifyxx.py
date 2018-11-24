### Created by Daniel Brisen, Nic Fergie, and Bella Pepke

import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from time import sleep
import webbrowser

#extra usernames and passwords:

#wvvk3mob8c4qncj1wb6jxmv6m
#spoodles353
#email: spotifymatch18@gmail.com
#pw: spoodles353


def wait(time):
    "Function delays program by a deteremined amount of seconds"
    sleep(time)


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
        #clear cache, exit gracefully, bellas environment will not run this line, comment if error
        os.remove(f".cache-{user}")
        #os.remove(f,".cache-{user}")
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
    "Function prints the tracks in a list"
    for song in songs:
        print(song['name']+ ' - ' + song['artists'][0]['name'])
        #if you get a utf error insert .encode("utf-8") like so:
        #print(song['name']+ ' - ' + song['artists'][0]['name']).encode("utf-8")

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def printCommonTracks(user_one_song_list, user_two_song_list):
    "Function prints tracks that are in common between two users"
    print("\n\n\n\nNow printing common songs...\n\n*************--------------------*************")
    for user_one_track in user_one_song_list:
         for user_two_track in user_two_song_list:
             if ((user_one_track['name']+ ' - ' + user_one_track['artists'][0]['name']).encode("utf-8")== (user_two_track['name']+ ' - ' + user_two_track['artists'][0]['name']).encode("utf-8")):
                 print((user_one_track['name']+ ' - ' + user_one_track['artists'][0]['name']).encode("utf-8")+ " ******** "+ (user_two_track['name']+ ' - ' + user_two_track['artists'][0]['name']).encode("utf-8"))

def logoutUser():
    "Function logs out a user"
    print("Now logging you out...")
    wait(5)
    webbrowser.open("http://www.spotify.com/logout")
    wait(10)

#when program starts logout any users, allow time for page to load
webbrowser.open("http://www.spotify.com/logout")
wait(5)

songs1 = []
songs2 = []

username1 = sys.argv[1]
token1 = auth(username1)
songs1 = getTracks(token1)
#printTracks(songs1)
#must run this code to remove cache for bellas computer:
#wait(5)
#os.remove("C:\Users\isabe\Documents\Networks\SpotifyMatch\.cache-brownbearhoopla")
logoutUser()


username2 = sys.argv[2]
token2 = auth(username2)
songs2 = getTracks(token2)
#printTracks(songs2)
#must run this code to remove cache for bellas computer:
#wait(5)
#os.remove("C:\Users\isabe\Documents\Networks\SpotifyMatch\.cache-wvvk3mob8c4qncj1wb6jxmv6m")
logoutUser()


printCommonTracks(songs1, songs2)
print("******************************** --------------------  ********************************")
print
