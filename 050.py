a = int(input('Введите число '))
while a < 10 or a > 20:
    if a < 10:
        print('Too low')
    else:
        print('Too high')
    a = int(input('Введите число '))
print('Thank you')