# Напишите класс Vector, который реализует методы математических операций и сравнения

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) <= (other.x**2 + other.y**2)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vector):
            return (self.x**2 + self.y**2) >= (other.x**2 + other.y**2)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


def main():
    # Примеры использования
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(1, 2)

    # Арифметические операции
    print(v1 + v2)  # Output: Vector(4, 6)
    print(v1 - v2)  # Output: Vector(-2, -2)
    print(v1 * 3)  # Output: Vector(3, 6)
    print(v1 / 2)  # Output: Vector(0.5, 1.0)

    # Сравнения
    print(v1 == v2)  # Output: False
    print(v1 == v3)  # Output: True
    print(v1 != v2)  # Output: True
    print(v1 < v2)  # Output: True (сравнение по длине вектора)
    print(v1 <= v2)  # Output: True (сравнение по длине вектора)
    print(v1 > v2)  # Output: False (сравнение по длине вектора)
    print(v1 >= v2)  # Output: False (сравнение по длине вектора)


if __name__ == "__main__":
    main()
