from .RawSonarr import RawSonarrAPI
from .models import Show


class Shows(RawSonarrAPI):
    def all_shows(self):
        """
        Get all shows added to Sonarr
        :return:
        """
        res = self.request_get(self.url('series')).json()
        return [Show(x) for x in res]

    def get_show(self, show_id):
        """
        Get show details by ID
        :param show_id:
        :return:
        """
        r = self.request_get(self.url(f"series/{show_id}"))
        return Show(r.json())
