#  Программа предлагает назввать правильный ответ от сложения случайных чисел
import random
number1 = random.randint (1, 1000)
number2 = random.randint (1, 1000)
print ('Сколько будет: ' + str (number1) + '+' + str (number2) + '?')
answer = input ()
if int (answer) == number1 + number2:
    print ('Верно!')
else:
    print ('Нет! Правильный ответ - ' + str (number1 + number2))
