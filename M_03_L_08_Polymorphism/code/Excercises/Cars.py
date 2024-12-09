# Создайте иерархию классов, которая описывает машины.
# Есть базовый класс Car.
#  Также есть два класса - PassengerCar и Truck,
#  которые наследуются от Car.
# В классах наследниках определить методы количества пассажиров и грузоподъемность авто соотвественно для класса
# PassengerCar и Truck.
# Вывести класс Pickup который будет наследоваться от классов PassengerCar и Truck
# и определять одновременно и количесво пассажаиров и грузоподъемность.
# Проверить передачу параметров из конструктора класса Pickup в конструкторы классов предков

class Car:
    pass


class PassengerCar(Car):
    pass


class Truck(Car):
    pass


class Pickup(PassengerCar, Truck):
    pass


def main():
    # Проверка передачи параметров в конструкторы классов-предков
    pickup = Pickup(make="Toyota", model="Hilux", year=2023, passengers=5, capacity=1.5)
    print(pickup)


if __name__ == "__main__":
    main()

# 2023 Toyota Hilux with capacity of 1.5 tons with 5 passengers
