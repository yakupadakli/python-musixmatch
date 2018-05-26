from musixmatch.client import Client
from musixmatch.models import Artist as ArtistModel


class Artist(Client):
    """Artist operations."""

    def __init__(self, **kwargs):
        super(Artist, self).__init__(**kwargs)
        self.fields_tag = "fields"

    def get(self, artist_id):
        """
        Get the artist data.

        :param artist_id: Musixmatch artist id.
        :return [Artist]: Artist Object.
        """
        url = "/artist.get"
        params = {"artist_id": artist_id}
        result = self._get(url, params=params)
        return ArtistModel._parse(result["message"]["body"]["artist"])
