import telebot
import random
import time
import os
from flask import Flask
import threading

# 1. Bot Token Setup
API_TOKEN = '8506856522:AAE-f6Fn9cNMVxIGVsLUMm8LUR-GTfvaYGg' #
bot = telebot.TeleBot(API_TOKEN)

# 2. Flask Server (Render active rakhne ke liye)
server = Flask(__name__)
@server.route("/")
def home():
    return "Maxxu Bot is Active with Gali Mode!"

def run():
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

# 3. Gali List (Normal Wali)
galiyan = [
    "Abe gadhe ki aulad!", "Shakal dekhi hai apni?", "Oye bewakoof insaan!", 
    "Dimag ghar chhod ke aaya hai kya?", "Nalayak kahin ke!", "Bade aaye chaudhary!", 
    "Abbe oye namune!", "Tere se na ho payega beta."
]

# 4. Human Chat Logic + Gali Spam
@bot.message_handler(func=lambda message: True)
def human_chat(message):
    text = message.text.lower()
    user_name = message.from_user.first_name
    user_id = message.from_user.id

    # AGAR AAPNE BOLA "ise suna kuch"
    if "ise suna kuch" in text:
        # Check karna ki ye kisi message ka reply hai ya nahi
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
            target_mention = f"[{target_user.first_name}](tg://user?id={target_user.id})"
            
            bot.send_message(message.chat.id, f"Theek hai bhai, abhi iski bajata hoon! 😈")
            
            # 20 baar tag karke spam karna
            for i in range(20):
                gali = random.choice(galiyan)
                bot.send_message(message.chat.id, f"{target_mention} {gali}", parse_mode="Markdown")
                time.sleep(0.5) # Thoda delay taaki Telegram ban na kare
            return
        else:
            bot.reply_to(message, "Bhai, pehle kisi ke message par 'Reply' toh karo jise sunana hai!")
            return

    # Normal Chat Logic
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1) 

    if "hi" in text or "hello" in text:
        reply = random.choice([f"Aur {user_name} bhai, kya haal chaal?", "Hi bhai, kya chal raha hai?"])
    elif "kaha hai" in text:
        reply = "Yahin hoon ⚡M A X X U💀..!..✍️bhai 😊 Bol kya kaam hai?" #
    else:
        # Fallback: English Sorry Line
        reply = "Sorry, I didn't understand. Could you please say that again?"

    bot.reply_to(message, reply)

# Start Everything
if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.infinity_polling()
