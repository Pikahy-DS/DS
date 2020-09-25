# -*- coding: utf8 --
while True:
  try:
    import telebot
    import config
    import random
    from telebot import types, TeleBot
    import datetime
    import sqlite3

    #import COVID19Py
    import pyowm
    from telebot.types import InlineKeyboardMarkup
    from pycbrf.toolbox import ExchangeRates
    import One
    import gc
    import time
    import Three
    bot: TeleBot = telebot.TeleBot(config.TOKEN2)
    owm = pyowm.OWM(config.TOKEN3, language = "ru")
    #covid19 = COVID19Py.COVID19()
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

        item1 = types.KeyboardButton('📅 Время')
        item2 = types.KeyboardButton('🏠 Домой')
        item3= types.KeyboardButton('⛅️Погода')
        item4 = types.KeyboardButton('🏫 На учебу')
        item5 = types.KeyboardButton('🔮 Гороскоп')

        markup.add(item5,item3)
        markup.add(item4,item2)

        bot.send_message(message.chat.id,
                         f"{random.choice(hello)}" + ", {0.first_name}!\nЯ - <b>Помошник</b>, бот созданный, чтобы упростить жизнь ".format(
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
            if call.data == 'Skorpion': #Гороскоп про скорпиона
                numbers = [1, 2, 3, 4, 5]
                ic = datetime.datetime.now(tz=None)
                date_time = ic.strftime("%d")
                colors = ["Красный", "Оранжевый", "Желтый", "Бежевый", "Серый", "Зеленый", "Синий", "Фиолетовый", "Белый",
                          "Коричневый", "Черный", "Розовый","Orange",'Black',"White"]
                Object = ["Карточка", "Ручка", "Карандаш", "Пенал", "Носочки", "Футболка", "Рубашка", "Цепочка", "Кольцо",
                          "Ключи", "Зарядка", "Наушнии", "Тетрадь", "Кружка", "Браслет", "Очки", "Антистресс", "Свеча",
                          "Кофе", "Чай","Зеркало","Фрукты","Овощи","Кофта","Телефон","Ноутбук","Маска","Часы","Ожерелье","Кулон","Гель для рук"]
                quotes = ["Never look back", "A life is a moment", "All we need is love", "Enjoy every moment",
                          "Follow your heart", "Live without regrets", "Live for yourself", "Strive for greatness",
                          "Work hard. Dream big", "Be a voice not an echo", "You are your only limit", "Let it be",
                          "Money often costs too much", "Cherish the moments", "Imagination rules the world",
                          "Do something with passion or not it all", "Illusion is the first of all pleasures",
                          "better to have ideals and dreams than nothing", "Only my dream keeps me alive",
                          "loyal to the one who is loyal to you", "Everything happens for a reason",
                          "If you never try you will never know", "It’s never too late to be what you might have been",
                          "Some people are poor, all they have is money","I am туть ^^","Be careful what you eat", "Don’t be afraid to experiment/try new things",
                          "Be careful not to upset or lose someone you love",
                          "Don’t lend money to friends or family",
                          "The problem can be overcome through open, honest dialogue",
                          "I love you, Kate!"]

                advice_1 = ["You may be exposed to a new vision of your future today, and one that you had not previously considered. Your partner may have quite a surprise in store for you. Not only do they want the relationship to continue to grow, they also want you both to do something very new and quite exciting together. Whatever it is, you will be thrilled.",
                            "If you've put in your time and done your homework, this day can prove very rewarding, Scorpio. Watch out for incredible opportunities hiding nearby. You have a great deal of physical energy today, although you may find it erratic and a bit out of control. Break free of anything that seems to be binding you. Shed the chains and live the way you want to live.",
                            "You are willing to commit to a certain extent, but yet you are hesitant to commit all the way. Don't be. Now is the time to do something with great confidence. Either pursue this idea with everything you've got, or don't pursue it at all.",
                            "As you take charge of your health, you may feel at times that there is a bit too much to keep track of! Diet, routine, exercise, illness, sleep - and everything else that is involved with this thing called 'self-love.' This is why you have friends. Your friends can help you assess your situation and figure out the best course of action. Sometimes laughing away the tension is all you really need!",
                            "You might have the chance to speak with new people in interesting fields, perhaps from foreign lands, Scorpio. Your conversational abilities are at an all-time high, so you'll not only enjoy talking with everyone, but they'll enjoy talking with you, too. Intriguing ideas and useful information could have your mind buzzing all night. Try to take a walk in the evening to clear your head.",
                            "Conversation today may not be at its most witty and sparkling, but you will nevertheless make quite a lot of progress romantically. The person you have set your sights on may not be the most talkative you have met, but they do have many other qualities that you intend to take seriously. You will probably make an impression if you behave calmly and considerately.",
                            "For every pharmaceutical treatment, there is a holistic way to take care of yourself! Pay attention to where you get your knowledge regarding wellness. Do you rely on what your parents taught you? (How is their health?) Do you believe what's written on all the packaging you buy? Do you have a friend or two who seem 'tuned in' to holistic health care practices? Open yourself to receiving knowledge from new sources and notice the healthy difference it can make in your life.",
                            "There is so much sensitivity in you. You may feel that peace is all you need to be happy, and be heartbroken to see what is going on in the world. Try giving yourself peace as much and as often as you can: peace in the bathtub, peace at the dinner table, and peace in bed. Learn to require in your own life what you want to see in the world. Drawing that power up in yourself will give you focus and ground you. Exercise is the mainstay of this dream.",
                            "Thanks to the day's planetary configuration, you will intuitively sense the state of world affairs. This aspect sends messages of brotherly love, and in many cases, meets with resistance. Give yourself the benefit of a healthy lifestyle during this critical time in the human story. A healthy lifestyle includes plenty of rest because an overactive mind can take you away from the basics. Rest, diet, and exercise should be your mantra during trying times.",
                            "This is a day of fresh beginnings for you, Scorpio. Accomplishments in the past foster a new sense of self-confidence, along with optimism and enthusiasm for the future. Travel lies ahead in the distant future, and possibly advancing your education in some way. Romance also looks promising. Go for a facial or massage today, if possible, or buy some new clothes. Start the new cycle by making your appearance match what you feel inside.",
                            "Something you might have wanted to keep between you and a few trusted friends could inadvertently be revealed, perhaps to the wrong people. Frustration and a sense of betrayal could plague you, but don't turn against those who knew. Even though this can be disconcerting, you can learn from it. Benjamin Franklin said, 'Two people can keep a secret only when one of them is dead.'",
                            "This is a time when you're likely to feel especially idealistic and hopeful. Spiritual experiences may have you on cloud nine, Scorpio. Your intuition is also strong. You might consider taking a future trip to a distant state or foreign country, perhaps one associated with a great spiritual tradition. Wait a day or two and talk it over with friends before making any specific arrangements.",
                            "Crazy as it seems, why not plan that trip you've been eager to go on, Scorpio? Adventure calls, and although there are a few obstacles to stop you from answering, you can’t wait to get out of your rut. There is a great big world out there, and you can’t wait to make the time to go and see some of it!",
                            "Today you're likely to experience a powerful burst of energy that may temporarily turn you into a workaholic. Chores may have piled up around the house that desperately need to be done. You may want to go through them like wildfire. You don't have to do them all at once. Take care of the most pressing tasks and then relax. The rest can wait. Ask family members to help.",
                            "Today you could be feeling warm and friendly toward everyone. You might be involved in virtual social events or receive invitations to future parties. You'll probably have a great time and make some new friends. Take care to take lots of vitamin C. There could be colds or other bugs flying around and you could be more susceptible to such infections at this time.",
                            "There could be some restrictions on your emotions today, Scorpio. You'll find that a practical, grounded force is working against your intuitive understanding of whatever issue concerns you. Do your best to anchor yourself in the truth before you scatter seeds of erratic emotions all over the place. It's important for you to maintain stability at all times.",
                            "Today, Scorpio, you might turn to practices like meditation or psychic development. Some vivid dreams over the past few days may have brought up personal issues that you need to clear up in order to progress. You may pick up on the thoughts and feelings of others more strongly than usual. If you've been thinking about learning to read tarot cards or runes, this is the day to start.",
                            "Emotions could be intense at work today as important projects approach their deadlines, Scorpio. You may put in more time than usual. Tempers might flare and co-workers clash, so stay calm and keep going. On the positive side, the financial and recognition payoffs for whatever you accomplish today should prove well worth the effort.",
                            "You may be feeling a bit on edge today, Scorpio. Your self-confidence is shaky and you may feel in need of new challenges. The tedious tasks you have in front of you don't inspire your imagination or creativity. Do what you can to get through this difficult day. Be extra kind to yourself by indulging in a good lunch or listening to classical music.",
                            "There's tension in the air today, Scorpio, and you might be restless and anxious to start something. There is plenty of energy around to feed you, but the trick is to make sure that you're doing things for the right reasons. Don't do things out of guilt, fear, or regret. Keep on the best path for the best reasons for the best results.",
                            "Scorpio, you're usually more outwardly directed, but today you might break that pattern. You could be in a contemplative mood and wondering about everything from metaphysics to philosophy to money to your future. You're basically feeling positive about life, but you might be at a crossroads now. It may take some serious thought before you decide which direction to go. Give yourself some time.",
                            "Financial worries might come up today, Scorpio. You may check your bank balance and find that you have little money. This might come as a shock, because you thought there was plenty there. Before you panic, ask whoever's in charge at the bank to double-check the records. It's probably a computer error. It shouldn't take long to correct, and you'll be able to breathe a sigh of relief.",
                            "There's an incredibly expansive feeling in the air that you should latch onto, Scorpio. Things are moving rapidly. You'll find long-term trends come together quite well. The thing to be aware of today is making sure you're operating based on facts you know to be true. Check your sources. Be cautious, but if you see an opportunity that looks good, run with it.",
                            "Today's a good day to check into advancing your career or education, Scorpio. The energy favors expansion and growth. When was the last time you learned a new skill? It doesn't have to be work related, either. If arranging flowers, skydiving, or programming websites is something that appeals to you, go for it. Never stop looking for ways to expand your knowledge.",
                            "If you've been feeling tired or sick lately, this will probably turn around for you today, Scorpio. Bouts of moodiness can be a real drain. Your emotional state has a pronounced effect on the way your body feels. Be sure to take care of your feelings as well as your body. If there are things that need to be worked out, do that now. The two really do go together.",
                            "Working within boundaries and restrictions could get to you today, Scorpio. Yours is an independent spirit, and your best achievements are often born of doing things your own way. Like it or not, we all have to follow rules. Finish what needs to be done. Afterward, you may find more freedom to act independently without consequences. Exercise patience and diligence as needed.",
                            "Continued success and good luck should have you feeling charged up to move ahead with plans and ideas. Your energy and enthusiasm are high, Scorpio. You're likely thinking about expanding your horizons, perhaps through travel or education. You should definitely give these serious thought. Plan carefully and take care not to move before the time is right.",
                            "Your heart has been active, Scorpio, and you're probably feeling the need to take charge of a certain relationship. Instead of being too hasty in your pursuit of this romance, you should probably do more planning. Look at the situation from a long-term perspective and see if the partnership is heading the way you want it to, based on how things are moving now. It could be that you're jumping ahead of the game.",
                            "Be yourself today - 100 percent you, Scorpio. The world needs more individuality. Revel in your unique qualities and be generous about sharing them with the world. Feel free to adopt a new and unconventional way of doing something - anything. Beware, however, that there may be a strong, grounding force that's trying to tie you down to tradition. Don't feel pressured to give in to the social norm.",
                            "There's a great deal of fuel to keep your fire raging today, Scorpio. Powerful situations are apt to come your way in which you're asked to take decisive action. Don't shy away from added responsibility. Your ego is very strong, which helps you take charge of any situation. Just make sure that you don't step on anyone's toes in the process.",
                            "There's a great deal of fuel to keep your fire raging today, Scorpio. Powerful situations are apt to come your way in which you're asked to take decisive action. Don't shy away from added responsibility. Your ego is very strong, which helps you take charge of any situation. Just make sure that you don't step on anyone's toes in the process.",
                            "Today is your day to dream and dream big, Scorpio. Think about what it is that you want most out of life. Aim your arrow to the stars and pull back your bow as far as possible. There's no limit to how far you can go. Your only limitation is your imagination. Don't worry if your plan doesn't seem to make any rational sense. Worry more about what you want and less about how you're going to get it."]


                bot.send_message(call.message.chat.id,
                                 f"♏Scorpio:\n{str(quotes[int(date_time)])}.\n✅ {str(colors[(int(date_time)// 2)])}\n✅ {str(Object[(int(date_time))])}"
                                 f"\n\n" + advice_1[int(date_time)]+"\n💰: " + random.choice(numbers) * "⭐" + f"\n❣: " + random.choice(
                                     numbers) * "⭐" + f"\n🏢: " + random.choice(numbers) * "⭐" + f"\n💊: " + random.choice(
                                     numbers) * "⭐")

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= call.message.text,
                                  reply_markup='')
            elif call.data == 'Oven':
                numbers = [1, 2, 3, 4, 5]
                ic = datetime.datetime.now(tz=None)
                date_time = ic.strftime("%d")
                colors = ["Красный", "Оранжевый", "Желтый", "Бежевый", "Серый", "Зеленый", "Синий", "Фиолетовый", "Белый",
                          "Коричневый", "Черный", "Розовый", "Orange", 'Black', "White"]
                Object = ["Карточка", "Ручка", "Карандаш", "Пенал", "Носочки", "Футболка", "Рубашка", "Цепочка", "Кольцо",
                          "Ключи", "Зарядка", "Наушнии", "Тетрадь", "Кружка", "Браслет", "Очки", "Антистресс", "Свеча",
                          "Кофе", "Чай", "Зеркало", "Фрукты", "Овощи", "Кофта", "Телефон", "Ноутбук", "Маска", "Часы",
                          "Ожерелье", "Кулон", "Гель для рук"]
                quotes = ["Never look back", "A life is a moment", "All we need is love", "Enjoy every moment",
                          "Follow your heart", "Live without regrets", "Live for yourself", "Strive for greatness",
                          "Work hard. Dream big", "Be a voice not an echo", "You are your only limit", "Let it be",
                          "Money often costs too much", "Cherish the moments", "Imagination rules the world",
                          "Do something with passion or not it all", "Illusion is the first of all pleasures",
                          "better to have ideals and dreams than nothing", "Only my dream keeps me alive",
                          "loyal to the one who is loyal to you", "Everything happens for a reason",
                          "If you never try you will never know", "It’s never too late to be what you might have been",
                          "Some people are poor, all they have is money", "I am туть ^^", "Be careful what you eat",
                          "Don’t be afraid to experiment/try new things",
                          "Be careful not to upset or lose someone you love",
                          "Don’t lend money to friends or family",
                          "The problem can be overcome through open, honest dialogue",
                          "I love you, Kate!"]

                advice_1 = [
                    "You may be exposed to a new vision of your future today, and one that you had not previously considered. Your partner may have quite a surprise in store for you. Not only do they want the relationship to continue to grow, they also want you both to do something very new and quite exciting together. Whatever it is, you will be thrilled.",
                    "If you've put in your time and done your homework, this day can prove very rewarding, Scorpio. Watch out for incredible opportunities hiding nearby. You have a great deal of physical energy today, although you may find it erratic and a bit out of control. Break free of anything that seems to be binding you. Shed the chains and live the way you want to live.",
                    "You are willing to commit to a certain extent, but yet you are hesitant to commit all the way. Don't be. Now is the time to do something with great confidence. Either pursue this idea with everything you've got, or don't pursue it at all.",
                    "As you take charge of your health, you may feel at times that there is a bit too much to keep track of! Diet, routine, exercise, illness, sleep - and everything else that is involved with this thing called 'self-love.' This is why you have friends. Your friends can help you assess your situation and figure out the best course of action. Sometimes laughing away the tension is all you really need!",
                    "You might have the chance to speak with new people in interesting fields, perhaps from foreign lands, Scorpio. Your conversational abilities are at an all-time high, so you'll not only enjoy talking with everyone, but they'll enjoy talking with you, too. Intriguing ideas and useful information could have your mind buzzing all night. Try to take a walk in the evening to clear your head.",
                    "Conversation today may not be at its most witty and sparkling, but you will nevertheless make quite a lot of progress romantically. The person you have set your sights on may not be the most talkative you have met, but they do have many other qualities that you intend to take seriously. You will probably make an impression if you behave calmly and considerately.",
                    "For every pharmaceutical treatment, there is a holistic way to take care of yourself! Pay attention to where you get your knowledge regarding wellness. Do you rely on what your parents taught you? (How is their health?) Do you believe what's written on all the packaging you buy? Do you have a friend or two who seem 'tuned in' to holistic health care practices? Open yourself to receiving knowledge from new sources and notice the healthy difference it can make in your life.",
                    "There is so much sensitivity in you. You may feel that peace is all you need to be happy, and be heartbroken to see what is going on in the world. Try giving yourself peace as much and as often as you can: peace in the bathtub, peace at the dinner table, and peace in bed. Learn to require in your own life what you want to see in the world. Drawing that power up in yourself will give you focus and ground you. Exercise is the mainstay of this dream.",
                    "Thanks to the day's planetary configuration, you will intuitively sense the state of world affairs. This aspect sends messages of brotherly love, and in many cases, meets with resistance. Give yourself the benefit of a healthy lifestyle during this critical time in the human story. A healthy lifestyle includes plenty of rest because an overactive mind can take you away from the basics. Rest, diet, and exercise should be your mantra during trying times.",
                    "This is a day of fresh beginnings for you, Scorpio. Accomplishments in the past foster a new sense of self-confidence, along with optimism and enthusiasm for the future. Travel lies ahead in the distant future, and possibly advancing your education in some way. Romance also looks promising. Go for a facial or massage today, if possible, or buy some new clothes. Start the new cycle by making your appearance match what you feel inside.",
                    "Something you might have wanted to keep between you and a few trusted friends could inadvertently be revealed, perhaps to the wrong people. Frustration and a sense of betrayal could plague you, but don't turn against those who knew. Even though this can be disconcerting, you can learn from it. Benjamin Franklin said, 'Two people can keep a secret only when one of them is dead.'",
                    "This is a time when you're likely to feel especially idealistic and hopeful. Spiritual experiences may have you on cloud nine, Scorpio. Your intuition is also strong. You might consider taking a future trip to a distant state or foreign country, perhaps one associated with a great spiritual tradition. Wait a day or two and talk it over with friends before making any specific arrangements.",
                    "Crazy as it seems, why not plan that trip you've been eager to go on, Scorpio? Adventure calls, and although there are a few obstacles to stop you from answering, you can’t wait to get out of your rut. There is a great big world out there, and you can’t wait to make the time to go and see some of it!",
                    "Today you're likely to experience a powerful burst of energy that may temporarily turn you into a workaholic. Chores may have piled up around the house that desperately need to be done. You may want to go through them like wildfire. You don't have to do them all at once. Take care of the most pressing tasks and then relax. The rest can wait. Ask family members to help.",
                    "Today you could be feeling warm and friendly toward everyone. You might be involved in virtual social events or receive invitations to future parties. You'll probably have a great time and make some new friends. Take care to take lots of vitamin C. There could be colds or other bugs flying around and you could be more susceptible to such infections at this time.",
                    "There could be some restrictions on your emotions today, Scorpio. You'll find that a practical, grounded force is working against your intuitive understanding of whatever issue concerns you. Do your best to anchor yourself in the truth before you scatter seeds of erratic emotions all over the place. It's important for you to maintain stability at all times.",
                    "Today, Scorpio, you might turn to practices like meditation or psychic development. Some vivid dreams over the past few days may have brought up personal issues that you need to clear up in order to progress. You may pick up on the thoughts and feelings of others more strongly than usual. If you've been thinking about learning to read tarot cards or runes, this is the day to start.",
                    "Emotions could be intense at work today as important projects approach their deadlines, Scorpio. You may put in more time than usual. Tempers might flare and co-workers clash, so stay calm and keep going. On the positive side, the financial and recognition payoffs for whatever you accomplish today should prove well worth the effort.",
                    "You may be feeling a bit on edge today, Scorpio. Your self-confidence is shaky and you may feel in need of new challenges. The tedious tasks you have in front of you don't inspire your imagination or creativity. Do what you can to get through this difficult day. Be extra kind to yourself by indulging in a good lunch or listening to classical music.",
                    "There's tension in the air today, Scorpio, and you might be restless and anxious to start something. There is plenty of energy around to feed you, but the trick is to make sure that you're doing things for the right reasons. Don't do things out of guilt, fear, or regret. Keep on the best path for the best reasons for the best results.",
                    "Scorpio, you're usually more outwardly directed, but today you might break that pattern. You could be in a contemplative mood and wondering about everything from metaphysics to philosophy to money to your future. You're basically feeling positive about life, but you might be at a crossroads now. It may take some serious thought before you decide which direction to go. Give yourself some time.",
                    "Financial worries might come up today, Scorpio. You may check your bank balance and find that you have little money. This might come as a shock, because you thought there was plenty there. Before you panic, ask whoever's in charge at the bank to double-check the records. It's probably a computer error. It shouldn't take long to correct, and you'll be able to breathe a sigh of relief.",
                    "There's an incredibly expansive feeling in the air that you should latch onto, Scorpio. Things are moving rapidly. You'll find long-term trends come together quite well. The thing to be aware of today is making sure you're operating based on facts you know to be true. Check your sources. Be cautious, but if you see an opportunity that looks good, run with it.",
                    "Today's a good day to check into advancing your career or education, Scorpio. The energy favors expansion and growth. When was the last time you learned a new skill? It doesn't have to be work related, either. If arranging flowers, skydiving, or programming websites is something that appeals to you, go for it. Never stop looking for ways to expand your knowledge.",
                    "If you've been feeling tired or sick lately, this will probably turn around for you today, Scorpio. Bouts of moodiness can be a real drain. Your emotional state has a pronounced effect on the way your body feels. Be sure to take care of your feelings as well as your body. If there are things that need to be worked out, do that now. The two really do go together.",
                    "Working within boundaries and restrictions could get to you today, Scorpio. Yours is an independent spirit, and your best achievements are often born of doing things your own way. Like it or not, we all have to follow rules. Finish what needs to be done. Afterward, you may find more freedom to act independently without consequences. Exercise patience and diligence as needed.",
                    "Continued success and good luck should have you feeling charged up to move ahead with plans and ideas. Your energy and enthusiasm are high, Scorpio. You're likely thinking about expanding your horizons, perhaps through travel or education. You should definitely give these serious thought. Plan carefully and take care not to move before the time is right.",
                    "Your heart has been active, Scorpio, and you're probably feeling the need to take charge of a certain relationship. Instead of being too hasty in your pursuit of this romance, you should probably do more planning. Look at the situation from a long-term perspective and see if the partnership is heading the way you want it to, based on how things are moving now. It could be that you're jumping ahead of the game.",
                    "Be yourself today - 100 percent you, Scorpio. The world needs more individuality. Revel in your unique qualities and be generous about sharing them with the world. Feel free to adopt a new and unconventional way of doing something - anything. Beware, however, that there may be a strong, grounding force that's trying to tie you down to tradition. Don't feel pressured to give in to the social norm.",
                    "There's a great deal of fuel to keep your fire raging today, Scorpio. Powerful situations are apt to come your way in which you're asked to take decisive action. Don't shy away from added responsibility. Your ego is very strong, which helps you take charge of any situation. Just make sure that you don't step on anyone's toes in the process.",
                    "There's a great deal of fuel to keep your fire raging today, Scorpio. Powerful situations are apt to come your way in which you're asked to take decisive action. Don't shy away from added responsibility. Your ego is very strong, which helps you take charge of any situation. Just make sure that you don't step on anyone's toes in the process.",
                    "Today is your day to dream and dream big, Scorpio. Think about what it is that you want most out of life. Aim your arrow to the stars and pull back your bow as far as possible. There's no limit to how far you can go. Your only limitation is your imagination. Don't worry if your plan doesn't seem to make any rational sense. Worry more about what you want and less about how you're going to get it."]

                bot.send_message(call.message.chat.id,
                                 f"♈️Aries:\n{str(random.choice(quotes))}.\n✅ {str(random.choice(colors))}\n✅ {str(random.choice(Object))}"
                                 f"\n\n" + str(random.choice(advice_1)) + "\n💰: " + random.choice(
                                     numbers) * "⭐" + f"\n❣: " + random.choice(
                                     numbers) * "⭐" + f"\n🏢: " + random.choice(numbers) * "⭐" + f"\n💊: " + random.choice(
                                     numbers) * "⭐")

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=call.message.text,
                                      reply_markup='')
        except Exception:
            bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
    @bot.message_handler(content_types = ['text'])
    def main(message): #Отвечает за кнопки на клавиатуре
            print(message.from_user)
            #528178987 - Катя
            #1005179687 - Дима
        #try:
            if message.chat.type == 'private':
                if message.text == '📅 Время':
                    try:
                        date2 = datetime.datetime(2020, 7, 8)
                        ic = datetime.datetime.now().isocalendar()
                        b = 'Числитель' if ic[1] % 2 != 0 else 'Знаменатель'
                        date_time = datetime.datetime.now(tz = None)
                        date_t = date2 - date_time
                        bot.reply_to(message, "Сейчас:  " + date_time.strftime("%d-%m-%Y %H:%M") + f" - {b}" )
                        #bot.reply_to(message, f"До сессии: {str(date_t.days)} дней\nСейчас: {b}")
                    except Exception:
                        bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
                elif message.text == '🔮 Гороскоп':
                    keyboard = types.InlineKeyboardMarkup()
                    key_yes = types.InlineKeyboardButton(text='Скорпион', callback_data='Skorpion')
                    key_no = types.InlineKeyboardButton(text="Овен", callback_data='Oven')
                    keyboard.add(key_no,key_yes)
                    bot.send_message(message.chat.id, 'По какому знаку показать гороскоп?:', reply_markup=keyboard)
                elif message.text == ('До новой жизни') or message.text == ('новой жизни') or message.text == ('Новой жизни') or message.text == ('Новая жизнь') or message.text == ('родина') or message.text == ('30') or message.text ==('🏠 Домой') or message.text == ('До дома') or message.text == ('до дома') or message.text == ('Домой') or message.text == ('Новая') or message.text == ('Родина') or message.text == ('Водстрой') or message.text == ('Дом'):
                    week = datetime.datetime.now().isocalendar() #Год, неделя, день посчету
                    if week[2] != 6 and week [2] != 7:
                        otpr = "Дурак"
                        otpr_next = otpr
                        otpr2 = otpr
                        otpr_next_1 = otpr
                        otpr_siti = otpr
                        otpr_next_2 = otpr
                        #Расписание автобусов  с ЖД вокзала:
                        Zhd_Vokzal_30 = [24000,27000,28800,31200,33000,35400,37200,39600,43200,44400,52200,55200,56400,58500,60000,61800,63600,65400,69000,73800]
                        Siti_Mol = [24900,27000,31800,35400,38400,42000,44400,48000,53400,59400,62400,66000,68400,72600]
                        #ic = time.mktime(datetime.datetime.now(tz = None).timetuple()) #Время в секундах
                        Zhd_Vokzal_30a = [26400,30000,38100,40800,44400,49500,53100,57300,62400,66000,70200,72600]
                        ic = datetime.datetime.now(tz = None)
                        #Переводим в секунды текущее время
                        sec = 3600 * int(ic.strftime("%H")) + 60 * int (ic.strftime("%M")) + int(ic.strftime("%S"))
                        for i in range(0,len(Zhd_Vokzal_30)):
                            if sec <= Zhd_Vokzal_30[i]:
                                secon = int(Zhd_Vokzal_30 [i])
                                otpr = datetime.timedelta(seconds = secon)
                                if i < int(len(Zhd_Vokzal_30)-1):
                                    secon_next = int(Zhd_Vokzal_30[i+1])
                                    otpr_next = datetime.timedelta(seconds = secon_next)
                                break
                            else:
                                continue
                        for i in range(0,len(Zhd_Vokzal_30a)):
                            if sec <= Zhd_Vokzal_30a[i]:
                                secon = int(Zhd_Vokzal_30a [i])
                                otpr2 = datetime.timedelta(seconds = secon)
                                if i < int(len(Zhd_Vokzal_30a)-1):
                                    secon_next_1 = int(Zhd_Vokzal_30a[i+1])
                                    otpr_next_1 = datetime.timedelta(seconds = secon_next_1)
                                break
                            else:
                                continue
                        for i in range(0,len(Siti_Mol)):
                            if sec <= Siti_Mol[i]:
                                secon = int(Siti_Mol[i])
                                otpr_siti = datetime.timedelta(seconds = secon)
                                if i < int(len(Siti_Mol)-1):
                                    secon_next_2 = int(Siti_Mol[i+1])
                                    otpr_next_2 = datetime.timedelta(seconds = secon_next_2)
                                break
                            else:
                                continue
                        bot.send_message(message.chat.id,
                                         f'<b>🚂 С ЖД вокзала:</b>\n<b>🚌 Автобус</b> №30\n<b>⌚️Время отправления</b> - {str(otpr)[:5]}\n<b>🔜Следующий - </b>{str(otpr_next)[:5]}\n\n<b>🚎 Автобус</b> №30A\n<b>⌚️Время отправления</b> - {str(otpr2)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_1)[:5]} \n\n<b>🏪 С СитиМолла:</b>   '
                                         f'\n<b>🚍 Автобус</b> №47\n<b>⌚️Время отправления</b> - {str(otpr_siti)[:5]}\n<b>🔜Следующий - </b>{str(otpr_next_2)[:5]} ',
                                         parse_mode='html')

                    elif int(week[2]) == 6: #Выходные
                        otpr = "Дурак"
                        otpr_next = otpr
                        otpr2 = otpr
                        otpr_next_1 = otpr
                        otpr_siti = otpr
                        otpr_next_2 = otpr
                        Zhd_Vokzal_30 = [24000,27000,28800,31200,33000,35400,37200,39600,43200,48600,52200,55200,56400,58500,60000,61800,63600,65400,69000,73800]
                        Siti_Mol = [27000,35400,42000,48000,62400,68400]
                        #ic = time.mktime(datetime.datetime.now(tz = None).timetuple()) #Время в секундах
                        Zhd_Vokzal_30a = [30000,38100,49500,57300,66000,72600]
                        ic = datetime.datetime.now(tz = None)

                        #Переводим в секунды текущее время
                        sec = 3600 * int(ic.strftime("%H")) + 60 * int (ic.strftime("%M")) + int(ic.strftime("%S"))

                        for i in range(0,len(Zhd_Vokzal_30)):
                            #print(i)
                            #print(i, ' ', int(len(Zhd_Vokzal_30)))
                            if sec <= Zhd_Vokzal_30[i]:
                                #print(i)
                                secon = int(Zhd_Vokzal_30 [i])
                                otpr = datetime.timedelta(seconds = secon)
                                if i < int(len(Zhd_Vokzal_30)-1):
                                    #print(i,' ',int(len(Zhd_Vokzal_30)))
                                    secon_next = int(Zhd_Vokzal_30[i+1])
                                    otpr_next = datetime.timedelta(seconds = secon_next)
                                break
                            else:
                                continue
                        #print(i)
                        for i in range(0,len(Zhd_Vokzal_30a)):
                            #print(i)
                            if sec <= Zhd_Vokzal_30a[i]:
                                #print('a-30a')
                                secon = int(Zhd_Vokzal_30a [i])
                                otpr2 = datetime.timedelta(seconds = secon)
                                if i < int(len(Zhd_Vokzal_30a)-1):

                                    secon_next_1 = int(Zhd_Vokzal_30a[i+1])
                                    otpr_next_1 = datetime.timedelta(seconds = secon_next_1)
                                break
                            else:
                                continue
                        #print('a')
                        for i in range(0,len(Siti_Mol)):
                            if sec <= Siti_Mol[i]:
                                secon = int(Siti_Mol[i])
                                otpr_siti = datetime.timedelta(seconds = secon)
                                if i < int(len(Siti_Mol)-1):
                                    secon_next_2 = int(Siti_Mol[i+1])
                                    otpr_next_2 = datetime.timedelta(seconds = secon_next_2)
                                break
                            else:
                                continue
                        #print('a')
                        bot.send_message(message.chat.id,
                                         f'<b>🚂 С ЖД вокзала:</b>\n<b>🚌 Автобус</b> №30\n<b>⌚️Время отправления</b> - {str(otpr)[:5]}\n<b>🔜Следующий - </b>{str(otpr_next)[:5]}\n\n<b>🚎 Автобус</b> №30A\n<b>⌚️Время отправления</b> - {str(otpr2)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_1)[:5]} \n\n<b>🏪 С СитиМолла:</b>   '
                                         f'\n<b>🚍 Автобус</b> №47\n<b>⌚️Время отправления</b> - {str(otpr_siti)[:5]}\n<b>🔜Следующий - </b>{str(otpr_next_2)[:5]} ',
                                         parse_mode='html')



                    else: #Выходные
                        otpr = "Дурак"
                        otpr_next = otpr
                        otpr2 = otpr
                        otpr_next_1 = otpr
                        otpr_siti = otpr
                        otpr_next_2 = otpr
                        Zhd_Vokzal_30 = [27000,31200,35400,39600,43200,55800,60000,64800,68400,73800]
                        Siti_Mol = [27000,35400,42000,48000,62400,68400]
                        #ic = time.mktime(datetime.datetime.now(tz = None).timetuple()) #Время в секундах
                        Zhd_Vokzal_30a = [33000,53100,62400,70200]
                        ic = datetime.datetime.now(tz = None)
                        #Переводим в секунды текущее время
                        sec = 3600 * int(ic.strftime("%H")) + 60 * int (ic.strftime("%M")) + int(ic.strftime("%S"))
                        for i in range(0,len(Zhd_Vokzal_30)):
                            if sec <= Zhd_Vokzal_30[i]:
                                secon = int(Zhd_Vokzal_30 [i])
                                otpr = datetime.timedelta(seconds = secon)
                                if i < int(len(Zhd_Vokzal_30)-1):
                                    secon_next = int(Zhd_Vokzal_30[i+1])
                                    otpr_next = datetime.timedelta(seconds = secon_next)
                                break
                            else:
                                continue
                        for i in range(0,len(Zhd_Vokzal_30a)):
                            if sec <= Zhd_Vokzal_30a[i]:
                                secon = int(Zhd_Vokzal_30a [i])
                                otpr2 = datetime.timedelta(seconds = secon)
                                if i < int(len(Zhd_Vokzal_30a)-1):
                                    secon_next_1 = int(Zhd_Vokzal_30a[i+1])
                                    otpr_next_1 = datetime.timedelta(seconds = secon_next_1)
                                break
                            else:
                                continue
                        for i in range(0,len(Siti_Mol)):
                            if sec <= Siti_Mol[i]:
                                secon = int(Siti_Mol[i])
                                otpr_siti = datetime.timedelta(seconds = secon)
                                if i < int(len(Siti_Mol)-1):
                                    secon_next_2 = int(Siti_Mol[i+1])
                                    otpr_next_2 = datetime.timedelta(seconds = secon_next_2)
                                break
                            else:
                                continue
                        bot.send_message(message.chat.id,
                                         f'<b>🚂 С ЖД вокзала:</b>\n<b>🚌 Автобус</b> №30\n<b>⌚️Время отправления</b> - {str(otpr)[:5]}\n<b>🔜Следующий - </b>{str(otpr_next)[:5]}\n\n<b>🚎 Автобус</b> №30A\n<b>⌚️Время отправления</b> - {str(otpr2)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_1)[:5]} \n\n<b>🏪 С СитиМолла:</b>   '
                                         f'\n<b>🚍 Автобус</b> №47\n<b>⌚️Время отправления</b> - {str(otpr_siti)[:5]}\n<b>🔜Следующий - </b>{str(otpr_next_2)[:5]} ',
                                         parse_mode='html')
                        #Переводим секунды в часы
                elif message.text == ('До учебы') or message.text == ('🏫 На учебу') or message.text == ('на учебу') or message.text == ('До родины') or message.text == ('До водстроя') or message.text == ('Каштановая') or message.text == ('до водстроя') or message.text ==('центр') or message.text == ('C новой жизни') or message.text == ('с новой жизни') or message.text == ('С Новой жизни') or message.text == ('До Белгу') or message.text == ('Белгу') or message.text == ('До белгу') or message.text == ('Учеба'):
                        #Расписание автобусов  к ЖД вокзалу:
                    week = datetime.datetime.now().isocalendar()
                    if week[2] != 6 and week [2] != 7:
                        otpr = "Дурак"
                        #otpr_next = otpr
                        #otpr2 = otpr
                        otpr_next_1 = otpr
                        otpr_siti = otpr
                        otpr_next_2 = otpr
                        otpr_a30=otpr
                        otpr_next_3 = otpr

                        Rodina = [22200,25200,26400,28800,30600,33000,34800,37200,39000,41400,45000,50400,54000,57000,58200,60000,61800,63600,65400,67200,71400,75000]
                        Vodstroi = [22800,24900,27300,30300,36000,39000,41400,45000,50400,56400,59400,62400,65400,69000]
                        a30 = [24600,27000,29700,32400,36000,43800,47400,50400,55200,60000,63000,68400]
                        ic = datetime.datetime.now(tz = None)
                        #Переводим в секунды текущее время
                        sec = 3600 * int(ic.strftime("%H")) + 60 * int (ic.strftime("%M")) + int(ic.strftime("%S"))
                        for i in range(0,len(Rodina)):
                            if sec <= Rodina[i]:
                                secon = int(Rodina [i])
                                otpr = datetime.timedelta(seconds = secon)
                                if i < int(len(Rodina)-1):
                                    secon_next_1 = int(Rodina[i+1])
                                    otpr_next_1 = datetime.timedelta(seconds = secon_next_1)
                                break
                            else:
                                continue
                        for i in range(0,len(Vodstroi)):
                            if sec <= Vodstroi[i]:
                                secon = int(Vodstroi[i])
                                otpr_siti = datetime.timedelta(seconds = secon)
                                if i < int(len(Vodstroi)-1):
                                    secon_next_2 = int(Vodstroi[i+1])
                                    otpr_next_2 = datetime.timedelta(seconds = secon_next_2)
                                break
                            else:
                                continue
                        for i in range(0,len(a30)):
                            if sec <= a30[i]:
                                secon = int(a30[i])
                                otpr_a30 = datetime.timedelta(seconds = secon)
                                if i < int(len(a30)-1):
                                    secon_next_3 = int(a30[i+1])
                                    otpr_next_3 = datetime.timedelta(seconds = secon_next_3)
                                break
                            else:
                                continue
                        bot.send_message(message.chat.id,
                                         f'<b>🏛 До родины:</b>\n<b>🚌 Автобус</b> №30\n<b>⌚️Время отправления</b> - {str(otpr)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_1)[:5]}\n\n<b>🚎 Автобус</b> №30A\n<b>⌚️Время отправления</b> - {str(otpr_a30)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_3)[:5]}\n\n<b>🏰 До водстроя:</b> '
                                         f'\n<b>🚎 Автобус</b> №47\n<b>⌚️Время отправления</b> - {str(otpr_siti)[:5]} \n<b>🔜Следующий -</b> {str(otpr_next_2)[:5]}',
                                         parse_mode='html')
                    elif week[2] == 6:
                        otpr = "Дурак"
                        # otpr_next = otpr
                        # otpr2 = otpr
                        otpr_next_1 = otpr
                        otpr_siti = otpr
                        otpr_next_2 = otpr

                        Rodina = [22200,25200,26400,28800,30600,33000,34800,37200,39000,41400,45000,50400,54000,57000,58200,60000,61800,63600,65400,67200,71400,75000]
                        Vodstroi = [24900,30300,39000,45000,50400,59400,65400]
                        a30 = [27000,36000,43800,55200,63000]
                        ic = datetime.datetime.now(tz = None)
                        #Переводим в секунды текущее время
                        sec = 3600 * int(ic.strftime("%H")) + 60 * int (ic.strftime("%M")) + int(ic.strftime("%S"))
                        for i in range(0,len(Rodina)):
                            if sec <= Rodina[i]:
                                secon = int(Rodina [i])
                                otpr = datetime.timedelta(seconds = secon)
                                if i < int(len(Rodina)-1):
                                    secon_next_1 = int(Rodina[i+1])
                                    otpr_next_1 = datetime.timedelta(seconds = secon_next_1)
                                break
                            else:
                                continue
                        for i in range(0,len(Vodstroi)):
                            if sec <= Vodstroi[i]:
                                secon = int(Vodstroi[i])
                                otpr_siti = datetime.timedelta(seconds = secon)
                                if i < int(len(Vodstroi)-1):
                                    secon_next_2 = int(Vodstroi[i+1])
                                    otpr_next_2 = datetime.timedelta(seconds = secon_next_2)
                                break
                            else:
                                continue
                        for i in range(0,len(a30)):
                            if sec <= a30[i]:
                                secon = int(a30[i])
                                otpr_a30 = datetime.timedelta(seconds = secon)
                                if i < int(len(a30)-1):
                                    secon_next_3 = int(a30[i+1])
                                    otpr_next_3 = datetime.timedelta(seconds = secon_next_3)
                                break
                            else:
                                continue
                        bot.send_message(message.chat.id,
                                         f'<b>🏛 До родины:</b>\n<b>🚌 Автобус</b> №30\n<b>⌚️Время отправления</b> - {str(otpr)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_1)[:5]}\n\n<b>🚎 Автобус</b> №30A\n<b>⌚️Время отправления</b> - {str(otpr_a30)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_3)[:5]}\n\n<b>🏰 До водстроя:</b> '
                                         f'\n<b>🚎 Автобус</b> №47\n<b>⌚️Время отправления</b> - {str(otpr_siti)[:5]} \n<b>🔜Следующий -</b> {str(otpr_next_2)[:5]}',
                                         parse_mode='html')
                    else:
                        otpr = "Дурак"
                        # otpr_next = otpr
                        # otpr2 = otpr
                        otpr_next_1 = otpr
                        otpr_siti = otpr
                        otpr_next_2 = otpr
                        otpr_next_3 = otpr
                        Rodina = [25200,28800,33000,37200,41400,45000,57600,62400,66600,70800,75000]
                        Vodstroi = [24900,30300,39000,45000,50400,59400,65400]
                        a30 = [31200,39600,60000,68400]
                        ic = datetime.datetime.now(tz = None)
                        #Переводим в секунды текущее время
                        sec = 3600 * int(ic.strftime("%H")) + 60 * int (ic.strftime("%M")) + int(ic.strftime("%S"))
                        for i in range(0,len(Rodina)):
                            if sec <= Rodina[i]:
                                secon = int(Rodina [i])
                                otpr = datetime.timedelta(seconds = secon)
                                if i < int(len(Rodina)-1):
                                    secon_next_1 = int(Rodina[i+1])
                                    otpr_next_1 = datetime.timedelta(seconds = secon_next_1)

                                break
                            else:
                                continue
                        for i in range(0,len(a30)):
                            if sec <= a30[i]:
                                secon = int(a30[i])
                                otpr_a30 = datetime.timedelta(seconds = secon)
                                if i < int(len(a30)-1):
                                    secon_next_3 = int(a30[i+1])
                                    otpr_next_3 = datetime.timedelta(seconds = secon_next_3)
                                break
                            else:
                                continue
                        for i in range(0,len(Vodstroi)):
                            if sec <= Vodstroi[i]:
                                secon = int(Vodstroi[i])
                                otpr_siti = datetime.timedelta(seconds = secon)
                                if i < int(len(Vodstroi)-1):
                                    secon_next_2 = int(Vodstroi[i+1])
                                    otpr_next_2 = datetime.timedelta(seconds = secon_next_2)
                                break
                            else:
                                continue
                        bot.send_message(message.chat.id,
                                         f'<b>🏛 До родины:</b>\n<b>🚌 Автобус</b> №30\n<b>⌚️Время отправления</b> - {str(otpr)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_1)[:5]}\n\n<b>🚎 Автобус</b> №30A\n<b>⌚️Время отправления</b> - {str(otpr_a30)[:5]}\n<b>🔜Следующий -</b> {str(otpr_next_3)[:5]}\n\n<b>🏰 До водстроя:</b> '
                                         f'\n<b>🚎 Автобус</b> №47\n<b>⌚️Время отправления</b> - {str(otpr_siti)[:5]} \n<b>🔜Следующий -</b> {str(otpr_next_2)[:5]}',
                                         parse_mode='html')
                elif message.text == '⛅️Погода':
                    try:
                        observation = owm.weather_at_place('Белгород')
                        w = observation.get_weather()
                        temp = w.get_temperature('celsius')['temp']
                        V = w.get_wind()
                        clothes = '🥶 Одевайся теплее' if (temp < 20 or V['speed'] > 10) else '🥵 Надевай легкую одежду'
                        bot.send_message(message.chat.id,
                                         'На улице сейчас ' + w.get_detailed_status() + '\n🌡Температура сейчас в районе ' + str(
                                             int(temp)) + ' °C\n' + '🌬Скорость ветра = ' + str(
                                             V['speed']) + ' м/с\n' + clothes)
                    except Exception:
                        bot.edit_message_text(call.message.chat.id,
                                              'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')

                        bot.send_message(message.chat.id, f'Я не знаю, что ответить, воспользуйся кнопочками (или напиши /help) {random.choice(smiles)}', reply_markup = markup)
                elif message.text == ("рандом") or message.text == ("Рандом") or message.text == ("Случайно") or message.text == ('случайно') or message.text == ("ран") or message.text == ('Ран'):
                    #bot.send_message(1005179687,'Куку')
                    bot.send_message(message.chat.id, random.randint(0,10))


        #except Exception:
            #bot.send_message(message.chat.id, f'Это что еще за покемон? {random.choice(smiles)}\nОшибка на сервер, сейчас кабанчики подскочат и порешают! {random.choice(smiles)}')
    # def games(message):
    #     bot.send_message(message.chat.id, 'Hello')
    #     bot.register_next_step_handler(message, welcome)

    bot.polling(none_stop = True)
  except Exception:
    pass
