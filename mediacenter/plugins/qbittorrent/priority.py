from pyrogram import emoji
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from mediacenter.api_interfaces.Qbittorrent import TorrentClient as QBT
from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.plugins.qbittorrent.torrents import torrent
from mediacenter.utils import custom_filters


@MediaCenterBot.on_callback_query(custom_filters.callback_query('incprio'))
async def increment_priority(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().increase_priority(torrent_hash)
        await callback.answer("Torrent Priority Increased")
        await torrent(_, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(custom_filters.callback_query('decprio'))
async def decrement_priority(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().decrease_priority(torrent_hash)
        await callback.answer("Torrent Priority Decreased")
        await torrent(_, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(custom_filters.callback_query('maxprio'))
async def decrement_priority(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().top_priority(torrent_hash)
        await callback.answer("Torrent Priority set to max")
        await torrent(_, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(custom_filters.callback_query('minprio'))
async def decrement_priority(_, callback: CallbackQuery):
    torrent_hash = callback.payload
    try:
        QBT().min_priority(torrent_hash)
        await callback.answer("Torrent Priority set to minimum")
        await torrent(_, callback, torrent_hash=torrent_hash, update=True, answer=False)
    except:
        await callback.answer("Something went wrong.")


@MediaCenterBot.on_callback_query(custom_filters.callback_query('priority'))
async def torrent_priorities(_, callback: CallbackQuery):
    torrent_hash = callback.payload

    buttons = [
        [
            InlineKeyboardButton(f"{emoji.UP_ARROW} Priority", f"incprio+{torrent_hash}"),
            InlineKeyboardButton(f"{emoji.DOWN_ARROW} Priority", f"decprio+{torrent_hash}"),
        ],
        [
            InlineKeyboardButton(f"{emoji.TOP_ARROW} Max Priority", f"maxprio+{torrent_hash}"),
            InlineKeyboardButton(f"{emoji.DOWN_ARROW} Min Priority", f"minprio+{torrent_hash}"),
        ],
        [
            InlineKeyboardButton(f"{emoji.BACK_ARROW} Back", f"priority_back+{torrent_hash}"),
        ]
    ]

    await callback.edit_message_reply_markup(
        InlineKeyboardMarkup(buttons)
    )
