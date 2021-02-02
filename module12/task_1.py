

def summa_n(n):
    summ = 0
    for i in range(n + 1):
        summ += i
    print(f'Я знаю, что сумма чисел от 1 до {n} равна {summ}')


num = int(input('Введите число: '))
summa_n(num)