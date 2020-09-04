from .RawAria2p import Aria2p


class GetDownloads(Aria2p):
    def get_downloads(self):
        """
        Get downloads from the client.
        :return:
        """
        return self.aria2.get_downloads()

    def get_status(self, status):
        """
        Get downloads with status
        :param status:
        :return:
        """
        return [download for download in self.get_downloads() if download.status == status]

    def get_completed(self):
        """
        Get completed downloads from client
        :return:
        """
        return self.get_status('complete')

    def get_error_downloads(self):
        """
        Get errored downloads from client
        :return:
        """
        return self.get_status('error')

    def get_removed(self):
        """
        Get removed downloads from client
        :return:
        """
        return self.get_status('removed')

    def get_active(self):
        """
        Get active downloads
        :return:
        """
        return self.get_status('active')
