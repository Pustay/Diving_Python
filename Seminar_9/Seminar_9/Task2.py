# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

import random
from typing import Callable
from random import randint

def check_nums(func: Callable):
    def wrapper(low_: int, high_: int, tries_: int):
        if low_ == 1 and high_ == 100 and 0 < tries_ < 11:
            result = func(low_, high_, tries_)
        else:
            a, b = randint(1, 100), randint(1, 100)
            result = func(min(a, b), max(a, b), tries_)
        return result
    return wrapper 

@check_nums
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