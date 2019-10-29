from mediacenter.plugins.admin.help import add_command_help
from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import errors as pyro_errors
from mediacenter.utilities.custom_filters import CustomFilters
from mediacenter.utilities.Qbittorrent import TorrentClient as QBT
# from mediacenter.utilities.helpers import split_list


@MediaCenterBot.on_message(CustomFilters.command("categories"))
async def categories(bot: MediaCenterBot, message: Message):
    await message.reply(
        "Categories\nSelect an action.",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("List", 'list_categories'), InlineKeyboardButton("Create", "create_categories")],
            ]
        )
    )


@MediaCenterBot.on_callback_query(CustomFilters.callback_query('list_categories', False))
async def list_categories(client: MediaCenterBot, callback: CallbackQuery):
    categories: dict = QBT().all_categories()

    categories_list = []
    for x in categories.keys():
        categories_list.append(categories.get(x).get('name'))

    categories_list = "\n".join(categories_list)

    full_text = (
        "Here are all of your categories\n"
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
        ['/categories', 'Start the category '],
    ]
)
