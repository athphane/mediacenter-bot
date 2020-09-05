from .RawAria2p import Aria2p


class Stats(Aria2p):
    def stats(self):
        """
        Get stats from client
        :return:
        """
        return self.aria2.get_stats()
