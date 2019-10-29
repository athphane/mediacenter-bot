from mediacenter.plugins.admin.help import add_command_help
from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message
from mediacenter.utilities.custom_filters import CustomFilters
from mediacenter.utilities.Qbittorrent import TorrentClient as QBT
from mediacenter.utilities.helpers import split_list


@MediaCenterBot.on_message(CustomFilters.command("categories"))
async def categories_menu(bot: MediaCenterBot, message: Message):
    categories: dict = QBT().all_categories()
    keys = categories.keys()
    categories_list = []
    for x in keys:
        categories_list.append(categories.get(x).get('name'))

    # split_list(categories_list, 3)

    await message.reply(str(categories_list))

# Command help section
add_command_help(
    'categories', [
        ['/categories', 'Start the category '],
    ]
)
