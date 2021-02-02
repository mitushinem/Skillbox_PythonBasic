def reverse_number(num):
    r_number = ''
    tmp_num = int(num)
    while True:
        r_number += str(tmp_num % 10)
        new_num = tmp_num // 10
        tmp_num = new_num
        if new_num == 0:
            break
    print('Число наоборот:', int(r_number))


while True:
    num = input('Введите число: ')
    if num == 0:
        break
    else:
        reverse_number(num)