from .RawAria2p import Aria2p


class GetDownloads(Aria2p):
    def get_downloads(self):
        """
        Get downloads from the client.
        :return:
        """
        return self.aria2.get_downloads()

    def get_download(self, gid):
        """
        Get download with corresponding gid from the client.
        :param gid:
        :return:
        """
        return self.aria2.get_download(gid)

    def __get_of_status(self, status):
        """
        Get downloads with status
        :param status:
        :return:
        """
        return [download for download in self.get_downloads() if download.status == status]

    def get_completed(self):
        """
        Get downloads with status 'complete'
        :return:
        """
        return self.__get_of_status('complete')

    def get_error_downloads(self):
        """
        Get downloads with status 'error'
        :return:
        """
        return self.__get_of_status('error')

    def get_removed(self):
        """
        Get downloads with status 'removed'
        :return:
        """
        return self.__get_of_status('removed')

    def get_active(self):
        """
        Get downloads with status 'active'
        :return:
        """
        return self.__get_of_status('active')
