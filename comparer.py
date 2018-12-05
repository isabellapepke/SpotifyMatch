from playlist import Playlist
from statistics import Statistics


class Comparer:
    """
    Class compares two playlists and contains information about their comparison
    Relevant Instance Variables defined in __init__ :
        playlist1 = playlist of user 1
        playlist2 = playlist of user 2
        comparison = tuple (sharedSongs, sharedArtists, artistsCount) of type (Playlist, Set, Int)
                        see playlist.compare() for more info
        similarity = similarity score for playlist1 and playlist2 of type float
    """
    def __init__(self, playlist1, playlist2):
        self.playlist1 = playlist1
        self.playlist2 = playlist2
        self.comparison = playlist1.compare(playlist2)
        self.calculator = Statistics()
        self.similarity = self.setSimilarity()

    def printCommonSongs(self):
        """Prints songs shared between both profiles"""
        print(self.comparison[0])

    def setSimilarity(self):
        """should not be used outside class, instead access Comparer.similarity"""
        plen1 = len(self.playlist1.songs)
        plen2 = len(self.playlist2.songs)
        sharedlen = len(self.comparison[0].songs)
        artistslen = self.comparison[2]
        similarity = self.calculator.similarityMetric(plen1, plen2, sharedlen, artistslen)
        return similarity

    def isSimilar(self, minSimilarity):
        return self.similarity >= minSimilarity

    def getMissingSongs(self, profile=0):
        """Returns: playlist with songs in playlist2 and not in playlist1 if param==0, songs in playlist1 not in playlist2 else"""
        if profile == 0:
            missingSongs = Playlist("missing from User 1", [])
            for song in self.playlist2.songs:
                if song in self.playlist1.songs:
                    continue
                missingSongs.add(song)
            return missingSongs

        missingSongs = Playlist("missing from User 2", [])
        for song in self.playlist1.songs:
            if song in self.playlist2.songs:
                continue
            missingSongs.add(song)
        return missingSongs
