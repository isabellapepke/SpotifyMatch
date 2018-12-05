### Created by Daniel Brisen, Nic Fergie, and Bella Pepke

import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from time import sleep
import webbrowser
from song import Song
from playlist import Playlist
from comparer import Comparer 

#extra usernames and passwords:

#wvvk3mob8c4qncj1wb6jxmv6m
#spoodles353
#email: spotifymatch18@gmail.com
#pw: spoodles353


def wait(time):
    "Function delays program by a deteremined amount of seconds--used for waiting for logout page"

    sleep(time)

def deleteCache():
    "Function deletes cache, raises exception if does not execute"

    try:
        os.remove(f,".cache-{user}")
    except:
        print("There was an error when trying to delete cache. \nYou must manually delete it after everytime you run the code.")

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
        print("\nAuthorized!\n")
        return token
    except:
        #if auth fails ... may be due to out-dated cache
        print("Could not obtain token for , " + user)
        print("Clearing Cache, please run again")
        deleteCache()
        sys.exit(0)

def makePlaylist(token, username):
    "Function returns list containing song library"

    sp = spotipy.Spotify(auth=token) #create Spotify object
    songs = []
    offset = 0 #this variable determines index in song library at which to begin song fetch
    playlist = Playlist(username, [])
    #begin fetching songs from library
    results = sp.current_user_saved_tracks(20,offset)
    while( not (results['items'] == []) ): #while there are still songs left in library
        for item in results['items']:
            track= item['track']
            songs.append(track)

        #increase offset to fetch next batch of songs, then fetch
        offset+=20
        results = sp.current_user_saved_tracks(20,offset)
    #create playlist object from json string of songs
    for song in songs:
        artists = []
        for artist in song['artists']:
            artists.append(artist['name'])
        track = Song(song['name'],artists)
        playlist.add(track)
    return playlist

def printCommonTracks(playlist1, playlist2):
    "Function prints tracks that are in common between two users"
    commonSongs = playlist1.compare(playlist2)[0]
    print("\n\n\n\nNow printing common songs...\n\n*************--------------------*************")
    try:
        print(commonSongs)
    except:
        print(str(commonSongs).encode())

def logoutUser():
    "Function logs out a user"

    print("\n\nNow logging you out...\n\n")
    webbrowser.open("http://www.spotify.com/logout")
    wait(5)


###########----Main----############

#Check for valid amount of command line arugments
if len(sys.argv) < 2:
    print("You must provide 2 Spotify Usernames as command-line arguments")
    print("Now exiting program")
    sys.exit()


#when program starts logout any users, allow time for page to load
webbrowser.open("http://www.spotify.com/logout")
wait(5)

songs1 = []
songs2 = []
username1 = ""
username2 = ""

username1 = sys.argv[1]
token1 = auth(username1)
songs1 = makePlaylist(token1, username1)
print("########### Songs in Playlist 1 ##############")
print(songs1)
logoutUser()


username2 = sys.argv[2]
token2 = auth(username2)
songs2 = makePlaylist(token2, username2)
print("########### Songs in Playlist 2 ##############")
print(songs2)
logoutUser()

comparer = Comparer(songs1, songs2)

print("########### Songs shared between both profiles ##############")
comparer.printCommonSongs()

print("########### Similarity Score for the two profiles ##############")
print(f"{comparer.similarity*100} %")
print("\n")

if(comparer.similarity == 1):
    print(f"The two profiles are identical!")

elif (comparer.isSimilar(0.5)):
    print(f"The two profiles are very similar, {username1}, you might like these songs from {username2}'s library:")
    wait(5)
    print("\n")
    print(comparer.getMissingSongs(0))
    print("\n")
    print(f"{username2}, you might like these songs from {username1}'s library:")
    print("\n")
    wait(5)
    print(comparer.getMissingSongs(1))

else:
    print("The two profiles are not very similar")

print("******************************** --------------------  ********************************")