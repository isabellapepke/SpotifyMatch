# SpotifyMatch
An application that takes two user profiles and outputs the similarities in songs and artists between them

## How to Run it:
enter python file name followed by two usernames:
python spotifyxx.py user1 user2

## Enviroment dependent errors
if html print error occurs, use commented line of code at 70 comment out line 68 like so:
        #print(song['name']+ ' - ' + song['artists'][0]['name'])
        print(song['name']+ ' - ' + song['artists'][0]['name']).encode("utf-8")


if cache error occurs, comment out delete cache at line 42, you will need to delete cache individually
        #os.remove(f".cache-{user}")
