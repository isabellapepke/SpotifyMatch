# SpotifyMatch
An application that takes two user profiles and outputs the similarities in songs and artists between them

## How to Run it
Enter python file name followed by two usernames:

        python spotifyxx.py user1 user2
        
A web browser will pop up and prompt for a user to login. Log in with user1 credentials.

Then it will automatically open another tab and logout user1.

A web browser will pop up and prompt for a user to login. Log in with user2 credentials.

## How to find your username
### Via Spotify.com
  If you do not know what your Spotify username is, log in to https://www.spotify.com/us/ 
  In the account overview, https://www.spotify.com/us/account/overview/, it will show your username. 

### Via Spotify application
  1. Open the desktop spotify application

  2. Click on your name on the upper right corner of the screen
  
  3. A screen with your name and bunch of playlist will show up. Click on the circle with the three dots in them. (...) 
  
  4. Click on "copy profile link" 

  5. Open up a browser and paste it into the search bar

  6. The number that shows at the end of the url is your username

## Enviroment dependent errors
If the page says "This site can't be reached" when you authenticate your account, ignore that and copy the url anyways. 
Here is what it might look like
![alt text](C:\Users\pepke101\Downloads\localhost_error.jpg)

#### Previous code errors that have been fixed:

If html print error occurs, use commented line of code at 70 comment out line 68 like so:
        
        #print(song['name']+ ' - ' + song['artists'][0]['name'])
        print(song['name']+ ' - ' + song['artists'][0]['name']).encode("utf-8")


If cache error occurs, comment out delete cache at line 42, you will need to delete cache individually
        
        #os.remove(f".cache-{user}")
