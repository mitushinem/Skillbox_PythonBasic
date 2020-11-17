
while True:
    val = input('Введите последовательность из 10 символов:')
    if len(val) == 10:
        for v in val:
            if v == 'a' or v == 'b':
                continue
            else:
                print('Ошибка ввода')
                break
        break

milk, step = 0, 0
for symbol in val:
    if symbol == 'b':
        milk += step * 2 + 2
    step += 1

print(f'В день будет произведено {milk} литров молока')