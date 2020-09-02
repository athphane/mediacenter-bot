import json

import requests
from deprecation import deprecated

from mediacenter import QBT_URL, QBT_USER, QBT_PASS


class TorrentClient:
    def __init__(self):
        self.qbt_url = str(QBT_URL)
        self.username = QBT_USER
        self.password = QBT_PASS
        self.http_url = f"{self.qbt_url}/api/v2"

        self.session = requests.Session()
        data = {
            'username': self.username,
            'password': self.password,
            'Accept': 'application/json'
        }

        login_request = self.session.post(self.get_api_url('auth/login'), data=data)

        if login_request.text == 'Ok.':
            self._is_authenticated = True

    def get_api_url(self, endpoint=''):
        api_url = self.http_url.rstrip('/')
        endpoint = endpoint.lstrip('/')

        if endpoint:
            api_url += f"/{endpoint}"

        return api_url

    def _request(self, endpoint, method, data=None, **kwargs):
        final_url = self.get_api_url(endpoint)

        if not self._is_authenticated:
            return

        rq = self.session
        if method == 'get':
            request = rq.get(final_url, **kwargs)
        else:
            request = rq.post(final_url, data, **kwargs)

        request.raise_for_status()
        request.encoding = 'utf_8'

        if len(request.text) == 0:
            data = json.loads('{}')
        else:
            try:
                data = json.loads(request.text)
            except ValueError:
                data = request.text

        return data

    def _get(self, endpoint, **kwargs):
        return self._request(endpoint, 'get', **kwargs)

    def _post(self, endpoint, data, **kwargs):
        return self._request(endpoint, 'post', data, **kwargs)

    def login(self):
        self.session = requests.Session()
        data = {
            'username': self.username,
            'password': self.password,
            'Accept': 'application/json'
        }

        login_request = self.session.post(self.get_api_url('auth/login'), data=data)

        if login_request.text == 'Ok.':
            self._is_authenticated = True
        else:
            return login_request.text

    @property
    def api_version(self):
        """
        Get version of qBitTorrent

        :return:
        """
        return self._get('app/version')

    def shutdown(self):
        """
        Shutdown qBitTorrent
        :return:
        """
        return self._get('app/shutdown')

    def torrents(self):
        """
        Get all torrents

        :return:
        """
        return self._get('torrents/info')

    def add_all_info(self, properties, torrent_hash):
        from_torrents = self.torrents()

        for torrent in from_torrents:
            if torrent['hash'] == torrent_hash:
                matched_torrent = dict(torrent)
                keys = matched_torrent.keys()

                for key in keys:
                    properties[key] = matched_torrent[key]

        return properties

    def single_torrent(self, torrent_hash):
        """
        Get torrent properties

        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/properties?hash={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def pause_torrent(self, torrent_hash):
        """
        Pause a torrent

        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/pause?hashes={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def resume_torrent(self, torrent_hash):
        """
        Resume a torrent

        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/resume?hashes={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def delete_torrent(self, torrent_hash, delete_files=False):
        """
        Delete torrent with or without files

        :param torrent_hash:
        :param delete_files:
        :return:
        """
        properties = self._get(
            f"torrents/delete?hashes={torrent_hash}&deleteFiles={'false' if not delete_files else 'true'}"
        )
        return self.add_all_info(properties, torrent_hash)

    @deprecated(details="We use delete_torrent function instead.")
    def delete_torrent_files(self, torrent_hash):
        """
        Delete torrent and its files.
        deprecated
        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/delete?hashes={torrent_hash}&deleteFiles=true')
        return self.add_all_info(properties, torrent_hash)

    def add_torrent(self, link):
        """
        Add new torrent from link

        :param link:
        :return:
        """
        data = {
            'urls': link,
        }

        return self._post(f'torrents/add', data=data)

    def find_torrent_name(self, torrent_hash):
        """
        Find torrent name based on hash

        :param torrent_hash:
        :return:
        """
        for x in self.torrents():
            if x['hash'] == torrent_hash:
                return x['name']

    def pause_all(self):
        """
        Pause all torrents

        :return:
        """
        return self._get(f'torrents/pause?hashes=all')

    def resume_all(self):
        """
        Resume all torrents

        :return:
        """
        return self._get(f'torrents/resume?hashes=all')

    def increase_priority(self, torrent_hash):
        """
        Increase torrent priority
        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/increasePrio?hashes={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def decrease_priority(self, torrent_hash):
        """
        Decrease torrent priority

        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/decreasePrio?hashes={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def top_priority(self, torrent_hash):
        """
        Set torrent as highest priority

        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/topPrio?hashes={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def min_priority(self, torrent_hash):
        """
        Set torrent as lowest priority

        :param torrent_hash:
        :return:
        """
        properties = self._get(f'torrents/bottomPrio?hashes={torrent_hash}')
        return self.add_all_info(properties, torrent_hash)

    def all_categories(self):
        """
        Get all categories

        :return:
        """
        return self._get(f'torrents/categories')

    def add_category(self, category_name):
        """
        Add a new category to qBitTorrent

        :param category_name:
        :return:
        """
        data = {
            'category': category_name,
            'savePath': None
        }

        return self._post(f'torrents/createCategory', data=data)
