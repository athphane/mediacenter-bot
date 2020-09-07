from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from mediacenter.database.users import UserDB
from mediacenter import MediaCenterBot
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters
from mediacenter.utils.helpers import split_list

modules = {
    'home': 'Home',
    'qbt': 'qBitTorrent',
    'sonarr': 'Sonarr',
    'aria2': 'Aria2'
}

buttons = []
for group in split_list(list(modules), 2):
    temp = []
    for btn in group:
        temp.append(InlineKeyboardButton(f"{modules[btn]}", f"switch+{btn}"))

    buttons.append(temp)

buttons = InlineKeyboardMarkup(buttons)


@MediaCenterBot.on_message(custom_filters.command(["modules", "module"]))
async def modules_switcher(_, message: Message):
    await message.reply("Here are the available modules. Select one to change to it.", reply_markup=buttons)
    print("This is the modules handler.")


@MediaCenterBot.on_callback_query(custom_filters.callback_query('switch'))
async def switch_module(_, callback: CallbackQuery):
    module = callback.payload
    UserDB().set_module(callback.from_user, module)
    await callback.answer()
    await callback.message.edit_text(f"Module Set to **{modules[module]}**. Select another to change to it.", reply_markup=buttons)

# Command help section
add_command_help(
    'switch', [
        ['/module(s)', 'Shows module selector'],
    ]
)
