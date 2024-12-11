# Создайте абстрактный класс Shape, который определяет абстрактный метод area().
# Затем создайте несколько подклассов, таких как Circle, Rectangle и Triangle,
# которые реализуют метод area() для вычисления площади соответствующих фигур.
#
# Используйте полиморфизм, чтобы создать функцию, которая принимает список фигур и выводит их площади.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def main():
    def print_areas(shapes):
        for shape in shapes:
            print(f"Area: {shape.area()}")

    # Тестирование
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)]
    print_areas(shapes)


if __name__ == "__main__":
    main()
