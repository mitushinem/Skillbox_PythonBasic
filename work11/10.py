
from math import degrees, radians

gradus = float(input('Введите угол тангажа в градусах: '))

g = gradus % 360

if degrees(-.28) <= g <= degrees(.28):
    print(f'Угол тангажа допустимый и составляет {g} градусов ( {radians(g)} радианы )')
else:
    print('Угол небезопасен!')