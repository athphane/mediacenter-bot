from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.torrents import torrent, torrents
from torrentbot.helpers.Qbittorrent import TorrentClient as QBT
import time


@TorrentBot.on_callback_query(CustomFilters.callback_query('back'))
async def back(client, callback: CallbackQuery):
    await torrents(client, callback.message, back=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('update'))
async def update(client, callback: CallbackQuery):
    torrent_hash = callback.data[7:]
    await torrent(client, callback, torrent_hash=torrent_hash, update=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('resume'))
async def resume_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.data[7:]
    QBT().resume_torrent(torrent_hash)
    await callback.answer("Torrent Resumed")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@TorrentBot.on_callback_query(CustomFilters.callback_query('pause'))
async def pause_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.data[6:]
    QBT().pause_torrent(torrent_hash)
    await callback.answer("Torrent Paused")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@TorrentBot.on_callback_query(CustomFilters.callback_query('delete'))
async def show_delete_options(client, callback: CallbackQuery):
    def delete_buttons(torrent_hash):
        buttons = [
            [
                InlineKeyboardButton("Delete Only Torrent", f"deltor+{torrent_hash}"),
                InlineKeyboardButton("Delete w/Files", f"delfile+{torrent_hash}"),
            ],
        ]

        return buttons

    torrent_hash = callback.data[7:]
    await callback.edit_message_text(
        "How do you want to delete this torrent?",
        reply_markup=InlineKeyboardMarkup(delete_buttons(torrent_hash))
    )


@TorrentBot.on_callback_query(CustomFilters.callback_query('deltor'))
async def delete_only_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.data[6:]
    QBT().delete_torrent(torrent_hash)
    await callback.answer("Torrent Deleted")
    time.sleep(2)
    await torrents(client, callback.message, back=True)
