

def find_money(x, y):
    from random import uniform
    x_1 = round(uniform(-10, 10), 3)
    y_1 = round(uniform(-10, 10), 3)
    print(x_1, y_1)
    if (x_1 - 1 <= x <= x_1 + 1) and (y_1 - 1 <= y <= y_1 + 1):
        print('Монетка рядом')
    else:
        print('Монетка не найдена')


x, y = float(input('Введите кооодинату Х ')), float(input('Введите кооодинату У '))
find_money(x,y)