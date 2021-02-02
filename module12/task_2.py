def test():
    num = int(input('Введите целое число: '))
    if num > -1:
        positive()
    else:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


test()
