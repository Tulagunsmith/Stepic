# Программа выводит максимальную и минимальную цифры во введенном числе
num, x, y = int(input()), 0, 9
while num != 0:
    digit = num % 10
    if digit > x:
        x = digit
    if digit < y:
        y = digit
    num = num // 10
print('Максимальная цифра равна', x) 
print('Минимальная цифра равна', y)