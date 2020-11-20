# Напишите программу, которая запрашивает у пользователя число N и находит сумму факториалов 1! + 2! + 3! +... + N!

n = int(input('Введите n!: '))
summ = 0
for factorial in range(1, n + 1):
    factorial_tmp = 1
    for j in range(1, factorial + 1):
        factorial_tmp *= j
    summ += factorial_tmp
    factorial_tmp = 1
print(summ)
