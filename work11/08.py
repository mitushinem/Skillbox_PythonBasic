botton_border = int(input('Ввод:\nНижняя граница: '))
top_border = int(input('Верхняя граница: '))
step = int(input('Шаг: '))

print('Вывод: ')
print('C', '\t', 'F')

for value in range(botton_border, top_border, step):
    if value == 0:
        print(0, '\t', 32)
    elif value != top_border:
        print(value, '\t', value * 1.8 + 32)
else:
    if value != top_border:
        print(top_border, '\t', top_border * 1.8 + 32)