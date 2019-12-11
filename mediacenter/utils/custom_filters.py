from pyrogram import Filters, CallbackQuery
import re
import shlex
from mediacenter import BOT_USERNAME


class CustomFilters(Filters):
    @staticmethod
    def command(
            commands: str or list,
            prefixes: str or list = "/",
            case_sensitive: bool = False
    ):
        """
            This is a drop in replacement for the default Filters.command that is included
            in Pyrogram. The Pyrogram one does not support /command@botname type commands,
            so this custom filter enables that throughout all groups and private chats.

            This filter works exactly the same as the original command filter even with support for multiple command
            prefixes and case sensitivity.

            Command arguments are given to user as message.command
        """

        def func(flt, message):
            text: str = message.text or message.caption
            message.command = None

            if not text:
                return False

            regex = "^({prefix})+(\\b{regex}\\b)(@{bot_name})?(.*)".format(
                prefix='|'.join(re.escape(x) for x in flt.prefixes),
                regex='|'.join(flt.commands),
                bot_name=BOT_USERNAME
            )

            matches = re.search(re.compile(regex), text)
            if matches:
                message.command = [matches.group(2)]
                for arg in shlex.split(matches.group(4).strip()):
                    message.command.append(arg)
                return True
            else:
                return False

        commands = commands if type(commands) is list else [commands]
        commands = {c if case_sensitive else c.lower() for c in commands}

        prefixes = [] if prefixes is None else prefixes
        prefixes = prefixes if type(prefixes) is list else [prefixes]
        prefixes = set(prefixes) if prefixes else {""}

        return Filters.create(
            func,
            "CustomCommandFilter",
            commands=commands,
            prefixes=prefixes,
            case_sensitive=case_sensitive
        )

    @staticmethod
    def callback_query(arg: str, payload=True):
        """
        Accepts arg at all times.
        if payload is True, extract payload from callback and assign to callback.payload
        if payload is False, only check if callback exactly matches argument
        """
        def func(flt, query: CallbackQuery):
            if payload:
                thing = "{}\+"
                if re.search(re.compile(thing.format(flt.data)), query.data):
                    search = re.search(re.compile(r"\+{1}(.*)"), query.data)
                    if search:
                        query.payload = search.group(1)
                    else:
                        query.payload = None

                    return True

                return False
            else:
                if flt.data == query.data:
                    return True

                return False

        return Filters.create(func, "CustomCallbackQueryFilter", data=arg)
