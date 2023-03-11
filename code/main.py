from user_cmd import *


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(user_id,
                     "Привет, я бот! Который поможет тебе решать задачи по сетям. /help для получения всех комманд.")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    user_id = message.from_user.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in KeyboardButton_values:
        button = telebot.types.KeyboardButton(KeyboardButton_values[i])
        keyboard.add(button)
    bot.send_message(user_id, 'Вот задачи, с которыми я могу помочь в решении, связанные с кодированием '
                              '<a href="https://t.me/help_gdz_computer_networks/3">инструкция</a>:',
                     reply_markup=keyboard, parse_mode='html', disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    try:
        user_text = message.text
        user_id = message.from_user.id
        if user_text == KeyboardButton_values["KBV_get_char_cp1251_dec"]:
            bot.send_message(user_id, "Введите символ в 10 сс (48)")
            bot.register_next_step_handler(message, bot_get_char_cp1251_dec, user_id)
        elif user_text == KeyboardButton_values["KBV_get_number_cp1251_dec"]:
            bot.send_message(user_id, "Введите символ")
            bot.register_next_step_handler(message, bot_get_number_cp1251_dec, user_id)
        elif user_text == KeyboardButton_values["KBV_get_number_cp1251_bin"]:
            bot.send_message(user_id, "Введите символ")
            bot.register_next_step_handler(message, bot_get_number_cp1251_bin, user_id)
    except Exception:
        bot.send_message(user_id, TEXT_error,
                         parse_mode='html')


bot.polling(none_stop=True)
