# Напишите класс, который разделит итератор и итерируемый объект.
class IterableClass:
    pass


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
