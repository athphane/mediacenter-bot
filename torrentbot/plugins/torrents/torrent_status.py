from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery
from torrentbot.utilities.custom_filters import CustomFilters
from torrentbot.plugins.torrents.torrents import torrent
from torrentbot.utilities.Qbittorrent import TorrentClient as QBT


@TorrentBot.on_callback_query(CustomFilters.callback_query('resume'))
async def resume_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().resume_torrent(torrent_hash)
    await callback.answer("Torrent Resumed")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@TorrentBot.on_callback_query(CustomFilters.callback_query('pause'))
async def pause_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().pause_torrent(torrent_hash)
    await callback.answer("Torrent Paused")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
