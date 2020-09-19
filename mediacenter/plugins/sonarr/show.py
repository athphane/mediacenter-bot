from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces import Sonarr
from mediacenter.api_interfaces.Sonarr import Show
from mediacenter.api_interfaces.Sonarr.models.show import SonarrImage
from mediacenter.utils import custom_filters


def create_message(show: Show):
    txt = (
        f"**{show.title}**\n"
        f"Released: {show.year}\n"
        f"Seasons: {show.seasonCount}\n"
    )

    return txt


def create_buttons(show):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Seasons", f'seasons+{show.id}'), InlineKeyboardButton("Resume", f'resume+{show}')],
        [
            InlineKeyboardButton("Banner", f'photo_change+{show.id}=banner'),
            InlineKeyboardButton("Poster", f'photo_change+{show.id}=poster'),
            InlineKeyboardButton("Fan Art", f'photo_change+{show.id}=fan_art')
        ],
    ])


@MediaCenterBot.on_callback_query(custom_filters.module_callback('sonarr', 'show'))
async def sonarr_view_show(_, callback: CallbackQuery):
    show_id = callback.payload
    await callback.answer("Fetching...")
    show = Sonarr().get_show(show_id)
    await MediaCenterBot.send_photo(
        callback.message.chat.id,
        show.banner.full_url,
        caption=create_message(show),
        reply_markup=create_buttons(show)
    )


@MediaCenterBot.on_callback_query(custom_filters.module_callback('sonarr', 'photo_change'))
async def sonarr_update_photo(_, callback: CallbackQuery):
    show_id, image_type = callback.payload.split('=')
    await callback.answer("Changing media...")
    show = Sonarr().get_show(show_id)
    image: SonarrImage = getattr(show, image_type)
    message = callback.message
    await MediaCenterBot.edit_message_photo(message, image.full_url)
