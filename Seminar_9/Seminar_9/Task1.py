# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток
# Внутри есть функция, которая запрашивает у пользователя число

import random
from typing import Callable

def guess_number(low: int = 10, high: int = 100, tries: int = 10) -> Callable:
    number = random.randint(low, high)
    
    def guess_game():
        count = 1
        while count <= tries:
            my_num = int(input(f'{count} попытка. Введите число от {low} до {high}: '))
            if my_num > number:
                print('Я загадал меньше')
            elif my_num < number:
                print('Я загадал больше')
            else:
                print(f'Да ты победил, я загадал {number}')
                break
            count += 1
        else:
            print("Извени, но ты проиграл, все попытки закончились")
    
    return guess_game

game = guess_number(1, 1000, 12)

game()