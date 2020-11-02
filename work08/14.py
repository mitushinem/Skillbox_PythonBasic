
boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
result = ''

if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения')
elif boys > girls:
    k = boys - girls
    for bgb in range(k):
        result += 'BGB'
    for bg in range(girls - k):
        result += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        result += 'GBG'
    for gb in range(boys - k):
        result += 'GB'

print(result)