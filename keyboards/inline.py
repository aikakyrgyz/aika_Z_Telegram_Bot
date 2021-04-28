from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
inline_key = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton('yes', callback_data='yes')
btn2 = InlineKeyboardButton('no', callback_data = 'no')
inline_key.add(btn1, btn2)

