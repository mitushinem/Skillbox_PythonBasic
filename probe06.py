# # work01
# N = int(input('Введите число'))
# num = 1
#
# while N >= num:
#     print(num ** 3)
#     num += 1

#work02
# sec = int(input('Сколько секунд ждать? '))
# while sec >= 0:
#     print(sec)
#     sec -=1

#work03
# name = input('Имя должника ')
# summ = int(input('Сумма долга '))
# print(name, 'ваша задолженность составляет', summ, 'рублей')
# while True:
#     user_data = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))
#     if user_data >= summ:
#         print('Отлично,', name, '! Вы погасили долг. Спасибо!')
#         break
#     else:
#         print('Маловато,', name, '. Давайте ещё раз.')

#work04
# n = int(input("Введите число:"))
# count = 0
# while n > 0:
#     count += 1
#     n = n // 10
# print("Количество цифр равно:", count)

# work05
# count = 0
# while True:
#     user_data = int(input('Введите число: '))
#     if user_data == 0:
#         break
#     elif user_data % 2 == 0:
#         count += 1
# print('Чётных чисел в последовательности:', count)

# work06
# while True:
#     num = int(input('Введите число:'))
#     if num == 0:
#         break
#     num1 = num // 1000
#     num2 = num % 1000
#     summ1 = (num1 % 10) + (num1 % 100 // 10) + (num1 // 100)
#     summ2 = (num2 % 10) + (num2 % 100 // 10) + (num2 // 100)
#     if summ1 == summ2:
#         print('Счастливый билет')
#     else:
#         print('Не счастливый билет')


#work07
# a = int(input('Введите первый член прогрессии: '))
# d = int(input('Введите разность: '))
# n = int(input('Введите количество членов прогрессии: '))
#
# count, summ = 0, 0
# while count < n:
#     print(a)
#     summ += a
#     a += d
#     count +=1
# print('Сумма прогрессии', summ)



#work08
km = int(input('Сколько километров пробежал спортсмен в первый день: '))
mileage = int(input('Пробег : '))
days = 1
while km < mileage:
    km = km * 1.1
    days += 1
print('На', days, 'день спортсмен пробежит', mileage, 'км')





#work09
# summ_plus, summ_minus = 0, 0
# while True:
#     num = int(input('Введите число: '))
#     if num > 0:
#         summ_plus += 1
#     elif num < 0:
#         summ_minus += 1
#     else:
#         break
# print('Кол-во положительных чисел:', summ_plus)
# print('Кол-во отрицательных чисел:', summ_minus)

#work10
# print('Начался 8-часовой рабочий день')
# hour, task_summ = 1, 0
# magazin = None
# while hour < 9:
#     print(hour, 'час')
#     task = int(input('Сколько задач решит Максим? '))
#     task_summ += task
#     tel = int(input('Звонит жена. Взять трубку? '))
#     if tel == 1:
#         magazin = True
#     else:
#         magazin = False
#     hour +=1
# print('Рабочий день закончился. Всего выполнено задач:', task_summ)
# if magazin:
#     print('Нужно зайти в магазин')

#work11

# max_temperature = 0
# while True:
#     temperature = int(input('Введите показания темпиратуры: '))
#     if temperature == 0:
#         break
#     elif temperature > max_temperature:
#         max_temperature = temperature
# print('Самая высокая темпиратура:', max_temperature)


#work12

# deposit = int(input('Сумма вклада: '))
# percent = float(input('Проценты: '))
# cached_deposit = int(input('Желаемая сумма вклада для снятия: '))
# year = 0
#
# while deposit <= cached_deposit:
#     deposit = round(((deposit * percent) / 100) + deposit)
#     print(deposit)
#     year += 1
# print('пройдёт', year, 'лет, прежде чем сумма достигнет значения', cached_deposit)




#work13
# num = int(input('Загадали число '))
# step = 0
# while True:
#     step += 1
#     user_data = int(input('Введите число '))
#     if user_data == num:
#         print('Вы угадали! Число попыток:', step)
#         break
#     elif user_data > num:
#         print('Число больше, чем нужно. Попробуйте ещё раз!')
#     else:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')


#work14

# from random import randint
# num = int(input('Я загадал число '))
# a, b, step = 1, 100, 0
# while True:
#     if 1 <= num <= 100:
#         step += 1
#         num_computers = randint(a, b)
#         if step == 7:
#             num_computers = num
#         print('Шаг', step)
#         print('Твое число равно, меньше или больше, чем число', num_computers)
#         if num == num_computers:
#             print('Компьютер угадал число за!', step, 'шагов')
#             break
#         elif num > num_computers:
#             print('Мое число больше чем!', num_computers)
#             a, b = num_computers, b
#         elif num < num_computers:
#             print('Мое число меньше чем!', num_computers)
#             a, b = a, num_computers
#     else:
#         print('Число должно быть в дивпазоне 1..100')
#         break
















