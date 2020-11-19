x, y, pos_x, pos_y = 15, 20, 8, 10

while True:
    print(f'[Программа]: Марсоход находится на позиции {pos_x}, {pos_y}, введите команду:')
    user_data = input('[Оператор]: ')

    if user_data == 'A':
        if pos_x == 0:
            pos_x, pos_y = pos_x, pos_y
        else:
            pos_x -= 1
            pos_y = pos_y
    elif user_data == 'D':
        if pos_x == 15:
            pos_x, pos_y = pos_x, pos_y
        else:
            pos_x += 1
            pos_y = pos_y
    elif user_data == 'W':
        if pos_y == 20:
            pos_y, pos_x = pos_y, pos_x
        else:
            pos_y += 1
            pos_x = pos_x
    elif user_data == 'S':
        if pos_y == 0:
            pos_y, pos_x = pos_y, pos_x
        else:
            pos_y -= 1
            pos_x = pos_x
    elif user_data == 'Q':
        break
