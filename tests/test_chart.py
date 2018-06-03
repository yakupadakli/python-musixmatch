import unittest

from musixmatch.models import Artist, Track
from tests.config import MusixmatchTestCase


class ChartTest(MusixmatchTestCase):

    def test_artists(self):
        artists = self.musixmatch.chart.artists("tr", page_size=5)
        self.assertIsInstance(artists, list)
        self.assertIsInstance(artists[0], Artist)
        self.assertEqual(len(artists), 5)

    def test_tracks(self):
        tracks = self.musixmatch.chart.tracks("tr", page_size=5)
        self.assertIsInstance(tracks, list)
        self.assertIsInstance(tracks[0], Track)
        self.assertEqual(len(tracks), 5)


if __name__ == "__main__":
    unittest.main()
