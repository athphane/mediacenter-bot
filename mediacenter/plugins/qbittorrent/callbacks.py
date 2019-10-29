from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import CallbackQuery
from mediacenter.utilities.custom_filters import CustomFilters
from mediacenter.plugins.qbittorrent.torrents import torrent, torrents


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('back', payload=False))
async def back(client, callback: CallbackQuery):
    await torrents(client, callback.message, back=True)


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('update'))
async def update(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    await torrent(client, callback, torrent_hash=torrent_hash, update=True)
