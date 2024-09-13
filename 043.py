a = int(input('Прямой или обратный отсчёт? \nпрямой - 0, обратный - 1: '))
if a == 0:
    b = int(input('Введите любое число: '))
    for i in range(1, b + 1):
        print(i)
elif a == 1:
    b = int(input('введите число до 20: '))
    if b < 20:
        for i in range(20, b - 1, -1):
            print(i)
    else:
        print('error')
else:
    print('error')
