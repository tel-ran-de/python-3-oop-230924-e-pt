# Напишите класс, который разделит итератор и итерируемый объект.

class IterableClass:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return IterableClassIterator(self.values)


class IterableClassIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration
        value = self.values[self.index]
        self.index += 1
        return value


def main():
    # Тестирование
    iterable = IterableClass([10, 20, 30])
    for value in iterable:
        print(value)  # Output: 10 20 30


if __name__ == '__main__':
    main()
