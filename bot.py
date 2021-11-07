import telebot
import sqlite3
import cryptonator
from telebot import types
import requests


token="702816278:AAGZcJic_Nfp39Ap66XpDIGVbx5NR-qtFkI"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="RUB", callback_data="RUB"))
    keyboard.add(types.InlineKeyboardButton(text="USD", callback_data="USD"))
    keyboard.add(types.InlineKeyboardButton(text="UAH", callback_data="UAH"))

    bot.send_message(message.chat.id, "Выбери удобную для тебя валюту!", reply_markup=keyboard)

    
@bot.message_handler(regexp="Курс Биткон")
def btc(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id,currency FROM users')
    row = cursor.fetchone()
    while row is not None:
        if row[0]==message.chat.id:
            if row[1]=="RUB":
                price_btc=str(cryptonator.get_exchange_rate('btc', 'rub'))
                bot.send_message(message.chat.id,"Курс биткоин RUB: "+price_btc+".",reply_to_message_id=message.message_id)
            elif row[1]=="UAH":
                price_btc=str(cryptonator.get_exchange_rate('btc', 'UAH'))
                bot.send_message(message.chat.id,"Курс биткоин UAH: "+price_btc+".",reply_to_message_id=message.message_id)
            else:
                price_btc=str(cryptonator.get_exchange_rate('btc', 'usd'))
                bot.send_message(message.chat.id,"Курс биткоин USD: "+price_btc+".",reply_to_message_id=message.message_id)
        row = cursor.fetchone()

@bot.message_handler(regexp="Курс Лайтокин")
def ltc(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id,currency FROM users')
    row = cursor.fetchone()
    while row is not None:
        if row[0]==message.chat.id:
            if row[1]=="RUB":
                price_btc=str(cryptonator.get_exchange_rate('ltc', 'rub'))
                bot.send_message(message.chat.id,"Курс лайткоин RUB: "+price_btc+".",reply_to_message_id=message.message_id)
            elif row[1]=="UAH":
                price_btc=str(cryptonator.get_exchange_rate('ltc', 'UAH'))
                bot.send_message(message.chat.id,"Курс лайткоин UAH: "+price_btc+".",reply_to_message_id=message.message_id)
            else:
                price_btc=str(cryptonator.get_exchange_rate('ltc', 'usd'))
                bot.send_message(message.chat.id,"Курс лайткоин USD: "+price_btc+".",reply_to_message_id=message.message_id)
        row = cursor.fetchone()

@bot.message_handler(regexp="Курс евро")
def evro(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id,currency FROM users')
    row = cursor.fetchone()
    while row is not None:
        if row[0]==message.chat.id:
            if row[1]=="RUB":
                price_btc=str(cryptonator.get_exchange_rate('eur', 'rub'))
                bot.send_message(message.chat.id,"Курс евро RUB: "+price_btc+".",reply_to_message_id=message.message_id)
            elif row[1]=="UAH":
                price_btc=str(cryptonator.get_exchange_rate('eur', 'UAH'))
                bot.send_message(message.chat.id,"Курс евро UAH: "+price_btc+".",reply_to_message_id=message.message_id)
            else:
                price_btc=str(cryptonator.get_exchange_rate('eur', 'usd'))
                bot.send_message(message.chat.id,"Курс евро USD: "+price_btc+".",reply_to_message_id=message.message_id)
        row = cursor.fetchone()

@bot.message_handler(regexp="Настройки")
def settings(message):
    keyboard = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    keyboard.add(types.InlineKeyboardButton(text="RUB", callback_data="RUB"))
    keyboard.add(types.InlineKeyboardButton(text="USD", callback_data="USD"))
    keyboard.add(types.InlineKeyboardButton(text="UAH", callback_data="UAH"))
    bot.send_message(message.chat.id, "Выбери удобную для тебя валюту!", reply_markup=keyboard)

@bot.message_handler(regexp="Курс доллара")
def dollar(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id,currency FROM users')
    row = cursor.fetchone()
    while row is not None:
        if row[0]==message.chat.id:
            if row[1]=="RUB":
                price_btc=str(cryptonator.get_exchange_rate('usd', 'rub'))
                bot.send_message(message.chat.id,"Курс доллара RUB: "+price_btc+".",reply_to_message_id=message.message_id)
            elif row[1]=="UAH":
                price_btc=str(cryptonator.get_exchange_rate('usd', 'UAH'))
                bot.send_message(message.chat.id,"Курс доллара UAH: "+price_btc+".",reply_to_message_id=message.message_id)
            else:
                bot.send_message(message.chat.id,"Курс доллара USD: 1",reply_to_message_id=message.message_id)
        row = cursor.fetchone()
    conn.close()


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard=telebot.types.ReplyKeyboardMarkup()
    keyboard.row('Курс Доллара','Курс Биткон')
    keyboard.row('Курс Лайтокин','Курс Евро')
    keyboard.row('Настройки')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE  FROM users WHERE chat_id=?', (call.message.chat.id,))
    if call.data == "USD":
        bot.send_message(call.message.chat.id, text="Вы выбрали USD для просмотра курсов валют!",reply_markup=keyboard)
    elif call.data == "RUB":
        bot.send_message(call.message.chat.id, text="Вы выбрали RUB для просмотра курсов валют!",reply_markup=keyboard)
    else:
        call.data == "UAH"
        bot.send_message(call.message.chat.id, text="Вы выбрали UAH для просмотра курсов валют!",reply_markup=keyboard)
    cursor.execute("INSERT INTO users (chat_id,currency) VALUES (?,?)",(call.message.chat.id,call.data))
    conn.commit()
    conn.close()

bot.polling(none_stop=True, interval=0)
