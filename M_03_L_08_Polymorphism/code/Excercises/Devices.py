# Создайте абстрактный класс Device, который определяет абстрактные методы turn_on() и turn_off().
# Затем создайте несколько подклассов, таких как Laptop, Smartphone и Tablet, которые реализуют эти методы
# для включения и выключения устройств.
#
# Используйте полиморфизм, чтобы создать функцию, которая принимает список устройств и выполняет действия
# включения и выключения для каждого устройства.

from abc import ABC, abstractmethod


class Device(ABC):
    pass


class Laptop(Device):
    pass


class Smartphone(Device):
    pass


class Tablet(Device):
    pass


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
