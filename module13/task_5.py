print('Задача 5. Число Эйлера')

# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.

# P.S: Формулу смотреть на сайте :)

# Пример:

# Точность: 1e-20
# Результат: 2.7182818284590455


def number_e(acc):
    from math import factorial
    result = 0
    i = 0
    member = 1

    while member > acc:
        member = 1 / factorial(i)
        result += member
        i += 1

    print(result)


accuracy = float(input('Точность:'))
number_e(accuracy)
