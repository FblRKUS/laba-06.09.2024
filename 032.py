from math import pi

r = int(input('Введите радиус круга: '))
h = int(input('Введите высоту цилиндра: '))
print(pi * r ** 2 * h * 10 ** 3 // 1 / 10 ** 3)
