from mediacenter import ALLOWED_USERS
from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message, Filters
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils.custom_filters import CustomFilters


@MediaCenterBot.on_message(CustomFilters.command("start"))
async def start(bot: MediaCenterBot, message: Message):
    await message.reply(f"Welcome to {MediaCenterBot.__name__}! I help you control your media center.")


async def real_restart(bot: MediaCenterBot, message: Message):
    await bot.restart()
    await message.reply("Restarted!")


@MediaCenterBot.on_message(Filters.user(ALLOWED_USERS) & CustomFilters.command("restart"))
async def restart(bot: MediaCenterBot, message: Message):
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
