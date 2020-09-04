from time import sleep

import pyrogram.errors as pyro_errors
from pyrogram import emoji
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from mediacenter.api_interfaces.qBittorrent.Qbittorrent import TorrentClient as QBT
from mediacenter import MediaCenterBot
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils.converters import human_bytes, human_unix_time, time_delta
from mediacenter.utils import custom_filters
from mediacenter.api_interfaces.aria2p import Aria2p


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("list"))
async def send_aria_list(_, message: Message):
    for x in Aria2p().get_completed():
        await MediaCenterBot.send_message(message.chat.id, x.status)


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("add"))
async def aria_add_download(_, message: Message):
    link = message.command[1:]
    Aria2p().add_download(link)
