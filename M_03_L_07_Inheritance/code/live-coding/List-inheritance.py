# Наследование от встроенного типа list
# Задача:
#
# Создайте класс, который наследует от встроенного типа list и добавляет дополнительные методы.
# Используйте функцию issubclass() для проверки, является ли созданный класс подклассом list.
#
# Шаги:
# Создайте класс CustomList, который наследует от list.
# Добавьте метод sum для вычисления суммы всех элементов списка.
# Добавьте метод mean для вычисления среднего значения элементов списка.
# Напишите функцию, которая принимает класс и проверяет, является ли он подклассом list с помощью issubclass().
# Протестируйте функцию и методы CustomList.
#
# Реализация:
# Наследование от list: Класс CustomList наследуется от list и добавляет методы sum и mean.
# Функция проверки: Функция check_list_subclass использует issubclass для проверки,
# является ли переданный класс подклассом list.
# Тестирование: Примеры показывают использование новых методов CustomList и проверку,
# является ли CustomList подклассом list.

class CustomList(list):
    def sum(self):
        return sum(self)

    def mean(self):
        if len(self) == 0:
            return 0
        return sum(self) / len(self)


def check_list_subclass(cls):
    return issubclass(cls, list)


def main():
    # Тестирование
    custom_list = CustomList([1, 2, 3, 4, 5])

    print(custom_list.sum())  # Output: 15
    print(custom_list.mean())  # Output: 3.0

    print(check_list_subclass(CustomList))  # Output: True
    print(check_list_subclass(list))  # Output: True
    print(check_list_subclass(dict))  # Output: False


if __name__ == "__main__":
    main()
