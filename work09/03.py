user_string = input('Введите текст: ')
number = 0
for st in user_string:
    number += 1
    if st == "*":
        print(f'В строке {user_string} "*" на {number} позиции')
        break
