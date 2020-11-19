# string = input('Введите текст: ').split()
# max_len = 0
#
# for s in string:
#     if len(s) > max_len:
#         max_len = len(s)
#
# print(f'Самое длинное слово состоит из {max_len} символов')


string = input('Введите текст: ')
max_len, len_word = 0, 0
str_tmp = string + ' '
for s in str_tmp:
    if s not in ' ':
        len_word += 1
    else:
        if len_word > max_len:
            max_len = len_word
            len_word = 0
        else:
            len_word = 0

print(f'Самое длинное слово состоит из {max_len} символов')