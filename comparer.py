from playlist import Playlist 
from statistics import Statistics

class Comparer:

    def __init__(self, playlist1, playlist2):
        self.playlist1 = playlist1
        self.playlist2 = playlist2
        self.comparison = playlist1.compare(playlist2)
        self.calculator = Statistics()
        self.similarity = self.setSimilarity()
    

    def printCommonSongs(self):
        print(self.comparison[0])
    
    def setSimilarity(self):
        plen1 = len(self.playlist1.songs)
        plen2 = len(self.playlist2.songs)
        sharedlen = len(self.comparison[0].songs)
        artistslen = self.comparison[2]
        similarity = self.calculator.similarityMetric(plen1, plen2, sharedlen, artistslen)
        return similarity
        
    def isSimilar(self, minSimilarity):
        return self.similarity >= minSimilarity

    def getMissingSongs(self, profile = 0):
        if profile == 0 :
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



            
    