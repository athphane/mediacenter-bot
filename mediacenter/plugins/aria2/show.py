from aria2p import Download
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces.aria2p import Aria2p
from mediacenter.utils import custom_filters


def create_message(download: Download):
    progress = "No Progress"

    if download.download_speed >= 1 and download.status == 'active':
        progress = f"{download.completed_length_string()}/{download.total_length_string()} ({download.progress_string()}) @ {download.download_speed_string()}\n\n"
    elif download.status != 'active':
        progress = f"{download.completed_length_string()}/{download.total_length_string()} ({download.progress_string()})\n\n"

    msg = (
        "Title:\n"
        f"{download.name}\n\n"
        "Progress:\n"
        f"{progress}"
        "ETA:\n"
        f"{download.eta_string()}"
    )

    return msg


def create_buttons(gid):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Update Stats", f'update_stats+{gid}'), InlineKeyboardButton("Back", 'back')],
        [InlineKeyboardButton("Pause", f'pause+{gid}'), InlineKeyboardButton("Resume", f'resume+{gid}')]
    ])


@MediaCenterBot.on_callback_query(custom_filters.current_module('aria2') & custom_filters.callback_query('show'))
async def aria_show_download(_, callback: CallbackQuery):
    gid = callback.payload
    await callback.answer("Fetching...")
    download = Aria2p().get_download(gid)
    try:
        await callback.message.edit_text(create_message(download), reply_markup=create_buttons(download.gid))
    except MessageNotModified:
        pass


@MediaCenterBot.on_callback_query(
    custom_filters.current_module('aria2') & custom_filters.callback_query('update_stats'))
async def aria_update_show(_, callback: CallbackQuery):
    await aria_show_download(None, callback)
