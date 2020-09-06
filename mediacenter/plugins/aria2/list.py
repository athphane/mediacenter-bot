from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces.aria2p import Aria2p
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters


def get_buttons():
    buttons = []
    for download in Aria2p().get_active():
        buttons.append([InlineKeyboardButton(f"{download.name}", f"show+{download.gid}")])

    return buttons


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("list"))
async def send_aria_list(_, message: Message):
    buttons = get_buttons()

    if buttons:
        await message.reply("Aria2c Active Downloads", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await message.reply("No Download Running!")


@MediaCenterBot.on_callback_query(custom_filters.current_module('aria2') & custom_filters.callback_query('back', False))
async def aria_go_back_to_list(_, callback: CallbackQuery):
    await callback.answer("Going back...")
    buttons = get_buttons()

    if buttons:
        await callback.message.edit("Aria2c Active Downloads", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await callback.message.edit("No Download Running!")


# Command help section
add_command_help(
    'aria2c', [
        ['/list', 'Lists all the running downloads on Aria2c'],
    ]
)
