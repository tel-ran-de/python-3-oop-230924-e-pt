# Проверка иерархии классов для геометрических фигур.
#
# Создайте иерархию классов для различных геометрических фигур.
# Используйте функцию issubclass() для проверки, являются ли определенные классы подклассами других классов
# в этой иерархии.
#
# Шаги:
# Создайте базовый класс Shape.
# Создайте подклассы Circle, Rectangle, и Triangle, которые наследуются от Shape.
# Создайте подкласс Square, который наследуется от Rectangle.
# Напишите функцию, которая принимает два класса и возвращает, является ли первый класс подклассом второго.
# Протестируйте функцию с использованием созданных классов.

class Shape:
    pass


class Circle(Shape):
    pass


class Rectangle(Shape):
    pass


class Triangle(Shape):
    pass


class Square(Rectangle):
    pass


def check_subclass(cls1, cls2):
    return issubclass(cls1, cls2)


def main():
    # Тестирование
    print(check_subclass(Square, Rectangle))  # Output: True
    print(check_subclass(Square, Shape))  # Output: True
    print(check_subclass(Circle, Rectangle))  # Output: False
    print(check_subclass(Triangle, Shape))  # Output: True


if __name__ == "__main__":
    main()
