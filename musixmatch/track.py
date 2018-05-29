# coding=utf-8
from musixmatch.client import Client
from musixmatch.models import Lyrics as LyricsModel
from musixmatch.models import Snippet as SnippetModel
from musixmatch.models import Subtitle as SubtitleModel
from musixmatch.models import Track as TrackModel


class Track(Client):
    """Track operations."""
    MAX_PAGE_SIZE = 99
    SORT_ASC = "asc"
    SORT_DESC = "desc"

    def __init__(self, **kwargs):
        super(Track, self).__init__(**kwargs)
        self.fields_tag = "fields"

    def get(self, track_id=None, common_track_id=None):
        """
        Get the album object using the Musixmatch id.

        :type track_id: string
        :type common_track_id: string

        :param track_id: The Musixmatch track id
        :param common_track_id: The Musixmatch common track id

        :return [Track]: Track Object.
        """
        assert track_id or common_track_id, "Track Id or Common Track Id is required"
        url = "/track.get"
        params = {"track_id": track_id, "commontrack_id": common_track_id}
        result = self._get(url, params=params)
        return TrackModel._parse(result["message"]["body"]["track"])

    def lyrics(self, track_id=None, common_track_id=None):
        """
        Get the lyrics for given track.

        :type track_id: string
        :type common_track_id: string

        :param track_id: The Musixmatch track id
        :param common_track_id: The Musixmatch common track id

        :return [Lyrics]: Lyrics Object.
        """
        assert track_id or common_track_id, "Track Id or Common Track Id is required"
        url = "/track.lyrics.get"
        params = {"track_id": track_id, "commontrack_id": common_track_id}
        result = self._get(url, params=params)
        return LyricsModel._parse(result["message"]["body"]["lyrics"])

    def lyrics_translation(self, track_id, language):
        """
        Get a translated lyrics for a given language.

        :type track_id: string
        :type language: string

        :param track_id: The Musixmatch track id.
        :param language: The language of the translated lyrics (ISO 639-1).

        :return [Lyrics]: Lyrics Object.
        """
        url = "/track.lyrics.translation.get"
        params = {"track_id": track_id, "selected_language": language}
        result = self._get(url, params=params)
        return LyricsModel._parse(result["message"]["body"]["lyrics"])

    def search(self, query, artist_id=None, genre_id=None, lyrics_lang=None, has_lyrics=None,
               artist_rating_sort=SORT_ASC, track_rating_sort=SORT_ASC, page=1, page_size=MAX_PAGE_SIZE):
        """
        Search for tracks.

        :type query: str
        :type artist_id: str
        :type genre_id: str
        :type lyrics_lang: str
        :type has_lyrics: bool
        :type artist_rating_sort: str
        :type track_rating_sort: str
        :type page: double
        :type page_size: double

        :param query: Search this parameter within the artist name.
        :param artist_id: Filter by this artist id.
        :param genre_id: Filter by this music category id.
        :param lyrics_lang: Filter by the lyrics language (en, it, ..).
        :param has_lyrics: Filter only contents with lyrics.
        :param artist_rating_sort: Sort by our popularity index for artists.
        :param track_rating_sort: Sort by our popularity index for tracks.
        :param page: Define the page number for paginated results.
        :param page_size: Define the page size for paginated results. Range is 1 to 99.

        :return [List]: Track List.
        """
        sort_options = [self.SORT_ASC, self.SORT_DESC]
        assert artist_rating_sort in sort_options, "Sorting must be %s or %s" % (self.SORT_ASC, self.SORT_DESC)
        assert track_rating_sort in sort_options, "Sorting must be %s or %s" % (self.SORT_ASC, self.SORT_DESC)
        url = "/track.search"
        params = {
            "q": query,
            "f_artist_id": artist_id,
            "f_music_genre_id": genre_id,
            "f_lyrics_language": lyrics_lang,
            "f_has_lyrics": has_lyrics,
            "s_artist_rating": artist_rating_sort,
            "s_track_rating": track_rating_sort,
            "page": page,
            "page_size": page_size + 1
        }
        result = self._get(url, params=params)
        track_list = map(lambda x: x["track"], result["message"]["body"]["track_list"])
        return TrackModel._parse_list(track_list)

    def snippet(self, track_id):
        """
        Get the snippet for a given track.

        A lyrics snippet is a very short representation of a song lyrics.
        It’s usually twenty to a hundred characters long and
        it’s calculated extracting a sequence of words from the lyrics.

        :type track_id: string

        :param track_id: The Musixmatch track id

        :return [Snippet]: Snippet Object.
        """
        url = "/track.snippet.get"
        params = {"track_id": track_id}
        result = self._get(url, params=params)
        return SnippetModel._parse(result["message"]["body"]["snippet"])

    def subtitle(self, common_track_id, subtitle_format="lrc", subtitle_length=None):
        """
        Retrieve the subtitle of a track.

        Return the subtitle of a track in LRC or DFXP format.
        Refer to Wikipedia LRC format page or DFXP format on W3c for format specifications.

        :type common_track_id: string
        :type subtitle_format: string
        :type subtitle_length: int

        :param common_track_id: The Musixmatch commontrack id.
        :param subtitle_format: The format of the subtitle (lrc,dfxp,stledu).
        :param subtitle_length: The desired length of the subtitle (seconds).

        :return [Snippet]: Snippet Object.
        """
        subtitle_formats = ["lrc", "dfxp", "stledu"]
        assert subtitle_format in subtitle_formats, "Sorting must be in %s" % str(subtitle_formats)
        url = "/track.subtitle.get"
        params = {
            "commontrack_id": common_track_id,
            "subtitle_format": subtitle_format,
            "f_subtitle_length": subtitle_length
        }
        result = self._get(url, params=params)
        return SubtitleModel._parse(result["message"]["body"]["snippet"])
