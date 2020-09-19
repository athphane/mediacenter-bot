from pyrogram.types import Message

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces import Sonarr
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.module_command('sonarr', 'stats'))
async def system_stats(_, message: Message):
    stats = Sonarr().status
    await message.reply(stats.version)
