# coding=utf-8
import requests

from musixmatch.expections import MusixmatchException, NotFound


class Client(object):
    """
    Musixmatch Client

    HTTP connections to and communication with Musixmatch API.
    """
    STATUS_CODES = {
        "400": "The request had bad syntax or was inherently impossible to be satisfied.",
        "401": "Authentication failed, probably because of invalid/missing API key.",
        "402": "The usage limit has been reached, "
             "either you exceeded per day requests limits or your balance is insufficient.",
        "403": "You are not authorized to perform this operation.",
        "404": "The requested resource was not found.",
        "405": "The requested method was not found.",
        "500": "Ops. Something were wrong.",
        "503": "Our system is a bit busy at the moment and your request can’t be satisfied.",
    }

    def __init__(self, api, **kwargs):
        self.api = api
        self.system_error_message = "Unknown System Error"

    def _request(self, url, method, params=None, data=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)
        params = params or {}
        params.update(self._get_default_params())
        headers = kwargs.pop("headers", {})

        try:
            response = requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
        except Exception as e:
            raise MusixmatchException("Connection error: %s" % e)

        try:
            result = response.json()
            if not self._is_2xx(response.status_code):
                raise MusixmatchException(self.system_error_message)
            else:
                status_code = result["message"]["header"]["status_code"]
                if not self._is_2xx(status_code):
                    raise MusixmatchException(self._get_status_code_error(status_code))

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

    def _get_default_params(self):
        return {"apikey": self.api.api_key, "format": "json"}

    def _get_status_code_error(self, status_code):
        return self.STATUS_CODES.get(str(status_code), self.system_error_message)

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
    def _is_404(status_code):
        return status_code == 404

    @staticmethod
    def _is_5xx(status_code):
        return 500 <= status_code <= 599
