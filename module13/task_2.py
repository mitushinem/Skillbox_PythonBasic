print('Задача 2. Функция максимума')


# Юра пишет различные полезные функции для Питона,
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию,
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.

# Юра задумался: может быть, её можно как-то использовать
# для нахождения максимума уже от трёх чисел?


# Напишите программу,
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.


def max_to_number(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return num1
    else:
        return num2


# def max_number(x1, x2, x3):
#     if max_to_number(x1, x2) >= x3:
#         return print(max_to_number(x1, x2))
#     elif max_to_number(x1, x3) >= x2:
#         return print(max_to_number(x1, x3))
#     elif max_to_number(x2, x3) >= x1:
#         return print(max_to_number(x2, x3))


x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))
# max_number(x1, x2, x3)
print(max_to_number(max_to_number(x1, x2) , x3))