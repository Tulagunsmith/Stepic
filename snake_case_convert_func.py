#  Программа конвертирует CamelCase в snake_case

# объявление функции
def convert_to_python_case(text):
    snake_case = ''
    for i in text:
        if i.isupper():
            snake_case += '_'
        snake_case += i.lower()
    return snake_case[1:]


# вызываем функцию
print(convert_to_python_case(input()))