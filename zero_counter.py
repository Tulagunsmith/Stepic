#  Программа для подсчета нолей во введенном числе
counter_1 = 0
num = input()
x = num.count('0')
if '0' in num:
    counter_1 = counter_1 + x
print(counter_1)
