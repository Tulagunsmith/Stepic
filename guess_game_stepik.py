#  Программа "Угадайка", загадывает число от 1 до 100, которое угадывает пользователь,
#  так же подсчитывает количество попыток и выводит их, позволяет настроить верхнюю границу поиска
#  и предлагает поиграть снова.

import random


def intro():
    print('Добро пожаловать в "Числовую Угадайку"!')
    print('Чтобы начать нажмите "Enter"')


def big_border(right):
    right = input('Выше какого числа от 1 до 100 мне нельзя загадывать? ')
    while not is_valid(right):
        print('Введите число от 1 до 100, выше которого я не стану загадывать. ')
        right = input()
    return int(right)


def is_valid(number):
    if number.isdigit():
        return int(number) in range(1, 101)
    else:
        return False


def guessing(AI, user):
    count = 0
    while user != AI:
        if not is_valid(user):
            print('А может быть все таки введём целое число от 1 до 100?')
            user = input('Введите число от 1 до 100: ')

        if is_valid(user):
            if int(user) > AI:
                print('Моё число меньше. Попробуй снова!')
                user = input('Введите число от 1 до 100: ')
                count += 1
            elif int(user) < AI:
                print('Моё число больше. Попробуй снова!')
                user = input('Введите число от 1 до 100: ')
                count += 1
            elif int(user) == num:
                print('Поздравляю! Ты угадал!')
                print(f'Я зададывала число {AI}. Ты справился с {count} попытки.')
                break


play_again = 'д'
while play_again == 'д':
    intro()
    num = random.randint(1, big_border(input()))
    guess = input('Введите число от 1 до 100: ')
    guessing(num, guess)
    print('Сыграем еще раз? д/н')
    if (input().lower()).startswith('д'):
        play_again = 'д'
    else:
        print('Что же... Увидимся!')
        break

