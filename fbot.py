import telebot
import random
import time
import os
from flask import Flask
import threading
import re

# 1. Setup
API_TOKEN = '8506856522:AAE-f6Fn9cNMVxIGVsLUMm8LUR-GTfvaYGg'
MAXXU_ID = 6363297042 
bot = telebot.TeleBot(API_TOKEN)

# 2. Flask
server = Flask(__name__)
@server.route("/")
def home(): return "Maxxu Ultimate Bot is Live!"

def run():
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

# 3. Data Lists
nrml_gali = ["Abe oye namune!", "Dimag bech khaya hai?", "Nalayak kahin ke!", "Oye bewakoof!", "Shakal dekhi hai apni?"]
shayari = [
    "Dosti ka rishta sabse pyara hai, tu mera yaar sabse nyara hai. ❤️",
    "Hum dosti mein jaan de dete hain, dushmani mein pehchan mita dete hain. 🔥",
    "Zindagi mein doston ka saath zaruri hai, warna har khushi adhuri hai. ✨"
]

# 4. Anti-Link & Welcome Handler
@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for user in message.new_chat_members:
        # Welcome Sticker (Ek pyara sa welcome sticker)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEL_mxl_...") 
        bot.reply_to(message, f"Swagat hai {user.first_name} bhai! Maxxu ke ilake mein rules follow karna. 🔥")

# 5. Full Message Handler
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    text = message.text.lower()
    sender_id = message.from_user.id
    chat_id = message.chat.id

    # --- 1. ANTI-LINK SYSTEM ---
    if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
        if sender_id != MAXXU_ID: # Maxxu links bhej sakta hai
            bot.delete_message(chat_id, message.message_id)
            bot.send_message(chat_id, f"⚠️ Oye {message.from_user.first_name}, group mein link bhejna mana hai!")
            return

    # --- 2. ADMIN ONLY COMMANDS (Maxxu Only) ---
    if sender_id == MAXXU_ID:
        if "ise suna kuch" in text and message.reply_to_message:
            target = message.reply_to_message.from_user
            m = bot.send_message(chat_id, "Ji bhai, abhi iski bajata hoon! 😈")
            spam_msgs = []
            for i in range(20):
                sent = bot.send_message(chat_id, f"[{target.first_name}](tg://user?id={target.id}) {random.choice(nrml_gali)}", parse_mode="Markdown")
                spam_msgs.append(sent.message_id)
                time.sleep(0.4)
            
            # --- 3. AUTO-DELETE (60 seconds baad clean-up) ---
            time.sleep(60)
            for msg_id in spam_msgs:
                try: bot.delete_message(chat_id, msg_id)
                except: pass
            bot.delete_message(chat_id, m.message_id)
            return

        elif "bas kar" in text:
            bot.reply_to(message, "Thik hai bhai, shant hoon. Agli baar bata dena! 😉")
            return

    # --- 4. ENTERTAINMENT (Sabke liye) ---
    if "shayari suna" in text:
        bot.reply_to(message, random.choice(shayari))
    elif "hi" in text or "hello" in text:
        bot.reply_to(message, f"Aur {message.from_user.first_name} bhai, kya haal?")
    elif "kaha hai" in text:
        bot.reply_to(message, "Yahin hoon ⚡M A X X U💀 bhai! Bol kya kaam hai?")
    else:
        # Har message par response
        bot.reply_to(message, "Sorry, I didn't understand. Could you please say that again?")

# Start
if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.infinity_polling()
