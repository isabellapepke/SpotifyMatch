# SpotifyMatch
An application that takes two user profiles and outputs the similarities in songs and artists between them

## How to Run it on comamand line
Enter python file name:

        python spotifyxx.py

You will be prompted for usernames

A web browser will pop up and prompt for a user to login. Log in with user1 credentials.

Then it will automatically open another tab and logout user1.

A web browser will pop up and prompt for a user to login. Log in with user2 credentials.

## To build docker image and run container
```
docker image build -t spotidock .
docker container run --rm -it --name spot spotidock
```
### Running in container
1. You will be prompted for first username
2. Visit this Webpage to log in to your account https://accounts.spotify.com/authorize?client_id=4814686cacd44e65ab9561e8744726ee&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A%2Fcallback&scope=user-library-read+user-read-email+user-read-private
3. Copy URL you were redirected to into the command line (Don't worry about the 404 error)
4. Visit https://www.spotify.com/logout to log out of the first account before entering second username.
5. Repeat steps 2-4

## How to find your username
### Via Spotify.com
  If you do not know what your Spotify username is, log in to https://www.spotify.com/us/
  In the account overview, https://www.spotify.com/us/account/overview/, it will show your username.

### Via Spotify application
  1. Open the desktop spotify application

  2. Click on your name on the upper right corner of the screen

  3. A screen with your name and playlists will show up. At the top, click on the circle with the three dots in them. (...)

  4. Click on: Share >> "copy profile link"

  5. Open up a browser and paste it into the search bar

  6. The number that shows at the end of the url is your username

## Enviroment dependent errors
If the page says "This site can't be reached" when you authenticate your account, ignore that and copy the url anyways.
Here is what it might look like

![photo](https://github.com/isabellapepke/SpotifyMatch/blob/master/localhost_error.png)

#### Previous code errors that have been fixed:

If html print error occurs, use commented line of code at 70 comment out line 68 like so:

        #print(song['name']+ ' - ' + song['artists'][0]['name'])
        print(song['name']+ ' - ' + song['artists'][0]['name']).encode("utf-8")


If cache error occurs, comment out delete cache at line 42, you will need to delete cache individually

        #os.remove(f".cache-{user}")
