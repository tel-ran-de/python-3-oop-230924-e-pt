# Напишите класс, который разделит итератор и итерируемый объект.
from operator import index


class IterableClass:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return IterClass(self.data)

class IterClass:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        num = self.data[self.index]
        self.index += 1
        return num


def main():
    # Тестирование
    iterable = IterableClass([10, 20, 30])
    for value in iterable:
        print(value)  # Output: 10 20 30


if __name__ == '__main__':
    main()

# 10
# 20
# 30
