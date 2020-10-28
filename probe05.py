# Задание 1

# experience = int(input('Введите количество опыта: '))
# if experience <= 1000:
#     level = 1
#     print('Ваш уровень:', level)
# elif 2500 >= experience > 1000:
#     level = 2
#     print('Ваш уровень:', level)
# elif 5000 >= experience > 2500:
#     level = 3
#     print('Ваш уровень:', level)
# else:
#     level = 4
#     print('Ваш уровень:', level)

# Задание 2

# a, b, c = int(input('Введите первое число ')), int(input('Введите второе число ')),int(input('Введите третье число '))
#
# if a == b or a == c or b == c:
#     print('Есть повторяющиеся значения!')
# elif a > b and a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)


# Задание 3
# x = int(input('Введите Х: '))
# if x > 0:
#     y = x - 12
#     print('Y =', y)
# elif x < 0:
#     y = x ** 2
#     print('Y =', y)
# else:
#     y = 5
#     print('Y =', y)


# Задание 4
# student_num = int(input('Введите место в списке поступающих '))
# entrance_ball = int(input('Введите количество баллов за экзамены '))
#
# if student_num < 11:
#     print('Поздравляем, Вы поступили!')
#     if entrance_ball >= 290:
#         print('Бонусом Вам будет начисляться стипендия')
#     else:
#         print('Но Вам не хватило баллов для стипендии')
# else:
#     print('Вы не поступили!')


# Задание 5
# day_week = int(input('Введите номер дня недели: '))
# hours = int(input('Введите количество часов до конца рабочего дня: '))
#
# if 0 < day_week < 8:
#     if 0 <= hours < 9:
#         if day_week == 1:
#             print('Сегодня понедельник')
#             print('Осталось работать', hours, 'часов')
#         elif day_week == 2:
#             print('Сегодня вторник')
#             print('Осталось работать', hours, 'часов')
#         elif day_week == 3:
#             print('Сегодня среда')
#             print('Осталось работать', hours, 'часов')
#         elif day_week == 4:
#             print('Сегодня четверг')
#             print('Осталось работать', hours, 'часов')
#         elif day_week == 5:
#             print('Сегодня пятница')
#             print('Осталось работать', hours, 'часов')
#             if 0 < hours <= 2:
#                 print('Можно уйти пораньше!')
#         elif day_week == 6:
#             print('Сегодня суббота')
#             print('Осталось работать', hours, 'часов')
#         elif day_week == 7:
#             print('Сегодня воскресенье')
#             print('Осталось работать', hours, 'часов')
#     else:
#         print('Рабочее время указано не верно!')
#
# else:
#     print('Номер дня недели указан не верно!')


# Задание 6

# client = int(input('Количество клиентов: '))
# seller = int(input('Количество продавцов: '))
# salary = int(input('Зарплата одного продавца: '))
#
# if (client // seller) > 4:
#     print('Слишком мало продавцов')
#     if salary < 20000:
#         salary += 2000
# else:
#     print('Продавцов достаточно')
#
# print('Зарплата продавцов', salary)


# Задание 7
# num = int(input('Введите двузначное число'))
# if not (10 <= num <= 99):
#     print('Введите двухзначное число')

# Задание 8

# num1 = int(input('Загадайте первое число:'))
# num2 = int(input('Загадайте второе число:'))
#
# if num1 % 2 == 0 or num2 % 2 == 0:
#     print('Одно из чисел чётное. Учитель заслужил конфету!')
# else:
#     print('Все числа нечетные. Ученики заслужили конфету!')

# Задание 9
#
# rating = int(input('Что получил по математике? '))
# if rating == 2 or rating == 3:
#     print('Плохо. Марш учиться!')
# elif rating == 4 or rating == 5:
#     print('Молодец! Можешь отдохнуть.')

# Задание 10
# num = int(input('Введите двузначное число '))
# if not (10 <= num <= 99) and not (-10 >= num >= -99):
#     print('Ошибка ввода!')

# Задание 11
# a, b, c = int(input('Введите первое число ')), int(input('Введите второе число ')),int(input('Введите третье число '))
#
# if a == b == c:
#     print('Все числа совпали', 3)
# elif a == b or a == c or b == c:
#     print('Есть два совпадения', 2)
# else:
#     print('Совпадений не найдено')
#
# Задание 12
#
# number_machines = int(input('Введите количество станков: '))
# room_area = int(input('Введите площадь помещения: '))
#
# if room_area >= 100 and number_machines >= 5:
#     print('Всё отлично, это наш вариант!')
# else:
#     print('Не подходит. Нужно искать дальше')


# Задание 13
#
# price = int(input('Введите цену квартиры: '))
# room_area = int(input('Введите площадь квартиры: '))
#
# if price <= 7000000 and room_area >= 80:
#     print('Подходит')
# elif price <= 10000000 and room_area >= 100:
#     print('Подходит')
# else:
#     print('Не подходит')


# Задание 14
#
# income = int(input('Введите сумму дохода: '))
#
# unpaid_30 = income - 50000
# unpaid_20 = unpaid_30 - 10000
# unpaid_13 = .13 * 10000
#
# if income >= 50000:
#     nalog = .3 * unpaid_30 + .2 * unpaid_20 + unpaid_13
#     print('С дохода', income, 'придется заплатить такой налог:', nalog)
# else:
#     nalog = .2 * (income - 10000) + unpaid_13
#     print('С дохода', income, 'придется заплатить такой налог:', nalog)


# Задание 15

time = int(input('Введите время: '))
if 0 <= time < 24:
    if (8 <= time < 9) or (12 <= time < 13) or (15 <= time < 18) or (20 <= time <= 22):
        print('Можно получить посылку')
    else:
        print('Посылку получить нельзя')
else:
    print('Ошибка ввода времени!')







