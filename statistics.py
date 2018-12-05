class Statistics:
    """Class to calulate similarity scores between two profiles"""

    def profileMetric(self, profile, sharedSongs, sharedArtists):
        """ Should not be called outside class definition"""
        numerator = sharedSongs + 0.5*(sharedSongs-sharedArtists)
        return numerator/profile 

    def  similarityMetric(self, profile1, profile2, sharedSongs, sharedArtists):
        """
        param: profile1 = double; number of songs in profile1
            profile2 = double; number of songs in profile2
            sharedSongs = double; number of shared songs between two profiles
            sharedArtists = double; number of pairs of songs with artists in common between two profiles
        returns: weighted average of similarity scores, weighted by playlist size
        """
        metric1 = self.profileMetric(profile1, sharedSongs, sharedArtists)
        metric2 = self.profileMetric(profile2, sharedSongs, sharedArtists)
        return ((profile1*metric1)+(profile2*metric2))/(profile1+profile2)
