from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from mediacenter import ADMIN
from mediacenter.api_interfaces import Sonarr
from mediacenter import MediaCenterBot
from mediacenter.utils import custom_filters


def get_buttons():
    buttons = []
    for show in Sonarr().all_shows():
        buttons.append([InlineKeyboardButton(f"{show.title}", f"show+{show.id}")])

    return buttons


@MediaCenterBot.on_message(custom_filters.module_command('sonarr', 'list'))
async def sonarr_list(_, message: Message):
    await message.reply("Here are all the shows.", reply_markup=InlineKeyboardMarkup(get_buttons()))


async def test_function(client: MediaCenterBot):
    await client.send_message(ADMIN, "Testing 102")


# add_job(test_function)
