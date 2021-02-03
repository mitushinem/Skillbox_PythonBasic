
def min_num(a, b):
    result = ((a + b) - abs(a - b)) / 2
    return result


a, b = int(input('Введите первое число ')), int(input('Введите второе число '))
print(int(min_num(a,b)))
