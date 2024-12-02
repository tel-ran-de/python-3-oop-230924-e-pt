# Создайте класс ComplexNumber, который будет представлять комплексные числа.
# Перегрузите различные магические методы для выполнения арифметических операций, сравнения и для
# управления атрибутами воспользуйтесь методами установки атрибутов.
# Добавьте логирование времени исполнения операций хеширования с помощью класс декоратора TimeLogger

# Классы-декораторы
class TimeLogger:
    pass

class ComplexNumber:
    pass


def main():
    # Тестирование
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = ComplexNumber(1, 2)

    # Арифметические операции
    print(c1 + c2)  # Output: (4 + 6i)
    print(c1 - c2)  # Output: (-2 + -2i)
    print(c1 * c2)  # Output: (-5 + 10i)
    print(c1 / c2)  # Output: (0.44 + 0.08i)

    # Сравнения
    print(c1 == c3)  # Output: True
    print(c1 != c2)  # Output: True
    print(c1 < c2)  # Output: True
    print(c1 <= c3)  # Output: True
    print(c1 > c2)  # Output: False
    print(c1 >= c3)  # Output: True

    # Хеширование и использование в set
    complex_set = {c1, c2, c3}
    print(complex_set)  # Output: {ComplexNumber(1, 2), ComplexNumber(3, 4)}

    # Управление атрибутами
    c1.new_attr = 10  # Setting attribute new_attr to 10
    print(c1.new_attr)  # Getting attribute new_attr
    del c1.new_attr  # Deleting attribute new_attr

    # Вызов объекта
    c1()  # Output: ComplexNumber called with (1 + 2i)

    # Представление объекта
    print(str(c1))  # Output: (1 + 2i)
    print(repr(c1))  # Output: ComplexNumber(1, 2)

    # Длина и абсолютное значение
    print(len(c1))  # Output: 2
    print(abs(c1))  # Output: 2.23606797749979def main():
    # Тестирование
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = ComplexNumber(1, 2)

    # Арифметические операции
    print(c1 + c2)  # Output: (4 + 6i)
    print(c1 - c2)  # Output: (-2 + -2i)
    print(c1 * c2)  # Output: (-5 + 10i)
    print(c1 / c2)  # Output: (0.44 + 0.08i)

    # Сравнения
    print(c1 == c3)  # Output: True
    print(c1 != c2)  # Output: True
    print(c1 < c2)  # Output: True
    print(c1 <= c3)  # Output: True
    print(c1 > c2)  # Output: False
    print(c1 >= c3)  # Output: True

    # Хеширование и использование в set
    complex_set = {c1, c2, c3}
    print(complex_set)  # Output: {ComplexNumber(1, 2), ComplexNumber(3, 4)}

    # Управление атрибутами
    c1.new_attr = 10  # Setting attribute new_attr to 10
    print(c1.new_attr)  # Getting attribute new_attr
    del c1.new_attr  # Deleting attribute new_attr

    # Вызов объекта
    c1()  # Output: ComplexNumber called with (1 + 2i)

    # Представление объекта
    print(str(c1))  # Output: (1 + 2i)
    print(repr(c1))  # Output: ComplexNumber(1, 2)

    # Длина и абсолютное значение
    print(len(c1))  # Output: 2
    print(abs(c1))  # Output: 2.23606797749979

if __name__ == "__main__":
    main()

