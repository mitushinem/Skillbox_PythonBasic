n = int(input('Введите размерность матрицы: '))

for row in range(n):
    for col in range(n):
        if col == row:
            print(1, end='\t')
        elif col == n - row - 1:
            print(1, end='\t')
        elif col > row and (col < n - row - 1):
            print(0, end='\t')
        else:
            print('2', end='\t')
    print()