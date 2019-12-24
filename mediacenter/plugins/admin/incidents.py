from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message, User
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils.custom_filters import CustomFilters
from mediacenter.database.incidents import Incident
from types import SimpleNamespace


def GetUserMentionable(user: User = None, user_dict: dict = None):
    """ Get mentionable text of a user."""
    if user is None and user_dict is not None:
        user = SimpleNamespace(**user_dict)

    if user.username:
        username = f"@{user.username}"
    else:
        if user.last_name:
            name_string = f"{user.first_name} {user.last_name}"
        else:
            name_string = f"{user.first_name}"

        username = f"<a href='tg://user?id={user.id}'>{name_string}</a>"

    return username


def format_message(incident):
    INCIDENT_MESSAGE = (
        "Here's the latest incident that happened\n\n"
        f"{GetUserMentionable(user_dict=incident['user'])} tried to get into the mainframe. It's fine. We caught him "
        f"in his tracks. He thought sending \"{incident['crime']}\" would do anything for him."
    )

    return INCIDENT_MESSAGE


@MediaCenterBot.on_message(CustomFilters.command("lastIncident", case_sensitive=True))
async def start(bot: MediaCenterBot, message: Message):
    incident = [x for x in Incident().find_latest_incident()]
    await message.reply(format_message(incident[0]))


# Command help section
add_command_help(
    'incidents', [
        ['/lastIncident', 'Shows the latest incident that occurred on {BOT_NAME}..'],
    ]
)
