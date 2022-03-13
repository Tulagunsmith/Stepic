#  Программа, которая подсчитывает количество введенных слов до стоп-слова
word, count = input(), 0
while word not in ('стоп', 'хватит', 'достаточно'):
    count += 1
    word = input()
print(count)