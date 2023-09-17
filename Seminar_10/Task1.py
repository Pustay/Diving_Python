# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi

class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def length(self):
        return round(2 + pi * self.radius, 2)

    def area(self):
        return round(pi * self.radius ** 2, 2)

krug = Circle(5)

print(krug.length())
print(krug.area())