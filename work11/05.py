from time import sleep

size_file = float(input('Укажите размер файла для скачивания: '))
speed = float(input('Какова скорость вашего соединения? '))
time = 0
download = 0
loading = 0

while download < size_file:
    sleep(1)
    download += speed
    if download > size_file:
        download = size_file
    time += 1
    loading = int(download * 100 / size_file)
    print(f'Прошло {time} сек. Скачано {int(download)} из {int(size_file)} Мб ({loading}%)')

