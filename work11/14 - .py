from math import sqrt

while True:
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))
    if a != 0:
        break

D = (b ** 2) - (4 * a * c)
print(D)

if b % 2 == 0:
    D = (b / 2) ** 2 - (a * c)
    if D > 0:
        x1 = (-(b / 2) - sqrt(D)) / a
        x2 = (-(b / 2) + sqrt(D)) / a
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    elif D == 0:
        x1 = - (b / (2 * a))
        print(x1)
    else:
        print('Корней нет')
elif a - b + c == 0:
    x1 = -1
    x2 = -c / a
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif a + b + c == 0:
    x1 = 1
    x2 = c / a
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)

else:
    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    elif D == 0:
        x1 = -b / 2 * a
        print(x1)
    else:
        print('Корней нет')
