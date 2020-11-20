import math

num = int(input('Введите кол-во чисел:'))

for _ in range(num):
    user_data = float(input('Введите число: '))
    if user_data > 0:
        if user_data == int(user_data):
            x = int(user_data)
        else:
            x = int(user_data + 1.0)
        result = math.log(x)
        print(f'log({x}) = {result}')
    else:
        if user_data == int(user_data):
            x = int(user_data)
        else:
            x = int(user_data - 1.0)
        result = math.exp(x)
        print(f'exp({x}) = {result}')


