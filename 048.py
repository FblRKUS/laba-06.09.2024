s = input('Кого хочешь пригласить на вечеринку? ')
count = 0
while s != 'no':
    print(f'{s} has been invited')
    count += 1
    s = input('Кого хочешь пригласить на вечеринку? (name or no) ')
print(f'ты пригласил {count} человек')