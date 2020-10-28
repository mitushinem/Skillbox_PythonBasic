x1, x2 = int(input('Координата начала отрезка: ')), int(input('Координата конца отрезка: '))
step = int(input('Шаг: '))
for x in range(x2, x1 - 1, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print('В точке', x, 'функция равна', y)