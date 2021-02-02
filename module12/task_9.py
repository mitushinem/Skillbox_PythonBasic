from random import randint


def rock_paper_scissors():
    # игра "Камень, ножницы, бумага"
    while True:
        action_computer = randint(1, 4)
        action = int(input('1 - Камень, 2 - ножницы, 3 - бумага, 0 - Выход: '))

        if action == action_computer:
            print('Нечья')
        elif action == 1:
            if action_computer == 2:
                print('Я выйграл')
            else:
                print('Я проирал')
        elif action == 2:
            if action_computer == 3:
                print('Я выйграл')
            else:
                print('Я проирал')
        elif action == 3:
            if action_computer == 1:
                print('Я выйграл')
            else:
                print('Я проирал')
        elif action == 0:
            break


def guess_the_number():
    # игра "Угадай число"
    random_number = randint(1, 10)
    while True:
        number = int(input('Введите число: '))
        if number == random_number:
            print('Вы угадали')
            break


def mainMenu():
    while True:
        game = int(input('1 - "Камень, ножницы, бумага", 2 - "Угадай число", 3 - Выход\nВыберите пункт меню: '))
        if game == 1:
            rock_paper_scissors()
        elif game == 2:
            guess_the_number()
        elif game == 3:
            break


mainMenu()
