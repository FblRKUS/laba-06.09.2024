total = int(input('Введите число ')) + int(input('Введите число '))
s = input('Хотите добавить ещё чисел? (y/n) ')
while s.lower() == 'y':
    total += int(input('Введите число '))
    s = input('Хотите добавить ещё чисел? (y/n) ')
print(total)
