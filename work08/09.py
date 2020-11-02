
letter = int(input('Введите размер письма'))
step = 0

if letter <= 12:
    print(f'Письмо поместилось в конверт за {step} шагов')
else:
    for _ in range(letter, 0, -1):
        letter -= letter // 2
        step += 1
        if letter <= 12:
            print(f'Письмо поместилось в конверт за {step} шагов')
            break
