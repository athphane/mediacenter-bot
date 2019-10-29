from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import CallbackQuery
from mediacenter.utilities.custom_filters import CustomFilters
from mediacenter.plugins.qbittorrent.torrents import torrent
from mediacenter.utilities.Qbittorrent import TorrentClient as QBT


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('resume'))
async def resume_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().resume_torrent(torrent_hash)
    await callback.answer("Torrent Resumed")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('pause'))
async def pause_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().pause_torrent(torrent_hash)
    await callback.answer("Torrent Paused")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
