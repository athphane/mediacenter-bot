import sys
import time
import random
import math
import pymongo

# ==========================
# Script variables
# ==========================
test = True  # Sends dummy data for the name, label and size
MONGO_URL = 'localhost'
DB_USERNAME = None
DB_PASSWORD = None

# ==========================
# Static variables
# ===========================
names = ['ubuntu-16.04.1-desktop-amd64.iso', 'Storks (2016) [1080p] [YTS.AG]', 'Mom.S04E08.HDTV.x264-LOL[eztv].mkv',
         '20160915_madsonic-6.1.8700-setup-x86.zip', 'Peace Is The Mission']
labels = ['Movie', 'TV Show', 'Music', 'Program', 'Game', 'eBook']
sizes = ['500000', '20000', '777758998']


# ==========================
# Used functions
# ==========================
def database():
    """Created Database connection"""
    client = pymongo.MongoClient(
        MONGO_URL,
        username=DB_USERNAME,
        password=DB_PASSWORD
    )
    db = client['mediacenterbot']
    return db


def human_bytes(b: int):
    """Converting byte to human readable form"""
    if b == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(b, 1024)))
    p = math.pow(1024, i)
    s = round(b / p, 2)
    return "%s %s" % (s, size_name[i])


if __name__ == '__main__':
    # Start of script
    date_run = time.asctime(time.localtime())

    # Sys args or random
    if not test:
        torrent_name = sys.argv[1]
        torrent_category = sys.argv[2]
        torrent_size = sys.argv[3]
    else:
        torrent_name = random.choice(names)
        torrent_category = random.choice(labels)
        torrent_size = random.choice(sizes)

    # Database connection
    db = database()['completed_torrents']

    data = {
        "name": torrent_name,
        "category": torrent_category,
        "size": human_bytes(int(torrent_size)),
        "date_run": date_run,
        'notified': False
    }

    # Inset to Database
    db.insert_one(data)

    print("Record added to database")
