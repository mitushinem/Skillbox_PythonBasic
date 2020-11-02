a, b = int(input('Введите a: ')), int(input('Введите b: '))
c, d = int(input('Введите c: ')), int(input('Введите d: '))

if 0 <= c <= d:
    for value in range(a, b + 1):
        if value % d == c:
            print(value)
else:
    print('Ошибка!')










