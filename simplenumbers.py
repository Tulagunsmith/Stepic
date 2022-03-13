#  Программа, которая выводит простые числа в заданном диапазоне
a, b = int(input()), int(input())
for i in range(a, b + 1):
    for j in range(2, i + 1):       
        if i / j == 1:
            print(i)
        if i % j == 0:
            break
