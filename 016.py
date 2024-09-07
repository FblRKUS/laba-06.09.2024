a = input('Сегодня идёт дождь? ')
if a.lower() == 'yes':
    b = input('а ветренно? ')
    if b.lower() == 'yes':
        print('it is to windy to take umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')
