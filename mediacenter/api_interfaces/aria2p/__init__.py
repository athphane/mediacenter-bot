from .get_downloads import GetDownloads
from .add_download import AddDownload
from .auto_purge import AutoPurge

class Aria2p(GetDownloads, AddDownload, AutoPurge):
    """Aria2p methods"""
