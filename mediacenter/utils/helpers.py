from types import SimpleNamespace

from pyrogram import User


def split_list(input_list, n):
    """
    Takes a list and splits it into smaller lists of n elements each.
    :param input_list:
    :param n:
    :return:
    """
    n = max(1, n)
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]


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
