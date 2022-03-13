# Игра позволяет пользователю угадать число от 1 до 20,
# число попыток выбирает пользователь
import random

guessTaken = 0

print('Привет! Как тебя зовут?')
name = input()

number = random.randint(1, 20)

print("Что ж, " + name + ", я загадала число от 1 до 20." + "\n")

x = input('Сколько попыток тебе понадобится, ' + name + "?" + '\n')
x = int(x)
print('Попробуй угадать.')

for guessTaken in range(x):

    guess = int(input())

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

    if guess != number:
        print('Не унывай, ' + name + '!')

if guess == number:
    guessTaken = str(guessTaken + 1)
    print('Отлично,' + name + '! Ты справился c ' + guessTaken + " попытки!")

if guess != number:
    number = str(number)
    print('Увы. Я загадала число: ' + number + '.')
