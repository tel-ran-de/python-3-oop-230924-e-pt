# Задача:
#
# Реализуйте паттерн Singleton для класса конфигурации, который загружает и хранит настройки приложения.
#
# Шаги:
# Создайте класс конфигурации с методом для загрузки настроек.
# Реализуйте паттерн Singleton, чтобы гарантировать, что создается только один экземпляр класса конфигурации.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

    def load_settings(self, settings):
        self.settings.update(settings)


def main():
    # Тестирование
    config1 = Configuration()
    config2 = Configuration()

    config1.load_settings({"debug": True, "db_host": "localhost"})
    print(config1.settings)  # Output: {'debug': True, 'db_host': 'localhost'}
    print(config2.settings)  # Output: {'debug': True, 'db_host': 'localhost'}

    print(config1 is config2)  # Output: True


if __name__ == "__main__":
    main()
