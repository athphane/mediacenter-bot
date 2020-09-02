import time

from pyrogram import emoji
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from mediacenter.api_interfaces.Qbittorrent import TorrentClient as QBT
from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.plugins.qbittorrent.torrents import all_torrents
from mediacenter.utils import custom_filters


@MediaCenterBot.on_callback_query(custom_filters.callback_query('delete_tor'))
async def show_delete_options(_, callback: CallbackQuery):
    def delete_buttons(torrent_hash):
        buttons = [
            [
                InlineKeyboardButton("Delete Only Torrent", f"deltor+{torrent_hash}"),
                InlineKeyboardButton("Delete w/Files", f"delfile+{torrent_hash}"),
            ],
        ]

        return buttons

    torrent_hash = callback.payload
    await callback.edit_message_text(
        "How do you want to delete this torrent?",
        reply_markup=InlineKeyboardMarkup(delete_buttons(torrent_hash))
    )


@MediaCenterBot.on_callback_query(custom_filters.callback_query('deltor'))
async def delete_torrent(_, callback: CallbackQuery, **kwargs):
    torrent_hash = kwargs.get('torrent_hash') if kwargs.get('torrent_hash') else callback.payload
    try:
        if kwargs.get('files'):
            QBT().delete_torrent_files(torrent_hash)
        else:
            QBT().delete_torrent(torrent_hash)

        await callback.answer("SUCCESS")
        await callback.message.reply(
            f"{emoji.FIRE} **Torrent {'and Files ' if kwargs.get('files') else ''}Deleted** {emoji.FIRE}"
        )
        time.sleep(2)
        await callback.message.delete()
        await all_torrents(_, callback.message)
    except Exception:
        await callback.answer("ERROR")
        await callback.message.reply(f"{emoji.SKULL} **An error has occurred** {emoji.SKULL}")


@MediaCenterBot.on_callback_query(custom_filters.callback_query('delfile'))
async def delete_only_torrent(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    await delete_torrent(_, callback, torrent_hash=torrent_hash, files=True)
