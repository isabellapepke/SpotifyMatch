class Song:
    """Class holds a song title and list of artists, it is equipped with equality overloads and __str__ method"""
    #class constructor
    def __init__(self, title, musicians):
        self.title = title
        self.artists = []
        for artist in musicians:
            self.artists.append(artist)
        
    # == overload
    def __eq__(self,other):
        if self.title == other.title:
           return(set(self.artists).intersection(other.artists) == set(self.artists).union(other.artists))
        return False
    
    # != overload
    def __neq__(self,other):
         return not (self==other) 
    
    #str() method
    def __str__(self):
        return self.title+" -- by: " +", ".join(self.artists)

            