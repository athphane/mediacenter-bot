from .RawAria2p import Aria2p
from aria2p import Download


class StartPause(Aria2p):
    def pause(self, download: Download):
        """
        Pause single download
        :return:
        """
        return self.aria2.pause([download])

    def resume(self, download: Download):
        """
        Resume single download
        :return:
        """
        return self.aria2.resume([download])

