import telebot
from t_bot_token import *
# Создание бота с токеном
bot = telebot.TeleBot(TOKEN_HERE)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling(none_stop=True)
