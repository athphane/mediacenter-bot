from torrentbot.torrentbot import TorrentBot
from pyrogram import Filters, Message
from torrentbot.plugins.help import add_command_help


async def restart(bot: TorrentBot, message: Message):
    await bot.restart()
    await message.reply("Restarted!")


@TorrentBot.on_message(Filters.command("start"))
async def repo(bot, message: Message):
    await message.reply("Welcome to TorrentBot! I help you control your qBittorrent client.")


@TorrentBot.on_message(Filters.command("restart"))
async def real_restart(bot, message: Message):
    await message.reply("Restarting TorrentBot.")
    from threading import Thread
    Thread(target=restart, args=(bot, message)).start()


# Command help section
add_command_help(
    'start', [['/start', 'This command just starts the torrentbot.. Nothing much..']]
)

add_command_help(
    'restart', [['/restart', 'Restarts the torrentbot. Lots happens in the background when restarting.']]
)