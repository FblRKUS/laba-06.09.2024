a = int(input("1) Square \n2)triangle\n\nenter a number:"))
if a == 1:
    b = int(input('длина стороны '))
    print(b ** 2)
elif a == 2:
    c = int(input('длина стороны '))
    h = int(input('высота к стороне '))
    print(c * h / 2)
else:
    print('error')