class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


def main():
    # Тестирование
    v1 = Vector(6, 9)
    v2 = Vector(3, 4)

    print(v1 + v2)  # Output: Vector(9, 13)
    print(v1 - v2)  # Output: Vector(3, 5)
    print(v1 * 2)  # Output: Vector(12, 18)
    print(v2 / 3)  # Output: Vector(2.0, 3.0)


if __name__ == "__main__":
    main()
