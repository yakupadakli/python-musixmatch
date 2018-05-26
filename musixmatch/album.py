from musixmatch.client import Client
from musixmatch.models import Album as AlbumModel
from musixmatch.models import Track as TrackModel


class Album(Client):
    """Album operations."""
    MAX_PAGE_SIZE = 99

    def __init__(self, **kwargs):
        super(Album, self).__init__(**kwargs)
        self.fields_tag = "fields"

    def get(self, album_id):
        """
        Get the album object using the Musixmatch id.

        :type album_id: string

        :param album_id: The Musixmatch album id

        :return [Album]: Album Object.
        """
        url = "/album.get"
        params = {"album_id": album_id}
        result = self._get(url, params=params)
        return AlbumModel._parse(result["message"]["body"]["album"])
