#  Программа определяет простое число ввел пользователь или сложное.
#  1 (единица) не является простым числом

# объявление функции
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True if num != 1 else False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))