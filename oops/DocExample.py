class Song:
    """Class to repenset a song

     Attributes:
         title(str): title of the songs
         artist(Artist) : An Artist object represet the songs creator
         duration(int) : The duration of songs
    """

    def __init__(self,title,artist,duration=0):
        """ songs init method

        Args:
            title(str): title of atribute
        """
        self.title = title
        self.artist = artist
        self.duration = duration