# Ex 1
# Создайте класс `Temperature` с методами для преобразования температуры из градусов Цельсия в Фаренгейты и Кельвины.
# Реализуйте методы как статические.
#
# #### Задание 2:
# Создайте класс `Counter` с атрибутом класса `count`,
# который будет отслеживать количество созданных экземпляров класса.
# Реализуйте метод класса `get_count`, который возвращает текущее значение `count`.

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Преобразует температуру из градусов Цельсия в Фаренгейты."""
        return celsius * 9/5 + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        """Преобразует температуру из градусов Цельсия в Кельвины."""
        return celsius + 273.15


class Counter:
    # Атрибут класса для отслеживания количества экземпляров
    count = 0

    def __init__(self):
        """Увеличивает счетчик при создании нового экземпляра."""
        Counter.count += 1

    @classmethod
    def get_count(cls):
        """Возвращает текущее значение счетчика."""
        return cls.count


def main():
    # Пример использования:
    print("Temperature Class example")
    celsius_temp = 25

    # Преобразование в Фаренгейты
    fahrenheit_temp = Temperature.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C = {fahrenheit_temp}°F")

    # Преобразование в Кельвины
    kelvin_temp = Temperature.celsius_to_kelvin(celsius_temp)
    print(f"{celsius_temp}°C = {kelvin_temp}K")

    # Пример использования:
    print("\nCounter Class example")
    # Создаем несколько экземпляров
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()

    # Получаем текущее количество экземпляров
    print(f"Number of instances created: {Counter.get_count()}")  # Output: 3


if __name__ == "__main__":
    main()
