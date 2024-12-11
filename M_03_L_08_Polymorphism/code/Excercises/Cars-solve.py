# Создайте иерархию классов, которая описывает машины.
# Есть базовый класс Car.
#  Также есть два класса - PassengerCar и Truck,
#  которые наследуются от Car.
# В классах наследниках определить методы количества пассажиров и грузоподъемность авто соответственно для класса
# PassengerCar и Truck.
# Вывести класс Pickup который будет наследоваться от классов PassengerCar и Truck
# и определять одновременно и количество пассажиров и грузоподъемность.
# Проверить передачу параметров из конструктора класса Pickup в конструкторы классов предков

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class PassengerCar(Car):
    def __init__(self, passengers, **kwargs):
        super(PassengerCar, self).__init__(**kwargs)
        self.passengers = passengers

    def __str__(self):
        return f"{super().__str__()} with {self.passengers} passengers"


class Truck(Car):
    def __init__(self, capacity, **kwargs):
        super(Truck, self).__init__(**kwargs)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()} with capacity of {self.capacity} tons"


class Pickup(PassengerCar, Truck):
    def __init__(self, **kwargs):
        super(Pickup, self).__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()}"


def main():
    # Проверка передачи параметров в конструкторы классов-предков
    pickup = Pickup(make="Toyota", model="Hilux", year=2023, passengers=5, capacity=1.5)
    print(pickup)
    print(Pickup.__mro__)


if __name__ == "__main__":
    main()
