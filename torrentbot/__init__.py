from configparser import ConfigParser
from torrentbot.torrentbot import TorrentBot
import ast
import logging
import sys

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)

# Read from config file
name = TorrentBot().__class__.__name__.lower()
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

# Get from config file.
ALLOWED_USERS = ast.literal_eval(config.get(name, 'users'))

try:
    BOT_USERNAME = config.get(name, 'bot_username')
except:
    print("BOT USERNAME IS REQUIRED. ADD TO CONFIG FILE")
    sys.exit()

QBT_URL = config.get('qbittorrent', 'qbt_url')
QBT_USER = config.get('qbittorrent', 'qbt_user')
QBT_PASS = config.get('qbittorrent', 'qbt_password')

# Extra details
__version__ = '0.2.0'
__author__ = 'athphane'

# Global Variables
