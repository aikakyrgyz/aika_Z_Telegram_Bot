import telebot
from decouple import config
from keyboards.inline import inline_key
import random
from random import randint
bot = telebot.TeleBot(config('TOKEN'))
secret_num = 0
num_tries =0


def generate_secret_num():
    global secret_num
    secret_num = randint(0, 100)

@bot.message_handler(commands=['start', ])
    

def welcome(message):
    bot.send_message(message.chat.id, "Welcome To Aika-Z-Bot", reply_markup = inline_key)

def guess(message):
    generate_secret_num()
    msg = bot.send_message(message.chat.id, 'Guess the number')
    bot.register_next_step_handler(msg, get_guess)

def get_guess(message):
    num = int(message.text)
    guessed = False
    while not guessed:
        global num_tries
        num_tries +=1
        if secret_num == num:
            # bot.register_next_step_handler(message, win)
            bot.send_message(message.chat.id, '\U00002714' +f'Congrats' + '\U0001F389')
            bot.send_message(message.chat.id, f'You won with {num_tries} tries')

            break
        elif num > 100 or num < 0:
            bot.send_message(message.chat.id, 'The number is out of range')
        else:
            bot.send_message(message.chat.id,'\U0000274C' + 'Oh no, your guess was wrong')
            if(num_tries>5):
                if num - secret_num > 0:
                    bot.send_message(message.chat.id,'\U0001F4A1'+'The secret number is smaller than '+ str(num))
                else:
                    bot.send_message(message.chat.id,'\U0001F4A1'+'The secret number is greater than '+ str(num))
            msg = bot.send_message(message.chat.id, 'Guess the number')
            bot.register_next_step_handler(msg, get_guess)
            break
            
def win(message):
    bot.send_message(message.chat.id, '\U00002714' +f'Congrats' + '\U0001F389')
    bot.send_message(message.chat.id, f'You needed just {num_tries} tries to guess the number. Yes, it was {secret_num}.\nGood bye!!!' + '\U0001F44B')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'Would you like to play? yes':
        guess(call.message)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'See you next time')
bot.polling(none_stop=True)
