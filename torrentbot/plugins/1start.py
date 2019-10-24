from torrentbot.torrentbot import TorrentBot
from pyrogram import Filters, Message
from torrentbot.plugins.help import add_command_help


@TorrentBot.on_message(Filters.command("start"))
async def repo(bot, message: Message):
    await message.reply("Welcome to TorrentBot! I help you control your qBittorrent client.")


async def restart(bot: TorrentBot, message: Message):
    await bot.restart()
    await message.reply("Restarted!")


@TorrentBot.on_message(Filters.command("restart"))
async def real_restart(bot, message: Message):
    await message.reply("Restarting TorrentBot.")
    import asyncio
    asyncio.get_event_loop().create_task(restart(bot, message))


# Command help section
add_command_help(
    'start', [['/start', 'This command just starts the torrentbot.. Nothing much..']]
)

add_command_help(
    'restart', [['/restart', 'Restarts the torrentbot. Lots happens in the background when restarting.']]
)