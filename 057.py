from random import randint

win = randint(1, 10)
a = int(input('Введите число: '))
while win != a:
    if a > win:
        print('Меньше')
    else:
        print('Больше')
    a = int(input('Введите число: '))
print(f'Да! Загаданное число {win}')
