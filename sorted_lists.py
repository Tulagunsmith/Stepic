#  Программа выводит отсортированный и распакованный список, составленный из определенного пользователем
#  числа малых отсортированных списков

def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

lines = int(input())
numbers = [int(c) for c in input().split()]
for _ in range(1, lines):
    numbers = quick_merge(numbers, [int(c) for c in input().split()])
print(*numbers)