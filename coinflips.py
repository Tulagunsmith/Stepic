#  Программа "Орлянка", пользователю предлагается угадать сколько раз выпадет "Орёл"
import random
import time
print ('''Я подброшу монетку 1000 раз. Угадай, сколько
        раз выпадет "Орел" (Нажми клавишу Enter, чтобы начать)''')
print ('Введи свой вариант: ')
guess = input ()
flips = 0
heads = 0
back = 0
while flips < 1000:
    if random.randint (0, 1) == 1:
        heads = heads + 1
        flips = flips + 1
    if random.randint (0, 1) == 0:
        flips = flips + 1
    if flips == 900:
        time.sleep (3)
        print ('900 подкидываний и "Орел" выпал ' + str (heads) + 'раз.')
    if flips == 100:
        time.sleep (1)
        print ('При 100 бросках, "Орел" выпал ' + str (heads) + 'раз.')
    if flips == 500:
        time.sleep (2)
        print ('Полпути пройдено и "Орел" выпал ' + str (heads) + 'раз.')

print ()
print ('Из 1000 подбрасываний монетки "Орел" выпал ' + str (heads) + 'раз!')
print ('Насколько вы близки к правильному ответу?')

if int (guess) < heads:
    print ('Маловато!')
if int (guess) > heads:
    print ('Многовато!')
if int (guess) == heads:
    print ('''Ты угадал! Иди и покупай лотерейный билет,
        пока удача тебе не изменила!''')
