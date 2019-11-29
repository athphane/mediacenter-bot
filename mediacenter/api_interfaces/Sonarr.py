import requests
from mediacenter import SONARR_API_URL, SONARR_API_KEY


class SonarrAPI(object):
    def __init__(self):
        self.host = SONARR_API_URL
        self.key = SONARR_API_KEY

    def url(self, endpoint):
        return f"{self.host}/{endpoint}"

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
