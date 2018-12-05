import song
class Playlist:
    """Class holds a username and a library of songs. It is equipped with a __str__ method and 
       equality operator oveloads
        List of class variables:
            userId = Spotify userId of playlist -- dec in function __init__
            songs = List of songs in playlist -- dec in function __init__
     """

    def __init__(self, userId = "none", songs = []):
        self.userId = userId 
        self.songs = songs

    # str() method
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

    def add (self, song):
        """adds parameter to playlist"""
        self.songs.append(song)

    def has(self, song):
        """returns true if parameter in playlist, false otherwise"""
        if song in self.songs:
            return True
        return False 
    
    def compare(self, other):
        """ Param: other playlist to compare
            Returns: tuple (sharedSongs, sharedArtists, artistsCount) of type (Playlist, Set, Int) where
                sharedSongs = playlist object containing songs in common
                sharedArtists = set of all artists who have at least one song in both playlists
                artistsCount = number pairs of songs (one song from each playlist) with the same artist
        """
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
    

