import unittest

from musixmatch.models import Album, Artist
from tests.config import MusixmatchTestCase


class ArtistTest(MusixmatchTestCase):

    def test_get(self):
        artist = self.musixmatch.artist.get("118")
        self.assertIsInstance(artist, Artist)

    def test_related(self):
        artists = self.musixmatch.artist.related("56", page_size=5)
        self.assertIsInstance(artists, list)
        self.assertIsInstance(artists[0], Artist)
        self.assertEqual(len(artists), 5)

    def test_search(self):
        artists = self.musixmatch.artist.search("prodigy", page_size=5)
        self.assertIsInstance(artists, list)
        self.assertIsInstance(artists[0], Artist)
        self.assertEqual(len(artists), 5)

        artists1 = self.musixmatch.artist.search("", artist_id="118", page_size=1)
        self.assertIsInstance(artists1, list)
        self.assertIsInstance(artists1[0], Artist)
        self.assertEqual(len(artists1), 1)

    def test_albums(self):
        albums = self.musixmatch.artist.albums("1039", page_size=5)
        self.assertIsInstance(albums, list)
        self.assertIsInstance(albums[0], Album)
        self.assertEqual(len(albums), 5)


if __name__ == "__main__":
    unittest.main()
