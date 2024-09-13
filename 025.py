name = input("Введите своё имя: ")
if len(name) < 5:
    surname = input("Введите свою фамилию: ")
    print(f'{name.upper()}{surname}')
    # print(f'{name.upper()}{surname.upper()}') - что значит "полное имя"?
else:
    print(name.lower())
