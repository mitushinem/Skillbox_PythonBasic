#1 - x**2/2! + x**4/4! - x**6/6! + x**8/8! - ...

def exponentiation(number, sqr):
    result = 1
    for _ in range(sqr):
        result *= number
    return result


def my_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def summa_row(x, accuracy):
    sqr = 2
    summa = 1
    member = 1
    step = 1

    while member > accuracy:
        member = exponentiation(x, sqr) / my_factorial(sqr)
        sqr += 2

        if step % 2 == 0:
            summa += member
        else:
            summa -= member

        step += 1
    print(summa)


acc = float(input('Введите точность: '))
x = int(input('Введите x: '))
summa_row(x, acc)