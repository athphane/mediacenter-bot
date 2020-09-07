from urllib.parse import urlencode
import requests
from mediacenter import SONARR_API_URL, SONARR_API_KEY


class RawSonarrAPI:
    def __init__(self):
        self.host = SONARR_API_URL
        self.key = SONARR_API_KEY

    def url(self, endpoint, params: dict = None):
        """
        URL constructor
        :param endpoint:
        :param params:
        :return:
        """
        if params is None:
            params = {}

        # encode incoming dict as url params
        params = urlencode(params)
        url = f"{self.host}/{endpoint}"

        return f"{url}?{params}" if params else url

    def url_with_key(self, endpoint, params: dict = None):
        """
        Add API key to url
        :param endpoint:
        :param params:
        :return:
        """
        url = self.url(endpoint.rstrip('/').lstrip('/'), {'apikey': self.key})
        return url

    def request_get(self, url, data=None):
        """
        Wrapper on the requests.get
        :param url:
        :param data:
        :return:
        """
        if data is None:
            data = {}

        headers = {
            'X-Api-Key': self.key
        }
        res = requests.get(url, headers=headers, json=data)
        return res
