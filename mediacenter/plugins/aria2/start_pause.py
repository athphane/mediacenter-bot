import asyncio

from pyrogram.types import CallbackQuery

from mediacenter import MediaCenterBot
from mediacenter.api_interfaces.aria2p import Aria2p
from mediacenter.utils import custom_filters
from .show import aria_show_download


@MediaCenterBot.on_callback_query(
    custom_filters.current_module('aria2') &
    (custom_filters.callback_query('pause') | custom_filters.callback_query('resume'))
)
async def aria_start_pause_single(_, callback: CallbackQuery):
    status = list()
    data = callback.data
    gid = callback.payload
    download = Aria2p().get_download(gid)

    if data.startswith('pause'):
        status = Aria2p().pause(download)
    elif data.startswith('resume'):
        status = Aria2p().resume(download)

    if status[0]:
        if data.startswith('pause'):
            await callback.answer("Paused")
        elif data.startswith('resume'):
            await callback.answer("Resumed")
    else:
        await callback.answer("An error has occurred.")

    await asyncio.sleep(3)
    await aria_show_download(None, callback)

