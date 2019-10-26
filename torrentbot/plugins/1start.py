from torrentbot import ALLOWED_USERS
from torrentbot.torrentbot import TorrentBot
from pyrogram import Message, Filters
from torrentbot.plugins.help import add_command_help
from torrentbot.helpers.custom_filters import CustomFilters


@TorrentBot.on_message(CustomFilters.command("start"))
async def start(bot, message: Message):
    await message.reply("Welcome to TorrentBot! I help you control your qBittorrent client.")


async def real_restart(bot: TorrentBot, message: Message):
    await bot.restart()
    await message.reply("Restarted!")


@TorrentBot.on_message(Filters.user(ALLOWED_USERS) & CustomFilters.command("restart"))
async def restart(bot, message: Message):
    await message.reply("Restarting TorrentBot.")
    import asyncio
    asyncio.get_event_loop().create_task(real_restart(bot, message))


# Command help section
add_command_help(
    'start', [['/start', 'This command just starts the torrentbot.. Nothing much..']]
)

add_command_help(
    'restart', [['/restart', 'Restarts the torrentbot. Lots happens in the background when restarting.']]
)