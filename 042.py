total = 0
for i in range(5):
    a = int(input('введите число: '))
    b = input('включить число в сумму? ')
    if b.lower() == 'yes':
        total += a
print(total)
