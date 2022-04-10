#  Программа, которая отсеивает ненадежные пароли по 4-м параметрам

# объявление функции
def is_password_good(password):
    count_uppercase = [i for i in password if i.isupper()]
    count_lowercase = [i for i in password if i.islower()]
    count_digit = [i for i in password if i.isdigit()]
    return True if all([count_digit, count_lowercase, count_uppercase]) and len(password) > 7 else False



# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))