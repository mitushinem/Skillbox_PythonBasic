
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end='')
        elif col == 24:
            print('|', end='')
        elif col == row + 29:
            print('\\', end='')
        elif col == -row + 19:
            print('/', end='')
        else:
            print(' ', end='')
    print()
#
#
# for row in range(5, -1, -1):
#     for col in range(6):
#         if col == row:
#             print('1', end=' ')
#         elif row > col:
#             print('0', end=' ')
#         else:
#             print('2', end=' ')
#     print()










