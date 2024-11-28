# Учебная задача: Создание класса EnhancedList с расширенной функциональностью
# Описание:
#
# Создайте класс EnhancedList, который будет вести себя как список, но с дополнительной функциональностью.
# Класс должен поддерживать следующие возможности:
#
# Логирование всех операций по установке, получению и удалению атрибутов.
# Ведение счетчика вызовов объекта.
# Функциональность функторов для добавления и умножения элементов списка.
# Реализация методов __str__, __repr__, __len__ и __abs__.
# Требования:
#
# Реализуйте методы __setattr__, __getattribute__, __getattr__ и __delattr__ для логирования операций.
# Реализуйте метод __call__ для ведения счетчика вызовов.
# Создайте классы-функторы для добавления и умножения элементов списка.
# Реализуйте класс-декоратор для логирования времени выполнения методов.
# Реализуйте методы __str__, __repr__, __len__ и __abs__.

import time


class EnhancedList:
    def __init__(self, items):
        super().__setattr__('items', items)
        super().__setattr__('log', [])
        # self.__setattr__('log', [])
        # self.log = []
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
        self.log.append(f"Call object as functor")
        self.call_count += 1
        print(f"Called {self.call_count} times")

    def __str__(self):
        self.log.append(f"Call __str__")
        return f"EnhancedList with items: {self.items}"

    def __repr__(self):
        self.log.append(f"Call __repr__")
        return f"EnhancedList({self.items})"

    def __len__(self):
        self.log.append(f"Call __len__")
        return len(self.items)

    def __abs__(self):
        return EnhancedList([abs(item) for item in self.items])


class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return other + self.value


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

    # Создание объекта EnhancedList
    elist = EnhancedList([1, -2, 3, -4])

    # Использование методов
    print('Использование __str__')
    print(elist)  # Использование __str__

    print('\nИспользование __repr__')
    print(repr(elist))  # Использование __repr__

    print('\nИспользование __len__')
    print(len(elist))  # Использование __len__

    print('\nИспользование __abs__')
    print(abs(elist))  # Использование __abs__

    # Функторы
    add_five = Adder(5)
    multiply_by_three = Multiplier(3)

    print(add_five(10))  # Output: 15
    print(multiply_by_three(10))  # Output: 30

    # Вызов объекта
    elist()  # Output: Called 1 times
    elist()  # Output: Called 2 times

    # Логирование операций
    elist.new_attr = 100  # Использование __setattr__
    print(elist.new_attr)  # Использование __getattribute__ и __getattr__
    del elist.new_attr  # Использование __delattr__

    # Лог операций
    print("\nLog of operations:")
    for entry in elist.log:
        print(entry)

    # Тестирование декоратора
    print(slow_function(1))


if __name__ == "__main__":
    main()
