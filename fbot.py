import telebot
import random
import time

# Aapka Token yahan hai
API_TOKEN = '8506856522:AAE-f6Fn9cNMVxIGVsLUMm8LUR-GTfvaYGg'
bot = telebot.TeleBot(API_TOKEN)

# 1. Welcome Message (Jab koi naya banda aaye)
@bot.message_handler(content_types=['new_chat_members'])
def welcome_user(message):
    for user in message.new_chat_members:
        bot.reply_to(message, f"Swagat hai {user.first_name} bhai! Maxxu ke ilake mein shanti banaaye rakhein. 🔥")

# 2. Smart Chat Logic (Jo aapne manga tha)
@bot.message_handler(func=lambda msg: True)
def chat_handler(message):
    text = message.text.lower()
    sender = message.from_user.first_name

    # Kaha hai tu/Kaha ho ka jawab
    if "kaha hai" in text or "kaha ho" in text:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(message, f"Yahin hoon {sender} bhai 😊 Bol kya kaam hai?")

    # So gaya kya ka jawab
    elif "so gya" in text or "so gaya" in text:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(message, "Nahi re, Maxxu hamesha jaag raha hai! 😈")

    # Tera naam kya hai
    elif "tera naam" in text or "tera name" in text:
        bot.reply_to(message, "Mera naam Maxxu hai, par tera bhai hoon! 😎")

    # Ek kaam hai ka jawab
    elif "ek kam hai" in text or "ek kaam h" in text:
        bot.reply_to(message, f"Haan {sender}, bol na kya kaam hai? Sharma mat! 😉")

    # Radhe Radhe logic
    elif "radhe radhe" in text:
        bot.reply_to(message, "Radhe Radhe! 🙏 Sab badhiya?")
import os
from flask import Flask
import threading

server = Flask(__name__)
@server.route("/")
def home():
    return "Bot is Live!"

def run():
    # Render ke liye port 10000 set karna zaroori hai
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Server aur Bot dono saath chalenge
    threading.Thread(target=run).start()
    bot.infinity_polling()
