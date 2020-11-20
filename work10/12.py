
name = input('Введите имя: ')
len_name = 0

for _ in name:
    len_name += 1

for row in range(3):
    for col in range(len_name + 4):
        if row == 0 or row == 2:
            if col == 0 or col == len_name + 3:
                print('|', end='')
            else:
                print('-', end='')
        elif row == 1:
            if col == 0 or col == len_name + 3:
                print('|', end='')
            elif col == 1 or col == len_name + 2:
                print(' ', end='')
            else:
                print(name[col-2], end='')

    print()
