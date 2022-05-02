#  Программа- генератор надежных паролей из цифр, заглавных и строчных букв латинского алфавита и долнительных символов.

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
freak_symbol = 'il1Lo0O'
chars = ''
password = ''


password_quantity = ''
password_length = ''
password_digit = ''
password_upper = ''
password_lower = ''
password_symbol = ''
password_freak = ''


def quantity(digit):
    while not digit.isdigit():
        digit = input('Введите, какое количество паролей необходимо сгенерировать? Используйте цифры: ')
    return int(digit)


def length(digit):
    while not digit.isdigit():
        digit = input('Введите, какое количество символов необходимо сгенерировать в пароле? Используйте цыфры. ')
    return int(digit)


def digit(answer, numbers):
    while answer not in ['д', 'н']:
        answer = input('Включать ли в пароль цифры? д/н Используйте для ответа буквы "д" и "н" ').lower()
    if answer == 'д':
        numbers += digits

    return numbers


def up_letter(answer, letters):
    while answer not in ['д', 'н']:
        answer = input('Включать ли в пароль заглавные буквы? д/н Используйте для ответа буквы "д" и "н" ').lower()
    if answer == 'д':
        letters += uppercase_letters

    return letters


def low_letter(answer, letters):
    while answer not in ['д', 'н']:
        answer = input('Включать ли в пароль строчные буквы? д/н Используйте для ответа буквы "д" и "н" ').lower()
    if answer == 'д':
        letters += lowercase_letters

    return letters


def symbols(answer, symbol):
    while answer not in ['д', 'н']:
        answer = input('Включать ли в пароль символы? д/н Используйте для ответа буквы "д" и "н" ').lower()
    if answer == 'д':
        symbol += punctuation

    return symbol


def freak(answer, symbol):
    while answer not in ['д', 'н']:
        answer = input('Включать ли в пароль неоднозначные символы? д/н Используйте для ответа буквы "д" и "н" ').lower()
    if answer == 'н':
        for element in freak_symbol:
            if element in symbol:
                symbol = symbol.replace(element, '')

    return symbol


for i in range(quantity(password_quantity)):
    password_length = length(password_length)
    chars += (digit(password_digit, chars) + up_letter(password_upper, chars) +
              low_letter(password_lower, chars) + symbols(password_symbol, chars))
    chars = freak(password_freak, chars)
    for j in range(password_length):
        password += chars[random.randint(0, len(chars))]
    print(f'Ваш пароль готов: {password}')
    password_length = ''
    chars = ''
    password = ''
