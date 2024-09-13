a = input('Сегодня идёт дождь? ')
if a.lower() == 'yes':
    b = input('А ветренно? ')
    if b.lower() == 'yes':
        print('It is to windy to take umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day!')
