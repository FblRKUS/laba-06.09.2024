name = input('Введите ваше имя: ')
num = int(input('Введите любое число: '))
if num < 10:
    print(f'{name}\n'*num)
else:
    print('Too high')
