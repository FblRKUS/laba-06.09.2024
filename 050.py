a = int(input('Введите число '))
while a < 10 or a > 20:
    if a < 10:
        print('too low')
    else:
        print('too high')
    a = int(input('Введите число '))
print('thank you')