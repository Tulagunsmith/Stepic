# Бесполезная программа "Эхо", со стоп-словом
word = str(input())
while word not in ('КОНЕЦ', 'конец'):
    print(word)
    word = str(input())
