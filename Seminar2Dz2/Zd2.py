# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

class SelfFraction:
    def __init__(myself, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise ValueError
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            nod = SelfFraction.check_nod(numerator, denominator)
            myself.num = numerator // nod
            myself.den = denominator // nod

    def __add__(myself, other):
        main_den = myself.den * other.den
        main_num = myself.num * other.den + other.num * myself.den
        return SelfFraction(main_num, main_den)

    def __mul__(myself, other):
        main_num = myself.num * other.num
        main_den = myself.den * other.den
        return SelfFraction(main_num, main_den)

    @staticmethod
    def check_nod(num: int, den: int) -> int:
        nod = 1
        for i in range(1, max(num, den) // 2 + 1):
            if num % i == 0 and den % i == 0:
                nod = i
        return nod

    def __str__(myself):
        return f'{myself.num}/{myself.den}'


fract_1 = input('Введите первую дробь формата a/b: ').split('/')
fract_2 = input('Введите вторую дробь формата a/b: ').split('/')

myself_fract_1 = SelfFraction(int(fract_1[0]), int(fract_1[1]))
myself_fract_2 = SelfFraction(int(fract_2[0]), int(fract_2[1]))
original_fract_1 = Fraction(int(fract_1[0]), int(fract_1[1]))
original_fract_2 = Fraction(int(fract_2[0]), int(fract_2[1]))

print(f'Сумма дробей -> {myself_fract_1 + myself_fract_2}')
print(f'Проверка -> {original_fract_1 + original_fract_2}')

print(f'Произведение дробей -> {myself_fract_1 * myself_fract_2}')
print(f'Проверка -> {original_fract_1 * original_fract_2}')