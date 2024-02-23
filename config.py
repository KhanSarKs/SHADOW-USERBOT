from os import getenv

API_ID = int(getenv("API_ID", "13335263"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "1253258650"))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1253258650").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/57d6eaccbc2ab0d477e8c.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/KhanSarKs/SHADOW-USERBOT")
BRANCH = getenv("BRANCH", "main")
