from torrentbot.plugins.admin.help import add_command_help
from torrentbot.torrentbot import TorrentBot
from pyrogram import Message
from torrentbot.helpers.custom_filters import CustomFilters


@TorrentBot.on_message(CustomFilters.command("categories"))
async def categories(bot: TorrentBot, message: Message):
    print(True)


# Command help section
add_command_help(
    'categories', [
        ['/categories', 'Start the category '],
    ]
)