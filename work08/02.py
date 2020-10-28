
num = int(input('Введите число: '))
summ = 0
for value in range(1, num + 1, 2):
    summ += value
print(f'Сумму нечётных чисел, лежащих в диапазоне от 1 до {num} равна {summ}')