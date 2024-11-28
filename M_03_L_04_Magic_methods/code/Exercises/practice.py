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
    pass


class Adder:
    pass


class Multiplier:
    pass


def TimeLogger(func):
    pass


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

# AdvancedCalculator with values: [1, -2, 3, -4]
# AdvancedCalculator([1, -2, 3, -4])
# 4
# AdvancedCalculator with values: [1, 2, 3, 4]
# 15
# 30
# Called 1 times
# Called 2 times
# 100
# Function slow_function executed in 1.000591 seconds
# Function ran for 1 seconds
