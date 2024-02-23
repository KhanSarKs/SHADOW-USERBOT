from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION

spam_chats = []
SUDO_USER = ("1253258650")
SUDO_USERS.append(OWNER_ID)

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="userbot/plugins"),
    in_memory=True,
)

client = Client(
    name="rj",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=STRING_SESSION,
    try:
        await app.join_chat("Dollx_spambot")
        await app.join_chat("DollxSpam_BOT")
        await app.join_chat("dominator_bot_support")
        await app.join_chat("dominator_bot_official")
        await app.join_chat("TechnoBot_Support")
        await app.join_chat("TechnoBot_Updates")
    except:
        pass
    if STRING_SESSION:
        LOGGER.info("Starting Bot ...")
        await ass.start()
        LOGGER.info("Bot Started.")
        try:
            print("Bot Started")
        except:
            pass
        try:
            await app.join_chat("Dollx_spambot")
            await app.join_chat("DollxSpam_BOT")
            await app.join_chat("dominator_bot_support")
            await app.join_chat("dominator_bot_official")
            await app.join_chat("TechnoBot_Support")
            await app.join_chat("TechnoBot_Updates")
        except:
            pass
    plugins=dict(root="userbot/plugins")
)

