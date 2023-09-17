# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform
MIN_SIZE = -1000
MAX_SIZE = 1000
print('\n'.join([f'{randint(MIN_SIZE, MAX_SIZE):>5} | {uniform(MIN_SIZE, MAX_SIZE):.3f}' for i in range(10)]))