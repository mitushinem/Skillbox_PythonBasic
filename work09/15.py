
# crypt_message = input('Введите зашифрованное сообщение: ')
# new_message = ''
# for index in range(0, len(crypt_message), 2):
#     new_message += crypt_message[index]
#
# crypt_message_reversed = ''.join(reversed(crypt_message))
#
# for index in range(0, len(crypt_message), 2):
#     new_message += crypt_message_reversed[index]
#
# print(new_message)

crypt_message = input('Введите зашифрованное сообщение: ')
new_message_1, new_message_2 = '', ''
step = 0
str_tmp = ''

for symbol in crypt_message:
    if step % 2 == 0:
        new_message_1 += symbol
    else:
        new_message_2 += symbol
    step += 1

for symbol in new_message_2:
    str_tmp = symbol + str_tmp

print(f'Расшифрованное сообщение: {new_message_1}{str_tmp}')