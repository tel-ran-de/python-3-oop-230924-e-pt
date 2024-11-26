# Ex 1
# Создайте базовый класс `Appliance` с методом `turn_on`, который должен быть переопределен в
# производных классах `WashingMachine` и `Refrigerator`.
# В каждом из производных классов метод `turn_on` должен выводить сообщение о том, что прибор включен.
# Создайте список различных приборов и продемонстрируйте полиморфизм, вызвав метод `turn_on` для каждого прибора.
#
# #### Задание 2:
# Создайте базовый класс `Employee` с методом `calculate_pay`,
# который должен быть переопределен в производных классах `SalariedEmployee` и `HourlyEmployee`.
# В классе `SalariedEmployee` метод должен рассчитывать ежемесячную зарплату на основе фиксированного оклада,
# а в классе `HourlyEmployee` — на основе количества отработанных часов и почасовой ставки.
# Продемонстрируйте полиморфизм, вызвав метод `calculate_pay` для объектов различных классов.

class Appliance:
    def turn_on(self):
        """Метод, который должен быть переопределен в производных классах."""
        raise NotImplementedError("This method should be overridden in a derived class")


class WashingMachine(Appliance):
    def turn_on(self):
        """Реализация метода для стиральной машины."""
        print("The washing machine is now ON.")


class Refrigerator(Appliance):
    def turn_on(self):
        """Реализация метода для холодильника."""
        print("The refrigerator is now ON.")


class Employee:
    def calculate_pay(self):
        """Метод, который должен быть переопределен в производных классах."""
        raise NotImplementedError("This method should be overridden in a derived class")


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        self.name = name
        self.annual_salary = annual_salary

    def calculate_pay(self):
        """Рассчитывает ежемесячную зарплату на основе фиксированного годового оклада."""
        monthly_pay = self.annual_salary / 12
        print(f"{self.name}'s monthly salary: {monthly_pay:.2f}")
        return monthly_pay


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        """Рассчитывает оплату на основе количества отработанных часов и почасовой ставки."""
        total_pay = self.hours_worked * self.hourly_rate
        print(f"{self.name}'s pay for {self.hours_worked} hours: {total_pay:.2f}")
        return total_pay


def main():
    # Список приборов
    print("Polymorphism example with machines")
    appliances = [WashingMachine(), Refrigerator()]

    # Демонстрация полиморфизма
    for appliance in appliances:
        appliance.turn_on()

    # Пример использования:
    print("\nPolymorphism example with employees")
    # Создаем список сотрудников разных типов
    employees = [
        SalariedEmployee("Alice", 72000),  # Годовой оклад $72,000
        HourlyEmployee("Bob", 160, 25),  # 160 часов в месяц по $25 в час
        SalariedEmployee("Charlie", 84000),  # Годовой оклад $84,000
        HourlyEmployee("Diana", 120, 30)  # 120 часов в месяц по $30 в час
    ]

    # Демонстрация полиморфизма
    for employee in employees:
        employee.calculate_pay()


if __name__ == "__main__":
    main()
