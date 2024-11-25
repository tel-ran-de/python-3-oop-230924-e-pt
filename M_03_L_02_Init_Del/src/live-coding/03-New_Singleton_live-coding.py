class Singleton:
    """
    Singleton through attribute
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


# Define decorator for creating singleton instances
def singleton_dec(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton_dec
class Singleton_dec:
    """
    Singleton through decorator
    """

    def __init__(self, value):
        self.value = value


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton_m(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


def main():
    # Use attribute
    # Создание объектов
    singleton1 = Singleton(10)
    singleton2 = Singleton(20)

    # Проверка, что оба объекта ссылаются на один и тот же экземпляр
    print(singleton1 is singleton2)  # Output: True
    print(singleton1.value)  # Output: 20
    print(singleton2.value)  # Output: 20

    # Use decorator
    # Создание объектов
    singleton3 = Singleton_dec(10)
    singleton4 = Singleton_dec(20)

    # Проверка, что оба объекта ссылаются на один и тот же экземпляр
    print(singleton3 is singleton4)  # Output: True
    print(singleton3.value)  # Output: 20
    print(singleton4.value)  # Output: 20

    # Use metaclass
    # Создание объектов
    singleton5 = Singleton_m(10)
    singleton6 = Singleton_m(20)

    # Проверка, что оба объекта ссылаются на один и тот же экземпляр
    print(singleton5 is singleton6)  # Output: True
    print(singleton5.value)  # Output: 20
    print(singleton6.value)  # Output: 20
