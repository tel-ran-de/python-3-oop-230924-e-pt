# Задание 1: Реализация геттера и сеттера для класса Person
# Описание:
#
# Создайте класс Person, который будет иметь приватные атрибуты name и age.
# Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
#
# Требования:
#
# Приватные атрибуты __name и __age.
# Методы get_name и set_name для доступа и изменения атрибута __name.
# Методы get_age и set_age для доступа и изменения атрибута __age.
# Проверка, что возраст не может быть отрицательным.
#
# Задание 2: Реализация геттера и сеттера для класса Rectangle
# Описание:
#
# Создайте класс Rectangle, который будет иметь приватные атрибуты width и height.
# Реализуйте геттеры и сеттеры для этих атрибутов без использования декораторов.
#
# Требования:
#
# Приватные атрибуты __width и __height.
# Методы get_width и set_width для доступа и изменения атрибута __width.
# Проверка, что ширина должна быть положительной.
# Методы get_height и set_height для доступа и изменения атрибута __height.
# Проверка, что высота должна быть положительной.

class Person:
    pass

class Rectangle:
    pass


def main():
    # Ex 1
    # Создание объекта Person
    person = Person("Alice", 30)

    # Доступ и изменение атрибута name
    print(person.get_name())  # Output: Alice
    person.set_name("Bob")
    print(person.get_name())  # Output: Bob

    # Доступ и изменение атрибута age
    print(person.get_age())  # Output: 30
    person.set_age(35)
    print(person.get_age())  # Output: 35

    # Проверка валидации возраста
    try:
        person.set_age(-5)
    except ValueError as e:
        print(e)  # Output: Age must be non-negative

    # Ex 2
    # Создание объекта Rectangle
    rectangle = Rectangle(10, 20)

    # Доступ и изменение атрибута width
    print(rectangle.get_width())  # Output: 10
    rectangle.set_width(15)
    print(rectangle.get_width())  # Output: 15

    # Доступ и изменение атрибута height
    print(rectangle.get_height())  # Output: 20
    rectangle.set_height(25)
    print(rectangle.get_height())  # Output: 25

    # Проверка валидации высоты и ширины
    try:
        rectangle.set_width(-5)
    except ValueError as e:
        print(e)  # Output: Width must be positive

    try:
        rectangle.set_height(-10)
    except ValueError as e:
        print(e)  # Output: Height must be positive


if __name__ == "__main__":
    main()

# Alice
# Bob
# 30
# 35
# Age must be non-negative
# 10
# 15
# 20
# 25
# Width must be positive
# Height must be positive
