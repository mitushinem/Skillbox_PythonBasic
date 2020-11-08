n = int(input('До взрыва осталось секунд: '))

for value in range(n, -1, -1):
    user_date = int(input('Обезвредить бомбу сейчас? Введите цифру: 1 - Да, 0 - Нет'))
    if value == 0:
        print(f'До взрыва осталось {value} секунд')
        print('Бомба взорвалась!')
    else:
        if user_date == 0:
            print(f'До взрыва осталось {value} секунд')
        elif user_date == 1:
            print(f'Бомба обезврежена, до взрыва оставалось {value} секунд.')
            break
