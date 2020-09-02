from xmlrpc.client import ServerProxy


class Aria2RPC(object):
    def __init__(self, url="http://localhost:6800/rpc", token=None):
        self._url = url
        if token:
            self._token = 'token:' + token
        else:
            self._token = token
        self._client = ServerProxy(self._url)

    def addUri(self, uris, options):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.addUri
        params = [uris, options]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.addUri(*params)

    def remove(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.remove
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.remove(*params)

    def forceRemove(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.forceRemove
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.forceRemove(*params)

    def pause(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.pause
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.pause(*params)

    def forcePause(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.forcePause
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.forcePause(*params)

    def pauseAll(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.pauseAll
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.pauseAll(*params)

    def forcePauseAll(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.forcePauseAll
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.forcePauseAll(*params)

    def unpause(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.unpause
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.unpause(*params)

    def unpauseAll(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.unpauseAll
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.unpauseAll(*params)

    def addTorrent(self, torrent):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.addTorrent
        params = [torrent]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.addTorrent(*params)

    def addMetalink(self, metalink):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.addMetalink
        params = [metalink]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.addMetalink(*params)

    def purgeDownloadResult(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.purgeDownloadResult
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.purgeDownloadResult(*params)

    def removeDownloadResult(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.removeDownloadResult
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.removeDownloadResult(*params)

    def getUris(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getUris
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getUris(*params)

    def getFiles(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getFiles
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getFiles(*params)

    def getPeers(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getPeers
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getPeers(*params)

    def getServers(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getServers
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getServers(*params)

    def tellStatus(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.tellStatus
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.tellStatus(*params)

    def tellActive(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.tellActive
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.tellActive(*params)

    def tellWaiting(self, offset, num):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.tellWaiting
        params = [offset, num]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.tellWaiting(*params)

    def tellStopped(self, offset, num):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.tellStopped
        params = [offset, num]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.tellStopped(*params)

    def changeOption(self, gid, options):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.changeOption
        params = [gid, options]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.changeOption(*params)

    def changeGlobalOption(self, options):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.changeGlobalOption
        params = [options]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.changeGlobalOption(*params)

    def getVersion(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getVersion
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getVersion(*params)

    def getOption(self, gid):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getOption
        params = [gid]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getOption(*params)

    def getGlobalOption(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getGlobalOption
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getGlobalOption(*params)

    def changePosition(self, gid, pos, how):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.changePosition
        params = [gid, pos, how]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.changePosition(*params)

    def changeUri(self, gid, fileIndex, delUris, addUris):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.changeUri
        params = [gid, fileIndex, delUris, addUris]
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.changeUri(*params)

    def getSessionInfo(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getSessionInfo
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getSessionInfo(*params)

    def shutdown(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.shutdown
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.shutdown(*params)

    def getGlobalStat(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.getGlobalStat
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.getGlobalStat(*params)

    def forceShutdown(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.forceShutdown
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.forceShutdown(*params)

    def saveSession(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#aria2.saveSession
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.aria2.saveSession(*params)

    def multicall(self, methods):
        # https://aria2.github.io/manual/en/html/aria2c.html#system.multicall
        params = [methods]
        if self._token:
            params.insert(0, self._token)
        return self._client.system.multicall(*params)

    def listMethods(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#system.listMethods
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.system.listMethods(*params)

    def listNotifications(self):
        # https://aria2.github.io/manual/en/html/aria2c.html#system.listNotifications
        params = []
        if self._token:
            params.insert(0, self._token)
        return self._client.system.listNotifications(*params)
