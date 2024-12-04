# Паттерн Singleton гарантирует, что у класса будет только один экземпляр, и
# предоставляет глобальную точку доступа к этому экземпляру.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42


def main():
    s1 = Singleton()
    s2 = Singleton()

    print(s1 == s2)  # Output: True
    print(s1.value)  # Output: 42


if __name__ == "__main__":
    main()
