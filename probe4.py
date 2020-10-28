# Задание 1
#
# sensor = int(input('На улице идёт дождь?: '))
# if sensor == 1:
#     print('Пошёл дождь. Возьмите зонтик!')
#
#
# Задание 2
#
# data1 = int(input('Введите кол-во баллов по русскому языку:'))
# data2 = int(input('Введите кол-во баллов по математике: '))
# data3 = int(input('Введите кол-во баллов по информатике: '))
# summ = data1 + data2 + data3
# if summ >= 270:
#     print('Поздравляю, ты поступил на бюджет!')
# else:
#     print('К сожалению, ты не прошёл на бюджет.')
#
#
# Задание 3
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')
#
# Задание 4
# price1 = int(input('Введите цену первого товара: '))
# price2 = int(input('Введите цену второго товара: '))
# price3 = int(input('Введите цену третьего товара: '))
#
# summ = price1 + price2 + price3
# if summ > 10000:
#     summ -= summ * .1
#     print('Сумма чека со скидкой 10%:', summ)
# else:
#     print('Сумма чека:', summ)
#
#
# Задание 5
# number = int(input('Введите число: '))
# if number < 0:
#     number = -number
#     print('Ввели', number, 'Ответ', number)
# else:
#     print('Ввели', number, 'Ответ', number)
#
#
# Задание 6
#
# cube_user = int(input('Кубик Кости: '))
# cube_boss = int(input('Кубик владельца: '))
#
# if cube_user >= cube_boss:
#     print('Разность: ', cube_user-cube_boss)
#     print('Костя платит')
# else:
#     print('Сумма: ', cube_user + cube_boss)
#     print('Владелец платит')
#
# print('Игра окончена')
#
#
# Задание 7
#
# money = int(input('Введите сумму, которую хотите снять: '))
# if money % 100 == 0:
#     print('Сумма доступна к снятию')
# else:
#     print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')
#
#
# Задание 8
# hours = int(input('Введите отработанные часы: '))
# money_food = int(input('Введите траты на еду: '))
# credit = int(input('Введите остаток по кредиту: '))
#
# salary = (200 * hours) / 2 ** 3 + hours
# if salary >= money_food + credit:
#     print('Часов хватает. Можно отдохнуть')
# else:
#     print('Часов не хватает. Придётся поработать!')
#
#
# Задание 9
# mileage = int(input('Пробег: '))
# number_day = int(input('Номер дня: '))
#
# if 100 <= mileage <= 999:
#     sum_num_mileage = mileage // 100 + mileage % 100 // 10 + mileage % 10
#     if sum_num_mileage > number_day:
#         mileage = 0
#         print('Сброс. Пробег: ', mileage)
#     else:
#         print('Сегодня не сломался. Пробег:', mileage)
#
# else:
#     print('Пробег указан не верно!')
#
#
# Задание 10
#
# a, b, c = int(input('Введите первое число ')), int(input('Введите второе число ')),int(input('Введите третье число '))
#
# if a == b or a == c or b == c:
#     print('Есть повторяющиеся значения!')
# else:
#     if a > b and a > c:
#         print(a)
#     else:
#         if b > c:
#             print(b)
#         else:
#             print(c)
