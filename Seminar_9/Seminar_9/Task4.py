# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

import json
import os

def decor(loop: int):
    def inner(func):
        result = []

        def wrapper(*args, **kwargs):
            for _ in range(loop):
                result.append(func(*args, **kwargs))
            return result

        return wrapper
    return inner

@decor(5)
def function_(a, b):
    return a + b

print(function_(3, 4))