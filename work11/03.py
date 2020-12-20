import math

num = int(input('Введите кол-во чисел:'))

for _ in range(num):
    user_data = float(input('Введите число: '))
    if user_data > 0:
        result = math.log(math.ceil(user_data))
        print(f'log({math.ceil(user_data)}) = {result}')
    else:
        result = math.exp(math.floor(user_data))
        print(f'exp({math.floor(user_data)}) = {result}')
