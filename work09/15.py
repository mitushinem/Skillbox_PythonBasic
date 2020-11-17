
crypt_message = input('Введите зашифрованное сообщение: ')
new_message = ''
for index in range(0, len(crypt_message), 2):
    new_message += crypt_message[index]

crypt_message_reversed = ''.join(reversed(crypt_message))

for index in range(0, len(crypt_message), 2):
    new_message += crypt_message_reversed[index]

print(new_message)