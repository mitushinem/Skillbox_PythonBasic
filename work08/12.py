
x = int(input('Дано число X: '))
x1, x2 = 1, 1

if not ((x % 2 == 0) and (1 < x < 65)):
    for i in range(1, 65):
        if i % 2 == 0:
            x2 *= (x - i)
        else:
            x1 *= (x - i)
    print('Ответ: ', x1 / x2)

else:
    print('На нуль делить нельзя!')
