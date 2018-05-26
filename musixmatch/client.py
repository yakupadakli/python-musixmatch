import requests

from musixmatch.expections import MusixmatchException


class Client(object):
    """
    Musixmatch Client

    HTTP connections to and communication with Musixmatch API.
    """

    def __init__(self, api, **kwargs):
        self.api = api

    def _request(self, url, method, params=None, data=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)
        headers = kwargs.pop("headers", {})

        try:
            response = requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
        except Exception as e:
            raise MusixmatchException("Connection error: %s" % e)

        try:
            if not self._is_2xx(response.status_code):
                error = response.json().get("message")
                raise MusixmatchException(error)
            result = response.json()
        except ValueError as e:
            result = None
        return result

    def _get(self, url, params=None, **kwargs):
        return self._request(url, "get", params=params, **kwargs)

    def _post(self, url, data=None, **kwargs):
        return self._request(url, "post", data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request(url, "delete", **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request(url, "put", data=data, **kwargs)

    @staticmethod
    def _is_1xx(status_code):
        return 100 <= status_code <= 199

    @staticmethod
    def _is_2xx(status_code):
        return 200 <= status_code <= 299

    @staticmethod
    def _is_3xx(status_code):
        return 300 <= status_code <= 399

    @staticmethod
    def _is_4xx(status_code):
        return 400 <= status_code <= 499

    @staticmethod
    def _is_5xx(status_code):
        return 500 <= status_code <= 599
