import telebot
from decouple import config
from keyboards.inline import inline_key
bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start', ])

def welcome(message):
    msg = bot.send_message(message.chat.id, "Welcome To Aika-Z-Bot", reply_markup = inline_key)
    bot.register_next_step_handler(msg, send_nik)

def send_nik(message):
    msg = bot.send_message(message.chat.id, 'Enter your nik')
    bot.register_next_step_handler(msg, send_age)

def send_age(message):
    msg = bot.send_message(message.chat.id, 'Enter your age')
    bot.register_next_step_handler(msg)

bot.polling(none_stop=True)
