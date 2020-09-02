from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram.types import Message
from mediacenter.utils import custom_filters
from mediacenter import BOT_USERNAME

CMD_HELP = {}


@MediaCenterBot.on_message(custom_filters.command("help"))
async def module_help(bot: MediaCenterBot, message: Message):
    cmd = message.command

    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) is 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) is 1:
        all_commands = "Please specify which module you want help for!! \nUsage: /help \"module_name\"\n\n"
        for x in CMD_HELP:
            all_commands += f"`{str(x)}`\n"

        await message.reply(all_commands)
        return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = ""
            this_command += f"Help for {str(help_arg)} module\n\n"

            for x in commands:
                this_command += f"{str(commands[x]['command'])}: {str(commands[x]['description'])}\n\n"

            await message.reply(this_command)
        else:
            await message.reply('`Please specify a valid module name.`')


def add_command_help(module_name: str, commands: list):
    """
    Adds a modules help information.
    :param module_name: name of the module
    :param commands: list of lists, with command and description each.
    """
    temp_dict = {}
    count = 1
    for x in commands:
        temp_dict[count] = {'command': x[0], 'description': x[1].format(BOT_NAME=MediaCenterBot.__name__)}
        count += 1

    CMD_HELP[module_name] = temp_dict
