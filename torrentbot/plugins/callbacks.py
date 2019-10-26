from torrentbot.torrentbot import TorrentBot
from pyrogram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Emoji
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.torrents import torrent, torrents
from torrentbot.helpers.Qbittorrent import TorrentClient as QBT
import time


@TorrentBot.on_callback_query(CustomFilters.callback_query('back', payload=False))
async def back(client, callback: CallbackQuery):
    await torrents(client, callback.message, back=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('update'))
async def update(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    await torrent(client, callback, torrent_hash=torrent_hash, update=True)


@TorrentBot.on_callback_query(CustomFilters.callback_query('resume'))
async def resume_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().resume_torrent(torrent_hash)
    await callback.answer("Torrent Resumed")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


@TorrentBot.on_callback_query(CustomFilters.callback_query('pause'))
async def pause_torrent(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    QBT().pause_torrent(torrent_hash)
    await callback.answer("Torrent Paused")
    await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)


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


@TorrentBot.on_callback_query(CustomFilters.callback_query('incprio'))
async def increment_priority(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().increase_priority(torrent_hash)
        await callback.answer("Torrent Priority Increased")
        await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@TorrentBot.on_callback_query(CustomFilters.callback_query('decprio'))
async def decrement_priority(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().decrease_priority(torrent_hash)
        await callback.answer("Torrent Priority Decreased")
        await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@TorrentBot.on_callback_query(CustomFilters.callback_query('priority'))
async def torrent_priorities(client, callback: CallbackQuery):
    torrent_hash = callback.payload

    buttons = [
        [
            InlineKeyboardButton(f"{Emoji.UP_ARROW} Priority", f"incprio+{torrent_hash}"),
            InlineKeyboardButton(f"{Emoji.DOWN_ARROW} Priority", f"decprio+{torrent_hash}"),
        ],
    ]

    await callback.edit_message_reply_markup(
        InlineKeyboardMarkup(buttons)
    )
