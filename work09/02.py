# Задача 2. Я стал новым пиратом!
#
# Старому капитану необходимо пополнить команду. Но попадут на его корабль только достойные! Он отобрал 10 человек и те,
# кто из них крикнет слово “Карамба”, попадут на борт.
#
# Пользователь вводит 10 слов. Напишите программу, которая определяет, сколько из них совпадают со словом “Карамба”.


number_string, number_person = 1, 0
while number_string < 11:
    user_data = input('Введите волшебное слово: ')
    number_string += 1
    if user_data == 'Карамба':
        print('Ты достоен быть в моей команде')
        number_person += 1

print(f'В мою команду попало {number_person}')
