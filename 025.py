name = input("Имя? \n")
if len(name) < 5:
    surname = input("Фамилия? \n")
    print(f'{name.upper()}{surname}')
    # print(f'{name.upper()}{surname.upper()}') - что значит "полное имя"?
else:
    print(name.lower())
