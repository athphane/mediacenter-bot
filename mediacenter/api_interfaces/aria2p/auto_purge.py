from .RawAria2p import Aria2p


class AutoPurge(Aria2p):
    def auto_purge(self, link):
        """
        Add a download to the client

        :param link:
        :return:
        """
        return self.aria2.autopurge()
