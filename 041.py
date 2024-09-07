name = input('имя? ')
num = int(input('число? '))
if num < 10:
    print(f'{name}\n'*num)
else:
    print('too high')
