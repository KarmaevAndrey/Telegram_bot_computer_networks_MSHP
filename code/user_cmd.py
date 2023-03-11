from network_def import *


def bot_get_char_cp1251_dec(message, user_id):
    user_text = int(message.text)
    bot.send_message(user_id, f"Символ под номером {user_text} в 10cc\n -> "
                              f"<code>{get_char_cp1251_dec(user_text)}</code>",
                     parse_mode='html')


def bot_get_number_cp1251_bin(message, user_id):
    user_text = message.text
    bot.send_message(user_id, f"Номер символа {user_text} в 2cc\n"
                              f"<code>{str(get_number_cp1251_bin(user_text))[2:]}</code>",
                     parse_mode='html')

def bot_get_number_cp1251_dec(message, user_id):
    user_text = message.text
    bot.send_message(user_id, f"Номер символа {user_text} в 10cc\n"
                              f"<code>{get_number_cp1251_dex(user_text)}</code>",
                     parse_mode='html')
