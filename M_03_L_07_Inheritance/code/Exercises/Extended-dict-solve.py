# Создайте класс TrackedDict, который наследует от встроенного типа dict и добавляет новые методы
# для отслеживания изменений в словаре. Используйте private и protected атрибуты для хранения состояния и
# добавьте методы для работы с этими атрибутами. Также проверьте, является ли TrackedDict подклассом dict с
# помощью функции issubclass() и используйте super() для вызова методов суперкласса.
#
# Шаги:
# Создайте класс TrackedDict, который наследует от dict.
# Добавьте private атрибут для хранения количества изменений (добавление/удаление элементов).
# Добавьте protected атрибут для хранения разрешенного количества изменений.
# Переопределите методы __setitem__ и __delitem__, чтобы увеличивать счетчик изменений и проверять его значение.
# Напишите методы для получения значений private и protected атрибутов.
# Проверьте, является ли TrackedDict подклассом dict с помощью функции issubclass().

class TrackedDict(dict):
    def __init__(self, max_changes):
        super().__init__()
        self.__change_count = 0
        self._max_changes = max_changes

    def __setitem__(self, key, value):
        if self.__change_count >= self._max_changes:
            print("Cannot add/change item: maximum number of changes reached")
        else:
            super().__setitem__(key, value)
            self.__change_count += 1

    def __delitem__(self, key):
        if self.__change_count >= self._max_changes:
            print("Cannot delete item: maximum number of changes reached")
        else:
            super().__delitem__(key)
            self.__change_count += 1

    def get_change_count(self):
        return self.__change_count

    def get_max_changes(self):
        return self._max_changes


def main():
    # Тестирование
    tracked_dict = TrackedDict(3)
    print(issubclass(TrackedDict, dict))  # Output: True

    tracked_dict['a'] = 1
    tracked_dict['b'] = 2
    tracked_dict['c'] = 3
    tracked_dict['d'] = 4  # Output: Cannot add/change item: maximum number of changes reached

    del tracked_dict['a']
    print(tracked_dict)  # Output: {'b': 2, 'c': 3}

    print(tracked_dict.get_change_count())  # Output: 3
    print(tracked_dict.get_max_changes())  # Output: 3


if __name__ == "__main__":
    main()
