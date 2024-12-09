# Создайте абстрактный класс Device, который определяет абстрактные методы turn_on() и turn_off().
# Затем создайте несколько подклассов, таких как Laptop, Smartphone и Tablet, которые реализуют эти методы
# для включения и выключения устройств.
#
# Используйте полиморфизм, чтобы создать функцию, которая принимает список устройств и выполняет действия
# включения и выключения для каждого устройства.

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Laptop(Device):
    def turn_on(self):
        return "Laptop is turned on."
    def turn_off(self):
        return "Laptop is turned off."


class Smartphone(Device):
    def turn_on(self):
        return "Smartphone is turned on."
    def turn_off(self):
        return "Smartphone is turned off."


class Tablet(Device):
    def turn_on(self):
        return "Tablet is turned on."
    def turn_off(self):
        return "Tablet is turned off."


def main():
    def operate_devices(devices_list):
        for device in devices_list:
            print(device.turn_on())
            print(device.turn_off())

    # Тестирование
    devices = [Laptop(), Smartphone(), Tablet()]
    operate_devices(devices)


if __name__ == "__main__":
    main()

# Laptop is turned on.
# Laptop is turned off.
# Smartphone is turned on.
# Smartphone is turned off.
# Tablet is turned on.
# Tablet is turned off.
