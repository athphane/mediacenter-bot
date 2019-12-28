from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Emoji
from mediacenter.utils.custom_filters import CustomFilters
from mediacenter.plugins.qbittorrent.torrents import torrent
from mediacenter.api_interfaces.Qbittorrent import TorrentClient as QBT


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('incprio'))
async def increment_priority(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().increase_priority(torrent_hash)
        await callback.answer("Torrent Priority Increased")
        await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('decprio'))
async def decrement_priority(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().decrease_priority(torrent_hash)
        await callback.answer("Torrent Priority Decreased")
        await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('maxprio'))
async def decrement_priority(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().top_priority(torrent_hash)
        await callback.answer("Torrent Priority set to max")
        await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('minprio'))
async def decrement_priority(client, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().min_priority(torrent_hash)
        await callback.answer("Torrent Priority set to minimum")
        await torrent(client, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('priority'))
async def torrent_priorities(client, callback: CallbackQuery):
    torrent_hash = callback.payload

    buttons = [
        [
            InlineKeyboardButton(f"{Emoji.UP_ARROW} Priority", f"incprio+{torrent_hash}"),
            InlineKeyboardButton(f"{Emoji.DOWN_ARROW} Priority", f"decprio+{torrent_hash}"),
        ],
        [
            InlineKeyboardButton(f"{Emoji.TOP_ARROW} Max Priority", f"maxprio+{torrent_hash}"),
            InlineKeyboardButton(f"{Emoji.DOWN_ARROW} Min Priority", f"minprio+{torrent_hash}"),
        ],
        [
            InlineKeyboardButton(f"{Emoji.BACK_ARROW} Back", f"priority_back+{torrent_hash}"),
        ]
    ]

    await callback.edit_message_reply_markup(
        InlineKeyboardMarkup(buttons)
    )
