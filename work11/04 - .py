
from math import log2

n = int(input('Введите длину сообщения: '))

k = 1
while True:
    if not log2(n).is_integer():
        print('Введенное количество символов - это не степень двойки')
        break
    elif 2 ** k >= n:
        print(f'в сообщении {n} символов. K = {k}. Вывод: 2 ** {k} = {2 ** k}')
        break
    else:
        k += 1






























