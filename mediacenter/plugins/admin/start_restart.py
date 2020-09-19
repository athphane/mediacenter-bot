import asyncio

from pyrogram.types import Message

from mediacenter import MediaCenterBot
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.command("start"))
async def start(_, message: Message):
    await message.reply(f"Welcome to {MediaCenterBot}! I help you control your media center.")


async def real_restart(bot, message: Message):
    await bot.restart()
    await message.reply("Restarted!")


@MediaCenterBot.on_message(custom_filters.allowed_users & custom_filters.command("restart"))
async def restart(bot: MediaCenterBot, message: Message):
    await message.reply(f"Restarting {MediaCenterBot}.")

    if 'p' in message.text and 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True, pip=True))
    elif 'p' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(pip=True))
    elif 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True))
    else:
        asyncio.get_event_loop().create_task(bot.restart())


# Command help section
add_command_help(
    'start', [
        ['/start', 'This command just starts the {BOT_NAME}.. Nothing much..'],
        ['/restart', 'Restarts the {BOT_NAME}. Lots happens in the background when restarting.']
    ]
)
