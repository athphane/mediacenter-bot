from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram import Message
from mediacenter.plugins.admin.help import add_command_help
from mediacenter.utils.custom_filters import CustomFilters
from mediacenter.database.incidents import Incident


@MediaCenterBot.on_message(CustomFilters.command("lastIncident", case_sensitive=True))
async def start(bot: MediaCenterBot, message: Message):
    last_incident = Incident().find_latest_incident()
    print(last_incident)
    # TODO: FIX THIS SHIT


# Command help section
add_command_help(
    'incidents', [
        ['/lastIncident', 'Shows the latest incident that occurred on {BOT_NAME}..'],
    ]
)