
def is_prime(n1, n2):
    if n1 > n2:
        min_n = n2
    else:
        min_n = n1

    nod = 1
    for i in range(2,min_n+1):
        if n1 % i == 0 and n2 % i == 0:
            nod = i
    return nod


n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
print(f'НОД чисел {n1} и {n2} равно {is_prime(n1, n2)}')
