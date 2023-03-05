from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9a85d0a873e2dd80d278d.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2ad7c9d508b26c3cc7c09.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://Silent_robo_11")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Mine_Bots")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5278339583").split()))
