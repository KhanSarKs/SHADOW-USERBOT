import os
import shutil
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from userbot import SUDO_USER

@Client.on_message(filters.command(["restart", "reload", "rs", "rl"], ".") & (filters.me | filters.user(SUDO_USER)))
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**Restarting...**")
    await message.delete()
    await reply.edit_text("Successfully Restarted sUsB...\n\n💞 Wait 1-2 minutes\nLoad plugins...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m userbot")
