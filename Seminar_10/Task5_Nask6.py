# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, type, age):
        self.__name, self.__age = type, age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Fish(Animal):

    def __init__(self, type, age, color):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__color = color

    def get_specific(self):
        return self.__color


class Mammal(Animal):

    def __init__(self, type, age, wool):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__wool = wool

    def get_specific(self):
        return self.__wool


class Bird(Animal):

    def __init__(self, type, age, feather):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__feather = feather

    def get_specific(self):
        return self.__feather

bird = Bird("Попугай", 3, "Белое")
fish = Fish("Дори", 1, "Голубая")
mammal = Mammal("Тузик", 9, "Чёрный")
print(f'Имя: {bird.get_name()}, Возраст: {bird.get_age()}, {bird.get_specific()}')
print(f'Имя: {fish.get_name()}, Возраст: {fish.get_age()}, {fish.get_specific()}')
print(f'Имя: {mammal.get_name()}, Возраст: {mammal.get_age()}, {mammal.get_specific()}')