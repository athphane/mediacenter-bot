from .RawSonarr import RawSonarrAPI


class SystemStats(RawSonarrAPI):
    def __get_system_status(self):
        """
        Get system status
        :return:
        """
        data = self.request_get(self.url('system/status')).json()
        return SystemStatus(data)

    @property
    def status(self):
        return self.__get_system_status()


class SystemStatus:
    def __init__(self, data: dict):
        self.version = data.get('version')
        self.buildTime = data.get('buildTime')
        self.isDebug = data.get('isDebug')
        self.isProduction = data.get('isProduction')
        self.isAdmin = data.get('isAdmin')
        self.isUserInteractive = data.get('isUserInteractive')
        self.startupPath = data.get('startupPath')
        self.appData = data.get('appData')
        self.osVersion = data.get('osVersion')
        self.isMono = data.get('isMono')
        self.isLinux = data.get('isLinux')
        self.branch = data.get('branch')
        self.authentication = data.get('authentication')
        self.startOfWeek = data.get('startOfWeek')
        self.urlBase = data.get('urlBase')
