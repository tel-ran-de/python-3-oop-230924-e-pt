# Паттерн Factory создает объекты без указания конкретного класса создаваемого объекта.

class Shape:
    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        return "Drawing Circle"


class Square(Shape):
    def draw(self):
        return "Drawing Square"


class ShapeFactory:
    def __call__(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")


def main():
    factory = ShapeFactory()
    circle = factory("circle")
    square = factory("square")

    print(circle.draw())  # Output: Drawing Circle
    print(square.draw())  # Output: Drawing Square


if __name__ == "__main__":
    main()
