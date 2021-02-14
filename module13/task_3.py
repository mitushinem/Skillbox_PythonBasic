print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225


def reverse(number):
    new_number = ''
    while number > 0:
        new_number += str(number % 10)
        number = number // 10

    return int(new_number)


def reverse_number(n, k):
    rev_n, rev_k = 0, 0

    rev_n = reverse(n)
    print('Первое число наоборот:', rev_n)
    rev_k = reverse(k)
    print('Второе число наоборот:', rev_k)

    summ = rev_n + rev_k
    print('Сумма:', summ)

    rev_summ = reverse(summ)
    print('Сумма наоборот:', rev_summ)


n, k = int(input('Введите первое число: ')), int(input('Введите второе число: '))
reverse_number(n, k)
