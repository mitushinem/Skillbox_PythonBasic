
# mens = int(input('Кол-во людей: '))
# hours = int(input('Кол-во часов: '))
#
# for hour in range(1, hours):
#     print(f'Идет {hour} час: ')
#     for men in range(hour, mens):
#         print(f'в очереди {men} человек')
#     print()

# p = int(input('Введите последовательность чисел '))
# w = 0
# for s in str(p):
#     if int(s) >= 5:
#         w += 1
# print(w)

n = int(input('введите n: '))

for row in range(n + 1):
    for col in range(row, n + 1):
        print(col, end=' ')
    print()









