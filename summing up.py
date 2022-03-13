#  Программа, которая подсчитывает сумму введенных чисел, количество которых задает пользователь.
total = 0  
num = int(input())  
for _ in range(num):   
    total += int(input())  
print(total)  