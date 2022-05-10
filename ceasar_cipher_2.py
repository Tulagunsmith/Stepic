#  Программа шифратор/дешифратор шифра Цезаря. Использует русский и английский алфавиты.


code = ''
language = ''
shift = ''
text = ''
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
shift_text = ''


def intro():
    print('###################', "# CAESAR'S SIPHER #", '###################', sep='\n' )
    print()
    print('Гай Юлий Цезарь, вероятно, сильно удивился бы тому, как будет выглядеть его шифр спустя 2000 лет. И что он '
          'еще вообще выглядит.',
          'Данная программа позволит вам зашифровать или расшифровать сообщения, используя шифр '
          'римского полководца.', sep='\n')
    print()


def what_to_do(answer):
    while answer not in ['да', "нет"]:
        answer = input('Если вы хотите зашивровать сообщение, введите "да", для расшифровки введите "нет": ').lower()
    return True if answer == 'да' else False


def lang(answer):
    while answer not in {'рус', 'англ', 'ru', 'eng'}:
        answer = input('Введите "рус"/"ru" для русского языка или "англ"/"eng" для английского: ').lower()
    return True if answer in ['рус', "ru"] else False


def parallax(number):
    while not number.isdigit():
        number = input('Введите величину смещения. Используйте цифры: ')
    number = int(number)
    return number


def user_yo(data):
    while not data:
        data = input('Введите текст, который необходимо обработать: ')
    for i in range(len(data)):
        if data[i] == 'ё':
            data = data.replace(data[i], 'е')
        elif data[i] == 'Ё':
            data = data.replace(data[i], 'Е')
    return data


def coding(data, languages, step, mutant):
    if languages:
        for char in data:
            if char.isalpha():
                if char.isupper():
                    mutant += (rus_alphabet[(rus_alphabet.find(char.lower()) + step) % len(rus_alphabet)]).upper()
                else:
                    mutant += rus_alphabet[(rus_alphabet.find(char) + step) % len(rus_alphabet)]
            else:
                mutant += char
    else:
        for char in data:
            if char.isalpha():
                if char.isupper():
                    mutant += (eng_alphabet[(eng_alphabet.find(char.lower()) + step) % len(eng_alphabet)]).upper()
                else:
                    mutant += eng_alphabet[(eng_alphabet.find(char) + step) % len(eng_alphabet)]
            else:
                mutant += char
    return mutant


def un_coding(data, languages, step, mutant):
    if languages:
        for char in data:
            if char.isalpha():
                if char.isupper():
                    mutant += (rus_alphabet[(rus_alphabet.find(char.lower()) - step) % len(rus_alphabet)]).upper()
                else:
                    mutant += rus_alphabet[(rus_alphabet.find(char) - step) % len(rus_alphabet)]
            else:
                mutant += char
    else:
        for char in data:
            if char.isalpha():
                if char.isupper():
                    mutant += (eng_alphabet[(eng_alphabet.find(char.lower()) - step) % len(eng_alphabet)]).upper()
                else:
                    mutant += eng_alphabet[(eng_alphabet.find(char) - step) % len(eng_alphabet)]
            else:
                mutant += char
    return mutant


intro()
code = what_to_do(code)
language = lang(language)
shift = parallax(shift)
text = user_yo(text)
print(coding(text, language, shift, shift_text) if code else un_coding(text, language, shift, shift_text))
