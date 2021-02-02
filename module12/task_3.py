def summa(num):
    summ_number = 0
    tmp_num = num
    while True:
        summ_number += tmp_num % 10
        new_num = tmp_num // 10
        tmp_num = new_num
        if new_num == 0:
            break
    print(f'Сумма чисел в числе {num} равна {summ_number}')


def min_number(num):
    min_num = num % 10
    tmp_num = num
    while True:
        num_1 = tmp_num % 10
        if num_1 < min_num:
            min_num = num_1
        new_num = tmp_num // 10
        tmp_num = new_num
        if new_num == 0:
            break
    print(f'Минимальное число в числе {num} равно {min_num}')


def max_number(num):
    max_num = num % 10
    tmp_num = num
    while True:
        num_1 = tmp_num % 10
        if num_1 > max_num:
            max_num = num_1
        new_num = tmp_num // 10
        tmp_num = new_num
        if new_num == 0:
            break
    print(f'Максимальное число в числе {num} равно {max_num}')


while True:
    num = int(input('Введите число: '))
    action = int(input(f'1 - Сумма чисел в числе,\n'
                       f'2 - Минимальное число в числе,\n'
                       f'3 - Максимальное число в числе,\n'
                       f'0 - Для выхода из программы.\n'
                       f'Выберите действие: '))
    if action == 1:
        summa(num)
    elif action == 2:
        min_number(num)
    elif action == 3:
        max_number(num)
    elif action == 0:
        break
