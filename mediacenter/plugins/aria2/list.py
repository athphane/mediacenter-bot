from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces.aria2p import Aria2p
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("list"))
async def send_aria_list(_, message: Message):
    buttons = []
    for download in Aria2p().get_active():
        buttons.append([InlineKeyboardButton(f"{download.name}", f"show+{download.gid}")])

    if buttons:
        await message.reply("Aria2c Active Downloads", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await message.reply("No Download Running!")
