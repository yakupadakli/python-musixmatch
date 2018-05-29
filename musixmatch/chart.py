from musixmatch.client import Client
from musixmatch.models import Artist as ArtistModel
from musixmatch.models import Track as TrackModel


class Chart(Client):
    """Chart operations."""
    MAX_PAGE_SIZE = 99

    def __init__(self, **kwargs):
        super(Chart, self).__init__(**kwargs)
        self.fields_tag = "fields"

    def artists(self, country, page=1, page_size=MAX_PAGE_SIZE):
        """
        Get the list of the top artists of a given country.

        :type country: string
        :type page: double
        :type page_size: double

        :param country: A valid country code.
        :param page: Define the page number for paginated results.
        :param page_size: Define the page size for paginated results. Range is 1 to 99.

        :return [List]: Artist List.
        """
        assert page_size <= self.MAX_PAGE_SIZE, "Page size must be lower than %s" % self.MAX_PAGE_SIZE
        url = "/chart.artists.get"
        params = {"country": country, "page": page, "page_size": page_size + 1}
        result = self._get(url, params=params)
        artist_list = map(lambda x: x["artist"], result["message"]["body"]["artist_list"])
        return ArtistModel._parse_list(artist_list)

    def tracks(self, country, has_lyrics=None, page=1, page_size=MAX_PAGE_SIZE):
        """
        Get the list of the top songs of a given country.

        :type country: string
        :type has_lyrics: bool
        :type page: double
        :type page_size: double

        :param country: A valid country code.
        :param has_lyrics: Filter only contents with lyrics.
        :param page: Define the page number for paginated results.
        :param page_size: Define the page size for paginated results. Range is 1 to 99.

        :return [List]: Tracks List.
        """
        assert page_size <= self.MAX_PAGE_SIZE, "Page size must be lower than %s" % self.MAX_PAGE_SIZE
        url = "/chart.tracks.get"
        params = {"country": country, "f_has_lyrics": has_lyrics, "page": page, "page_size": page_size + 1}
        result = self._get(url, params=params)
        track_list = map(lambda x: x["track"], result["message"]["body"]["track_list"])
        return TrackModel._parse_list(track_list)
