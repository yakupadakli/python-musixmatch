from musixmatch.album import Album
from musixmatch.artist import Artist


class Musixmatch(object):
    """Musixmatch API"""
    BASE_URL = "http://api.musixmatch.com/ws"
    VERSION = "1.1"

    def __init__(self, api_key, **kwargs):
        """
        Musixmatch Api Instance Constructor

        :param kwargs:
        """
        self.api_key = api_key
        self.base_url = "%s/%s" % (self.BASE_URL, self.VERSION)

    @property
    def artist(self):
        """
        Musixmatch Artist Operations

        Available methods:


        get: Get the artist data.
        related: Get related artists.
        search: Search for artists.
        albums: Get the albums of an artist.
        """
        return Artist(api=self)

    @property
    def album(self):
        """
        Musixmatch Artist Operations

        Available methods:


        get: Get the album object using the Musixmatch id.
        tracks: Get the songs of an album.
        """
        return Album(api=self)
