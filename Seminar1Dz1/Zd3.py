# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:

# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
answer = None
defeat = False
attempt = 0

print("Я загадал число от 0 до 1000. У тебя есть 10 попыток, чтобы его угадать).")
while attempt < 10:
    answer = int(input("Введи число: "))
    attempt += 1
    if answer == num:
        print(f"Ура! Ты угадал число {num} за {attempt} попыток.")
        answer = True
        break
    elif answer < num:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")

print(f"У тебя закончились попытки. Загаданное число было {num}." if not defeat else '')