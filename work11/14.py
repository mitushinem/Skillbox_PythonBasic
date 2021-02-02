from math import sqrt

while True:
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))
    if a != 0:
        break

D = (b ** 2) - (4 * a * c)

if D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x1 = -b / 2 * a
    print(x1)
else:
    print('Корней нет')
