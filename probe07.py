# work01

# for code in 114,12,14,10605,4907,450:
#     if code % 2 == 0 and code % 3 != 0:
#         print('Число подходит')
#     else:
#         print('Число не подходит')


# work02

# count = 0
# for _ in range(11):
#     user_date = int(input('Введите число '))
#     if user_date > 0 and user_date % 2 == 0:
#         count += 1
# print('Всего', count, 'чисел одновременно четные и положительные.')

# work03

# salare_summ = 0
# for month in range(1, 13):
#     user_date = int(input(f'Введите зарплату за {month} месяц '))
#     salare_summ += user_date
#
# print('Средняя зарплата за 12 месяцев:', salare_summ / 12)


# work04
# while True:
#     userdata = int(input('Введите число пингвинов'))
#     if 1 <= userdata <= 9:
#         break
#     else:
#         print('Ошибка ввода')
#
# for _ in range(userdata):
#     print('   _~_    ')
#     print('  (o o)   ')
#     print(' /  V  \  ')
#     print('/(  _  )\ ')
#     print('  ^^ ^^   ')

# work05
# breach = 0
# for sector in range(30, 36):
#     sector_men = int(input(f'Людей в {sector} секторе: '))
#     if 0 < sector_men <= 10:
#         print('Всё спокойно.')
#     else:
#         print('Нарушение! Слишком много людей в секторе!')
#         breach += 1
# print('Количество нарушений:', breach)


# work06
# x1, x2 = int(input('Координата начала отрезка ')), int(input('Координата конца отрезка '))
# for x in range(x1, x2 + 1):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print('В точке', x, 'функция равна', y)


# work07
# n = int(input('Введите натуральное число: '))
#
# for i in range(100,1000):
#     if n == (i // 100 + i % 100 // 10 + i % 10):
#         print(i)


# work08
# n = int(input('Введите натуральное число: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print('Факториал числа', n, 'равен', factorial)



# work09
# n = int(input('Сколько учаников в классе: '))
# value_3, value_4, value_5 = 0, 0, 0
# for i in range(n):
#     value = int(input('Оценка: '))
#     if value == 5:
#         value_5 += 1
#     elif value == 4:
#         value_4 += 1
#     else:
#         value_3 += 1
#
# if (value_3 > value_4) and (value_3 > value_5):
#     print('Сегодня больше троечников')
# elif (value_4 >= value_3) and (value_4 > value_5):
#     print('Сегодня больше хорошистов ')
# elif (value_5 > value_3) and (value_5 >= value_4):
#     print('Сегодня больше отличников ')
# else:
#     print('все молодцы')


# work10
# a, b = int(input('Введите начало отрезка')), int(input('Введите конец отрезка'))
# step, summ = 0, 0
# for x in range(a,b+1):
#     if x % 3 == 0:
#         summ += x
#         step += 1
# print(f'среднее арифметическое всех чисел из отрезка [{a}; {b}], которые кратны числу 3:', summ/step)


# work11
# n = int(input('Введите количество бактерий '))
# a, b = int(input('Стартовая температура в первой пробирке: ')), int(input('Конечная температура в первой пробирке: '))
# population_1, population_2 = 1, 1
# for value in range(a, b+1):
#     population_1 *= value
# print('Популяция в первой пробирке:', n * population_1)
#
# c, d = int(input('Стартовая температура во второй пробирке: ')), int(input('Конечная температура во второй пробирке: '))
# for value in range(c, d+1):
#     population_2 *= value
# print('Популяция во второй пробирке:', n * population_2)
# print('Разность популяции: ', n * population_1 - n * population_2)

# work12

# for value in range(10, 100):
#     if (value // 10 * value % 10) * 3 == value:
#         print(value)

# work13
# n = 1
# while n <= 9:
#     line = ''
#     for value in range(1, n + 1):
#         line += str(value)
#     print(line)
#     n += 1

# work14
# status = False
# number = int(input(f'Введите 1 число: '))
# number_temp = number
#
# for val in range(2, 11):
#     number = int(input(f'Введите {val} число: '))
#     if number >= number_temp:
#         status = True
#         number_temp = number
#     else:
#         status = False
#
# if status:
#     print('Числа упорядоченые')
# else:
#     print('Числа не упорядоченые')

#work15
# from random import randint
# n = int(input('Введите число карточек: '))
# summ = 0
# for i in range(1, n):
#     summ += i
# random_number = randint(1, n)
#
# print(summ - (summ - random_number))




























