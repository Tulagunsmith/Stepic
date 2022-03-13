#  Программа, которая определяет состоит ли число из одинаковых цифр


num = int(input())
x = num % 10
answer = 'YES'
while num != 0:
    if x != num % 10:
        answer = 'NO'
        break
    num //= 10
print(answer)