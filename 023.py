s = input('Введите строчку из стихотворения: ')
print(len(s))
a, b = map(int, input('Начальная и конечная позиция: ').split())
print(s[a - 1:b])
