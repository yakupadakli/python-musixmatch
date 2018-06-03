import os
import unittest

from musixmatch.api import Musixmatch

SKIP_TEST = True

api_key = os.environ.get('API_KEY', '')


class MusixmatchTestCase(unittest.TestCase):

    def setUp(self):
        self.musixmatch = Musixmatch(api_key)
