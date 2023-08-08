# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число в десятичной системе: '))

print(f'Встроенная функция hex -> {hex(num)}')

def hex(number: int) -> str:
    if not number:
        return '0 x 0'
    result = ''
    my_hex = list('0123456789abcdef')
    while number > 0:
        result = my_hex[number % 16] + result
        number //= 16
    return '0x' + result

print(f'Собственная функция hex -> {hex(num)}')