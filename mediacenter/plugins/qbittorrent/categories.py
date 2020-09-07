from pyrogram import errors as pyro_errors
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from mediacenter.api_interfaces.qBittorrent.Qbittorrent import TorrentClient as QBT
from mediacenter import MediaCenterBot
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.current_module('qbt') & custom_filters.command("categories"))
async def all_categories(_, message: Message):
    await message.reply(
        "Categories\nSelect an action.",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("List", 'list_categories'), InlineKeyboardButton("Create", "create_categories")],
            ]
        )
    )


@MediaCenterBot.on_callback_query(custom_filters.current_module('qbt') & custom_filters.callback_query('list_categories', False))
async def list_categories(_, callback: CallbackQuery):
    categories: dict = QBT().all_categories()

    categories_list = []
    for x in categories.keys():
        categories_list.append(categories.get(x).get('name'))

    categories_list = "\n".join(categories_list)

    full_text = (
        "Here are all of your categories\n\n"
        "{categories}"
    )

    await callback.answer("Listing Categories")

    try:
        await callback.edit_message_text(
            full_text.format(categories=categories_list),
            reply_markup=callback.message.reply_markup
        )
    except pyro_errors.MessageNotModified:
        pass


# Command help section
add_command_help(
    'categories', [
        ['/categories', 'Start the category'],
    ]
)
