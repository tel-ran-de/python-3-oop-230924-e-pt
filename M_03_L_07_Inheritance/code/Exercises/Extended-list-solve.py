# Создайте класс ExtendedList, который наследует от встроенного типа list и добавляет несколько новых методов.
# Используйте private и protected атрибуты для хранения состояния и добавьте методы для работы с этими атрибутами.
# Также проверьте, является ли ExtendedList подклассом list с помощью функции issubclass() и используйте super()
# для вызова методов суперкласса.
#
# Шаги:
# Создайте класс ExtendedList, который наследует от list.
# Добавьте private атрибут для хранения количества удалений элементов.
# Добавьте protected атрибут для хранения максимального размера списка.
# Добавьте метод append, который проверяет максимальный размер перед добавлением элемента.
# Добавьте метод remove, который увеличивает счетчик удалений при удалении элемента.
# Напишите методы для получения значений private и protected атрибутов.
# Проверьте, является ли ExtendedList подклассом list с помощью функции issubclass().

class ExtendedList(list):
    def __init__(self, max_size):
        super().__init__()
        self.__removal_count = 0
        self._max_size = max_size

    def append(self, item):
        if len(self) >= self._max_size:
            print("Cannot add item: list is full")
        else:
            super().append(item)

    def remove(self, item):
        super().remove(item)
        self.__removal_count += 1

    def get_removal_count(self):
        return self.__removal_count

    def get_max_size(self):
        return self._max_size


def main():
    # Тестирование
    ex_list = ExtendedList(3)
    print(issubclass(ExtendedList, list))  # Output: True

    ex_list.append(1)
    ex_list.append(2)
    ex_list.append(3)
    ex_list.append(4)  # Output: Cannot add item: list is full

    ex_list.remove(2)
    print(ex_list)  # Output: [1, 3]

    print(ex_list.get_removal_count())  # Output: 1
    print(ex_list.get_max_size())  # Output: 3


if __name__ == "__main__":
    main()
