from configparser import ConfigParser
from logging.handlers import TimedRotatingFileHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from mediacenter.mediacenterbot import MediaCenterBot
import ast
import logging
import sys

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        TimedRotatingFileHandler('logs/mediacenter.log', when="midnight", encoding=None,
                                 delay=False, backupCount=10),
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)

# Manually setting APScheduler logger level because it's not set by default.
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

# Read from config file
name = MediaCenterBot().__class__.__name__.lower()
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

# The bot username is required cause CustomFilters.command needs it for the regex.
try:
    BOT_USERNAME = config.get(name, 'bot_username')
except:
    print("BOT USERNAME IS REQUIRED. ADD TO CONFIG FILE")
    sys.exit()

# Get from config file.
ADMIN = config.get(name, 'admin')
ALLOWED_USERS: list = ast.literal_eval(config.get(name, 'users'))

MONGO_URL = config.get('mongo', 'url')
DB_NAME = config.get('mongo', 'db_name')
DB_USERNAME = config.get('mongo', 'db_username')
DB_PASSWORD = config.get('mongo', 'db_password')

QBT_URL = config.get('qbittorrent', 'qbt_url')
QBT_USER = config.get('qbittorrent', 'qbt_user')
QBT_PASS = config.get('qbittorrent', 'qbt_password')

SONARR_API_URL = config.get('sonarr', 'sonarr_api_url')
SONARR_API_KEY = config.get('sonarr', 'sonarr_api_key')

# Extra details
__version__ = '0.2.0'
__author__ = 'athphane'

# Scheduler
scheduler = AsyncIOScheduler()

# Global Variables
client = None
