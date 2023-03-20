from requests import get
from telebot import TeleBot, types
from telebot.types import InlineKeyboardButton as Ib
from bs4 import BeautifulSoup as Bs

bot = TeleBot("5028563439:AAEdhKx01Bn8Xjd2jHdLkiIY5xnlWPoVZSA")


@bot.message_handler(commands=['start'])
def welcome(message): bot.send_message(message.chat.id, f"Привет,{message.chat.first_name}!\nНапиши название фильма")


def search(t, i):
    try:
        s = Bs(get(f'http://w139.zona.plus/search/{t}').text, "lxml")
        c = s.find("a", class_="results-item").get("href")
        k = types.InlineKeyboardMarkup().add(Ib(text="🍿Смотреть🍿", url=f'http://w139.zona.plus{c}'))
        bot.send_message(i, f'[ᅠ](http://w139.zona.plus{c})', parse_mode='MarkdownV2', reply_markup=k)
    except AttributeError:
        if len(t) > 1: search(t[:-1], i)


@bot.message_handler(content_types=['text'])
def group(message): search(message.text.replace(" ", "%20"), message.chat.id)


bot.polling(none_stop=True)
