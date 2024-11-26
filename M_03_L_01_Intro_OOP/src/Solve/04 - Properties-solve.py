# Ex 1
# Создайте класс `Employee` с приватными атрибутами `__name` и `__salary`.
# Реализуйте геттеры и сеттеры для этих атрибутов, добавив проверку,
# что зарплата не может быть ниже минимальной зарплаты (например, 10000).

# Ex 2
# Создайте класс `Circle` с приватным атрибутом `__radius`.
# Реализуйте свойства (property) для получения и установки значения радиуса,
# а также метод для вычисления площади круга.

import math


class Employee:
    MIN_SALARY = 10000  # Минимальная зарплата

    def __init__(self, name, salary):
        """Инициализация сотрудника с именем и зарплатой."""
        self.__name = name
        self.__salary = None  # Приватный атрибут
        self.set_salary(salary)  # Устанавливаем зарплату через сеттер, чтобы применить проверку

    # Геттер для имени
    def get_name(self):
        """Возвращает имя сотрудника."""
        return self.__name

    # Сеттер для имени
    def set_name(self, name):
        """Устанавливает имя сотрудника."""
        if not name.strip():
            print("Name cannot be empty.")
        else:
            self.__name = name
            print(f"Name set to {self.__name}")

    # Геттер для зарплаты
    def get_salary(self):
        """Возвращает зарплату сотрудника."""
        return self.__salary

    # Сеттер для зарплаты
    def set_salary(self, salary):
        """Устанавливает зарплату сотрудника с проверкой на минимальное значение."""
        if salary < self.MIN_SALARY:
            print(f"Salary cannot be less than {self.MIN_SALARY}.")
        else:
            self.__salary = salary
            print(f"Salary set to {self.__salary}")


class Circle:
    def __init__(self, radius):
        """Инициализация круга с заданным радиусом."""
        self.__radius = None
        self.radius = radius  # Устанавливаем радиус через свойство

    @property
    def radius(self):
        """Геттер для радиуса."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Сеттер для радиуса с проверкой на корректность."""
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self.__radius = value

    def area(self):
        """Вычисляет площадь круга."""
        return math.pi * (self.__radius ** 2)


def main():
    # Пример использования:
    print("Class Employee example")
    # Создаем сотрудника
    employee = Employee("Alice", 12000)

    # Получаем имя и зарплату
    print(f"Employee Name: {employee.get_name()}")
    print(f"Employee Salary: {employee.get_salary()}")

    # Изменяем имя
    employee.set_name("Bob")

    # Устанавливаем новую зарплату
    employee.set_salary(15000)

    # Пытаемся установить слишком низкую зарплату
    employee.set_salary(9000)

    # Получаем текущие данные сотрудника
    print(f"Updated Employee Name: {employee.get_name()}")
    print(f"Updated Employee Salary: {employee.get_salary()}")

    # Пример использования:
    print("\nClass Circle example")
    # Создаем круг
    circle = Circle(5)

    # Получаем радиус
    print(f"Radius: {circle.radius}")

    # Устанавливаем новый радиус
    circle.radius = 10
    print(f"Updated Radius: {circle.radius}")

    # Вычисляем площадь круга
    print(f"Area: {circle.area()}")

    # Попытка установить некорректный радиус
    try:
        circle.radius = -3
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
