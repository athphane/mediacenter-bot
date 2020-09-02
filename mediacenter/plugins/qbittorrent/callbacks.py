from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram.types import CallbackQuery
from mediacenter.utils import custom_filters
from mediacenter.plugins.qbittorrent.torrents import torrent, all_torrents


@MediaCenterBot.on_callback_query(custom_filters.callback_query('back', payload=False))
async def back(client, callback: CallbackQuery):
    await all_torrents(client, callback.message, back=True)


@MediaCenterBot.on_callback_query(custom_filters.callback_query('priority_back'))
async def priority_back(client, callback: CallbackQuery):
    await torrent(client, callback)


@MediaCenterBot.on_callback_query(custom_filters.callback_query('update'))
async def update(client, callback: CallbackQuery):
    await torrent(client, callback, update=True)
