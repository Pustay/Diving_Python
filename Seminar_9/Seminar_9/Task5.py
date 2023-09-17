# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте: (задача 1)
# декораторами для сохранения параметров,
# декоратором контроля значений и
# декоратором для многократного запуска.
# Выберите верный порядок декораторов.

import json
import os
import random
from typing import Callable

def json_safe(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not os.path.exists(f'result.json'):
            print(result)
            with open(f'result.json', 'w', encoding='utf-8') as f:
                atr = ','.join(list(map(str, args))) + '|' + ','.join(
                    list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                json.dump({atr: result},  f, indent=4, ensure_ascii=False)

        else:
            with open(f'result.json', 'r', encoding='utf-8') as f_read:
                json_data = json.load(f_read)
            print(json_data)
            with open(f'result.json', 'w', encoding='utf-8') as f_write:
                atr = ','.join(list(map(str, args))) + '|' + ','.join(
                    list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                json_data[atr] = result
                json.dump(json_data, f_write, indent= 4, ensure_ascii=False)

        return result
    
    return wrapper

def decor(loop: int):
    def inner(func):
        result = []

        def wrapper(*args, **kwargs):
            for _ in range(loop):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    
    return inner

def check_nums(func: Callable):
    def wrapper(l_lim: int, h_lim: int, tries_: int):
        if l_lim > h_lim or l_lim< 0 or h_lim > 100:
            l_lim = 1
            h_lim = 100
        if 0 < tries_ < 11:
            tries_ = random.randint(1, 10)

        result = func(l_lim, h_lim, tries_)
        return result
    
    return wrapper

@decor(3)
@json_safe
@check_nums

def guess_number(low: int = 10, high: int = 100, tries: int = 10) -> str:
    count = 1
    number = random.randint(low, high)
    while count <= tries:
        my_num = int(input(f'{count}  из {tries}  попытка. Введите число от {low} до {high}: '))
        if my_num > number:
            print('Я загадал меньше')
        elif my_num < number:
            print('Я загадал больше')
        else:
            result = f'Да ты победил c {count} попытки, я загадал {number}'
            break
        count += 1
    else:
        result = "Извени, но ты проиграл, все попытки закончились"
    print(result)
    return result
    

guess_number(-1, 1000, 15)