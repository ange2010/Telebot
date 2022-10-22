import telebot
from telebot import types
import os
from fuzzywuzzy import fuzz


bot = telebot.TeleBot('5749401917:AAFHfMSnviBYrl-SbuL8Ohw5bet5Xjdpucc')
mas = []

if os.path.exists('data/boltun.txt'):
    f = open('data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if len(x.strip()) > 2:
            mas.append(x.strip().lower())
    f.close()

def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if 'u: ' in q:
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if aa > a and aa != a:
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне Привет ')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    f = open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s = answer(message.text)
    f.write('u: ' + message.text + '\n' + s + '\n')
    f.close()
    bot.send_message(message.chat.id, s)

bot.polling(none_stop=True, interval=0)

# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u> </b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text.lower() == 'привет':
#        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('project1.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Крутое фото!', parse_mode='html')
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://itproget.com'))
#     bot.send_message(message.chat.id, 'Перейдите на сайт', parse_mode='html', reply_markup=markup)
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     website = types.KeyboardButton('Веб сайт')
#     start = types.KeyboardButton('Start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

# bot.polling(none_stop=True, interval=0)
