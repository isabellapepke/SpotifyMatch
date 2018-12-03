class Statistics:
    """Class to calulate similarity scores between two profiles"""

    # param: profile = double; number of songs in profile1
    #        sharedSongs = double; number of shared songs between two profiles
    #        sharedArtists = double; number of pairs of songs with artists in common between two profiles
    def profileMetric(profile, sharedSongs, sharedArtists):
        numerator = sharedSongs + 0.5(sharedSongs-sharedArtists)
        return numerator/profile 

    #param: profile1 = double; number of songs in profile1
    #       profile2 = double; number of songs in profile2
    #       sharedSongs = double; number of shared songs between two profiles
    #       sharedArtists = double; number of pairs of songs with artists in common between two profiles
    #return: weighted average of similarity scores, weighted by playlist size
    def  similarityMetric(profile1, profile2, sharedSongs, sharedArtists):
        metric1 = profileMetric(profile1, sharedSongs, sharedArtists)
        metric2 = profileMetric(profile2, sharedSongs, sharedArtists)
        return ((profile1*metric1)+(profile2*metric2))/(profile1+profile2)
