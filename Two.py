# -*- coding: utf8 -*-
import  random
#while 2 < 3:
 #   print ("Секунд:", 3600* int(input('Hour: '))+60*int(input('min: ')))
# -*- coding: utf8 -*-
import telebot
import config
import random
from telebot import types, TeleBot
import datetime
import sqlite3
from Python.db import init_db
from Python.db import add_message
from Python.db import count_messages
from Python.db import list_messages
import pyowm
from telebot.types import InlineKeyboardMarkup
from pycbrf.toolbox import ExchangeRates
import One
import gc
import time
import Three
bot: TeleBot = telebot.TeleBot(config.TOKEN2)
con = sqlite3.connect('anketa.db')
cursor = con.cursor()
@bot.message_handler(commands = ['start'])
def welcome(message):

    #keybroad
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)

    item1 = types.KeyboardButton('📅 Время')
    item2 = types.KeyboardButton('🏠 Домой')
    item3= types.KeyboardButton('⛅️Погода')
    item4 = types.KeyboardButton('🏫 На учебу')
    item5 = types.KeyboardButton('🔮 Гороскоп')

    markup.add(item5,item3)
    markup.add(item4,item2)

    bot.send_message(message.chat.id,
                     f"Gygd",  reply_markup = markup)
    print(message.from_user)
@bot.message_handler(commands = ['help'])
def helps(message):
    pass
@bot.callback_query_handler(func = lambda call: True) #Отвечает за виртуальные кнопки
def callback_woker(call):
    pass

@bot.message_handler(content_types = ['text'])
def main(message): #Отвечает за кнопки на клавиатуре
        print(message.from_user)
        id = message.from_user.id
        if message.chat.type == 'private':
           if message.text == ('🔮 Гороскоп'):
             bot.send_message(message.from_user.id, "Как тебя зовут?")
             bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, access_msg)

   # res = access_msg(name,get_surname)

@bot.message_handler(func=lambda message: message.chat.id)
def access_msg(message):
    global surname
    surname = message.text
    bot.send_message(528178987, 'ПРИВЕТИКИ, КАТЮШКА, Я ПО ТЕБЕ СКУЧАЮ')
    id = message.from_user.id
    init_db()
    add_message(user_id= id, text=name, Family = surname)
    bot.send_message(message.chat.id, count_messages(user_id = id))
    messages = list_messages(user_id = id, limit=2)
    text = '\n\n'.join([f'#{message_user_id} - {message_text} - {message_Family}' for message_user_id, message_text, message_Family in messages])
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, 'Доступ ограничен')
    #except Exception:


bot.polling(none_stop = True)
