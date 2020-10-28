
meter = int(input('Сколько метров уже выкапано: '))
k = int(input('Через сколько метров посажена картошка: '))
potatoes_summ = 0

for value in range(meter, 101, k):
    potatoes_summ += 3

print(f'Антон соберет {potatoes_summ} клубней картошки.')









