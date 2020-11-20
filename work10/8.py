while True:
    num1 = int(input('Введите начало диапазона: '))
    num2 = int(input('Введите конец диапазона: '))
    if num1 > num2:
        print('Неверный диапазон! Первое число больше второго! Введите заново!')
    else:
        break

for i in range(num1, num2 + 1):
    result = i
    print(i, end=' ')
    while result != 1:
        if result % 2 == 0:
            result = result / 2
            print(int(result), end=' ')
        else:
            result = (result * 3 + 1) / 2
            print(int(result), end=' ')
    print()