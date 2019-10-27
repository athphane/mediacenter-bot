from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.torrents.torrents import torrent, torrents


@TorrentBot.on_callback_query(CustomFilters.callback_query('back', payload=False))
async def back(client, callback: CallbackQuery):
    await torrents(client, callback.message, back=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('update'))
async def update(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    await torrent(client, callback, torrent_hash=torrent_hash, update=True)


