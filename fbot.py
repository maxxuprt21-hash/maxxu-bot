import telebot
import random
import time
import os
from flask import Flask
import threading
import re

# 1. Setup - Darling Maxxu Special
API_TOKEN = '8506856522:AAE-f6Fn9cNMVxIGVsLUMm8LUR-GTfvaYGg'
MAXXU_ID = 6363297042
MAXXU_USERNAME = "@maxxu_ig"
bot = telebot.TeleBot(API_TOKEN)

# 2. Flask Server
server = Flask(__name__)
@server.route("/")
def home(): return f"Maxxu ({MAXXU_USERNAME}) Bot is Live!"

def run():
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

# 3. Data Lists
nrml_gali = ["Abe oye namune!", "Dimag bech khaya hai?", "Nalayak kahin ke!", "Oye bewakoof!", "Shakal dekhi hai apni?"]

# Shayari List (Short version for test, add more later)
shayari_list = ["Teri saanson ki garmahat...", "Aankhon se jo baat hui...", "Tera naam lete hi..."] 

# 4. Message Handler
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    try:
        text = message.text.lower()
        sender_id = message.from_user.id
        chat_id = message.chat.id
        user_name = message.from_user.first_name
        mention = f"[{user_name}](tg://user?id={sender_id})"

        # --- 1. ROMANTIC & MOOD ---
        romantic_triggers = ["mood", "jaan", "baby", "love you", "love u", "shona", "maxxu"]
        if any(word in text for word in romantic_triggers):
            chosen = random.choice(shayari_list)
            response = f"Oye {mention}, suniye...\n\n*{chosen}*\n\n✨ 'Next' likho agli ke liye!\n❤️ **Darling Maxxu**"
            bot.send_message(chat_id, response, parse_mode="Markdown")
            return

        # --- 2. NEXT ---
        elif text == "next":
            chosen = random.choice(shayari_list)
            bot.send_message(chat_id, f"*{chosen}*\n\n🙌 Sab **Darling Maxxu** ka karam hai!", parse_mode="Markdown")
            return

        # --- 3. ADMIN GALI (Only for @maxxu_ig) ---
        if sender_id == MAXXU_ID:
            if "ise suna kuch" in text and message.reply_to_message:
                target = message.reply_to_message.from_user
                for i in range(10): # Range kam rakhi hai test ke liye
                    bot.send_message(chat_id, f"[{target.first_name}](tg://user?id={target.id}) {random.choice(nrml_gali)}", parse_mode="Markdown")
                    time.sleep(0.5)
                return

        # --- 4. SHAYARI TRIGGER ---
        if "shayari" in text or "sayari" in text:
            chosen = random.choice(shayari_list)
            bot.send_message(chat_id, f"*{chosen}*\n\n❤️ **Darling Maxxu (@maxxu_ig)**", parse_mode="Markdown")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.infinity_polling()
