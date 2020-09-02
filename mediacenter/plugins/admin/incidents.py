from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram.types import Message
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils import custom_filters
from mediacenter.database.incidents import Incident
from mediacenter.utils.helpers import GetUserMentionable


def format_message(incident):
    INCIDENT_MESSAGE = (
        "Here's the latest incident that happened\n\n"
        f"{GetUserMentionable(user_dict=incident['user'])} tried to get into the mainframe. It's fine. We caught him "
        f"in his tracks. He thought sending \"{incident['crime']}\" would do anything for him."
    )

    return INCIDENT_MESSAGE


@MediaCenterBot.on_message(custom_filters.command("lastIncident", case_sensitive=True))
async def start(bot: MediaCenterBot, message: Message):
    incident = [x for x in Incident().find_latest_incident()]
    await message.reply(format_message(incident[0]))


# Command help section
add_command_help(
    'incidents', [
        ['/lastIncident', 'Shows the latest incident that occurred on {BOT_NAME}...'],
    ]
)
