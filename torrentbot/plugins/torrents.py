from torrentbot.torrentbot import TorrentBot
from pyrogram import Filters, Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Emoji
import pyrogram.errors as pyro_errors
from torrentbot.helpers.converters import human_bytes, human_unix_time, time_delta
from time import sleep, time
from torrentbot.helpers.custom_filters import CustomFilters
from torrentbot.plugins.help import add_command_help
from torrentbot.helpers.Qbittorrent import TorrentClient as QBT


def make_torrent_buttons(torrent_hash):
    buttons = [
        [
            InlineKeyboardButton("Resume", f"resume+{torrent_hash}"),
            InlineKeyboardButton("Pause", f"pause+{torrent_hash}")
        ],
        [
            InlineKeyboardButton("Delete", f"delete+{torrent_hash}"),
            InlineKeyboardButton("Update", f"update+{torrent_hash}"),
        ],
        [
            InlineKeyboardButton("Back", f"back"),
        ]
    ]

    return buttons


@TorrentBot.on_message(Filters.command("list"))
async def send_torrent_list(bot, message: Message):
    text = ""
    count = 1
    for x in QBT().torrents():
        text += f"{count}. {x['name']}\n\n"
        count += 1

    await message.reply(text)


@TorrentBot.on_message(Filters.command("torrents"))
async def torrents(bot, message: Message, **kwargs):
    buttons = []

    torrents = QBT().torrents()
    if len(torrents) == 0:
        await message.reply(f"**You have no torrents!** {Emoji.EXCLAMATION_MARK}")
        return

    for x in torrents:
        button = [
            InlineKeyboardButton(
                text=x['name'],
                callback_data=f"torrent+{x['hash']}"
            )
        ]
        buttons.append(button)

    if kwargs.get('back'):
        await message.edit_text("Here is all the torrent's available", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await message.reply("Here is all the torrent's available", reply_markup=InlineKeyboardMarkup(buttons))


@TorrentBot.on_message(Filters.command("add"))
async def add_torrent(bot, message: Message):
    try:
        torrent_link = message.command[1]
        added_torrent = QBT().add_torrent(torrent_link)

        if added_torrent == "Ok.":
            await message.reply(f"**Torrent Added Successfully! {Emoji.PARTY_POPPER}**")
        else:
            await message.reply(f"Either that was an incorrect torrent link or you just sent some gibberish "
                          f"{Emoji.FACE_VOMITING} "
                          f"Nothing I can do to fix that {Emoji.MAN_SHRUGGING_MEDIUM_LIGHT_SKIN_TONE}")

    except IndexError:
        await message.reply("Please send a the link to the torrent after the command")


@TorrentBot.on_callback_query(CustomFilters.callback_query('torrent'))
async def torrent(client, callback: CallbackQuery, **kwargs):
    if kwargs.get('torrent_hash'):
        torrent_hash = kwargs.get('torrent_hash')
    else:
        torrent_hash = callback.data[8:]

    if kwargs.get('update') and (False if kwargs.get('answer') else True):
        await callback.answer("Updating...")

    if kwargs.get('update'):
        sleep(3)

    torrent_details = QBT().single_torrent(torrent_hash)
    completed_on = human_unix_time(torrent_details['completion_date'])

    constructed_message = (
        f"**Torrent**:\n"
        f"__{QBT().find_torrent_name(torrent_hash)}__\n\n"

        f"**Status**:\n"
        f"__{torrent_details['state']}__\n\n"

        f"**Size**:\n"
        f"__{human_bytes(torrent_details['total_size'])}__\n\n"

        f"**Category**:\n"
        f"__{torrent_details['category'] if torrent_details['category'] else 'None'}__\n\n"

        f"**Time Elapsed**:\n"
        f"__{time_delta(torrent_details['time_elapsed'])}__\n\n"

        f"**Completed on**:\n"
        f"__{completed_on}__\n\n"
    )

    buttons = make_torrent_buttons(torrent_hash)

    try:
        await callback.edit_message_text(
            constructed_message,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except pyro_errors.MessageNotModified:
        await callback.answer("No change")
        message = await callback.message.reply("Torrent details have not changed")
        sleep(2)
        await message.delete()


# Command help section
add_command_help(
    'list', [['/list', 'Lists all the torrents in the client.']],
)

add_command_help(
    'torrents', [['/torrents', 'Sends torrent buttons to interact with each torrent.']],
)

