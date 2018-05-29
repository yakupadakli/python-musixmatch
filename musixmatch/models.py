from musixmatch.expections import NotFound


class ResultSet(list):
    """A list like object that holds results from a Musixmatch API query."""


class Model(object):
    _not_found_error_class = NotFound
    _remove_tag = None

    def __init__(self, **kwargs):
        self._repr_values = {"id": "Id"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls._not_found_error_class()

        instance = cls() if data else None
        for key, value in data.items():
            key = key.split(cls._remove_tag)[-1]
            if type(value) == str:
                value = value.strip()
            setattr(instance, key, value)
        return instance

    @classmethod
    def _parse_list(cls, data, sub_item=False):
        """Parse a list of JSON objects into a result set of model instances."""
        results = ResultSet()
        data = data or []
        for obj in data:
            if obj:
                results.append(cls._parse(obj, sub_item=sub_item))
        return results

    def __repr__(self):
        items = filter(lambda x: x[0] in self._repr_values.keys(), vars(self).items())
        state = ['%s: %s' % (self._repr_values[k], repr(v)) for (k, v) in items]
        return '<%s: %s >' % (self.__class__.__name__, ', '.join(state))


class Artist(Model):
    _remove_tag = "artist_"

    def __init__(self, **kwargs):
        super(Artist, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "id": "Id"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        artist = super(Artist, cls)._parse(data, sub_item=sub_item)

        if hasattr(artist, "alias_list"):
            artist.alias_list = ArtistAlias._parse_list(artist.alias_list, sub_item=True)

        if hasattr(artist, "primary_genres"):
            primary_genres = map(lambda x: x.get("music_genre"),  artist.primary_genres.get("music_genre_list", []))
            artist.primary_genres = Genre._parse_list(primary_genres, sub_item=True)

        if hasattr(artist, "secondary_genres"):
            secondary_genres = map(lambda x: x.get("music_genre"), artist.secondary_genres.get("music_genre_list", []))
            artist.secondary_genres = Genre._parse_list(secondary_genres, sub_item=True)

        return artist


class Genre(Model):
    _remove_tag = "music_genre_"

    def __init__(self, **kwargs):
        super(Genre, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "id": "Id"}


class ArtistAlias(Model):
    _remove_tag = "artist_"

    def __init__(self, **kwargs):
        super(ArtistAlias, self).__init__(**kwargs)
        self._repr_values = {"alias": "Alias"}


class Album(Model):
    _remove_tag = "album_"

    def __init__(self, **kwargs):
        super(Album, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "id": "Id"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        album = super(Album, cls)._parse(data, sub_item=sub_item)

        if hasattr(album, "primary_genres"):
            primary_genres = map(lambda x: x.get("music_genre"),  album.primary_genres.get("music_genre_list", []))
            album.primary_genres = Genre._parse_list(primary_genres, sub_item=True)

        if hasattr(album, "secondary_genres"):
            secondary_genres = map(lambda x: x.get("music_genre"), album.secondary_genres.get("music_genre_list", []))
            album.secondary_genres = Genre._parse_list(secondary_genres, sub_item=True)

        return album


class Track(Model):
    _remove_tag = "track_"

    def __init__(self, **kwargs):
        super(Track, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "id": "Id", "album_name": "Album Name"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        track = super(Track, cls)._parse(data, sub_item=sub_item)

        if hasattr(track, "primary_genres"):
            primary_genres = map(lambda x: x.get("music_genre"),  track.primary_genres.get("music_genre_list", []))
            track.primary_genres = Genre._parse_list(primary_genres, sub_item=True)

        if hasattr(track, "secondary_genres"):
            secondary_genres = map(lambda x: x.get("music_genre"), track.secondary_genres.get("music_genre_list", []))
            track.secondary_genres = Genre._parse_list(secondary_genres, sub_item=True)

        return track


class Lyrics(Model):
    _remove_tag = "lyrics_"

    def __init__(self, **kwargs):
        super(Lyrics, self).__init__(**kwargs)
        self._repr_values = {"id": "Id", "language": "Language"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        lyrics = super(Lyrics, cls)._parse(data, sub_item=sub_item)

        if hasattr(lyrics, "translated_lyrics"):
            lyrics.translated_lyrics = TranslatedLyrics._parse_list(lyrics.translated_lyrics, sub_item=True)

        return lyrics


class TranslatedLyrics(Model):

    def __init__(self, **kwargs):
        super(TranslatedLyrics, self).__init__(**kwargs)
        self._repr_values = {"language": "Language"}


class Snippet(Model):
    _remove_tag = "snippet_"

    def __init__(self, **kwargs):
        super(Snippet, self).__init__(**kwargs)
        self._repr_values = {"body": "Body", "language": "Language"}


class Subtitle(Model):
    _remove_tag = "subtitle_"

    def __init__(self, **kwargs):
        super(Subtitle, self).__init__(**kwargs)
        self._repr_values = {"id": "Id", "language": "Language"}
