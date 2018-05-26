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
