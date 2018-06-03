import unittest

from musixmatch.models import Album
from musixmatch.models import Track
from tests.config import MusixmatchTestCase


class AlbumTest(MusixmatchTestCase):

    def test_get(self):
        album = self.musixmatch.album.get("14250417")
        self.assertIsInstance(album, Album)

    def test_tracks(self):
        tracks = self.musixmatch.album.tracks("13750844", page_size=10)
        self.assertIsInstance(tracks, list)
        self.assertIsInstance(tracks[0], Track)
        self.assertEqual(len(tracks), 10)


if __name__ == "__main__":
    unittest.main()
