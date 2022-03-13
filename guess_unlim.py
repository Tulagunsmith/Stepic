# Это игра по угадыванию чисел с бесконечными попытками
import random

guessTaken = 0

print('Привет! Как тебя зовут?')
name = input()

number = random.randint(1, 20)

print("Что ж, " + name + ", я загадала число от 1 до 20." + "\n")

x = input('Сколько попыток тебе понадобится, ' + name + "?" + '\n')
x = int(x)
print('Попробуй угадать.')
guess = -1
while guess != number:

    guess = int(input())

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

    if guess != number:
        print('Не унывай, ' + name + '!')
        guessTaken += 1
        print(guessTaken, "-я попытка")

if guess == number:
    guessTaken += 1
    print('Отлично,' + name + '! Ты справился c ', guessTaken, " попытки!")

if guess != number:
    number = str(number)
    print('Увы. Я загадала число: ' + number + '.')
