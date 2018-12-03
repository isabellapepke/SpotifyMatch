import song
class Playlist:
    """List of class variables:
        userId = Spotify userId of playlist -- dec in function __init__
        songs = List of songs in playlist -- dec in function __init__
     """
    #class constructor
    def __init__(self, userId = "none", songs = []):
        self.userId = userId 
        self.songs = songs
    
    #str() method
    def __str__(self):
        string = ""
        for song in self.songs:
            string += str(song) + "\n"
        return string

    # == overload
    def __eq__(self, other):
        for song in self.songs:
            if not (song in other.songs):
                return False
        return True
    
    # != oveload
    def __neq__(self,other):
        return not (self == other)

    #adds parameter to playlist
    def add (self, song):
        self.songs.append(song)

    #returns true if parameter in playlist, false otherwise
    def has(self, song):
        if song in self.songs:
            return True
        return False 
    
    #Param: other playlist to compare
    #Returns: tuple (sharedSongs, sharedArtists, artistsCount) where
    #   sharedSongs = playlist object containing songs in common
    #   sharedArtists = set of all artists who have at least one song in both playlists
    #   artistsCount = number pairs of songs (one song from each playlist) with the same artist
    def compare(self, other):
        sharedSongs = Playlist("none",[])
        sharedArtists = set()
        artistsCount = 0
        artistPairs = []
        for song in self.songs:
            if song in other.songs:
                sharedSongs.add(song)
            for track in other.songs:
                if song.artists == track.artists:
                    if not (track in artistPairs):
                        for artist in song.artists:
                            sharedArtists.add(artist)
                        artistPairs.append(track)
                        artistsCount+=1
        return (sharedSongs, sharedArtists, artistsCount)
    

