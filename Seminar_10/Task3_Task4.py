# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from random import randint

class Human:


    def __init__(self, last_name: str, name: str, age: int, patronymic: str = None):
        self._name = name
        self._last_name = last_name
        self._patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age +=1

    def get_age(self):
        return self._age

    def full_name(self):
        return (f'{self._last_name} {self._name} {"" if self._patronymic is None else (self._patronymic + " ")}ему'
                f'{self._age} лет')


class Employee(Human):
    def __init__(self, last_name, name, age, patronymic):
        super().__init__(last_name, name, age, patronymic)
        self.u_id = str(random.randint(1, 999999)).zfill(0)
        self.lvl_access = int(self.u_id % 7)

stone = Employee('Панфилов', 'Кирилл', 39, 'Владимирович')

print(stone.u_id)
print(stone.lvl_access)

alisa = Human('Худякова', 'Алиса', 18)

print(stone.full_name())
print(alisa.full_name())
stone.birthday()
print(stone.full_name())
print(alisa.full_name())



