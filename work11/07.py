from math import pi

radius = float(input('Введите радиус случайной планеты: '))
v_land = 10.8321 * 10**11
v_planet = 4/3 * pi * radius ** 3

result = round((v_land / v_planet), 3)

if result > 1:
    print(f'Объём планеты Земля больше в {result} раз')
else:
    print(f'Объём планеты Земля меньше в {result} раз')