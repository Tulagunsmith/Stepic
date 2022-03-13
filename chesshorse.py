#  Программа, которая выводит 'yes', если шахматный конь может сделать следующий ход
x, y, a, b = (int(input()) for _ in range(4))
n = x + y
z = a + b
if x != a and y != b:
    if (abs(x - a) == 1 and abs(y - b) == 2) or (abs(x - a) == 2 and abs(y - b) == 1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')