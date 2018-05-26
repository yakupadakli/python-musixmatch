from musixmatch.client import Client
from musixmatch.models import Artist as ArtistModel


class Artist(Client):
    """Artist operations."""
    MAX_PAGE_SIZE = 99

    def __init__(self, **kwargs):
        super(Artist, self).__init__(**kwargs)
        self.fields_tag = "fields"

    def get(self, artist_id):
        """
        Get the artist data.

        :type artist_id: string
        :param artist_id: Musixmatch artist id.

        :return [Artist]: Artist Object.
        """
        url = "/artist.get"
        params = {"artist_id": artist_id}
        result = self._get(url, params=params)
        return ArtistModel._parse(result["message"]["body"]["artist"])

    def related(self, artist_id, page=1, page_size=MAX_PAGE_SIZE):
        """
        Get the artist data.

        :type artist_id: string
        :type page: double
        :type page_size: double

        :param artist_id: The musiXmatch artist id.
        :param page: Define the page number for paginated results.
        :param page_size: Define the page size for paginated results. Range is 1 to 99.

        :return [List]: Artist List.
        """
        assert page_size <= self.MAX_PAGE_SIZE, "Page size must be lower than %s" % self.MAX_PAGE_SIZE
        url = "/artist.related.get"
        params = {"artist_id": artist_id, "page": page, "page_size": page_size + 1}
        result = self._get(url, params=params)
        artist_list = map(lambda x: x["artist"], result["message"]["body"]["artist_list"])
        return ArtistModel._parse_list(artist_list)

    def search(self, query, artist_id=None, page=1, page_size=MAX_PAGE_SIZE):
        """
        Search for artists.

        :type query: string
        :type artist_id: string
        :type page: double
        :type page_size: double

        :param query: Search this parameter within the artist name.
        :param artist_id: The Musixmatch artist id.
        :param page: Define the page number for paginated results.
        :param page_size: Define the page size for paginated results. Range is 1 to 99.

        :return [List]: Artist List.
        """
        assert page_size <= self.MAX_PAGE_SIZE, "Page size must be lower than %s" % self.MAX_PAGE_SIZE
        url = "/artist.search"
        params = {"q_artist": query, "f_artist_id": artist_id, "page": page, "page_size": page_size + 1}
        result = self._get(url, params=params)
        artist_list = map(lambda x: x["artist"], result["message"]["body"]["artist_list"])
        return ArtistModel._parse_list(artist_list)
