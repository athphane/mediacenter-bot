from .get_downloads import GetDownloads
from .add_download import AddDownload
from .auto_purge import AutoPurge
from .stats import Stats
from .start_pause import StartPause


class Aria2p(GetDownloads, AddDownload, AutoPurge, Stats, StartPause):
    """Aria2p methods"""
