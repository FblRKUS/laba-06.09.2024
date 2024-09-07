a = int(input('Сколько людей ты хочешь послать на вечеринку? '))
if a < 10:
    for i in range(a):
        b = input('Как их зовут? ')
        print(f'{b} has been invited')
else:
    print('too many people')
