n = int(input('Введите высоту пирамиды: '))
n1 = 1
for i in range(1, n + 1):
    print(' ' * (n - i + 1), end='')
    for j in range(1, i + 1):
        print(n1, end=' ')
        n1 += 2
    print()

