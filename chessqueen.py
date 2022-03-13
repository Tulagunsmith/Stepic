#  Программа, которая выводит 'yes', если шахматный ферзь может сделать следующий ход
x, y, a, b = (int(input()) for _ in range(4))
n = x + y
z = a + b
if x == a or y == b:
    print('YES')
elif x != a and y != b and (abs(x - a) == abs(y - b)):
    if (n == z) or (n % 2 == z % 2):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
