#  Программа, которая просчитывает может ли шахматная ладья сделать следующий ход
#  на бесконечном поле
x, y, a, b = [int(input()) for _ in range(4)]
print('YES' if a == x or b == y else 'NO')
