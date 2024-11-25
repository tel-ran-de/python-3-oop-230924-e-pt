class Car:
    wheel = 4

    def __init__(self):
        self.fuel = 100
        self.distance = 200
        print(f'Class car __init__(fuel={self.fuel}, distance={self.distance})')


class Truck(Car):
    def __init__(self, weight):
        super().__init__()
        self.weight = weight
        print(f'Class Truck __init__(weight={self.weight})')


class Light_car(Car):
    def __init__(self, passengers):
        super().__init__()
        self.passengers = passengers
        print(f'Class Light_car __init__(passengers={self.passengers})')


def main():
    # print('Base class "Car"')
    # car1 = Car()
    # print(car1.wheel)
    # print(car1.fuel)
    # print('Change fuel')
    # car1.fuel = 50
    # print(car1.fuel)

    print('\nClass "Truck"')
    truck1 = Truck(weight=100)
    print(truck1.wheel)
    print(truck1.fuel)
    print(truck1.distance)

    print('\nClass "Light_car"')
    light_car1 = Light_car(passengers=100)
    print(light_car1.wheel)
    print(light_car1.fuel)
    print(light_car1.distance)
    print(light_car1.passengers)
    

if __name__ == "__main__":
    main()
