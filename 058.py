from random import randint

count = 0
for i in range(5):
    a = randint(1, 100)
    b = randint(1, 100)
    s = int(input(f'{a} + {b} = '))
    if s == a + b:
        count += 1
print(f'Вы набрали {count} из 5 очков')
