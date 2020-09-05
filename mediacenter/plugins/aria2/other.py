from prettytable import PrettyTable
from pyrogram.types import Message

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces.aria2p import Aria2p
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("purge"))
async def aria_purge(_, message: Message):
    output = Aria2p().auto_purge()
    if output == 'OK':
        await message.reply("Purged everything from Aria2c")
    else:
        await message.reply("Purge failed.")


@MediaCenterBot.on_message(custom_filters.current_module('aria2') & custom_filters.command("stats"))
async def aria_stats(_, message: Message):
    output = Aria2p().stats()

    ac = PrettyTable()
    ac.field_names = ['Aria2c', 'Stats']
    ac.header = True
    ac.align = 'l'

    ac.add_row(["Active", output.num_active])
    ac.add_row(["Waiting", output.num_waiting])
    ac.add_row(["Stopped", output.num_stopped])
    ac.add_row(["DL", output.download_speed_string()])
    ac.add_row(["UL", output.upload_speed_string()])

    await message.reply(f"```{str(ac)}```")
