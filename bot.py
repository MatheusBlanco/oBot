import os
import telebot

token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, u"Oi ameguinho")

@bot.message_handler(func=lambda  message: True)
def shout_message(message):
    content = message.text
    if content == "oi":
        bot.send_message(chat_id=message.chat.id, text="Eu não faço nada ainda, então joga isso aqui: ")
        bot.open
    else:
        bot.send_message(chat_id=message.chat.id, text="Digita /start de novo")

bot.polling()