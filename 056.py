from random import randint

win = randint(1, 10)
a = int(input('Введите число: '))
while win != a:
    a = int(input('НЕТ! Введите число: '))
print(f'Да! Загаданное число {win}')
