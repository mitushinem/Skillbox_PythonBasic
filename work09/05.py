num = int(input('Введите число: '))

x = 1
for n in range(0, num + 1, 2):
    if x > num:
        print(n, " ")
    else:
        print(n, x)
        x += 2
