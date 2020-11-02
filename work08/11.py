

n = int(input('Введите натуральное число: '))
s = 1
for i in range(1, n + 1):
    if i % 2 == 0:
        s += 1 / 2 ** i
    else:
        s -= 1 / 2 ** i

print(s)