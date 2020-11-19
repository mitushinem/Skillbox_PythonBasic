# name = input('Введите ФИ: ').split()
#
# print('Фамилия:', name[0])
# print('Имя:', name[1])


fio = input('Введите ФИ: ')

f, i = '', ''
for symbol in fio:
    if symbol not in ' ':
        f += symbol
    else:
        break

i = fio.replace(f,'').strip()

print('Фамилия:', f)
print('Имя:', i)
