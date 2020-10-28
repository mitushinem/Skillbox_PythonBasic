
a, b, c = int(input('Введите a: ')), int(input('Введите b: ')), int(input('Введите c: '))
summ, iteration = 0, 0
for value in range(a, b + 1):
    if value % c == 0:
        summ += value
        iteration += 1
print(f'среднее арифметическое всех чисел из отрезка [{a}; {b}], которые кратны числу {c} равно {summ/iteration}')