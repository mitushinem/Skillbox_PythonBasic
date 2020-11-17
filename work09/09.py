passwd = input('Введите строку: ')

max_s, num = 0, 0
for string in passwd:
    if string in 's':
        num += 1
    else:
        if max_s > num:
            num = 0
        else:
            max_s = num
            num = 0


print('Самая длинная последовательность:', max_s)