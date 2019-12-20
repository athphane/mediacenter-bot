from mediacenter import ALLOWED_USERS
from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message, Filters
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils.custom_filters import CustomFilters


@MediaCenterBot.on_message(CustomFilters.command("lastIncident", case_sensitive=True))
async def start(bot: MediaCenterBot, message: Message):
    await message.reply("Welcome to TorrentBot! I help you control your media center.")


# Command help section
add_command_help(
    'incidents', [
        ['/lastIncident', 'Shows the latest incident that occurred on {BOT_NAME}..'],
    ]
)