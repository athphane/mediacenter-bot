from mediacenter import ALLOWED_USERS, ADMIN
from mediacenter.database.users import User
from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message, Emoji, CallbackQuery

# CONSTANTS
NOT_ALLOWED_MESSAGE = (f'**{Emoji.FIRE} You are not allowed! {Emoji.FIRE}\n'
                       f'{Emoji.FIRE} This incident will be reported! {Emoji.FIRE}**')

GROUPS_NOT_ALLOWED_MESSAGE = (f'**{Emoji.FIRE} Groups are not allowed! {Emoji.FIRE}\n'
                              f'{Emoji.FIRE} This incident will be reported! {Emoji.FIRE}**')


@MediaCenterBot.on_message(group=-1)
async def stop_user_from_doing_anything(bot: MediaCenterBot, message: Message):
    """
    Checks if user is allowed to use MediaCenterBot
    """
    # Updates user details if they are supposed to be in the system
    if message.from_user.id in User().all_user_ids():
        User().update_user(message)

    if message.from_user.id not in User().all_user_ids():
        if message.chat and message.chat.type in {"group", "supergroup"}:
            await message.reply(GROUPS_NOT_ALLOWED_MESSAGE)
            message.stop_propagation()
        else:
            await message.reply(NOT_ALLOWED_MESSAGE)
            message.stop_propagation()
    else:
        message.continue_propagation()


@MediaCenterBot.on_callback_query(group=-1)
async def stop_user_from_doing_anything_callback(client, callback: CallbackQuery):
    """
    Checks if user is allowed to use MediaCenterBot via CallbackQuery
    """
    if callback.message.from_user.id not in User().all_user_ids():
        if callback.message.chat and callback.message.chat.type in {'group', 'supergroup'}:
            await callback.answer('Groups not allowed.')
            await callback.edit_message_text(GROUPS_NOT_ALLOWED_MESSAGE)
            callback.stop_propagation()

        await callback.edit_message_text(NOT_ALLOWED_MESSAGE)
        callback.stop_propagation()


# Adds the users to the database if they do not already exist
User().create_user_with_id(ADMIN)
for x in ALLOWED_USERS:
    User().create_user_with_id(x)
