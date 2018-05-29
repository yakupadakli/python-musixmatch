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

    def tracks(self, album_id, has_lyrics=None, page=1, page_size=MAX_PAGE_SIZE):
        """
        Get the songs of an album.

        :type album_id: string
        :type has_lyrics: bool
        :type page: double
        :type page_size: double

        :param album_id: The Musixmatch album id
        :param has_lyrics: Filter only contents with lyrics
        :param page: Define the page number for paginated results.
        :param page_size: Define the page size for paginated results. Range is 1 to 99.

        :return [List]: Tracks List.
        """
        url = "/album.tracks.get"
        params = {"album_id": album_id, "f_has_lyrics": has_lyrics, "page": page, "page_size": page_size + 1}
        result = self._get(url, params=params)
        track_list = map(lambda x: x["track"], result["message"]["body"]["track_list"])
        return TrackModel._parse_list(track_list)
