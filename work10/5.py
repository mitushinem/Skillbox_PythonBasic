
n = 10
for row in range(n):
    for col in range(n):
        if col == row:
            print('^', end='')
        elif col == n - row - 1:
            print('^', end='')

        else:
            print(' ', end='')
    print()