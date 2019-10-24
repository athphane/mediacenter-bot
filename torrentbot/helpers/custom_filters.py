import os
import re
from pyrogram import Filters, Message, CallbackQuery


class CustomFilters:
    @staticmethod
    def command(commands: list or str):
        commands = commands if type(commands) is list else [commands]
        prep_for_regex = '|'.join(commands)

        regex = "^(/)+({regex})(@{bot_name})?".format(regex=prep_for_regex, bot_name=os.getenv("BOT_USERNAME"))

        def f(_, m):
            m.matches = [i for i in _.p.finditer(m.text or m.caption or "")]
            return bool(m.matches)

        return Filters.create(f, "CustomCommandFilter", p=re.compile(regex, 0))

    @staticmethod
    def callback_query(arg: str):
        def f(flt, query: CallbackQuery):
            if flt.data in query.data:
                return True
            else:
                return False

        return Filters.create(f, "CustomCallbackQueryFilter", data=arg)
