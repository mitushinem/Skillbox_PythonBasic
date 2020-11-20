#
# number = int(input('Сколько натуральных чисел вводить: '))
#
# max_number, summ_number = 0, 0
#
# for n in range(1, number + 1):
#     tmp = 0
#     for s in str(n):
#         tmp += int(s)
#     if tmp > summ_number:
#        max_number = n
#        summ_number = tmp
#        tmp = 0
#     else:
#         tmp = 0
# print(f'Максимальное число {max_number}, сумма чего чисел равна {summ_number}')


# Задача 10. Наибольшая сумма цифр
#
# Вводится N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.

# Пользователь сначала вводит количество натуральных чисел.
# Далее мы создаём цикл, в котором количество итераций будет соответствовать введёному числу.
# После этого мы суммируем цифры каждого числа по очереди.
# В итоге должны вывести число с максимальной суммой чисел и сумму.
# Давайте попробуем.


number = int(input('Сколько натуральных чисел проверить: '))
max_number, summ_number = 0, 0
step = 1

while step < number + 1:
    user_data = int(input(f'Введите натуральное число {step}: '))
    element_number_sum = 0
    num_value = user_data
    while num_value > 0:
        element_number_sum += num_value % 10
        num_value = num_value//10
    if summ_number < element_number_sum:
        summ_number = element_number_sum
        max_number = user_data
    print(f'Число: {max_number}, сумма чисел = {summ_number}')
    step += 1
print(f'Максимальное число {max_number}, сумма чисел равна {summ_number}')