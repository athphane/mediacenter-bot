import math
from datetime import datetime as unix_to_timestamp
import datetime


def human_bytes(b, dp=2):
    """ Converts bytes to human readable string"""
    if b == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(b, 1024)))
    p = math.pow(1024, i)
    s = round(b / p, dp)
    return "%s %s" % (s, size_name[i])


def human_unix_time(seconds):
    return unix_to_timestamp.utcfromtimestamp(int(seconds)).strftime('%Y-%m-%d %H:%M:%S')


def time_delta(seconds):
    return str(datetime.timedelta(seconds=seconds))
