from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.torrents import torrent, torrents
from torrentbot.helpers.Qbittorrent import TorrentClient as QBT
import time


@TorrentBot.on_callback_query(CustomFilters.callback_query('back'))
def back(client, callback: CallbackQuery):
    torrents(client, callback.message, back=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('update'))
def update(client, callback: CallbackQuery):
    torrent_hash = callback.data[7:]
    torrent(client, callback, torrent_hash=torrent_hash, update=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('resume'))
def resume_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.data[7:]
    QBT().resume_torrent(torrent_hash)
    callback.answer("Torrent Resumed")
    torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@TorrentBot.on_callback_query(CustomFilters.callback_query('pause'))
def pause_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.data[6:]
    QBT().pause_torrent(torrent_hash)
    callback.answer("Torrent Paused")
    torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@TorrentBot.on_callback_query(CustomFilters.callback_query('delete'))
def show_delete_options(client, callback: CallbackQuery):
    def delete_buttons(torrent_hash):
        buttons = [
            [
                InlineKeyboardButton("Delete Only Torrent", f"deltor+{torrent_hash}"),
                InlineKeyboardButton("Delete w/Files", f"delfile+{torrent_hash}"),
            ],
        ]

        return buttons

    torrent_hash = callback.data[7:]
    callback.edit_message_text("How do you want to delete this torrent?",
                               reply_markup=InlineKeyboardMarkup(delete_buttons(torrent_hash))
                               )


@TorrentBot.on_callback_query(CustomFilters.callback_query('deltor'))
def delete_only_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.data[6:]
    QBT().delete_torrent(torrent_hash)
    callback.answer("Torrent Deleted")
    time.sleep(2)
    torrents(client, callback.message, back=True)
