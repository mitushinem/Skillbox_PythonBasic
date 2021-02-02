
def NOD(n1, n2):
    if n1 > n2:
        num = n1
        num_d = n2
    else:
        num = n2
        num_d = n1

    ostatok = n1 % n2
    n = num_d
    while True:
        tmp = n % ostatok


n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))

print(f'НОД чисел {n1}, {n2} равно {NOD(n1, n2)}')