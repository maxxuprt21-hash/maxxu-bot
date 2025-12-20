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

# 2. Flask Server (For 24/7 Render)
server = Flask(__name__)
@server.route("/")
def home(): return f"Maxxu ({MAXXU_USERNAME}) Bot is Live!"

def run():
    port = int(os.environ.get("PORT", 10000))
    server.run(host="0.0.0.0", port=port)

# 3. Data Lists
nrml_gali = ["Abe oye namune!", "Dimag bech khaya hai?", "Nalayak kahin ke!", "Oye bewakoof!", "Shakal dekhi hai apni?"]

# Yahan aapki saari 200+ shayariyaan hain
shayari_list = [
    "Teri saanson ki garmahat, mere khayalon ko bechain kar jaati hai.",
    "Aankhon se jo baat hui, jism tak utar aayi.",
    "Tera naam lete hi, dhadkan zara tez ho jaati hai.",
    "Raat ki khamoshi mein, tera khayal sabse zyada bolta hai.",
    "Teri nazron ka nasha, sharab se gehra laga.",
    "Labon ki muskurahat mein, kitni shararat chhupi hai.",
    "Tu paas ho, to har lamha zinda lagta hai.",
    "Teri khushboo ne, mere sab iraade bigaad diye.",
    "Ishq ka junoon ho tum, aadat nahi.",
    "Tere bina bhi, tera hi khayal saath chalta hai.",
    "Aankhon ka jadoo, dil pe seedha vaar karta hai.",
    "Teri baatein, raat ko aur gehra bana deti hain.",
    "Jism se pehle, rooh ne tujhe chuaa.",
    "Tera zikr ho, to sharm bhi muskura jaati hai.",
    "Tere kareeb aana, khud se door hona hai.",
    "Saans saans mein, tera ehsaas bhara hai.",
    "Teri aankhon ki chamak, khwaab jaga deti hai.",
    "Dil ke parde pe, tera hi scene chalta hai.",
    "Tu muskura de, mausam bhi badal jaaye.",
    "Tere khayal ka sparsh, bahut gehra hota hai.",
    "Teri aankhon mein doobna, mujhe pasand hai.",
    "Tere lafzon mein, narm si aag jalti hai.",
    "Dil ko chhed jaaye, tera halka sa ishara.",
    "Tu saath ho, to darr bhi khoobsurat lage.",
    "Teri saanson ki leher, mujhe baha le jaaye.",
    "Aaj phir, khayalon mein tera libaas chamka.",
    "Teri nazar ka jhukna, sab kuch keh jaata hai.",
    "Tera naam, labon pe aate hi meetha ho jaata hai.",
    "Teri baahon ka khayal, sukoon bhi, aag bhi.",
    "Tu paas ho, to waqt thahar jaaye.",
    "Teri khamoshi bhi, bahut shor karti hai.",
    "Tere saath hone ka ehsaas, kaafi hai.",
    "Aankhon mein sharm, dil mein tufaan.",
    "Teri yaadein, raat ko aur gehra kar deti hain.",
    "Tu muskura ke dekhe, sab pighal jaaye.",
    "Teri ungliyon ka khayal, dil ko chhoo jaata hai.",
    "Ishq mein sharafat, thodi kam pad jaati hai.",
    "Teri aankhon se baat, lafzon se aage nikal jaati hai.",
    "Tu ho, to bechaini bhi pyaari lage.",
    "Teri saanson ka ehsaas, mere paas rehta hai.",
    "Khayalon mein tera aana, aadat ban gayi.",
    "Tere bina bhi, tu hi saath hoti hai.",
    "Teri nazar ka teer, seedha dil pe lagta hai.",
    "Tu paas aaye, to dhadkan bol uthti hai.",
    "Teri baaton mein, nasha sa ghula hai.",
    "Raat aur tu, dono hi gehre ho.",
    "Teri aankhon ka rang, khwaabon se gehra hai.",
    "Tere saath, khamoshi bhi bolti hai.",
    "Teri muskurahat, sab kuch bhula deti hai.",
    "Tu chhoo le khayalon mein, kaafi hai.",
    "Teri saanson ka saath, mujhe zinda rakhta hai.",
    "Teri baahon ka khayal, dil ko gher leta hai.",
    "Aankhon se shuru hua ishq, dil tak pahunch gaya.",
    "Teri adaon mein, shararat bhari hai.",
    "Tu saath ho, to raat aur gehri ho jaaye.",
    "Teri baatein, khud ko bhula deti hain.",
    "Ishq ka rang, teri aankhon mein dikhta hai.",
    "Tu paas aaye, to sab theek lagta hai.",
    "Teri saanson ka ehsaas, mere khayalon mein hai.",
    "Tu muskuraye, dil bechain ho jaaye.",
    "Teri nazar ka jadoo, lafzon ka mohtaaj nahi.",
    "Raat ki hawa mein, tera naam ghula hai.",
    "Teri khamoshi, mujhe aur paas bulati hai.",
    "Tu ho, to khayal bhi garam ho jaate hain.",
    "Teri aankhon ki gehraai, mujhe kheench leti hai.",
    "Tere kareeb, khud ko bhool jaata hoon.",
    "Teri baaton mein, meethi si aag hai.",
    "Tu paas aaye, to saans ruk si jaaye.",
    "Teri yaadon ka nasha, dheere dheere chadhta hai.",
    "Tu saath ho, to darr bhi khoobsurat lage.",
    "Teri aankhon ka jhukna, dil ko chhed deta hai.",
    "Raat aur tera khayal, saath saath chalte hain.",
    "Teri baahon ka sapna, sukoon deta hai.",
    "Tu ho, to khwaab aur gehre ho jaate hain.",
    "Teri muskurahat, raat ko roshan kar deti hai.",
    "Teri saanson ka ehsaas, mere paas hai.",
    "Tu paas aaye, to waqt pighal jaaye.",
    "Teri aankhon mein, ishq likha hai.",
    "Tere khayal ka sparsh, dil ko hila deta hai.",
    "Tu saath ho, to har lamha khaas ho.",
    "Teri khamoshi, mujhe bechain kar deti hai.",
    "Tere lafzon ka nasha, dheere dheere chadhta hai.",
    "Tu paas ho, to raat aur gehri ho.",
    "Teri aankhon ka rang, khwaabon se gehra.",
    "Tere saath, har ehsaas tez ho jaata hai.",
    "Teri baatein, dil ko chhoo jaati hain.",
    "Tu ho, to bechaini bhi pyaari lage.",
    "Teri nazar ka asar, lamba rehta hai.",
    "Tere khayalon mein, khud ko paata hoon.",
    "Tu paas aaye, to saans bhar jaaye.",
    "Teri muskurahat, dil ko pighla deti hai.",
    "Raat ke saaye mein, tera naam chamakta hai.",
    "Teri aankhon ka jadoo, chhodta nahi.",
    "Tu ho, to khamoshi bhi mehsoos hoti hai.",
    "Teri baahon ka khayal, raat bhar jagata hai.",
    "Tu paas ho, to khud se milta hoon.",
    "Teri saanson ka saath, dil ko sukoon deta hai.",
    "Teri baatein, khayalon ko garam karti hain.",
    "Tu ho, to ishq mukammal lage.",
    "Teri aankhon mein, poori kahani hai.",
    "Tere kareeb, har ehsaas gehra ho jaata hai.",
    "Teri muskurahat, raat ko bhi sharma deti hai.",
    "Tu paas aaye, to dhadkan bol uthti hai.",
    "Teri nazar, sab keh jaati hai.",
    "Teri baahon ka khayal, dil ko gher leta hai.",
    "Tu ho, to khwaab bhi sach lagte hain.",
    "Teri saanson ka nasha, dheere dheere chadhta hai.",
    "Tere lafzon ka sparsh, dil ko chhoo jaata hai.",
    "Tu paas ho, to waqt tham jaaye.",
    "Teri aankhon ki gehraai, mujhe bulaati hai.",
    "Teri khamoshi, bahut kuch keh jaati hai.",
    "Raat aur tera khayal, saath saath jalte hain.",
    "Teri muskurahat, dil ko sukoon deti hai.",
    "Tu ho, to har lamha pyaara lage.",
    "Teri baatein, khud ko bhula deti hain.",
    "Teri aankhon ka jadoo, dil ko baandh leta hai.",
    "Tu paas aaye, to khud se door ho jaata hoon.",
    "Teri saanson ka ehsaas, mere paas rehta hai.",
    "Teri nazar ka teer, seedha dil pe lagta hai.",
    "Tu ho, to ishq aur gehra ho jaata hai.",
    "Teri muskurahat, raat ko roshan karti hai.",
    "Tere khayal ka sparsh, dil ko jaga deta hai.",
    "Tu paas ho, to har baat khaas ho jaati hai.",
    "Teri aankhon mein, nasha sa ghula hai.",
    "Teri baatein, khayalon ko garam karti hain.",
    "Tu ho, to bechaini bhi meethi lage.",
    "Teri baahon ka sapna, sukoon deta hai.",
    "Teri nazar ka asar, der tak rehta hai.",
    "Tu paas aaye, to saans ruk si jaaye.",
    "Teri muskurahat, dil ko chhed deti hai.",
    "Teri aankhon ki gehraai, mujhe kheench leti hai.",
    "Raat ke andhere mein, tera naam chamakta hai.",
    "Tu ho, to khamoshi bhi bolti hai.",
    "Teri baatein, dil ko narm kar deti hain.",
    "Tu paas aaye, to waqt pighal jaaye.",
    "Teri saanson ka ehsaas, mere khayalon mein hai.",
    "Teri nazar ka jadoo, chhodta nahi.",
    "Tu ho, to ishq mukammal lage.",
    "Teri muskurahat, sab kuch bhula deti hai.",
    "Tere kareeb, har lamha zinda lage.",
    "Teri khamoshi, mujhe aur paas bulati hai.",
    "Teri aankhon ka rang, raat se gehra hai.",
    "Tu paas ho, to khwaab aur gehre ho jaate hain.",
    "Teri baatein, raat ko aur garam karti hain.",
    "Tu ho, to dil bechain rehna chahe.",
    "Teri baahon ka khayal, sukoon bhi, aag bhi.",
    "Teri nazar, sab keh jaati hai.",
    "Tu paas aaye, to saans bhar jaaye.",
    "Teri muskurahat, raat ko sharma deti hai.",
    "Teri aankhon mein, ishq chamakta hai.",
    "Teri saanson ka saath, mujhe zinda rakhta hai.",
    "Teri baatein, dil ko chhoo jaati hain.",
    "Tu ho, to khud se milta hoon.",
    "Teri nazar ka teer, dil ko chhed deta hai.",
    "Teri muskurahat, sukoon ka sabab hai.",
    "Tu paas ho, to waqt ruk jaaye.",
    "Teri aankhon ki gehraai, mujhe bulaati hai.",
    "Teri khamoshi, bahut kuch keh jaati hai.",
    "Tu ho, to ishq aur gehra ho jaata hai.",
    "Teri baahon ka khayal, raat bhar jagata hai.",
    "Teri muskurahat, dil ko pighla deti hai.",
    "Raat aur tera khayal, saath saath jalte hain.",
    "Teri baatein, khud ko bhula deti hain.",
    "Tu paas aaye, to dhadkan tez ho jaaye.",
    "Teri aankhon ka jadoo, chhodta nahi.",
    "Tu ho, to har ehsaas khaas ho jaata hai.",
    "Teri saanson ka ehsaas, mere paas hai.",
    "Teri nazar ka asar, lamba rehta hai.",
    "Tu paas ho, to bechaini bhi pyaari lage.",
    "Teri muskurahat, raat ko roshan karti hai.",
    "Teri aankhon mein, poori kahani hai.",
    "Tere kareeb, har lamha zinda lagta hai.",
    "Teri baatein, dil ko narm kar deti hain.",
    "Tu ho, to khwaab bhi sach lagte hain.",
    "Teri nazar, sab keh jaati hai.",
    "Tu paas aaye, to saans ruk si jaaye.",
    "Teri muskurahat, sab kuch bhula deti hai.",
    "Teri saanson ka saath, sukoon deta hai.",
    "Tu ho, to ishq mukammal lage.",
    "Teri aankhon ki gehraai, mujhe kheench leti hai.",
    "Teri khamoshi, mujhe aur paas bulati hai.",
    "Raat ke saaye mein, tera naam chamakta hai.",
    "Tu paas ho, to waqt pighal jaaye.",
    "Teri baatein, khayalon ko garam karti hain.",
    "Teri muskurahat, dil ko chhed deti hai.",
    "Tu ho, to har baat khaas ho jaati hai.",
    "Teri nazar ka jadoo, dil ko baandh leta hai.",
    "Tu paas aaye, to dhadkan bol uthti hai.",
    "Teri saanson ka ehsaas, mere khayalon mein hai.",
    "Teri aankhon mein, ishq likha hai.",
    "Teri muskurahat, raat ko sharma deti hai.",
    "Tu ho, to bechaini bhi meethi lage.",
    "Teri baatein, khud ko bhula deti hain.",
    "Tu paas ho, to khamoshi bhi bolti hai.",
    "Teri nazar ka teer, seedha dil pe lagta hai.",
    "Teri saanson ka saath, mujhe zinda rakhta hai.",
    "Tu ho, to ishq aur gehra ho jaata hai.",
    "Teri muskurahat, sukoon ka sabab hai.",
    "Tu paas aaye, to waqt tham jaaye.",
    "Teri aankhon ki gehraai, mujhe apna bana leti hai.",
    "Tumhari aankhon ka nasha, sharab se zyada gehra hai.",
    "Tum muskurati ho, aur raat aur bhi haseen ho jaati hai.",
    "Tumhari baatein, dil ko dheere dheere nanga kar jaati hain.",
    "Tum paas hoti ho, to saans bhi romantic lagti hai.",
    "Tumhari aankhon mein doobna, meri aadat ban chuki hai.",
    "Tumhari smile, mere khayalon ko kapde utar deti hai.",
    "Tum bolti kam ho, par mehsoos zyada hoti ho.",
    "Tumhari khamoshi bhi, mujhe chhoo jaati hai.",
    "Tum paas baitho bas, baaki sab khud ho jaata hai.",
    "Tumhari nazar, seedha dil ke button pe lagti hai.",
    "Tumhari hansi, mere sab control tod deti hai.",
    "Tumhari aankhon ka kajal, meri neend chura leta hai.",
    "Tum saath ho, to waqt bhi slow ho jaata hai.",
    "Tumhari baaton mein ek meethi si garmi hai.",
    "Tumhara naam, hothon pe aate hi mood badal deta hai.",
    "Tumhari ek smile, poori raat ka plan bana deti hai.",
    "Tumhari aankhon mein shararat bhi hai, mohabbat bhi.",
    "Tumhara chup rehna bhi, bohot kuch keh jaata hai.",
    "Tumhare paas hone se hi, dil zinda lagta hai.",
    "Tumhari saans ki halki si awaaz bhi kaafi hai.",
    "Tumhari aankhen, jaise raaz bhari kitaab ho.",
    "Tumhari baatein, dheere dheere aag lagati hain.",
    "Tumhari smile, meri kamzori hai.",
    "Tumhare saath, khamoshi bhi romantic lagti hai.",
    "Tumhari nazar, pooch kar nahi lagti.",
    "Tum paas hoti ho, to dil badtameez ho jaata hai.",
    "Tumhari aankhon ka contact, saara kaam kharab kar deta hai.",
    "Tumhari baaton mein ek dangerous attraction hai.",
    "Tum saath ho, to raat aur gehri ho jaati hai.",
    "Tumhari smile, mujhe dheere dheere pagal banati hai.",
    "Tumhari aankhen, dil ko touch kar jaati hain.",
    "Tumhari baatein, seedha imagination pe lagti hain.",
    "Tumhare kareeb rehna, ek alag hi feeling deta hai.",
    "Tumhari nazar, jaise bula rahi ho.",
    "Tumhari smile, meri saari thakaan utaar deti hai.",
    "Tumhari aankhon mein kuch toh hai, jo mujhe kheenchta hai.",
    "Tum paas aati ho, to saans tez ho jaati hai.",
    "Tumhari baatein, raat ko aur lambi bana deti hain.",
    "Tumhari khamoshi bhi, bohot loud hoti hai.",
    "Tumhari smile, dil pe slow poison hai.",
    "Tumhari aankhen, mujhe chupchaap bula leti hain.",
    "Tumhari baaton ka tone, kaam bigaad deta hai.",
    "Tum paas hoti ho, to sab kuch personal lagta hai.",
    "Tumhari smile, meri neend ka dushman hai.",
    "Tumhari aankhon ka jadoo, dheere dheere chadhta hai.",
    "Tumhari baatein, seedha mood pe kaam karti hain.",
    "Tumhare paas hona hi, kaafi hai.",
    "Tumhari nazar, thodi si naughty lagti hai.",
    "Tumhari smile, mujhe aur chahne pe majboor karti hai.",
    "Tumhari aankhen, bohot kuch waada karti hain.",
    "Tumhari baatein, raat ko aur bhi garam bana deti hain.",
    "Tum paas hoti ho, to khayal bhi bold ho jaate hain.",
    "Tumhari smile, mere dil ka volume badha deti hai.",
    "Tumhari aankhon mein ek meethi si aag hai.",
    "Tumhari khamoshi, mujhe aur kareeb kheenchti hai.",
    "Tumhari baaton ka andaaz, dangerous hai.",
    "Tum saath ho, to har pal special lagta hai.",
    "Tumhari nazar, thodi si shararti hai.",
    "Tumhari smile, meri saari planning bhula deti hai.",
    "Tumhari aankhen, dil ko permission nahi deti.",
    "Tumhari baatein, dheere dheere bechain karti hain.",
    "Tum paas ho, to heartbeat bolne lagti hai.",
    "Tumhari smile, meri kamzori ka proof hai.",
    "Tumhari aankhen, saaf jhoot bolti hain.",
    "Tumhari khamoshi, bohot kuch keh deti hai.",
    "Tumhari baaton ka effect, slow par deep hota hai.",
    "Tum paas hoti ho, to hawa bhi romantic lagti hai.",
    "Tumhari nazar, rukne nahi deti.",
    "Tumhari smile, raat ko aur gehra kar deti hai.",
    "Tumhari aankhen, mujhe control nahi karne deti.",
    "Tumhari baatein, imagination ko jagati hain.",
    "Tum saath ho, to har pal thoda bold ho jaata hai.",
    "Tumhari smile, meri saari theory fail kar deti hai.",
    "Tumhari aankhen, bohot kuch chhupa ke rakhti hain.",
    "Tumhari khamoshi, mujhe aur paas bulati hai.",
    "Tumhari baaton mein ek alag si garmi hai.",
    "Tum paas hoti ho, to raat jaldi nahi hoti.",
    "Tumhari nazar, seedha dil ke andar jaati hai.",
    "Tumhari smile, mujhe aur zinda kar deti hai.",
    "Tumhari aankhen, meri aadat banti ja rahi hain.",
    "Tumhari baatein, dheere dheere nasha ban jaati hain.",
    "Tum paas ho, to sab kuch real lagta hai.",
    "Tumhari smile, meri saari dikkat bhula deti hai.",
    "Tumhari aankhen, bohot kuch maangti hain.",
    "Tumhari khamoshi, bohot kuch chhed jaati hai.",
    "Tumhari baaton ka asar, der tak rehta hai.",
    "Tum saath ho, to waqt ruk sa jaata hai.",
    "Tumhari nazar, thodi si dangerous hai.",
    "Tumhari smile, mujhe aur bold bana deti hai.",
    "Tumhari aankhen, meri soch badal deti hain.",
    "Tumhari baatein, raat ko aur gehra bana deti hain.",
    "Tum paas hoti ho, to sab kuch possible lagta hai.",
    "Tumhari smile, meri saari energy le jaati hai.",
    "Tumhari aankhen, bohot kuch promise karti hain.",
    "Tumhari khamoshi, mujhe aur curious banati hai.",
    "Tumhari baaton ka taste, addictive hai.",
    "Tum saath ho, to dil zyada bolta hai.",
    "Tumhari nazar, chupchaap kaam kar jaati hai.",
    "Tumhari smile, meri saari lines bhula deti hai.",
    "Tumhari aankhen, meri raaton ki wajah hain."
]

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
            f"Oye {mention}, aapke liye ek shayari hai...\n\n"
            f"*{chosen}*\n\n"
            "✨ Achha lage toh Thank you bol ke 'Next' likhna, agli sunauga!\n"
            f"❤️ Ye sab **Darling Maxxu ({MAXXU_USERNAME})** ki daya hai!"
        )
        bot.send_message(chat_id, response, parse_mode="Markdown")
        return

    # --- 2. NEXT SYSTEM ---
    elif text == "next":
        chosen = random.choice(shayari_list)
        response = (
            f"Ek aur suniye {mention}...\n\n"
            f"*{chosen}*\n\n"
            "✨ Agli chahiye toh phir 'Next' likho!\n"
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
        try: bot.delete_message(chat_id, message.message_id)
        except: pass
        return

    # --- 5. NORMAL REPLIES (Shayari/Sayari) ---
    if "shayari" in text or "sayari" in text:
        chosen = random.choice(shayari_list)
        bot.send_message(chat_id, f"*{chosen}*\n\n✨ Shayari acchi lage toh 'Next' likhna...\n❤️ Aur **Darling Maxxu ({MAXXU_USERNAME})** ko Thank you bolna!", parse_mode="Markdown")
        return

    # Fallback response (Har message par active reply)
    bot.reply_to(message, "Kuch samajh nahi aaya bhai, thoda saaf bolo!")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.infinity_polling()
