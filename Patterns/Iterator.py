# Паттерн Iterator предоставляет способ последовательного доступа ко всем элементам коллекции
# без раскрытия ее внутреннего представления.

class MyIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


def main():
    items = [1, 2, 3, 4]
    iterator = MyIterator(items)

    for item in iterator:
        print(item)  # Output: 1 2 3 4


if __name__ == '__main__':
    main()
