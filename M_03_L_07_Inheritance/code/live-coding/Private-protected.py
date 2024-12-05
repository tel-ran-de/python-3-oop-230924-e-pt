# Private and protected attribute

class ParentClass:
    def __init__(self, protected_value, private_value):
        self._protected_attr = protected_value
        self.__private_attr = private_value

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, value):
        self.__private_attr = value


class ChildClass(ParentClass):
    def get_protected_attr(self):
        return self._protected_attr


def main():
    # Тестирование
    parent = ParentClass(50, 100)
    child = ChildClass(30, 60)

    print(parent.get_private_attr())  # Output: 100
    parent.set_private_attr(150)
    print(parent.get_private_attr())  # Output: 150

    print(child.get_protected_attr())  # Output: 30

    # Доступ к защищенному атрибуту напрямую (по соглашению не рекомендуется)
    print(child._protected_attr)  # Output: 30

    # Попытка доступа к приватному атрибуту напрямую вызовет ошибку
    # print(child.__private_attr)  # AttributeError: 'ChildClass' object has no attribute '__private_attr'

    # Доступ к приватному атрибуту через name mangling
    print(child._ParentClass__private_attr)  # Output: 60


if __name__ == "__main__":
    main()
