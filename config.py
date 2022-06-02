import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
BOT_ARAB_NAME = getenv("BOT_ARAB_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "EL_RAYEQ")
ALIVE_NAME = getenv("ALIVE_NAME", "Dev")
BOT_USERNAME = getenv("BOT_USERNAME", "EL_RAYEQ_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "EL_RAYEQ_B0T")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Source_Arbawy1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SOURCE_ARBAWY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5002164804").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ئ ؤ ء 😹 😂 💋 🌚 🙈 / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/eeb7d3c56bbb24506639d.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/alielsayed76/a")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/eeb7d3c56bbb24506639d.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/eeb7d3c56bbb24506639d.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/eeb7d3c56bbb24506639d.jpg")
