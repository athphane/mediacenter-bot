from .RawAria2p import Aria2p


class AddDownload(Aria2p):
    def add_download(self, link):
        """
        Add a download to the client

        :param link:
        :return:
        """
        return self.aria2.add_uris(link)
