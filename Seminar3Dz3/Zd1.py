# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# результирующем списке не должно быть дубликатов.

items = [0, 1, 1, 2, 2, 5, 6, 7, 7, 8, 9]

all_set = set()
for item in items:
    if items.count(item) > 1:
        all_set.add(item)

print("Исходный список ->", items)
print("Cписок с дублирующимися элементами ->", list(all_set))