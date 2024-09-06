from math import pi

r = int(input('радиус круга: '))
h = int(input('высота цилиндра: '))
print(pi * r ** 2 * h * 10 ** 3 // 1 / 10 ** 3)
