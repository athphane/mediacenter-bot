from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from mediacenter.api_interfaces.qBittorrent.Qbittorrent import TorrentClient as QBT
from mediacenter import MediaCenterBot
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.current_module('qbt') & custom_filters.command("controls"))
async def controls(_, message: Message):
    await message.reply(
        "Here are some master controls..",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(f"Resume All", f"resume_all"),
                InlineKeyboardButton(f"Pause All", f"pause_all"),
            ],
        ])
    )


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('pause_all', payload=False))
async def pause_all(_, callback: CallbackQuery):
    try:
        await callback.answer("Pausing all torrents.")
        QBT().pause_all()
    except:
        await callback.answer("An error occurred..")
        await callback.edit_message_text("An error occurred. Please retry later..")


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('resume_all', payload=False))
async def resume_all(_, callback: CallbackQuery):
    try:
        await callback.answer("Resuming all torrents.")
        QBT().resume_all()
    except:
        await callback.answer("An error occurred..")
        await callback.edit_message_text("An error occurred. Please retry later..")
