import telebot
import random
import os
from flask import Flask
import threading

# 1. Setup
API_TOKEN = '8506856522:AAE-f6Fn9cNMVxIGVsLUMm8LUR-GTfvaYGg'
MAXXU_ID = 6363297042 
MAXXU_USERNAME = "@maxxu_ig"
bot = telebot.TeleBot(API_TOKEN)

# 2. Flask Server for Render
server = Flask(__name__)
@server.route("/")
def home(): return "Bot is Live!"

def run():
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

# 3. Shayari List (Formatting saaf kar di hai taaki crash na ho)
shayari_list = [
    "Teri saanson ki garmahat, mere khayalon ko bechain kar jaati hai.",
    "Tumhari smile, mere khayalon ko kapde utar deti hai.",
    "Tumhari aankhon ka nasha, sharab se zyada gehra hai.",
    "Tum paas baitho bas, baaki sab khud ho jaata hai."
]

# 4. Message Handler
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    try:
        text = message.text.lower()
        sender_id = message.from_user.id
        chat_id = message.chat.id
        user_name = message.from_user.first_name

        # --- SPECIAL TRIGGERS (Maxxu, Mood, Jaan) ---
        if any(word in text for word in ["maxxu", "mood", "jaan", "baby", "love you"]):
            chosen = random.choice(shayari_list)
            response = (
                f"Oye {user_name}, suno...\n\n"
                f"{chosen}\n\n"
                f"Achha lage toh Thank you bol ke 'Next' likhna!\n"
                f"Sab Darling Maxxu ({MAXXU_USERNAME}) ki daya hai!"
            )
            bot.send_message(chat_id, response) # Simple text, no markdown to avoid crash
            return

        # --- NEXT SYSTEM ---
        elif text == "next":
            chosen = random.choice(shayari_list)
            response = (
                f"Ek aur tere liye {user_name}...\n\n"
                f"{chosen}\n\n"
                f"Aur chahiye toh 'Next' likho!\n"
                f"Sab Darling Maxxu ({MAXXU_USERNAME}) ka karam hai!"
            )
            bot.send_message(chat_id, response)
            return

        # --- SHAYARI / SAYARI ---
        elif "shayari" in text or "sayari" in text:
            chosen = random.choice(shayari_list)
            response = (
                f"{chosen}\n\n"
                f"Shayari acchi lage toh 'Next' likhna...\n"
                f"Aur Darling Maxxu ({MAXXU_USERNAME}) ko Thank you bolna!"
            )
            bot.send_message(chat_id, response)
            return

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.infinity_polling()
