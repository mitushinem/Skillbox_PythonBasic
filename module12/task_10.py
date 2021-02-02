# Напишите игру — текстовый квест. Игрок находится в квартире, его задача — покинуть её.
# Игрок свободно перемещается по квартире, пока не покинет её. В квартире есть три комнаты (спальня, кухня, ванна) и коридор.
# В ванну можно попасть из коридора и спальни. В спальню можно попасть из ванны и коридора.
# На кухню можно попасть только из коридора.
# Коридор связан со всеми комнатами, но в нём дополнительно есть дверь наружу.
# На кухне открыто окно. Если игрок пытается выбраться через него, то разбивается и проигрывает.

# Пример:
# Вы в спальне. Куда идём?
# 1 — в ванну
# 2 — в коридор
#
# 2
#
# Вы в коридоре. Куда идём?
# 1 — в спальню
# 2 — в ванну
# 3 — на кухню
# 4 — в дверь
#
# 2
#
# Вы в ванне. Куда идём?
# 1 — в коридор
# 2 — в спальню
#
# 2
#
# Вы в спальне...


def bedroom():
    # Спальная
    print('Вы в спальне. Куда идём?')
    while True:
        step = int(input('1 — в ванну, 2 — в коридор '))
        if step == 1 or step == 2:
            break

    if step == 1:
        bath()
    elif step == 2:
        corridor()


def kitchen():
    # Кухня
    print('Вы на кухне. Куда идём?')
    while True:
        step = int(input('1 — в коридор, 2 — в окно '))
        if step == 1 or step == 2:
            break

    if step == 1:
        corridor()
    elif step == 2:
        print('Ты проиграл')
        exit(0)


def bath():
    # Ванная
    print('Вы в ванне. Куда идём?')

    while True:
        step = int(input('1 — в коридор, 2 — в спальню '))
        if step == 1 or step == 2:
            break

    if step == 1:
        corridor()
    elif step == 2:
        bedroom()


def corridor():
    # Коридор
    print('Вы в коридоре. Куда идём?')
    while True:
        step = int(input('1 — в спальню, 2 — в ванну, 3 — на кухню, 4 — в дверь '))
        if step > 0 and step < 5:
            break

    if step == 1:
        bedroom()
    elif step == 2:
        bath()
    elif step == 3:
        kitchen()
    elif step == 4:
        print('Выход')
        exit(0)


def main(userdata):
    if userdata == 1:
        bedroom()
    elif userdata == 2:
        bath()
    elif userdata == 3:
        kitchen()
    elif userdata == 4:
        corridor()


userdata = int(input('Я тут. 1 — в спальне, 2 — в ванной, 3 — на кухне, 4 — в коридоре '))
main(userdata)
