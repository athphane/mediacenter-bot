from .RawAria2p import Aria2p


class AutoPurge(Aria2p):
    def auto_purge(self):
        """
        Add a download to the client
        :return:
        """
        return self.aria2.autopurge()
