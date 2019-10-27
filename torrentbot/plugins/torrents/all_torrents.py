from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.helpers.Qbittorrent import TorrentClient as QBT


@TorrentBot.on_message(CustomFilters.command("controls"))
async def controls(bot, message: Message):
    await message.reply(
        "Here are some master controls..",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(f"Resume All", f"resume_all"),
                InlineKeyboardButton(f"Pause All", f"pause_all"),
            ],
        ])
    )


@TorrentBot.on_callback_query(CustomFilters.callback_query('pause_all', payload=False))
async def pause_all(client, callback: CallbackQuery):
    try:
        print("hits")
        QBT().pause_all()
        await callback.answer("Pausing all torrents.")
    except:
        await callback.answer("An error occurred..")
        await callback.edit_message_text("An error occurred. Please retry later..")


@TorrentBot.on_callback_query(CustomFilters.callback_query('resume_all', payload=False))
async def resume_all(client, callback: CallbackQuery):
    try:
        QBT().resume_all()
        await callback.answer("Resuming all torrents.")
    except:
        await callback.answer("An error occurred..")
        await callback.edit_message_text("An error occurred. Please retry later..")
