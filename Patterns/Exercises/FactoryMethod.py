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


# Клиентский код
def distribute_cargo(total_cargo):
    remaining_cargo = total_cargo
    factories = []
    while remaining_cargo > 0:
        if remaining_cargo >= 500:
            factories.append(Ship(500))
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

# Delivering 500 units by ship. 250 units left.
# Delivering 100 units by truck. 150 units left.
# Delivering 100 units by truck. 50 units left.
# Delivering 50 units by truck.
# Ship with capacity 500, Truck with capacity 100, Truck with capacity 100, Truck with capacity 100
