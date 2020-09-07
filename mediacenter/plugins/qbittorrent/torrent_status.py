from pyrogram.types import CallbackQuery

from mediacenter.api_interfaces.qBittorrent.Qbittorrent import TorrentClient as QBT
from mediacenter import MediaCenterBot
from mediacenter.plugins.qbittorrent.torrents import torrent
from mediacenter.utils import custom_filters


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('resume'))
async def resume_torrent(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().resume_torrent(torrent_hash)
    await callback.answer("Torrent Resumed")
    await torrent(_, callback, torrent_hash=torrent_hash, update=True, answer=False)


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('pause'))
async def pause_torrent(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().pause_torrent(torrent_hash)
    await callback.answer("Torrent Paused")
    await torrent(_, callback, torrent_hash=torrent_hash, update=True, answer=False)
