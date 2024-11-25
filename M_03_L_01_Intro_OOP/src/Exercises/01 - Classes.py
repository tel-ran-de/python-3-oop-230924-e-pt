# Ex 1
# Создайте базовый класс `Person` с атрибутами `name` и `age`.
# Затем создайте два производных класса `Student` и `Teacher`.
# Класс `Student` должен иметь дополнительный атрибут `student_id`, а класс `Teacher` — атрибут `subject`.
# Реализуйте методы для вывода информации о каждом объекте.

# Ex 2
# Создайте класс `Vehicle` с атрибутами `make` и `model`.
# Создайте производный класс `Car` с дополнительным атрибутом `num_doors` (количество дверей) и
# производный класс `Motorcycle` с атрибутом `has_sidecar` (имеет ли мотоцикл коляску).
# Реализуйте метод, который выводит полное описание транспортного средства.

class Person:
    """
    Base class Person
    attributes:
        name: string
        age: int
    """
    pass  # you code here


class Student(Person):
    """
    Class Student
    attributes: student_id: int
    """
    pass  # you code here


class Teacher(Person):
    """
    Class Teacher
    attributes: subject: string
    """
    pass  # you code here


class Vehicle:
    """
    Class Vehicle
    attributes:
        make: string
        model: string
    """
    pass  # you code here


class Car(Vehicle):
    """
    Class Car
    attributes:
        num_doors: int
    """
    pass  # you code here


class Motorcycle(Vehicle):
    """
    Class Motorcycle
    attributes:
        has_sidecar: bool
    """
    pass  # you code here


def main():
    pass  # you code here


if __name__ == '__main__':
    main()
