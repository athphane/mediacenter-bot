from .RawSonarr import RawSonarrAPI


class Episodes(RawSonarrAPI):
    def episodes(self, series_id):
        """
        Get all of the episodes of a given series id
        :param series_id:
        :return:
        """
        params = {
            'seriesId': series_id
        }

        return self.request_get(self.url('episode', params)).json()
