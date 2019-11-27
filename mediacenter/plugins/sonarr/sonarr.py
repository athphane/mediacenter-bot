from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message, Filters
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils.custom_filters import CustomFilters


@MediaCenterBot.on_message(CustomFilters.command("sonarr"))
async def sonarr(bot: MediaCenterBot, message: Message):
    await message.reply("Sonarr command. I do absolutely nothing.")
