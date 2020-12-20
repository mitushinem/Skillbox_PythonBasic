while True:
    hour = int(input('Часов: '))
    minute = int(input('Минут: '))
    second = int(input('Секунд: '))

    if (0 <= hour < 12) and (0 <= minute < 60) and (0 <= second < 60):
        break

result = round((30 * (hour + (minute + .016 * second)/60)), 5)

print(result)
