# Напишите класс Vector, который реализует методы математических операций и сравнения

class Vector:
    pass


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


# Vector(4, 6)
# Vector(-2, -2)
# Vector(3, 6)
# Vector(0.5, 1.0)
# False
# True
# True
# True
# True
# False
# False
