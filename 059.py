from random import randint

array = ['red', 'blue', 'green', 'white', 'black']
prompt = {'red': 'blood', 'blue': 'sky', 'green': 'grass', 'white': "cloud", "black": 'nothing'}
print(f'Цвета:', end=' ')
for color in array:
    print(color, end=', ')
win = array[randint(0, 4)]
s = input('\nВыберите цвет: ')
while win != s:
    print(f'Нет. Подсказка: {prompt[win]}')
    s = input('выберите цвет: ')
print('Да!')
