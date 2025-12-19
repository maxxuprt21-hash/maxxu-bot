import telebot
import random
import time
import os
from flask import Flask
import threading
import re

# 1. Setup - @maxxu_ig special
API_TOKEN = '8506856522:AAE-f6Fn9cNMVxIGVsLUMm8LUR-GTfvaYGg'
MAXXU_ID = 6363297042 
MAXXU_USERNAME = "@maxxu_ig"
bot = telebot.TeleBot(API_TOKEN)

# 2. Flask Server
server = Flask(__name__)
@server.route("/")
def home(): return "Maxxu (@maxxu_ig) Bot is Live!"

def run():
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

# 3. Mega Shayari List (200+ wali list)
# (Yahan wahi 200 shayariyaan paste karna jo aapne pehle di thi)
shayari_list = [
    "Teri saanson ki garmahat, mere khayalon ko bechain kar jaati hai.",
    "Tumhari smile, mere khayalon ko kapde utar deti hai.",
    "Tumhari aankhon ka nasha, sharab se zyada gehra hai."
]

nrml_gali = ["Abe oye namune!", "Dimag bech khaya hai?", "Nalayak kahin ke!"]

# 4. Message Handler
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    text = message.text.lower()
    sender_id = message.from_user.id
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={sender_id})"

    # --- 1. ROMANTIC & MOOD COMMANDS ---
    romantic_triggers = ["mood", "jaan", "baby", "love you", "love u", "shona", "maxxu"]
    
    if any(word in text for word in romantic_triggers):
        chosen = random.choice(shayari_list)
        response = (
            f"Oye {mention}, suno...\n\n"
            f"*{chosen}*\n\n"
            "✨ Accha laga toh Thank you bol ke 'Next' likhna!\n"
            f"❤️ Ye sab **Darling Maxxu ({MAXXU_USERNAME})** ki daya hai!"
        )
        bot.send_message(chat_id, response, parse_mode="Markdown")
        return

    # --- 2. NEXT SYSTEM ---
    elif text == "next":
        chosen = random.choice(shayari_list)
        response = (
            f"Ek aur tere liye {mention}...\n\n"
            f"*{chosen}*\n\n"
            "✨ Aur chahiye toh 'Next' likho!\n"
            f"🙌 Sab **Darling Maxxu ({MAXXU_USERNAME})** ka karam hai!"
        )
        bot.send_message(chat_id, response, parse_mode="Markdown")
        return

    # --- 3. ADMIN PRIVILEGES (Only for @maxxu_ig) ---
    if sender_id == MAXXU_ID:
        if "ise suna kuch" in text and message.reply_to_message:
            target = message.reply_to_message.from_user
            bot.send_message(chat_id, f"Ji **Maxxu Bhai**, abhi iski bajata hoon! 😈")
            for i in range(20):
                bot.send_message(chat_id, f"[{target.first_name}](tg://user?id={target.id}) {random.choice(nrml_gali)}", parse_mode="Markdown")
                time.sleep(0.4)
            return
        elif "bas kar" in text:
            bot.reply_to(message, f"Thik hai **Darling Maxxu**, ab main shant hoon! 😉")
            return

    # --- 4. ANTI-LINK ---
    if re.search(r'http[s]?://', text) and sender_id != MAXXU_ID:
        bot.delete_message(chat_id, message.message_id)
        return

    # --- 5. NORMAL REPLIES ---
    if "shayari suna" in text:
        chosen = random.choice(shayari_list)
        bot.send_message(chat_id, f"*{chosen}*\n\n✨ Shayari acchi lage toh 'Next' likhna...\n❤️ Aur **Darling Maxxu ({MAXXU_USERNAME})** ko Thank you bolna!", parse_mode="Markdown")
    elif "hi" in text or "hello" in text:
        bot.reply_to(message, f"Aur {user_name} bhai, kya haal?")
    elif "kaha hai" in text:
        bot.reply_to(message, f"Yahin hoon **Maxxu** bhai! Bol kya kaam hai?")
    else:
        bot.reply_to(message, "Sorry, I didn't understand. Could you please say that again?")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.infinity_polling()
