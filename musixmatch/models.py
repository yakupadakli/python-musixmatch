from musixmatch.expections import NotFound


class ResultSet(list):
    """A list like object that holds results from a Musixmatch API query."""


class Model(object):
    _not_found_error_class = NotFound
    remove_tag = None

    def __init__(self, **kwargs):
        self._repr_values = {"id": "Id"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls._not_found_error_class()

        instance = cls() if data else None
        for key, value in data.items():
            key = key.split(cls.remove_tag)[-1]
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
    remove_tag = "artist_"

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
    remove_tag = "music_genre_"

    def __init__(self, **kwargs):
        super(Genre, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "id": "Id"}


class ArtistAlias(Model):
    remove_tag = "artist_"

    def __init__(self, **kwargs):
        super(ArtistAlias, self).__init__(**kwargs)
        self._repr_values = {"alias": "Alias"}
