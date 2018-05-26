import six


class MusixmatchException(Exception):
    """Musixmatch exception"""

    def __init__(self, message=None, **kwargs):
        self.message = six.text_type(message) if message else "Unknown error"
        super(MusixmatchException, self).__init__(message, **kwargs)

    def __str__(self):
        return self.message


class NotFound(MusixmatchException):
    message = six.text_type("Not Found")
