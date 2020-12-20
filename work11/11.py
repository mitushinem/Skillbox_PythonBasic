while True:
    print('Введите местоположение коня \n')
    point_start_x1 = float(input())
    point_start_y1 = float(input())
    if (0.0 <= point_start_x1 < .9) and (0.0 <= point_start_y1 < .9):
        break

while True:
    print('Введите местоположение точки на доске \n')
    point_start_x2 = float(input())
    point_start_y2 = float(input())
    if (0.0 <= point_start_x2 < .9) and (0.0 <= point_start_y2 < .9):
        break

x1, y1 = int(point_start_x1 * 10) % 10, int(point_start_y1 * 10) % 10
x2, y2 = int(point_start_x2 * 10) % 10, int(point_start_y2 * 10) % 10

if ((x2 == x1 + 2) or (x2 == x1 - 2)) and ((y2 == y1 + 1) or (y2 == y1 - 1)):
    print(f'Конь в клетке ({x1}, {y1}). Точка в клетке ({x2}, {y2})')
    print('Да, конь может ходить в эту точку.')
elif ((x2 == x1 + 1) or (x2 == x1 - 1)) and ((y2 == y1 + 2) or (y2 == y1 - 2)):
    print(f'Конь в клетке ({x1}, {y1}). Точка в клетке ({x2}, {y2})')
    print('Да, конь может ходить в эту точку.')
else:
    print('Конь может ходить только Буквой Г')
