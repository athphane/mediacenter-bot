from torrentbot import ALLOWED_USERS
from torrentbot.torrentbot import TorrentBot
from pyrogram import Filters, Message, Emoji, CallbackQuery

# CONSTANTS
NOT_ALLOWED_MESSAGE = (f'**{Emoji.FIRE} You are not allowed! {Emoji.FIRE}\n'
                       f'{Emoji.FIRE} This incident will be reported! {Emoji.FIRE}**')


@TorrentBot.on_message(~Filters.user(ALLOWED_USERS), group=-1)
async def stop_user_from_doing_anything(bot, message: Message):
    """
    Checks if user is allowed to use TorrentBot
    """
    await message.reply(NOT_ALLOWED_MESSAGE)
    message.stop_propagation()


@TorrentBot.on_callback_query(~Filters.user(ALLOWED_USERS), group=-1)
async def stop_user_from_doing_anything_callback(client, callback: CallbackQuery):
    """
    Checks if user is allowed to use TorrentBot via CallbackQuery
    """
    await callback.answer('GTFO')
    await callback.edit_message_text(NOT_ALLOWED_MESSAGE)
    callback.stop_propagation()
