for row in range(20):
    for col in range(50):
        if row == 9 and col == 49:
            print('>', end='')
        elif row == 9 and col == 24:
            print('+', end='')
        elif row == 9:
            print('-', end='')
        elif row == 0 and col == 24:
            print('^', end='')
        elif col == 24:
            print('|', end='')

        else:
            print(' ', end='')
    print()
