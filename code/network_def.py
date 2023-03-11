from settings import *


def get_char_cp1251_dec(dec):  # получаем символ из числа в 10сс
    try:
        return codecs.decode(bytes([dec]), 'cp1251')
    except Exception:
        return TEXT_error


def get_char_cp1251_bin(bin):  # получаем символ из числа в 2сс
    try:
        char_num = int(bin, 2)
        return codecs.decode(bytes([char_num]), 'cp1251')
    except Exception:
        return TEXT_error


def get_number_cp1251_dex(char):
    try:
        return ord(char.encode('cp1251'))
    except Exception:
        return TEXT_error


def get_number_cp1251_bin(char):
    try:
        return bin(ord(char.encode('cp1251')))
    except Exception:
        return TEXT_error

if __name__ == "__main__":
    pass
