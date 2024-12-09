# Создайте абстрактный класс Shape, который определяет абстрактный метод area().
# Затем создайте несколько подклассов, таких как Circle, Rectangle и Triangle,
# которые реализуют метод area() для вычисления площади соответствующих фигур.
#
# Используйте полиморфизм, чтобы создать функцию, которая принимает список фигур и выводит их площади.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    pass


class Circle(Shape):
    pass


class Rectangle(Shape):
    pass


class Triangle(Shape):
    pass


def main():
    def print_areas(shapes):
        for shape in shapes:
            print(f"Area: {shape.area()}")

    # Тестирование
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)]
    print_areas(shapes)


if __name__ == "__main__":
    main()

# Area: 78.53981633974483
# Area: 24
# Area: 10.5