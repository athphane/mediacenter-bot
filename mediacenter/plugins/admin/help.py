from mediacenter.mediacenterbot import MediaCenterBot
from pyrogram.types import Message
from mediacenter.utils import custom_filters
from mediacenter import BOT_USERNAME
from mediacenter.utils.helpers import split_list
from prettytable import PrettyTable
CMD_HELP = {}


@MediaCenterBot.on_message(custom_filters.command("help"))
async def module_help(bot: MediaCenterBot, message: Message):
    cmd = message.command

    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        all_commands = ""
        all_commands += "Please specify which module you want help for!! \nUsage: `.help [module_name]`\n\n"

        ac = PrettyTable()
        ac.header = False
        ac._title = "Modules"
        ac.align = 'l'

        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])

        await message.reply(f"```{str(ac)}```")

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = ""
            this_command += f"--**Help for {str(help_arg)} module**--\n".upper()

            for x in commands:
                this_command += f"**{str(x)}**:\n```{str(commands[x])}```\n\n"

            await message.reply(this_command, parse_mode='markdown')
        else:
            await message.reply('`Please specify a valid module name.`', parse_mode='markdown')


def add_command_help(module_name: str, commands: list):
    """
    Adds a modules help information.
    :param module_name: name of the module
    :param commands: list of lists, with command and description each.
    """

    # Key will be group name
    # values will be dict of dicts of key command and value description

    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
