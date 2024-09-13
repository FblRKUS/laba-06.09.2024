a = int(input("1) Square \n2) triangle\n\nenter a number: "))
if a == 1:
    b = int(input('Длина стороны: '))
    print(b ** 2)
elif a == 2:
    b = int(input('Длина стороны: '))
    h = int(input('Высота к стороне: '))
    print(b * h / 2)
else:
    print('error')
