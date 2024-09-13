total = 0
for i in range(5):
    a = int(input('Введите любое число: '))
    b = input('Включить число в сумму? (yes/no) ')
    if b.lower() == 'yes':
        total += a
print(total)
