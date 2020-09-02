from pyrogram.types import Message

from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.command("start"))
async def start(_, message: Message):
    await message.reply(f"Welcome to {MediaCenterBot.__name__}! I help you control your media center.")


async def real_restart(bot, message: Message):
    await bot.restart()
    await message.reply("Restarted!")


@MediaCenterBot.on_message(custom_filters.allowed_users & custom_filters.command("restart"))
async def restart(bot, message: Message):
    await message.reply(f"Restarting {MediaCenterBot.__name__}.")
    import asyncio
    asyncio.get_event_loop().create_task(real_restart(bot, message))


# Command help section
add_command_help(
    'start', [
        ['/start', 'This command just starts the {BOT_NAME}.. Nothing much..'],
        ['/restart', 'Restarts the {BOT_NAME}. Lots happens in the background when restarting.']
    ]
)
