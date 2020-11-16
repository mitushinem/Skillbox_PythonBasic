number_rows = int(input('Введите кол-во рядов: '))
number_seats = int(input('Введите кол-во сидений в ряду: '))
distance = int(input('Введите расстояние между рядами: '))

for row in range(number_rows):
    print('=' * number_seats, '*' * distance, '=' * number_seats)
