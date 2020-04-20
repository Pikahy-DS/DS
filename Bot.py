import telebot
import config
import random
from telebot import types, TeleBot
import datetime
import COVID19Py
import pyowm
from telebot.types import InlineKeyboardMarkup
from pycbrf.toolbox import ExchangeRates
import One
import gc
import time
bot: TeleBot = telebot.TeleBot(config.TOKEN)
owm = pyowm.OWM(config.TOKEN2, language = "ru")
covid19 = COVID19Py.COVID19()
smiles = [
    '❤','😘','😂','☺','😳','😚','😅','🙊','😐','😋','😆','😃','🤣','😍','🥰','😘','😝','🧐','🤬','😡','🤯'
]
hello = [
    'Good morning', 'Good evening, i"m the dispatcher ', 'Good night', 'You are welcome', 'Thanks', 'Доброе утро', 'Hello', 'Hi', 'Привет','Добрый вечер, я диспетчер'
]
@bot.message_handler(commands = ['start'])
def welcome(message):

    #keybroad
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
    #item4 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("👑 COVID19")
    item6 = types.KeyboardButton('Вакансии')
    item5 = types.KeyboardButton('📅 Время')
    item1 = types.KeyboardButton('📚 Расписание пар')
    item3= types.KeyboardButton('⛅️Погода')
    item4 = types.KeyboardButton('💶 Курс валют')
    markup.add(item4, item2, item3)
    markup.add(item5,item6)
    markup.add(item1)
    bot.send_message(message.chat.id,
                     f"{random.choice(hello)}" + ", {0.first_name}!\nЯ - <b>{1.first_name}</b>, а ты нет, бот созданный чтобы упростить тебе жизнь ".format(
                         message.from_user, bot.get_me()) + f"{random.choice(smiles)}",
                     parse_mode='html', reply_markup = markup)
    print(message.from_user)
@bot.message_handler(commands = ['help'])
def helps(message):
    ic = datetime.datetime.now(tz=None)
    date_time= ic.strftime("%d-%m-%Y")
    bot.send_message(message.chat.id, 'Ля, ты че <b>покемон</b>, запутался?\nНу, не бойся, ща я тебе помогу осмыслить, что к чему', parse_mode = 'html')
    bot.send_message(message.chat.id, f'Вот мой <b>полный</b> список команд на {date_time} :\n/help - Ну то что ты и вызвал, <b>красавчик</b> {smiles[3]}\n/start - Опа, вот это поворот, не правда ли? {random.choice(smiles)}\nИ все, братишка, приплыли, больше команд нет {random.choice(smiles)}', parse_mode = 'html')

@bot.callback_query_handler(func = lambda call: True) #Отвечает за виртуальные кнопки
def callback_woker(call):
    try:
        if call.data == 'yes':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True )
            item1 = types.KeyboardButton("Да ")
            item2 = types.KeyboardButton("Нет")
            item3 = types.KeyboardButton('Возврат в главное меню')
            markup.add(item1, item2)
            markup.add(item3)
            bot.send_message(call.message.chat.id, 'А я доверяю тебе 😏 ')

            bot.send_message(call.message.chat.id, 'Ты приготовился к игре? 😈 ', reply_markup = markup )
        elif call.data == 'no':
            bot.send_message(call.message.chat.id, f'И Я ТЕБЕ НЕ ДОВЕРЯЮ {random.choice(smiles)}')
        elif call.data == 'one':
            keyboard = types.InlineKeyboardMarkup()
            Yes1 = types.InlineKeyboardButton(text='Да', callback_data='Yes1')
            keyboard.add(Yes1)
            No1 = types.InlineKeyboardButton(text="Нет", callback_data='No1')
            keyboard.add(No1)
            bot.send_message(call.message.chat.id, 'И так, у тебя ровно одна попытка' + f'\nЗагадай число {random.choice(smiles)}')
            bot.send_message(call.message.chat.id, 'Загадал?', reply_markup = keyboard)
        elif call.data == 'two':
            keyboard = types.InlineKeyboardMarkup()
            Yes1 = types.InlineKeyboardButton(text='Да', callback_data='Yes1')
            keyboard.add(Yes1)
            No1 = types.InlineKeyboardButton(text="Нет", callback_data='No1')
            keyboard.add(No1)
            bot.send_message(call.message.chat.id, 'И так, у тебя ровно две попытки' + f'\nЗагадай число {random.choice(smiles)}')
            bot.send_message(call.message.chat.id, 'Загадал?', reply_markup=keyboard)
        elif call.data == 'LOL' or call.data == 'LOL1':
            bot.send_message(call.message.chat.id, f'Ну все <b>шутник</b>, на \nэтом\n шутки и <b>закончились</b> {random.choice(smiles)}', parce_mode = 'html')
        elif call.data == 'Yes1':
            keyboard = types.InlineKeyboardMarkup()
            Yes2 = types.InlineKeyboardButton(text = 'Да', callback_data = 'Yes2')
            No2 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'No2')
            keyboard.add(Yes2, No2)
            bot.send_message(call.message.chat.id, f'И так, ты загадал число {random.randint(1,100)}, я прав? {random.choice(smiles)} ',reply_markup = keyboard )
        elif call.data == 'Yes2':
            keyboard = types.InlineKeyboardMarkup()
            Yes3 = types.InlineKeyboardButton(text = 'Да', callback_data = 'Yes3')
            No3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'No3')
            keyboard.add(Yes3, No3)
            bot.send_message(call.message.chat.id, f'Уфф, какой я мощный, ДА? {random.choice(smiles)}', reply_markup = keyboard)
        elif call.data == 'Yes3' or call.data == 'No3':
            bot.send_message(call.message.chat.id, f'Все равно я мощный {random.choice(smiles)}')
        elif call.data == 'VAK':
            bot.send_message(call.message.chat.id, 'Загружаю...')
            job = []
            i = 0
            # One.main()
            # with open('../Python/text.data', 'r', encoding='utf - 8') as f:
            #     for word in f.readlines():
            #         job = [work for work in range(1,4)]
            #         bot.send_message(call.message.chat.id, f'{job[0]}\n{job[1]}\n{job[2]}\n{job[3]}')
            #         if i > 3:
            #             i = 0
            #             job.clear()
            #         else:
            #             i = i + 1
            #             job.append(word)
        elif call.data == 'VAK1':
            job = []
            i = 0
            bot.send_message(call.message.chat.id, 'Загружаю...')
            #One.main()
            with open('../Python/text.data', 'r', encoding='utf - 8') as f:
                for word in f.readlines():
                    if i >= 4:
                        i = 0
                        bot.send_message(call.message.chat.id, f'{job[0]}\n{job[1]}\n{job[2]}\n{job[3]}')
                        job.clear()
                    else:
                        i = i + 1
                        job.append(word)
                    #print(word)
                    #bot.send_message(call.message.chat.id, f'{word}\n{word}\n{word}')
        elif call.data == 'No2' or call.data == 'No1':
            keyboard = types.InlineKeyboardMarkup()
            Yes3 = types.InlineKeyboardButton(text='Да', callback_data='Yes1')
            No3 = types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(Yes3, No3)
            bot.send_message(call.message.chat.id, f'Попробуем еще раз', reply_markup= keyboard)
        elif call.data == 'Russia':
            location = covid19.getLocationByCountryCode("RU")
            date = location[0]['last_updated'].split('T')
            time = date[1].split(".")
            final_message = f"<u>Данные по стране Россия:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                            f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}"
            bot.send_message(call.message.chat.id, final_message, parse_mode='html')
        elif call.data == 'Usa':
            location = covid19.getLocationByCountryCode("US")
            date = location[0]['last_updated'].split('T')
            time = date[1].split(".")
            final_message = f"<u>Данные по стране США:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                            f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}"
            bot.send_message(call.message.chat.id, final_message, parse_mode='html')
        elif call.data == 'EU':
            location = covid19.getLocationByCountryCode("IT")
            date = location[0]['last_updated'].split('T')
            time = date[1].split(".")
            final_message = f"<u>Данные по стране Италия:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                            f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}"
            bot.send_message(call.message.chat.id, final_message, parse_mode='html')
        elif call.data == 'Ukraine':
            location = covid19.getLocationByCountryCode("UA")
            date = location[0]['last_updated'].split('T')
            time = date[1].split(".")
            final_message = f"<u>Данные по стране Украина:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                            f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}"
            bot.send_message(call.message.chat.id, final_message, parse_mode='html')
        elif call.data == 'All':
            try:
                location = covid19.getLatest()
                final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
                bot.send_message(call.message.chat.id, final_message, parse_mode = 'html')
            except Exception:
                bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
        elif call.data == 'Numerator':

            keyboard = types.InlineKeyboardMarkup()
            Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='Monday')
            keyboard.add(Monday)
            Tuesday = types.InlineKeyboardButton(text="Вторник", callback_data='Tuesday')
            keyboard.add(Tuesday)
            Wednesday = types.InlineKeyboardButton(text="Среда", callback_data='Wednesday')
            keyboard.add(Wednesday)
            Thursday = types.InlineKeyboardButton(text="Четверг", callback_data='Thursday')
            keyboard.add(Thursday)
            Friday = types.InlineKeyboardButton(text="Пятница", callback_data='Friday')
            keyboard.add(Friday)
            bot.send_message(call.message.chat.id, "Выбери день недели: ", reply_markup = keyboard)
            #bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id-1, reply_markup = '')
            # remove inline buttons

        # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
        #                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11"
        elif call.data == 'EUR':
            try:
                ic = datetime.datetime.now(tz=None)
                date_time = datetime.datetime.now(tz=None)
                rates = ExchangeRates(ic)
                date_time= ic.strftime("%d-%m-%Y")
                EUR = str(rates['EUR'][4])
                bot.send_message(call.message.chat.id, f'На <u>{date_time}:</u> \n1 евро = {EUR[:4]} руб.', parse_mode = 'html')
            except Exception:
                bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
        elif call.data == 'USD':
            try:
                ic = datetime.datetime.now(tz=None)
                date_time = datetime.datetime.now(tz=None)
                rates = ExchangeRates(ic)
                date_time= ic.strftime("%d-%m-%Y")
                USD = str(rates['USD'][4])
                bot.send_message(call.message.chat.id, f'На <u>{date_time}:</u> \n1 доллар = {USD[:4]} руб.', parse_mode = 'html')
            except Exception:
                bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
        elif call.data == 'Monday':
            bot.send_message(call.message.chat.id, 'Понедельник - Числитель \n1 пара: ТАУ (Практика) \n2 пара: ФИЗ - РА \n3 пара: Электротехника (Лекция) ')
        elif call.data == 'Tuesday':
            bot.send_message(call.message.chat.id, 'Вторник - Числитель \n1 пара: Алгоритмизация и программирование (Лекция) \n2 пара: Электробезопасность (Лекция) \n3 пара: Электротехика (Курсовая) ')
        elif call.data == 'Wednesday':
            bot.send_message(call.message.chat.id, 'Среда - Числитель \n1 пара: ТАУ (Лекция) \n2 пара: ТАУ (Лабораторная) \n  ')
        elif call.data == 'Thursday':
            bot.send_message(call.message.chat.id, 'Четверг - Числитель \n1 пара: Электроника (Лекция) \n2 пара: Прикладная Механика (Лекция) \n  ')
        elif call.data == 'Friday':
            bot.send_message(call.message.chat.id, 'Пятница - Числитель \n1 пара: Электроника (Лабораторная) \n2 пара: Базы Данных (Лабораторная) \n3 пара: Электротехника (Практика) ')
        elif call.data == 'Monday1':
            bot.send_message(call.message.chat.id,  'Понедельник - Знаменатель \n2 пара: ФИЗ - РА \n3 пара: Электротехника (Лекция) ')
        elif call.data == 'Tuesday1':
            bot.send_message(call.message.chat.id, 'Вторник - Знаменатель \n1 пара: Алгоритмизация и программирование (Практика) \n2 пара: Электробезопасность (Пратика) \n3 пара: Электротехника (Курсовая) ')
        elif call.data == 'Wednesday1':
            bot.send_message(call.message.chat.id, 'Среда - Знаменатель \n1 пара: Датчики (Лекция) \n2 пара: Датчики (Практика) \n3 пара: Электротехника (Лабораторная) ')
        elif call.data == 'Thursday1':
            bot.send_message(call.message.chat.id, 'Четверг - Знаменатель \n1 пара: Электроника (Лекция) \n2 пара: Прикладная Механика (Лекция) \n 3 пара: Прикладная Механика (Практика)')
        elif call.data == 'Friday1':
            bot.send_message(call.message.chat.id, 'Пятница - Знаменатель \n1 пара: Алгоритмизция и программирование (Лабораторная) \n2 пара: Базы Данных (Лабораторная) \n3 пара: Базы Данных (Лекция) ')
        elif call.data == 'Denominator':

            keyboard = types.InlineKeyboardMarkup()
            Monday1 = types.InlineKeyboardButton(text='Понедельник', callback_data='Monday1')
            keyboard.add(Monday1)
            Tuesday1 = types.InlineKeyboardButton(text="Вторник", callback_data='Tuesday1')
            keyboard.add(Tuesday1)
            Wednesday1 = types.InlineKeyboardButton(text="Среда", callback_data='Wednesday1')
            keyboard.add(Wednesday1)
            Thursday1 = types.InlineKeyboardButton(text="Четверг", callback_data='Thursday1')
            keyboard.add(Thursday1)
            Friday1 = types.InlineKeyboardButton(text="Пятница", callback_data='Friday1')
            keyboard.add(Friday1)
            bot.send_message(call.message.chat.id, 'Выбери день недели: ', reply_markup=keyboard)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= call.message.text,
                              reply_markup='')
    except Exception:
        bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
@bot.message_handler(content_types = ['text'])
def main(message): #Отвечает за кнопки на клавиатуре
    try:
        if message.chat.type == 'private':
            if message.text == '🎲 Рандомное число':
                bot.send_message(message.chat.id, str(random.randint(0,100)))
            elif message.text == '🎰 Игра':
                keyboard = types.InlineKeyboardMarkup()
                key_yes = types.InlineKeyboardButton(text=' Да', callback_data='yes')
                keyboard.add(key_yes)
                key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
                keyboard.add(key_no)
                bot.send_message(message.chat.id, 'Ты доверяешь мне?', reply_markup = keyboard)
            elif message.text == 'Возврат в главное меню':
                bot.register_next_step_handler(message, welcome)
            elif message.text == 'Нет':
                bot.register_next_step_handler(message, welcome)
                bot.send_message(message.chat.id, 'Напиши любое сообщение')
            elif message.text == 'Да':
                keyboard = types.InlineKeyboardMarkup()
                key_yes = types.InlineKeyboardButton(text='Бесконечность не предел (-♾: ♾+)', callback_data='one')
                keyboard.add(key_yes)
                key_no = types.InlineKeyboardButton(text="Попытки стремятся к нулю 🔜", callback_data='two')
                keyboard.add(key_no)
                bot.send_message(message.chat.id, 'Как ты думаешь, сколько у тебя попыток?) 🙀 ', reply_markup=keyboard)
            elif message.text == '📚 Расписание пар':
                keyboard = types.InlineKeyboardMarkup()
                key_yes = types.InlineKeyboardButton(text='Числитель', callback_data='Numerator')
                keyboard.add(key_yes)
                key_no = types.InlineKeyboardButton(text="Знаменатель", callback_data='Denominator')
                keyboard.add(key_no)
                bot.send_message(message.chat.id, 'Числитель или Знаменатель?', reply_markup=keyboard)
            elif message.text == '📅 Время':
                date2 = datetime.datetime(2020, 6, 1)
                ic = datetime.datetime.now().isocalendar()
                b = 'Числитель' if ic[1] % 2 != 0 else 'Знаменатель'
                date_time = datetime.datetime.now(tz = None)
                date_t = date2 - date_time
                bot.reply_to(message, "Сейчас:  " + date_time.strftime("%d-%m-%Y %H:%M") + f" - {b}" + f"\nДо сессии: {str(date_t.days)} дней")
                #bot.reply_to(message, f"До сессии: {str(date_t.days)} дней\nСейчас: {b}")
            elif message.text == "👑 COVID19":
                keyboard: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                key_yes = types.InlineKeyboardButton(text='Россия', callback_data='Russia')

                key_no = types.InlineKeyboardButton(text="США", callback_data='Usa')
                keyboard.add(key_no, key_yes)
                key_go = types.InlineKeyboardButton(text="Украина", callback_data='Ukraine')

                key_mo = types.InlineKeyboardButton(text="Во всем мире", callback_data='All')
                key_d = types.InlineKeyboardButton(text="Италия", callback_data='EU')
                keyboard.add(key_go, key_d)
                keyboard.add(key_mo)
                bot.send_message(message.chat.id, 'По какой стране вывести информацию?', reply_markup=keyboard)
            elif message.text == '⛅️Погода':
                observation = owm.weather_at_place('Старый Оскол')
                w = observation.get_weather()
                temp = w.get_temperature('celsius')['temp']
                V = w.get_wind()
                clothes = 'Одевайся теплее' if (temp < 20 or V['speed'] < 10) else 'Надевай легкую одежду'
                bot.send_message(message.chat.id, 'На улице сейчас ' + w.get_detailed_status() + '\nТемпература сейчас в районе '+ str(int(temp)) + ' °C\n' + 'Скорость ветра = ' + str(V['speed']) + ' м/с\n' + clothes)
            elif message.text == '💶 Курс валют':
                keyboard = types.InlineKeyboardMarkup()
                key_yes = types.InlineKeyboardButton(text='Евро', callback_data='EUR')
                key_no = types.InlineKeyboardButton(text="Доллар", callback_data='USD')
                keyboard.add(key_no, key_yes)
                bot.send_message(message.chat.id, f'По какой валюте вывести информацию? {random.choice(smiles)}', reply_markup = keyboard)
            elif message.text == 'Вакансии':
                keyboard = types.InlineKeyboardMarkup()
                vak_1 = types.InlineKeyboardButton(text = 'Без опыта, студенты', callback_data = 'VAK')
                vak_2 = types.InlineKeyboardButton(text = 'IT отрасль', callback_data = 'VAK1')
                keyboard.add(vak_1,vak_2)
                bot.send_message(message.chat.id, f'<u>Выбери категорию:</u> ', parse_mode = 'html', reply_markup = keyboard)
            else:
                #bot.send_message('620389844', f'Я не знаю, что ответить {random.choice(smiles)}')
                markup = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard = True)
                item6 = types.KeyboardButton('🎰 Игра')
                markup.add(item6)


                bot.send_message(message.chat.id, f'Я не знаю, что ответить, воспользуйся кнопочками (или напиши /help) {random.choice(smiles)}', reply_markup = markup)


    except Exception:
        bot.send_message(message.chat.id, f'Это что еще за покемон? {random.choice(smiles)}\nОшибка на сервер, сейчас кабанчики подскочат и порешают! {random.choice(smiles)}')
# def games(message):
#     bot.send_message(message.chat.id, 'Hello')
#     bot.register_next_step_handler(message, welcome)

bot.polling(none_stop = True)
 