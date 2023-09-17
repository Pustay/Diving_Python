# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, side_a: float, side_b: float = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b

    def length(self):
        return (self.side_a + self.side_b) * 2


    def area(self):
        return self.side_a * self.side_b

rec1 = Rectangle(5,6)

print(rec1.length())
print(rec1.area())