name = input("Имя? \n")
if len(name) < 5:
    surname = input("Фамилия? \n")
    print(f'{name.upper()}{surname}')
else:
    print(name.lower())