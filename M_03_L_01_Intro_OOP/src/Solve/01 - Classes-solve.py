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

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    """
    Class Student
    attributes:
        student_id: int
    """

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Teacher(Person):
    """
    Class Teacher
    attributes:
        subject: string
    """

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class Vehicle:
    """
    Class Vehicle
    attributes:
        make: string
        model: string
    """

    def __init__(self, make, model):
        self.make = make
        self.model = model


class Car(Vehicle):
    """
    Class Car
    attributes:
        num_doors: int
    """

    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors


class Motorcycle(Vehicle):
    """
    Class Motorcycle
    attributes:
        has_sidecar: bool
    """

    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar


def main():
    person_1 = Person('John', 25)
    print(f'Person: {person_1.name}, {person_1.age}')

    student_1 = Student('John', 25, 123)
    print(f'Student: {student_1.name}, {student_1.age}, {student_1.student_id}')

    teacher_1 = Teacher('John', 25, 'Math')
    print(f'Teacher: {teacher_1.name}, {teacher_1.age}, {teacher_1.subject}')

    vehicle = Vehicle('Toyota', 'Corolla')
    print(f'Vehicle: {vehicle.make}, {vehicle.model}')

    car = Car('Toyota', 'Corolla', 4)
    print(f'Car: {car.make}, {car.model}, {car.num_doors}')

    motorcycle = Motorcycle('Honda', 'CBR', True)
    print(f'Motorcycle: {motorcycle.make}, {motorcycle.model}, {motorcycle.has_sidecar}')


if __name__ == '__main__':
    main()
