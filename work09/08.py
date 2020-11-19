# name = input('Введите ФИ: ').split()
#
# print('Фамилия:', name[0])
# print('Имя:', name[1])


fio = input('Введите ФИ: ')

f, i = '', ''
status = True
for symbol in fio:
    if symbol not in ' ':
        if status:
            f += symbol
        else:
            i += symbol
    else:
        status = False

print('Фамилия:', f)
print('Имя:', i)

