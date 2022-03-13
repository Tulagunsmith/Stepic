#  Программа, которая максимальное и идущее по величине перед ним числа в диапазоне, который задает пользователь
n, y, total = int(input()), 0, 0
for _ in range(n):
    x = int(input())
    if total < x:
        y = total
        total = x
    elif y < x < total:
        y = x
print(total)
print(y)
