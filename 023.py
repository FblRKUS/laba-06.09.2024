s = input('введи строчку из стихотворения: ')
print(len(s))
a, b = map(int, input('начальная и конечная позиция: ').split())
print(s[a - 1:b])
