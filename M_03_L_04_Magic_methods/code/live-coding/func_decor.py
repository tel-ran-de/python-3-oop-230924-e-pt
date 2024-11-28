class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"Called {self.count} times")


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Function {self.func.__name__} called with args: {args}, kwargs: {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"Function {self.func.__name__} returned: {result}")
        return result


def main():
    # Тестирование класса
    counter = Counter()
    counter()  # Output: Called 1 times
    counter()  # Output: Called 2 times
    counter()  # Output: Called 3 times

    # Тестирование функторов
    double = Multiplier(2)
    triple = Multiplier(3)

    print(double(5))  # Output: 10
    print(triple(5))  # Output: 15

    # Использование класса-декоратора
    @Logger
    def add(a, b):
        return a + b

    # Тестирование декоратора
    add(2, 3)
    # Output:
    # Function add called with args: (2, 3), kwargs: {}
    # Function add returned: 5


if __name__ == "__main__":
    main()
