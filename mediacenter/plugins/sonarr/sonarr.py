from pyrogram.types import Message

from mediacenter import ADMIN
from mediacenter.api_interfaces.sonarr.Sonarr import SonarrAPI
from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.command("sonarr"))
async def sonarr(_, message: Message):
    # Sending the first item in the list for now. TG text limit
    await message.reply(SonarrAPI().get_series()[0])


async def test_function(client: MediaCenterBot):
    await client.send_message(ADMIN, "Testing 102")


# add_job(test_function)
