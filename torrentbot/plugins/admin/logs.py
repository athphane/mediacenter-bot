import time
import os
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.admin.help import add_command_help
from torrentbot.torrentbot import TorrentBot
from pyrogram import Message


@TorrentBot.on_message(CustomFilters.command('log'))
async def send_log_file(bot: TorrentBot, message: Message):
    if os.path.exists('torrentbot.log'):
        await message.reply_chat_action('upload_document')
        await message.reply_document(
            document='torrentbot.log',
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
