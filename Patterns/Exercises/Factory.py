# Задача:
#
# Реализуйте паттерн Factory для создания различных видов транспорта (автомобили, велосипеды, самолеты).
#
# Шаги:
# Создайте базовый класс для транспорта.
# Создайте классы для конкретных видов транспорта.
# Реализуйте фабрику для создания транспорта по типу.

class Transport:
    pass


class Car(Transport):
    pass


class Bike(Transport):
    pass


class Plane(Transport):
    pass


class TransportFactory:
    pass


def main():
    # Тестирование
    factory = TransportFactory()

    car = factory.create_transport("car")
    bike = factory.create_transport("bike")
    plane = factory.create_transport("plane")

    print(car.move())  # Output: Car is moving
    print(bike.move())  # Output: Bike is moving
    print(plane.move())  # Output: Plane is flying


if __name__ == "__main__":
    main()

# Car is moving
# Bike is moving
# Plane is flying