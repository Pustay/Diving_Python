# Погружение в Python (семинары)
## Урок 1. Основы Python

### Задача 1
✔Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

### Задача 2
✔Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

### Задача 3
✔Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

## Урок 2. Простые типы данных

### Задача 1
✔Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

### Задача 2
✔Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

## Урок 3. Коллекции

### Задача 1
✔Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

### Задача 2
✔В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

### Задача 3
✔Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

## Урок 4. Функции

### Задача 1
✔Напишите функцию для транспонирования матрицы

### Задача 2
✔Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
