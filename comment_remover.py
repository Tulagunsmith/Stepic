#  Программа для курса Степик, которая убирает комментарии, если они есть,
#  из вводимых строк кода. Первый ввод по условиям задачи - это количество
#  вводимых строк кода в формате "#число".
number = input()
num = int(number[number.find('#') + 1::])
for i in range(num):
    code_line = input()
    if '#' in code_line:
        print(code_line[:code_line.find('#')].rstrip())
    else:
        print(code_line)