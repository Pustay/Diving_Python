# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

from operator import itemgetter

list = {'Рюкзак': 2, 'Палатка': 10, 'Мангал': 3, 'Котелок': 2, 'Спальник': 2, 'Нож': 1.2, 'Топор': 3, 'Фляжка': 1.5, 'Спички': 0.5, 'Вода': 4, 'Консервы':6 }
max_limit = 23
weight = 0
capacity = 0
print("Рюкзак: ", list)
print("Список вещей в", max_limit, "кг")
for things, value in dict(sorted(list.items(), key=itemgetter(1))).items():
    weight += list[things]

    if weight <= max_limit:
        print(things, ' = ', value)
        capacity += list[things]

print("Весь вес содержимого:",capacity)
