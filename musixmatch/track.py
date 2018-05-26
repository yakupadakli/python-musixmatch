from musixmatch.client import Client
from musixmatch.models import Lyrics as LyricsModel
from musixmatch.models import Track as TrackModel


class Track(Client):
    """Album operations."""
    MAX_PAGE_SIZE = 99

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
