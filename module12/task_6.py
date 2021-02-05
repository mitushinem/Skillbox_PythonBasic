

def find_money(x, y):
    if (-1 <= x <= 1) and (- 1 <= y <= 1):
        print('Монетка рядом')
    else:
        print('Монетка не найдена')


x, y = float(input('Введите кооодинату Х ')), float(input('Введите кооодинату У '))
find_money(x,y)