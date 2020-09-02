import os
import time

from pyrogram import emoji
from pyrogram.types import Message

from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters


@MediaCenterBot.on_message(custom_filters.command(['log', 'logs', 'logger']))
async def send_log_file(_, message: Message):
    if os.path.exists('logs/mediacenter.log'):
        await message.reply_chat_action('upload_document')
        await message.reply_document(
            document='logs/mediacenter.log',
            caption=f"{emoji.CLIPBOARD}: `{time.ctime(time.time())}`"
        )
    else:
        await message.reply("Oddly enough, there is no log file. Try again?")


# Command help section
add_command_help(
    'logs', [
        ['/log', 'Sends the system log file as is before the command is sent.'],
    ]
)
