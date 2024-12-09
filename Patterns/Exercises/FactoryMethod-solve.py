# Есть несколько типов транспорта, которые используются для доставки:
# Грузовик (Truck) — подходит для наземной доставки и может перевезти до 100 тонн груза.
# Корабль (Ship) — используется для доставки по воде и может перевезти до 500 тонн груза.

# Вам нужно реализовать:
# Базовый класс Transport, который задает общий интерфейс для всех видов транспорта.
# Классы-наследники для каждого вида транспорта (Truck, Ship) и объем перевозимого на каждом типе груза.
# Фабричный метод в базовом классе, который будет реализован в подклассах:
# Класс TruckFactory должен создавать объекты Truck.
# Класс ShipFactory должен создавать объекты Ship.
# Требования:
#
# Каждый вид транспорта должен уметь выполнять метод deliver, который принимает общее количество груза,
# выводит, как именно он доставляет груз (например, "Доставка на грузовике") и возвращает количество груза
# которое не вошло в данный транспорт.
# Фабричный метод должен находиться в классах TruckFactory и ShipFactory, и использоваться для создания объектов
# Truck и Ship.

# Напишите код, чтобы разобрать общий груз по типам доставки с использованием полиморфизма и фабричного метода.
# Выведите каким набором транспорта вы смогли перевезти заявленный груз.

from abc import ABC, abstractmethod


# Базовый класс Transport
class Transport(ABC):
    def __init__(self, capacity):
        self.capacity = capacity  # Максимальная вместимость транспорта

    @abstractmethod
    def deliver(self, cargo):
        """Метод доставки, который должен быть реализован в подклассах."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with capacity {self.capacity}"


# Класс Truck
class Truck(Transport):
    def deliver(self, cargo):
        """Доставка грузовиком."""
        if cargo <= self.capacity:
            print(f"Delivering {cargo} units by truck.")
            return 0  # Весь груз помещается
        else:
            print(f"Delivering {self.capacity} units by truck. {cargo - self.capacity} units left.")
            return cargo - self.capacity  # Остаток груза


# Класс Ship
class Ship(Transport):
    def deliver(self, cargo):
        """Доставка кораблем."""
        if cargo <= self.capacity:
            print(f"Delivering {cargo} units by ship.")
            return 0  # Весь груз помещается
        else:
            print(f"Delivering {self.capacity} units by ship. {cargo - self.capacity} units left.")
            return cargo - self.capacity  # Остаток груза


# Базовый класс фабрики TransportFactory
class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self):
        """Фабричный метод для создания транспорта."""
        pass


# Фабрика для грузовиков
class TruckFactory(TransportFactory):
    def create_transport(self):
        return Truck(capacity=100)  # Грузовик с вместимостью 100


# Фабрика для кораблей
class ShipFactory(TransportFactory):
    def create_transport(self):
        return Ship(capacity=500)  # Корабль с вместимостью 500


# Клиентский код
def distribute_cargo(total_cargo):
    remaining_cargo = total_cargo
    factories = []
    while remaining_cargo > 0:
        if remaining_cargo >= 500:
            factories.append(ShipFactory().create_transport())
            remaining_cargo = factories[-1].deliver(remaining_cargo)
        elif 500 > remaining_cargo >= 100:
            factories.append(Truck(100))
            remaining_cargo = factories[-1].deliver(remaining_cargo)
        else:
            factories.append(Truck(100))
            factories[-1].deliver(remaining_cargo)
            break

    print(*factories, sep=', ')


def main():
    # Пример использования
    distribute_cargo(750)


if __name__ == "__main__":
    main()
