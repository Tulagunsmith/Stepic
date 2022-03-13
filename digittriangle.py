#  Программа, которая строит числовой треугольник с двумя сторонами, равными 'num'
num, x = int(input()), 0
for i in range(1, num + 1):
    for j in range(i):
        x += 1
        print(x, end=' ')
    print()