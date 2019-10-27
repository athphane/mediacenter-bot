from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Emoji
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.torrents.torrents import torrents
from torrentbot.helpers.Qbittorrent import TorrentClient as QBT
import time


@TorrentBot.on_callback_query(CustomFilters.callback_query('delete_tor'))
async def show_delete_options(client, callback: CallbackQuery):
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


@TorrentBot.on_callback_query(CustomFilters.callback_query('deltor'))
async def delete_torrent(client, callback: CallbackQuery, **kwargs):
    torrent_hash = kwargs.get('torrent_hash') if kwargs.get('torrent_hash') else callback.payload
    try:
        if kwargs.get('files'):
            QBT().delete_torrent_files(torrent_hash)
        else:
            QBT().delete_torrent(torrent_hash)

        await callback.answer("SUCCESS")
        await callback.message.reply(
            f"{Emoji.FIRE} **Torrent {'and Files ' if kwargs.get('files') else ''}Deleted** {Emoji.FIRE}"
        )
        time.sleep(2)
        await callback.message.delete()
        await torrents(client, callback.message)
    except Exception:
        await callback.answer("ERROR")
        await callback.message.reply(f"{Emoji.SKULL} **And error has occurred** {Emoji.SKULL}")


@TorrentBot.on_callback_query(CustomFilters.callback_query('delfile'))
async def delete_only_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    await delete_torrent(client, callback, torrent_hash=torrent_hash, files=True)