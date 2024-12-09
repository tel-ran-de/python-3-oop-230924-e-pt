# Наследование от встроенного типа dict.
#
# Создайте класс, который наследует от встроенного типа dict и добавляет дополнительные методы.
# Используйте функцию issubclass() для проверки, является ли созданный класс подклассом dict.
#
# Шаги:
# Создайте класс CustomDict, который наследует от dict.
# Добавьте метод invert, который возвращает новый словарь с инвертированными ключами и значениями.
# Добавьте метод merge, который объединяет текущий словарь с другим словарем.
# Напишите функцию, которая принимает класс и проверяет, является ли он подклассом dict с помощью issubclass().
# Протестируйте функцию и методы CustomDict.

class CustomDict(dict):
    def invert(self):
        return {v: k for k, v in self.items()}

    def merge(self, other_dict):
        for key, value in other_dict.items():
            if key in self:
                self[key] += value
            else:
                self[key] = value


def check_dict_subclass(cls):
    return issubclass(cls, dict)


def main():
    # Тестирование
    custom_dict = CustomDict({'a': 1, 'b': 2, 'c': 3})

    print(custom_dict.invert())  # Output: {1: 'a', 2: 'b', 3: 'c'}

    custom_dict.merge({'b': 3, 'd': 4})
    print(custom_dict)  # Output: {'a': 1, 'b': 5, 'c': 3, 'd': 4}

    print(check_dict_subclass(CustomDict))  # Output: True
    print(check_dict_subclass(dict))  # Output: True
    print(check_dict_subclass(list))  # Output: False


if __name__ == "__main__":
    main()
