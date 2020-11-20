
n = int(input('введите N: '))
print(n)
for j in range(n):
    tmp_str = ''
    for i in range(n, -n - 1, -1):
        if i == 0:
            continue
        if i < 0:
            tmp_str += str(-(i))
        else:
            tmp_str += str(i)

    str_new = ''
    for s in tmp_str:
        if int(s) < n - j:
            str_new += '.'
        else:
            str_new += s
        tmp_str = ''
    print(str_new, end='')

    print()