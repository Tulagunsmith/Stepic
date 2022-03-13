# Программа, которая переворачивает введенное число
num = int(input())
while num != 0:
    digit = num % 10
    num = num // 10
    print(digit, end='')