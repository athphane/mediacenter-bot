from pyrogram.types import CallbackQuery

from mediacenter import MediaCenterBot
from mediacenter.plugins.qbittorrent.torrents import torrent, all_torrents
from mediacenter.utils import custom_filters


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('back', payload=False))
async def back(_, callback: CallbackQuery):
    await all_torrents(_, callback.message, back=True)


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('priority_back'))
async def priority_back(_, callback: CallbackQuery):
    await torrent(_, callback)


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('update'))
async def update(_, callback: CallbackQuery):
    await torrent(_, callback, update=True)
