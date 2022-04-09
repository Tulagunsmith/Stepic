#  Программа выдает True, если треугольник, введенный пользователем является "невырожденным", т.е.
#  сумма длин любых его двух сторон больше третьей.

# объявление функции
def is_valid_triangle(side1, side2, side3):
    cheat = sorted([side1, side2, side3])
    return cheat[0] + cheat[1] > cheat[2]


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))