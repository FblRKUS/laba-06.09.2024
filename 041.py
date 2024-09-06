name = input('имя? ')
num = int(input('число? '))
if num < 10:
    for i in range(num):
        print(name)
else:
    print('too high')
