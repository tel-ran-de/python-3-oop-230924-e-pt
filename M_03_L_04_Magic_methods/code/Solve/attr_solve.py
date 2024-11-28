# Создание класса с логированием доступа к атрибутам
# Описание:
#
# Создайте класс LoggedAttributes, который будет вести лог всех операций по установке, получению и
# удалению атрибутов, а также предоставлять значения по умолчанию для отсутствующих атрибутов.
# Все операции должны логироваться в список log.
#
# Требования:
#
# Переопределите метод __setattr__ для логирования установки атрибутов.
# Переопределите метод __getattribute__ для логирования доступа к атрибутам.
# Переопределите метод __getattr__ для логирования и предоставления значения по умолчанию для отсутствующих атрибутов.
# Переопределите метод __delattr__ для логирования удаления атрибутов.
# Шаги:
#
# Создайте класс LoggedAttributes.
# Добавьте список log в качестве атрибута класса для хранения логов операций.
# Реализуйте методы __setattr__, __getattribute__, __getattr__ и __delattr__ с логированием операций.
# Тестируйте класс, создавая экземпляр и выполняя различные операции с атрибутами.

class LoggedAttributes:
    def __init__(self):
        super().__setattr__('log', [])

    def __setattr__(self, name, value):
        self.log.append(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        log = super().__getattribute__('log')
        log.append(f"Getting attribute {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        self.log.append(f"Attribute {name} not found, returning default value")
        return "Default value"

    def __delattr__(self, name):
        self.log.append(f"Deleting attribute {name}")
        super().__delattr__(name)


def main():
    # Тестирование класса
    obj = LoggedAttributes()

    # Установка атрибутов
    obj.name = "Alice"
    obj.age = 30

    # Доступ к существующим атрибутам
    print(obj.name)  # Output: Alice
    print(obj.age)  # Output: 30

    # Доступ к несуществующему атрибуту
    print(obj.height)  # Output: Default value

    # Удаление атрибута
    del obj.age

    # Попытка доступа к удаленному атрибуту
    print(obj.age)  # Output: Default value

    # Логи операций
    print("\nLog of operations:")
    for entry in obj.log:
        print(entry)


if __name__ == '__main__':
    main()
