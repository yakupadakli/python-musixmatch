import unittest

from musixmatch.models import Artist, Track, Lyrics, Snippet, Subtitle
from tests.config import MusixmatchTestCase


class TrackTest(MusixmatchTestCase):

    def test_get(self):
        track = self.musixmatch.track.get(track_id="15445219")
        self.assertIsInstance(track, Track)

        track1 = self.musixmatch.track.get(common_track_id="5920049")
        self.assertIsInstance(track1, Track)

    def test_lyrics(self):
        lyrics = self.musixmatch.track.lyrics(track_id="15953433")
        self.assertIsInstance(lyrics, Lyrics)

    def test_lyrics_translation(self):
        # TODO
        # This method requires authentication.
        # lyrics = self.musixmatch.track.lyrics_translation("15953433", "tr")
        # self.assertIsInstance(lyrics, Lyrics)
        pass

    def test_search(self):
        tracks = self.musixmatch.track.search("tarkan", page_size=5)
        self.assertIsInstance(tracks, list)
        self.assertIsInstance(tracks[0], Track)
        self.assertEqual(len(tracks), 5)

    def test_snippet(self):
        snippet = self.musixmatch.track.snippet("16860631")
        self.assertIsInstance(snippet, Snippet)

    def test_subtitle(self):
        # TODO
        # This method requires authentication with api key and a commercial plan.
        # subtitle = self.musixmatch.track.subtitle("10074988")
        # self.assertIsInstance(subtitle, Subtitle)
        pass


if __name__ == "__main__":
    unittest.main()
