''' 
В организации есть два типа людей: сотрудники и обычные люди. 
Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) 
Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), 
который должен быть шестизначным положительным целым числом.

Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для 
управления данными о людях (Фамилия, Имя, Отчество, Возраст). 
Класс должен проверять валидность входных данных и генерировать 
исключения InvalidNameError и InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и 
добавлять уникальный идентификационный номер (ID). 
Класс Employee также должен проверять валидность ID и генерировать 
исключение InvalidIdError, если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника 
на основе суммы цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить, 
что исключения работают корректно при передаче неверных данных.

'''

class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name:
            raise InvalidNameError(f"Invalid name: {last_name}. Name should be a non-empty string.")
        if not last_name or not first_name or not middle_name:
            raise InvalidNameError(f"Invalid name: {first_name}. Name should be a non-empty string.")
        if not middle_name:
            raise InvalidNameError(f"Invalid name: {middle_name}. Name should be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id_number):
        super().__init__(last_name, first_name, middle_name, age)
        if not isinstance(id_number, int) or id_number < 100000 or id_number > 999999:
            raise InvalidIdError(
                f"Invalid id: {id_number}. Id should be a 6-digit positive integer between 100000 and 999999.")

        self.id_number = id_number

    def get_level(self):
        return sum([int(digit) % 7 for digit in str(self.id_number)])

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.id_number}, Level: {self.get_level()}"