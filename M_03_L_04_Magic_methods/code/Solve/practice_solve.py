# Задача: Создание класса AdvancedCalculator с расширенной функциональностью
# Описание:
#
# Создайте класс AdvancedCalculator, который будет выполнять базовые арифметические операции и
# предоставлять расширенные возможности. Класс должен поддерживать следующие возможности:
#
# Логирование всех операций по установке, получению и удалению атрибутов.
# Ведение счетчика вызовов объекта.
# Функциональность функторов для сложения и умножения чисел.
# Реализация методов __str__, __repr__, __len__ и __abs__.
# Требования:
#
# Реализуйте методы __setattr__, __getattribute__, __getattr__ и __delattr__ для логирования операций.
# Реализуйте метод __call__ для ведения счетчика вызовов.
# Создайте классы-функторы для сложения и умножения чисел.
# Реализуйте класс-декоратор для логирования времени выполнения методов.
# Реализуйте методы __str__, __repr__, __len__ и __abs__.

import time


class AdvancedCalculator:
    def __init__(self, values):
        super().__setattr__('values', values)
        super().__setattr__('log', [])
        self.call_count = 0

    def __setattr__(self, name, value):
        self.log.append(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        log = super().__getattribute__('log')
        log.append(f"Getting attribute {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        self.log.append(f"Attribute {name} not found, returning default value")
        return "Default value"

    def __delattr__(self, name):
        self.log.append(f"Deleting attribute {name}")
        super().__delattr__(name)

    def __call__(self):
        self.call_count += 1
        print(f"Called {self.call_count} times")

    def __str__(self):
        return f"AdvancedCalculator with values: {self.values}"

    def __repr__(self):
        return f"AdvancedCalculator({self.values})"

    def __len__(self):
        return len(self.values)

    def __abs__(self):
        return AdvancedCalculator([abs(value) for value in self.values])


class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value + other


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


class TimeLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {self.func.__name__} executed in {elapsed_time:.6f} seconds")
        return result


def main():
    # Пример использования

    @TimeLogger
    def slow_function(seconds):
        time.sleep(seconds)
        return f"Function ran for {seconds} seconds"

    # Создание объекта AdvancedCalculator
    calc = AdvancedCalculator([1, -2, 3, -4])

    # Использование методов
    print(calc)  # Использование __str__
    print(repr(calc))  # Использование __repr__
    print(len(calc))  # Использование __len__
    print(abs(calc))  # Использование __abs__

    # Функторы
    add_five = Adder(5)
    multiply_by_three = Multiplier(3)

    print(add_five(10))  # Output: 15
    print(multiply_by_three(10))  # Output: 30

    # Вызов объекта
    calc()  # Output: Called 1 times
    calc()  # Output: Called 2 times

    # Логирование операций
    calc.new_attr = 100  # Использование __setattr__
    print(calc.new_attr)  # Использование __getattribute__ и __getattr__
    del calc.new_attr  # Использование __delattr__

    # # Лог операций
    # print("\nLog of operations:")
    # for entry in calc.log:
    #     print(entry)

    # Тестирование декоратора
    print(slow_function(1))


if __name__ == '__main__':
    main()
