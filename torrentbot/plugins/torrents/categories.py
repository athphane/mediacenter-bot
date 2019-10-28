from torrentbot.plugins.admin.help import add_command_help
from torrentbot.torrentbot import TorrentBot
from pyrogram import Message
from torrentbot.utilities.custom_filters import CustomFilters
from torrentbot.utilities.Qbittorrent import TorrentClient as QBT
from torrentbot.utilities.helpers import split_list


@TorrentBot.on_message(CustomFilters.command("categories"))
async def categories_menu(bot: TorrentBot, message: Message):
    categories: dict = QBT().all_categories()
    keys = categories.keys()
    categories_list = []
    for x in keys:
        categories_list.append(categories.get(x).get('name'))

    # split_list(categories_list, 3)

    await message.reply(categories_list)

# Command help section
add_command_help(
    'categories', [
        ['/categories', 'Start the category '],
    ]
)