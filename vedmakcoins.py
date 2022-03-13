# Программа, которая подсчитывает общее количество монет
# номиналом 25, 10, 5 и 1 в заданной пользователем цене
num, count = int(input()), 0
while num != 0:
    if num >= 25:
        num -= 25
        count += 1
    elif num >= 10:
        num -= 10
        count += 1
    elif num >= 5:
        num -= 5
        count += 1
    else:
        num -= 1
        count += 1
print(count)
