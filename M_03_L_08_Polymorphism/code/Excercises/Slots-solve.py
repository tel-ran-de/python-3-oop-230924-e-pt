# Создайте два класса: один с использованием __slots__, а другой без его использования.
# Напишите методы для добавления, удаления и изменения атрибутов в обоих классах. Сравните использование памяти
# и поведение __dict__ в каждом случае.
#
# Шаги:
# Создайте класс ClassWithDict, который не использует __slots__, и реализуйте методы для добавления,
# удаления и изменения атрибутов.
# Создайте класс ClassWithSlots, который использует __slots__, и реализуйте аналогичные методы.
# Напишите код для создания экземпляров каждого класса, добавления, удаления и изменения атрибутов.
# Сравните использование памяти каждым классом.
# Попробуйте получить доступ к __dict__ в обоих классах и объясните результаты.

class ClassWithDict:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def add_attr(self, name, value):
        self.__dict__[name] = value

    def del_attr(self, name):
        if name in self.__dict__:
            del self.__dict__[name]
        else:
            print(f"Attribute {name} not found")

    def update_attr(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
        else:
            print(f"Attribute {name} not found")

class ClassWithSlots:
    __slots__ = ['attr1', 'attr2', 'attr3']

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def add_attr(self, name, value):
        if name in self.__slots__:
            setattr(self, name, value)
        else:
            print(f"Cannot add attribute {name} to slots")

    def del_attr(self, name):
        if hasattr(self, name):
            setattr(self, name, None)
        else:
            print(f"Attribute {name} not found")

    def update_attr(self, name, value):
        if hasattr(self, name):
            setattr(self, name, value)
        else:
            print(f"Attribute {name} not found")


def main():
    # Тестирование
    dict_obj = ClassWithDict(10, 20)
    slots_obj = ClassWithSlots(10, 20)

    # Работа с ClassWithDict
    print(dict_obj.__dict__)  # Output: {'attr1': 10, 'attr2': 20}
    dict_obj.add_attr('attr3', 30)
    print(dict_obj.__dict__)  # Output: {'attr1': 10, 'attr2': 20, 'attr3': 30}
    dict_obj.del_attr('attr2')
    print(dict_obj.__dict__)  # Output: {'attr1': 10, 'attr3': 30}
    dict_obj.update_attr('attr1', 40)
    print(dict_obj.__dict__)  # Output: {'attr1': 40, 'attr3': 30}

    # Работа с ClassWithSlots
    # print(slots_obj.__dict__)  # Raises AttributeError
    slots_obj.add_attr('attr3', 30)
    print(slots_obj.attr3)  # Output: 30
    slots_obj.del_attr('attr2')
    print(slots_obj.attr2)  # Output: None
    slots_obj.update_attr('attr1', 40)
    print(slots_obj.attr1)  # Output: 40


if __name__ == "__main__":
    main()
