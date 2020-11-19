# message = input('Введите слово: ')
# if message[0] == message[-1]:
#     print('Первая и последняя буквы одинаковые')
# else:
#     print('Первая и последняя буквы разные')


message = input('Введите слово: ')
s1, s2 = '', ''

message_len = 0

for _ in message:
    message_len += 1

if message_len > 1:
    for key, value in enumerate(message):
        if key == 0:
            s1 = value
        elif key == message_len - 1:
            s2 = value

    if s1 == s2:
        print('Первая и последняя буквы одинаковые')
    else:
        print('Первая и последняя буквы разные')
else:
    print('Введите более одной буквы ')