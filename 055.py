from random import randint

win = randint(1, 5)
a = int(input('Введите число '))
if a == win:
    print('Well done')
    exit()
elif a > win:
    print('Меньше')
else:
    print('Больше')
a = int(input('Введите число '))
print('Correct') if a == win else print('You lose')
