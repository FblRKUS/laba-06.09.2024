compnum = 50
a = int(input('Введите число '))
count = 1
while a != compnum:
    if a > compnum:
        print('Загаданное число меньше')
    if a < compnum:
        print('Загаданное число больше')
    a = int(input('Введите число '))
    count += 1
print(f'Well done, you took {count} attempts')
