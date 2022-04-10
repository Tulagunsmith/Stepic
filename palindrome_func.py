#  Программа, которая определяет является введенная строка палиндромом

# объявление функции
def is_palindrome(text):
    txet = [i.lower() for i in text if i.isalpha()]
    return txet == txet[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))