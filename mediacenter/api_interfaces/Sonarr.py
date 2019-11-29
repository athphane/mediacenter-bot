from urllib.parse import urlencode
import requests
from mediacenter import SONARR_API_URL, SONARR_API_KEY


class SonarrAPI(object):
    def __init__(self):
        self.host = SONARR_API_URL
        self.key = SONARR_API_KEY

    def url(self, endpoint, params: dict = None):
        # default params
        if params is None:
            params = {}

        # encode incoming dict as url params
        params = urlencode(params)
        return f"{self.host}/{endpoint}?{params}"

    def request_get(self, url, data=None):
        """Wrapper on the requests.get"""
        if data is None:
            data = {}
        headers = {
            'X-Api-Key': self.key
        }
        res = requests.get(url, headers=headers, json=data)
        return res

    # ENDPOINT SERIES
    def get_series(self):
        """Get all of the series that are added to sonarr."""
        res = self.request_get(self.url('series'))
        return res.json()

    # ENDPOINT EPISODES
    def get_episodes(self, series_id):
        """Get all of the episodes of a given series id"""
        params = {
            'seriesId': series_id
        }
        res = self.request_get(self.url('episode', params))
        return res.json()
