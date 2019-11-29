from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.api_interfaces.Sonarr import SonarrAPI
from pyrogram import Message
from mediacenter.utils.custom_filters import CustomFilters


@MediaCenterBot.on_message(CustomFilters.command("sonarr"))
async def sonarr(bot: MediaCenterBot, message: Message):
    # Sending the first item in the list for now. TG text limit
    await message.reply(SonarrAPI().get_series()[0])
