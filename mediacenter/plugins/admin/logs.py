import time
import os
from mediacenter.utils.custom_filters import CustomFilters
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message


@MediaCenterBot.on_message(CustomFilters.command('log'))
async def send_log_file(bot: MediaCenterBot, message: Message):
    if os.path.exists('mediacenter.log'):
        await message.reply_chat_action('upload_document')
        await message.reply_document(
            document='logs/mediacenter.log',
            caption="time now is: {}".format(time.ctime(time.time()))
        )
    else:
        await message.reply("Oddly enough, there is no log file. Try again?")


# Command help section
add_command_help(
    'logs', [
        ['/log', 'Sends the system log file as is before the command is sent.'],
    ]
)
