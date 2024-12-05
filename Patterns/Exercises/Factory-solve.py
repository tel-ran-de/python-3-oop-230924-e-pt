# Задача:
#
# Реализуйте паттерн Factory для создания различных видов транспорта (автомобили, велосипеды, самолеты).
#
# Шаги:
# Создайте базовый класс для транспорта.
# Создайте классы для конкретных видов транспорта.
# Реализуйте фабрику для создания транспорта по типу.

class Transport:
    def move(self):
        raise NotImplementedError


class Car(Transport):
    def move(self):
        return "Car is moving"


class Bike(Transport):
    def move(self):
        return "Bike is moving"


class Plane(Transport):
    def move(self):
        return "Plane is flying"


class TransportFactory:
    @staticmethod
    def create_transport(transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "bike":
            return Bike()
        elif transport_type == "plane":
            return Plane()
        else:
            raise ValueError("Unknown transport type")


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
