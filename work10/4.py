l, h = int(input('Введите длину: ')), int(input('Введите ширину: '))

for x in range(h):
    print('|', end=' ')
    if x == 0 or x == h - 1:
        for y in range(l):
            print('-', end=' ')
    else:
        for y in range(l):
            print(' ', end=' ')
    print('|', end=' ')
    print()