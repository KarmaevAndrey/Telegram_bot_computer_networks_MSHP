import codecs
import telebot
from telebot import types
from t_bot_token import *

bot = telebot.TeleBot(TOKEN_HERE)

KeyboardButton_values = {"KBV_get_char_cp1251_dec": "Получение символа по номеру 10cc",
                         "KBV_get_number_cp1251_dec": "Получение номера в 10cc по символу",
                         "KBV_get_number_cp1251_bin": "Получение номера в 2cc по символу"}


TEXT_error = '  ERROR см инструкцю /help'
if __name__ == "__main__":
    for i in KeyboardButton_values:
        print(i)
