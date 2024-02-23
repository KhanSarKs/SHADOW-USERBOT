import asyncio
import importlib
from pyrogram import Client, idle
from userbot import client, app

async def start_bot():
    await app.start()
    try:
        await app.join_chat("Dollx_spambot")
        await app.join_chat("DollxSpam_BOT")
        await app.join_chat("dominator_bot_support")
        await app.join_chat("dominator_bot_official")
        await app.join_chat("TechnoBot_Support")
        await app.join_chat("TechnoBot_Updates")
    except:
        pass
        
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
    print("LOG: Founded Bot token Booting..")
    print("USERBOT SUCCESSFULLY STARTED ✅✅")
    await client.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
