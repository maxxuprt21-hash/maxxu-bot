import os
import asyncio
import random
import datetime
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ===== YOUR API DETAILS (ENVIRONMENT SE UTAYEGA) =====
API_ID = int(os.environ.get("API_ID", "4962914"))
API_HASH = os.environ.get("API_HASH", "0e862963853723ae6738cfd98f6ad8d1")
STRING_SESSION = os.environ.get("STRING_SESSION") # Ye Render se uthayega
# ====================================================

# Yahan StringSession use ho raha hai jo Render ke liye best hai
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

STOP = False
TAGGED = 0
DELAY_MIN = 4
DELAY_MAX = 9

CUTE_MESSAGES = [
    "you bring good vibes 💖", "hope you’re smiling today 😊",
    "you matter a lot ✨", "sending positive energy ⚡",
    "you’re honestly amazing 🌟", "keep shining like this 🔥",
    "just spreading some love ❤️", "you make this place better 🌈",
    "good vibes only for you 🌸"
]

def tag_user(user):
    return f"@{user.username}" if user.username else f"[{user.first_name}](tg://user?id={user.id})"

@client.on(events.NewMessage(pattern=r"\.help", outgoing=True))
async def help_cmd(event):
    await event.delete()
    await event.respond("🛡️ **Userbot Commands**\n\n`.start` – Start tagging\n`.stop` – Stop tagging\n`.stats` – Show stats\n`.alive` – Check bot status")

@client.on(events.NewMessage(pattern=r"\.alive", outgoing=True))
async def alive_cmd(event):
    await event.edit("✅ **Maxxu Bot is Online!**")

@client.on(events.NewMessage(pattern=r"\.start", outgoing=True))
async def start_tag(event):
    global STOP, TAGGED
    STOP = False
    TAGGED = 0
    await event.delete()
    async for user in client.iter_participants(event.chat_id):
        if STOP: break
        if user.bot or user.deleted: continue
        mention = tag_user(user)
        message = f"{mention} {random.choice(CUTE_MESSAGES)}"
        await client.send_message(event.chat_id, message)
        TAGGED += 1
        await asyncio.sleep(random.randint(DELAY_MIN, DELAY_MAX))

@client.on(events.NewMessage(pattern=r"\.stop", outgoing=True))
async def stop_tag(event):
    global STOP
    STOP = True
    await event.edit("🛑 **Tagging Stopped!**")

@client.on(events.NewMessage(pattern=r"\.stats", outgoing=True))
async def stats_cmd(event):
    await event.edit(f"📊 **Tagged users so far:** {TAGGED}")

print("🚀 Userbot running...")
client.start()
client.run_until_disconnected()
