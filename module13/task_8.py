print('Задача 8. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
#
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
#
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
#
# Известно, что глубина точно больше нуля и меньше четырёх метров.
#
# Обеспечьте контроль ввода.
#
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
#
# Приблизительная глубина безопасной кладки: 0.732421875 м


def xxx(level):
    # 1x ** 3 − 3x ** 2 − 12x + 10-level = 0
    # a_1 * x^3 - b_1 * x^2 - c_1 * x + d = 0

    # x^3 - a * x^2 - c * x + c = 0

    # a =  3
    # b =  12
    # c =  10-level
    pass


max_level = float(input('Введите максимально допустимый уровень опасности: '))
