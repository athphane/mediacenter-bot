from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces.aria2p import Aria2p
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("add"))
async def aria_add_download(_, message: Message):
    link = message.command[1:]
    new_download = Aria2p().add_download(link)
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Show Details", f"show+{new_download.gid}")]])
    await message.reply(f"Started download of '{new_download.name}'!", reply_markup=button)


# Command help section
add_command_help(
    'aria2c', [
        ['/add', 'Add a new download. Send link as argument.'],
    ]
)
