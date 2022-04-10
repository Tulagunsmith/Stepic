#  Программа выводит следующее по возрастанию простое число, после числа, введенного пользователем.

# объявление функции
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True if num != 1 else False

# считываем данные
n = int(input())

while n:
    n += 1
    if is_prime(n):
        print(n)
        break
